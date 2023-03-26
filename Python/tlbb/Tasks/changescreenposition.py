#coding=utf-8
import Actions
import gevent

class changescreenposition():
    def __init__(self, person):
        self.person = person

    def run(self,screenid,x,y):
        if self.person['SceneId'] == screenid or self.person['m_nResID'] == screenid:
            sendcommand = u'goto = ' + unicode(x) + u',' + unicode(y)
        else:
            sendcommand = u'goto = ' + unicode(x) + u',' + unicode(y) + u' = ' + unicode(screenid)
            
        
            
        if self.person['SceneId'] != screenid:
            # gevent.sleep(2)
            # self.person.ACG_CHARMOVE(self.person['posx']+1, self.person['posz']+1)
            # gevent.sleep(2)
            # self.person.ACGIdle()
            # gevent.sleep(2)
            # self.person.ACG_CHARMOVE(self.person['posx']-1, self.person['posz']-1)
            gevent.sleep(2)
            self.person.ACGIdle()


            res = self.person.ACG_COMMAND(sendcommand)
            if res[0] == False:
                return res
                
    
            res = Actions.Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NOTIFYCHANGESCENE",60)
            if res[0] == False:
                return res
            
            res = self.person.ACGAskChangeScene()
            if res[0] == False:
                return res
    
            res = self.person.ACGENTERSCENE(1)
            if res[0] == False:
                return res
            return  res
        else:
            res = self.person.ACG_COMMAND(sendcommand)
            if res[0] == False:
                return res

            res = Actions.Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_DELALLOBJ",30)
            if res[0] == False:
                return res

            return res

    
    
        

