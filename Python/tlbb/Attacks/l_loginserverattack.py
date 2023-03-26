import project
from locust import Locust, task, TaskSet
import random
import binascii
import socket
import struct
import TestParam

#visit http://127.0.0.1:8089/ for loadtest testing

ConnectToServer = "self.client.AConnectToServer(TestParam.server_ip, TestParam.server_port)"


class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        eval(ConnectToServer)
        

class TestPerson(GameLocust):
    min_wait = 100
    max_wait = 1000
    
    class task_set(TaskSet):
        @task(1)    
        def randomattack(self):
            try:
                self.client.AattackRandom()
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                eval(ConnectToServer)

        @task(1)    
        def wrongcontent(self): 
            try:
                self.client.AttackWrongContent(TestParam.account_startwith, TestParam.client_version)
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                eval(ConnectToServer)


        @task(1)    
        def errorsize(self): 
            try:
                self.client.AttackErrorSize(TestParam.account_startwith, TestParam.client_version)
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                eval(ConnectToServer)

        @task(1)
        def errorcontent(self): 
            try:
                self.client.AttackErrorContent()
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                eval(ConnectToServer)

        @task(1)    
        def largecontent(self): 
            try:
                self.client.AttackLargeContent(TestParam.account_startwith, TestParam.client_version)
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                eval(ConnectToServer)
 
        @task(1)    
        def shortcontent(self): 
            try:
                self.client.AttackShortContent(TestParam.account_startwith, TestParam.client_version)
            except socket.error, info:
                print 'reconnect'
                self.client['socket'].close()
                eval(ConnectToServer)
