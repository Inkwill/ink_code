# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/2/16 by ChengLongLong
-----------------------------------------------------------------------
Description:    只上架珍兽
-----------------------------------------------------------------------
History:   
2017/2/16 
=======================================================================
'''

import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import time
import gevent
import logging
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
                gevent.sleep(120)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise

        self.client.changescreenposition(0, 111 + random.random(), 155 + random.random())
        gevent.sleep(2)
        self.client.ACGIdle()

        #添加GM
        self.client.ACG_COMMAND(u'levelup = 50')
        gevent.sleep(1)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'clearbag')
        gevent.sleep(1)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'addmoney =99999999')
        gevent.sleep(1)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'addyuanbao =99999999')
        gevent.sleep(1)
        self.client.ACGIdle()
        self.client.ACG_ASK_EXCHANGEMONEY(999999, 2, 1)
        gevent.sleep(1)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'createpettomyself =52408')
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()

        #上架物品
        self.client.ACG_CONSIGNSALEITEM(self.client['m_uPetGuid'], 1, 200)
        gevent.sleep(3)
        self.client.ACGIdle()

        self.client.taskqueue_append("ACGIdle", 60)


class TestPerson(GameLocust):
    max_wait = 600
    min_wait = 500

    class task_set(TaskSet):
        @task(10)
        def login(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName'] + u' perform task, exception error!!!'
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)

if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()