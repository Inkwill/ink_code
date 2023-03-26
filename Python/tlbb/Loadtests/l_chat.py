# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/14 by 粟品容
-----------------------------------------------------------------------
Description:    聊天
-----------------------------------------------------------------------
History:   
2016/09/14：粟品容创建
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import time
import gevent
import logging
import traceback
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



        gevent.sleep(2)



        self.client.ACG_COMMAND(u'levelup = 20')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'addmoney = 5000000')
        gevent.sleep(2)
        self.client.ACGIdle()
        
        self.client.ACGGuildApply()
        gevent.sleep(5)
        self.client.ACGIdle()

        self.client.ACCTEAMINVITE()
        gevent.sleep(10)
        self.client.ACGIdle()
        
        self.client.ACGAskServerTime()
        gevent.sleep(5)
        self.client.ACGIdle()  

        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACGChat",0, 0) #0 附近聊天， 2： 世界聊天 ，6：帮会聊天 ,1:队伍聊天
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACGChat",0, 2)
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACGChat",0, 6)



class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def chat(self):
            try:
                self.client.taskqueue_execute() 
            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
                traceback.print_exc()
                self.client.taskqueue_cleanup()
                self.client['socket'].close()
                raise 


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()