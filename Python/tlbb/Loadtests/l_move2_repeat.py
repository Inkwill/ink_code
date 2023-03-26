# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/11/9 by luoyunpeng
-----------------------------------------------------------------------
Description:    登陆,移动,再登出,换一个帐号,登陆,移动再登出,一直重复做下去
-----------------------------------------------------------------------
History:   
2016/11/9 luoyunpeng
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import time
import gevent
import logging
#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"
ReLogin = "self.client.relogin(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"

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
            print self.client['userName']+ u' login, socket error!!!'
            self.client['socket'].close()
            raise


        gevent.sleep(3)
        self.client.taskqueue_append("ACG_CHARMOVE",0,13.8997402191,38.984954834)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,11.741771698,37.3592605591)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,10.4629402161,39.2045898438)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,11.8052043915,40.9342956543)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,13.9375457764,40.6074638367)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,15.7044277191,39.5217819214)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,14.8258543015,37.5096702576)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,12.2444438934,37.2290306091)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACG_CHARMOVE",0,13.6825141907,38.9691619873)
        self.client.taskqueue_append("ACGIdle",2)
        self.client.taskqueue_append("ACGAskQuit",0)
        self.client.taskqueue_append("reborn",0)
        self.client.taskqueue_append("login",0,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)
        self.client.taskqueue_append("ACGIdle",3)

        


class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def chat(self):
            try:
                self.client.taskqueue_execute()
            except Exception,e:
                print self.client['userName']+ u' perform task, exception error!!!'
                print Exception,":",e
                gevent.sleep(60)
                self.client['userName'] = None
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(120)
                    res = eval(Login)
                #self.client.taskqueue_cleanup()
                #self.client['socket'].close()
                #logging.exception(e)
                #raise


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()