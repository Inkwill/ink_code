# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/09 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部  四绝庄副本
-----------------------------------------------------------------------
History:   
2016/10/09：姚俊创建
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import random
import gevent
import traceback

#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"
g_NpcObjId = 38
g_ScriptID = 402051
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
            

        PosList = [[107,228],[107,229],[107,230],[106,228],[106,229],[106,227]]
        
        
        templist = PosList[random.randint(0,5)]
        
        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(2)
        self.client.ACG_COMMAND(u'levelupallxiulian = 50')
        gevent.sleep(2)
        self.client.ACG_COMMAND(u'levelup = 79')
        gevent.sleep(2)
        self.client.changescreenposition(1,templist[0],templist[1])
        gevent.sleep(2)
        
        self.client.ACCTEAMINVITE()
        gevent.sleep(5)
        self.client.ACGIdle()
        self.client.ACGCharDefaultEvent(g_NpcObjId)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACGEventRequest(g_NpcObjId,g_ScriptID,g_ExIndex)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACGAskChangeScene()
        gevent.sleep(10)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.taskqueue_append("ACG_CHARMOVE",0,99,9)
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0,99,2)
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0,97,8)
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
                traceback.print_exc()
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