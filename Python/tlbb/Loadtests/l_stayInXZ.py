# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/21 by luoyunpeng
-----------------------------------------------------------------------
Description:    �����ֳ��������㸽�������ƶ�
-----------------------------------------------------------------------
History:
2016/09/21 luoyunpeng
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import time
import gevent
import logging

# visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version,False,False)"


class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__(*args, **kwargs)
        self.client = project.projectmodule.person(True)
        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print self.client['userName'] + u' login, socket error!!!'
            self.client['socket'].close()
            raise

        gevent.sleep(3)

        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACGIdle()
        gevent.sleep(2)


        self.client.taskqueue_append("ACGIdle", 5)




class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200

    class task_set(TaskSet):
        @task(10)
        def chat(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName'] + u' perform task, exception error!!!'
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)
                    # self.client.taskqueue_cleanup()
                    # self.client['socket'].close()
                    # logging.exception(e)
                    # raise


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()