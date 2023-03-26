# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/18 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部   创建帮会
-----------------------------------------------------------------------
History:   
2016/10/18：姚俊创建
2017/1/17：鹿振宇修改
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


g_NpcObjId = 2
g_ScriptID = 30
g_ExIndex = 2
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
            

        self.client.ACG_COMMAND(u'levelup = 40')
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACG_COMMAND(u'addmoney = 500000')
        gevent.sleep(5)
        self.client.ACGIdle()
        
       
        
        self.client.ACGGuildApply()
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACGAskServerTime()
        gevent.sleep(5)
        self.client.ACGIdle()    
        
        

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
                    
if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()
