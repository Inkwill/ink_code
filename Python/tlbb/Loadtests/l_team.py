# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/29 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部  组队功能
-----------------------------------------------------------------------
History:   
2016/09/29：姚俊创建
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
import traceback
#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"

class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        res = eval(Login)
        while (res[0] == False):
            gevent.sleep(10)
            res = eval(Login)
        
        self.client.ACG_CHARMOVE(11,38)
        other_account = int(self.client['userName'][1:]) + 1000000000
        other_person = project.projectmodule.person(True)
        res = other_person.login(TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)
        while (res[0] == False):
            self.client.ACGIdle()
            res = other_person.login(TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)
            
        self.client['other_person'] = other_person   
        self.client['person_set'] = project.projectmodule.personset()

        self.client['person_set'].taskqueue_append(self.client, "ACCTEAMINVITE", 0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGTeamApply",0,self.client['userName'])
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGTeamRetApply", 0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        
        self.client['person_set'].taskqueue_append(self.client, "ACGTeamLeave", 0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGTeamLeave", 0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle",2)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle",2)

class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def team(self):
            try:
                self.client['person_set'].taskqueue_execute()
            except socket.error, info:
                print self.client['userName']+ u' perform task, exception error!!!'
                traceback.print_exc()
                self.client['socket'].close()
                self.client['other_person']['socket'].close()
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(10)
                    res = eval(Login)
                    
                other_account = int(self.client['m_Account']) + 10000000
                
                res = self.client['other_person'].login(TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)
                while (res[0] == False):
                    self.client.ACGIdle()
                    self.client['other_person'].login(TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)
