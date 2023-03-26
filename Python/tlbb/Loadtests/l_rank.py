# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:
-----------------------------------------------------------------------
Description:    排行榜功能
-----------------------------------------------------------------------
History:   
2016/10/26：粟品容创建
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
        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.taskqueue_append("ACGRequireRankList", 0 ,0, 1, 10 )
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,1, 1, 10 )
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,2, 1, 10 )
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,4, 1, 10 )
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,3, 1, 10 )
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,5, 1, 10 )
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,6, 1, 10 )
        self.client.taskqueue_append("ACGIdle",15)


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
                print Exception
                print e
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()