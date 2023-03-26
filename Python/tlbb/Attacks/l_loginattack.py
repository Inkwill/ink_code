import project
from locust import Locust, task, TaskSet
import random
import binascii
import socket
import struct
import TestParam
import gevent

#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"


class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        res = eval(Login)
        while (res[0] == False):
            gevent.sleep(60)
            res = eval(Login)
        

class TestPerson(GameLocust):
    min_wait = 100
    max_wait = 1000
    
    class task_set(TaskSet):
        @task(1)    
        def randomattack(self):
            try:
                self.client.ALoginAttackRandom()
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                gevent.sleep(500)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(60)
                    res = eval(Login)
                    
        @task(1)    
        def wrongcontent(self): 
            try:
                self.client.ALoginAttackWrongContent() 
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                gevent.sleep(500)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(60)
                    res = eval(Login)

        @task(1)    
        def errorsize(self): 
            try:
                self.client.ALoginAttackErrorSize() 
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                gevent.sleep(500)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(60)
                    res = eval(Login)

        @task(1)
        def errorcontent(self): 
            try:
                self.client.ALoginAttackErrorContent() 
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                gevent.sleep(500)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(60)
                    res = eval(Login)

        @task(1)    
        def largecontent(self): 
            try:
                self.client.ALoginAttackLargeContent() 
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                gevent.sleep(500)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(60)
                    res = eval(Login)
 
        @task(1)    
        def shortcontent(self): 
            try:
                self.client.ALoginAttackShortContent() 
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                gevent.sleep(500)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(60)
                    res = eval(Login)
