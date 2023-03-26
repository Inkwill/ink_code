'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:       
-----------------------------------------------------------------------
Description:    tlbb  

-----------------------------------------------------------------------
History:   
2016/09/19

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
#         try:
#             res = eval(Login)
#             assert res[0] == True
        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(60)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise
        
        self.client.taskqueue_append("ACGIdle",15)     


class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
        
    
    class task_set(TaskSet):
        @task(1)
        def login(self):
            try:
                self.client.taskqueue_execute() 
            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
                traceback.print_exc()
                self.client.taskqueue_cleanup()
                self.client['socket'].close()
                raise 
