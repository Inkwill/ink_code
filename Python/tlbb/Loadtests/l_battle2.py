# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/01/12 by luzhenyu
-----------------------------------------------------------------------
Description:    battle qinhuangdigong
-----------------------------------------------------------------------
History:   
2017/01/12 luzhenyu created
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
        
        #升级
        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()

        #无敌
        self.client.ACG_COMMAND(u'iamgod')
        gevent.sleep(2)
        self.client.ACGIdle()

        
        #转场
        if int(self.client['userName'][1:])%2 == 0:
            self.client.changescreenposition(21, 49, 144)
        else:
            self.client.changescreenposition(34, 49, 144)
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()




        self.client['battle_monster'] = {}
        self.client['battle_path'] = [(random.randint(35,65), random.randint(125,165)), (random.randint(35,65), random.randint(125,165))]
        self.client['battle_path_index'] = 0

        self.client.taskqueue_append("battle_path", 300)
        self.client.taskqueue_append("ACGIdle", 1)

        
        

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