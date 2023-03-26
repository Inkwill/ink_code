# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/01/02 by luzhenyu
-----------------------------------------------------------------------
Description:    骑乘
-----------------------------------------------------------------------
History:   
2017/01/02 luzhenyu created
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
import random
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
        
        self.client.ACG_COMMAND(u'levelup = 15')
        gevent.sleep(2)
        self.client.ACGIdle()
        
        self.client.changescreenposition(1, 156, 90)
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        
        



        self.client.ACG_COMMAND(u'createitem = 11000020 == 1')
        gevent.sleep(3)
        self.client.ACGIdle()
        self.client.ACG_RIDEBAGMOVEITEM(0)
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_CHARUSESKILL(0,5,-1,0,0)
        gevent.sleep(2)
        self.client.ACGIdle()



#         self.client.taskqueue_append("ACG_RIDEBAGMOVEITEM",0,0)
#         self.client.taskqueue_append("ACGIdle",1)
#         self.client.taskqueue_append("ACG_CHARUSESKILL",0,0,5,-1,0,0) 
#         self.client.taskqueue_append("ACGIdle",3)
#         self.client.taskqueue_append("AFreezeToAction",0,"ACGIdle",1)
#         self.client.taskqueue_append("ACGIdle",1)

#         for i in range(0,100):
#             self.client.taskqueue_append("ACG_CHARMOVE",0, 156, random.randint(156,230))
#             self.client.taskqueue_append("ACGIdle",6)

        self.client.taskqueue_append("ACGIdle",999999)

        
        

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