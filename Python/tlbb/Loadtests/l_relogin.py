# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/19 by 安然Ȼ��anran3_yd@cyou-inc.com)
-----------------------------------------------------------------------
Description:    tlbb  

-----------------------------------------------------------------------
History:   
2016/09/19: 安然创建

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


class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(15)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise
        
        self.client.taskqueue_append("ACGIdle",15)     
        self.client.taskqueue_append("disconnect",0,90)
        self.client.taskqueue_append("relogin",0,TestParam.server_ip,TestParam.server_port,TestParam.account_startwith,TestParam.client_version)


class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
        
    
    class task_set(TaskSet):
        @task(1)
        #random
        def login(self):
            try:
                self.client.taskqueue_execute() 

            except Exception, e:
                print str(self.client['account'])+' perform task, exception error!!!'
                self.client.taskqueue_cleanup()
                self.client['socket'].close()
                logging.exception(e)
                raise
