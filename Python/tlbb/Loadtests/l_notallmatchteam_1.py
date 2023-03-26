# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/11 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部  自动匹配队伍 （不满队）
-----------------------------------------------------------------------
History:   
2016/10/11：姚俊创建
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
        self.client.changescreenposition(1,templist[0],templist[1])
        gevent.sleep(2)
        
        self.client['notallmatchstate'] = "start"
                
        self.client.taskqueue_append("captain_notallmatching",0)
        
        self.client.taskqueue_append("ACGIdle",0)
        

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