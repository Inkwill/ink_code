# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/1/19 by 鹿振宇
-----------------------------------------------------------------------
Description:    天龙八部  组队聊天
-----------------------------------------------------------------------
History:   
2017/01/19：鹿振宇创建
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
        
        # self.client.changescreenposition(2,72,38)
        other_account = int(self.client['userName']) + 10000000
        other_person = project.projectmodule.person(True)
        res = other_person.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)
        while (res[0] == False):
            self.client.ACGIdle()
            res = other_person.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)
            



        # other_person.changescreenposition(2,72,38)


        gevent.sleep(2)
        other_person.ACGIdle()


        self.client.ACCTEAMINVITE()


        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        other_person.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        other_person.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        other_person.ACGIdle()


        other_person.ACGTeamApply(self.client['userName'])


        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        other_person.ACGIdle()



        self.client.ACGTeamRetApply()


        gevent.sleep(2)
        other_person.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        other_person.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client['other_person'] = other_person
        self.client['person_set'] = project.projectmodule.personset()

        #开始循环聊天


        self.client['person_set'].taskqueue_append(self.client, "ACGChat",0 ,1 )
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 10)
        self.client['person_set'].taskqueue_append(self.client['other_person'],"ACGChat",0,1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 10)
        

        
        


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

                res = self.client['other_person'].login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)
                while (res[0] == False):
                    self.client.ACGIdle()
                    self.client['other_person'].login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, other_account, TestParam.client_version)




if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client['person_set'].taskqueue_execute()