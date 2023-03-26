import Tasks
from locust import events
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)s: %(message)s',datefmt='%H:%M:%S')

class person:
    def __init__(self, loadtestflag=False):
        self.__data = {}
        self.__action = {}
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0
        self.__loadflag = loadtestflag
        self.__data['inputbuffer'] = ""
        self.__data['socket'] = None
        self.__data['is_packect_truncated'] = False
        self.__data['packet_rec_time'] = 0
        self.__data['heartbeatTime'] = 0
        
        self.__data['userName'] = None
        self.__data['posx'] = 0
        self.__data['posz'] = 0
        self.__data['SceneId'] = 0
        self.__data['m_ObjID'] = 0
        self.__data['m_Guid'] = 0
        self.__data['menPai'] = 0
        self.__data['targetmark'] = []
        self.__data['monsterdic'] = {}
        self.__data['targetdic'] = {}


        
    def setdata (self, name, value):
        self.__data[name] = value
        return self.getdata(name)
    
    def getdata (self, name):
        if self.__data.has_key(name) and self.__data[name] != None:
            return self.__data[name]
        else:
            return None
        
    def getloadflag (self):
        return self.__loadflag
        
    def cleanup_data (self):
        self.__data = {}
        
    def __getitem__(self, name):
        return self.getdata(name)
    
    def __setitem__(self, name, value):
        return self.setdata(name, value)
    
    def __getattr__(self, name):
        def errorinfo(*args, **kwargs):
            return (False,0,"Action: %s not defined" % name)
        if name in Tasks.__all__:
            if self.__action.__class__.__name__ != name:
                self.__action = eval('Tasks.%s.%s(self)' % (name,name))
            func = self.__action.run
        elif name in Tasks.Actions.__all__:
            if self.__action.__class__.__name__ != name:
                self.__action = eval('Tasks.Actions.%s.%s(self)' % (name,name))
            func = self.__action.run
        else:
            return errorinfo
        
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if self.__loadflag:
                if result is not None:
                    if result[0] == True:
                        events.request_success.fire(request_type="GameRobot", name=name, response_time=result[1], response_length=0)
                    else:
                        events.request_failure.fire(request_type="GameRobot", name=name, response_time=result[1], exception=None)
            return result
        return wrapper

    def __str__(self):
        return Tasks.Actions.NetPackets.STAFMarshalling.formatObject(self.__data)
    
    def __repr__(self):
        return Tasks.Actions.NetPackets.STAFMarshalling.formatObject(self.__data)
    
    def dump(self):
        return Tasks.Actions.NetPackets.STAFMarshalling.formatObject(self.__data)
    
    def getaction(self, name):
        return self.__getattr__(name)

    def taskqueue_append(self,taskname,duration_time=0, *args):
        self.__taskqueue.append((taskname,duration_time,args))
        
    def taskqueue_cleanup(self):
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0
 
    def taskqueue_execute(self):
        if len(self.__taskqueue) == 0:
            return (True,0,"Task queue is empty")
        res = self.__getattr__(self.__taskqueue[self.__taskqueueindex][0])(*self.__taskqueue[self.__taskqueueindex][2])
        queuelen = len(self.__taskqueue)
        if self.__taskqueue[self.__taskqueueindex][1] > 0:  #execute for duration_time 
            if self.__taskqueuetimestamp == 0:              #execute first time
                self.__taskqueuetimestamp = time.time()
            else:
                total_time = int((time.time() - self.__taskqueuetimestamp) * 1000)
                if total_time >= self.__taskqueue[self.__taskqueueindex][1]*1000:  #queue index + 1
                    if self.__taskqueueindex >= (queuelen-1):
                        self.__taskqueueindex = 0
                    else:
                        self.__taskqueueindex += 1
                    self.__taskqueuetimestamp = 0
        else:                                                #execute once
            if self.__taskqueueindex >= (queuelen-1):
                self.__taskqueueindex = 0
            else:
                self.__taskqueueindex += 1
        return res


class personset:
    def __init__(self):
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0
        
    def taskqueue_append(self, personobj, taskname,duration_time=0, *args):
        self.__taskqueue.append((personobj, taskname,duration_time,args))
 
    def taskqueue_execute(self):
        res = ((self.__taskqueue[self.__taskqueueindex][0]).getaction(self.__taskqueue[self.__taskqueueindex][1]))(*self.__taskqueue[self.__taskqueueindex][3])
        queuelen = len(self.__taskqueue)
        if self.__taskqueue[self.__taskqueueindex][2] > 0:  #execute for duration_time 
            if self.__taskqueuetimestamp == 0:              #execute first time
                self.__taskqueuetimestamp = time.time()
            else:
                total_time = int((time.time() - self.__taskqueuetimestamp) * 1000)
                if total_time >= self.__taskqueue[self.__taskqueueindex][2]*1000:  #queue index + 1
                    if self.__taskqueueindex >= (queuelen-1):
                        self.__taskqueueindex = 0
                    else:
                        self.__taskqueueindex += 1
                    self.__taskqueuetimestamp = 0
        else:                                                #execute once
            if self.__taskqueueindex >= (queuelen-1):
                self.__taskqueueindex = 0
            else:
                self.__taskqueueindex += 1
        return res

    def taskqueue_cleanup(self):
        self.__taskqueue = []
        self.__taskqueueindex = 0
        self.__taskqueuetimestamp = 0

if __name__ == "__main__":

    import gevent
    aa = person()

    aa.login("182.254.221.101",1233,"182.254.221.101",1231,264,"0.7.42")
    
    gevent.sleep(3)
    aa.ACGIdle()
    gevent.sleep(3)
    aa.ACGIdle()
    gevent.sleep(3)
    aa.ACGIdle()
    
    
    aa.ACG_CHARMOVE(aa['posx']+1, aa['posz']+1)
    gevent.sleep(2)
    aa.ACGIdle()


    aa.ACG_COMMAND(u'levelup = 50')
    gevent.sleep(3)
    aa.ACGIdle()
    aa.changescreenposition(1,153,153)
    gevent.sleep(5)
    aa.ACGIdle()

        

#         length = len(langfang)
#         for i in range(length):
#             aa.taskqueue_append("ACG_CHARMOVE",0,langfang[i][0],langfang[i][1])
#             aa.taskqueue_append("ACGIdle",8)
# 
#         for i in range(length):
#             aa.taskqueue_append("ACG_CHARMOVE",0,langfang[length-i-1][0],langfang[length - i -1][1])
#             aa.taskqueue_append("ACGIdle",8)
    aa.taskqueue_append("ACG_CHARMOVE",0,156,156)
    aa.taskqueue_append("ACGIdle",15)
    aa.taskqueue_append("ACG_CHARMOVE",0,156,238)
    aa.taskqueue_append("ACGIdle",15)  
    #-------------------bb-------------
    bb = person()

    bb.login("182.254.221.101",1233,"182.254.221.101",1231,265,"0.7.42")
    
    gevent.sleep(3)
    bb.ACGIdle()
    gevent.sleep(3)
    bb.ACGIdle()
    gevent.sleep(3)
    bb.ACGIdle()
    
    
    bb.ACG_CHARMOVE(bb['posx']+1, bb['posz']+1)
    gevent.sleep(2)
    bb.ACGIdle()


    bb.ACG_COMMAND(u'levelup = 50')
    gevent.sleep(3)
    bb.ACGIdle()
    bb.changescreenposition(1,153,153)
    gevent.sleep(5)
    bb.ACGIdle()

        

#         length = len(langfang)
#         for i in range(length):
#             aa.taskqueue_append("ACG_CHARMOVE",0,langfang[i][0],langfang[i][1])
#             aa.taskqueue_append("ACGIdle",8)
# 
#         for i in range(length):
#             aa.taskqueue_append("ACG_CHARMOVE",0,langfang[length-i-1][0],langfang[length - i -1][1])
#             aa.taskqueue_append("ACGIdle",8)
    bb.taskqueue_append("ACG_CHARMOVE",0,156,156)
    bb.taskqueue_append("ACGIdle",15)
    bb.taskqueue_append("ACG_CHARMOVE",0,156,238)
    bb.taskqueue_append("ACGIdle",15)      

    while 1:
        aa.taskqueue_execute()
        bb.taskqueue_execute()








    