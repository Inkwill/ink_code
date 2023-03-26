# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/08 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部  三环副本
-----------------------------------------------------------------------
History:   
2016/10/08：姚俊创建
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
g_NpcObjId = 14
g_ScriptID = 900039
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
            

        PosList = [[49,155],[48,154],[48,157],[45,157],[44,155],[45,154]]
        
        
        templist = PosList[random.randint(0,5)]
        
        self.client.ACG_COMMAND(u'levelup = 40')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'iamgod')
        gevent.sleep(2)
        self.client.ACGIdle()
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
        gevent.sleep(5)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client['battle_monster'] = {}
        self.client['battle_path'] = [(16,109),(16,105),(16,102),(16,98),(16,95),(16,92),(16,88),(16,92),(19,86),(22,82),(20,79),(20,75),(20,70),(20,66),(20,62),(21,56),(21,52),\
                             (21,46),(21,40),(21,34),(22,30),(25,27),(31,24)]
        self.client['battle_path_index'] = 0
        
        self.client.taskqueue_append("battle_path",300)
        self.client.taskqueue_append("ACGIdle",1)

class TestPerson(GameLocust):
    min_wait = 500
    max_wait = 700
    
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

                self.client.taskqueue_cleanup()
                self.client.taskqueue_append("ACGIdle",1)