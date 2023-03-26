# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/11 by 粟品容
-----------------------------------------------------------------------
Description:    天龙八部  活动英雄试炼
-----------------------------------------------------------------------
History:   
2016/10/11：粟品容
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import random
import gevent

#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"
g_NpcObjId = 6
g_ScriptID = 900011
g_ExIndex = 1
class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        
        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise
            

        PosList = [[151,45],[150,45],[149,45],[149,44],[151,42],[152,43]]
        
        
        templist = PosList[random.randint(0,5)]
        
        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(2)
        self.client.ACG_COMMAND(u'levelupallxiulian = 80')
        gevent.sleep(2)
        self.client.ACG_COMMAND(u'levelup = 100')
        gevent.sleep(2)
        #self.client.ACG_COMMAND(u'createitem = 30000061 = 0 = 10')
        #gevent.sleep(2)
        self.client.changescreenposition(1,templist[0],templist[1])
        gevent.sleep(2)
        
        self.client.ACCTEAMINVITE()
        gevent.sleep(5)
        self.client.ACGIdle()
        gevent.sleep(5)
        self.client.ACGIdle()
                
        self.client.ACGCharDefaultEvent(g_NpcObjId)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACGEventRequest(g_NpcObjId,g_ScriptID,g_ExIndex, False)
        self.client.ACG_EXECUTESCRIPT(900011, u'HeroTrials', [1, 6])
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACGAskChangeScene()
        gevent.sleep(10)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.taskqueue_append("ACG_CHARMOVE",0,44.072,32.83)
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0,42.99, 37.88)
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0,20.22, 33.26)
        self.client.taskqueue_append("ACGIdle",5)
        

class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def laosanhuan(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)

                gevent.sleep(2)
                self.client.ACGIdle()
                gevent.sleep(2)
                self.client.ACGIdle()
                gevent.sleep(2)
                self.client.ACGIdle()


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()