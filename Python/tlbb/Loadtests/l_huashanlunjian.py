# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/1/19 by ChengLongLong
-----------------------------------------------------------------------
Description:    华山论剑副本
-----------------------------------------------------------------------
History:   
2017/1/19 
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

        gevent.sleep(1)
        self.client.ACGIdle()

        self.client.changescreenposition(0, 111, 155)
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACG_COMMAND(u'levelupallxiulian =90')
        gevent.sleep(1)
        self.client.ACGIdle()

        temp = random.randint(1,3)

        if temp==1:
            self.client.ACG_COMMAND(u'levelup = 45')
            gevent.sleep(1)
            self.client.ACGIdle()
        elif temp ==2:
            self.client.ACG_COMMAND(u'levelup = 65')
            gevent.sleep(1)
            self.client.ACGIdle()
        elif temp ==3:
            self.client.ACG_COMMAND(u'levelup = 85')
            gevent.sleep(1)
            self.client.ACGIdle()

        self.client.AGC_CHARDEFAULTEVENT(49)
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACGEventRequest(49, 2100, 2)
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACGAskChangeScene()
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACGENTERSCENE(1)
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACCTEAMINVITE()
        gevent.sleep(1)
        self.client.ACGIdle()

        self.client.ACG_CHARMOVE(random.random() * 2 + 18, 32 + random.random() * 2)
        gevent.sleep(1)
        self.client.ACGIdle()

        self.client['state_huashan'] = 'start'

        self.client.taskqueue_append("huashanlunjian", 0)
        self.client.taskqueue_append("ACGIdle", 1)


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

