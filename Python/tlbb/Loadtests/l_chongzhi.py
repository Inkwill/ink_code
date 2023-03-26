# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/11/18 by 粟品容
-----------------------------------------------------------------------
Description:    tlbb 充值压测
-----------------------------------------------------------------------
History:
2016/11/18：粟品容创建
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

Login = "self.client.login_chongzhi(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"

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


        gevent.sleep(2)
        self.client.ACG_ASK_BALANCE(0)
        self.client.taskqueue_append("ACG_ASK_BALANCE", 0, 1)
        self.client.taskqueue_append("ACGIdle",60)



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
                print "self.buf:", self.client['inputbuffer']
                print e
                raise


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()