# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/28 by yaojun
-----------------------------------------------------------------------
Description:
-----------------------------------------------------------------------
History:   
2016/10/28
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import gevent
import logging
import traceback
#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"

class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        self.client['monsterdic'] = {}
        self.client['targetmark'] = [17]

        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise

        self.client.ACG_COMMAND(u'createitem =10101052 =','PACKET_GC_NOTIFYEQUIP')
        gevent.sleep(2)
        self.client.ACGIdle()
        
        self.client.ACGUseEquip()
        gevent.sleep(2)
        self.client.ACGIdle()
        
        
        self.client.taskqueue_append("Mission",0,0)
        self.client.taskqueue_append("ACGIdle",3)
        self.client.taskqueue_append("ACGAskQuit",0)
        self.client.taskqueue_append("reborn",0)
        self.client.taskqueue_append("login",0,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)
        self.client.taskqueue_append("ACGIdle",3)
        self.client.taskqueue_append("ACG_COMMAND",0,u'createitem =10101052 =','PACKET_GC_NOTIFYEQUIP')
        self.client.taskqueue_append("ACGIdle",3)
        self.client.taskqueue_append("ACGUseEquip",0)
        self.client.taskqueue_append("ACGIdle",3)
                                           
class TestPerson(GameLocust):
    min_wait = 500
    max_wait = 600
    
    class task_set(TaskSet):
        @task(10)    
        def chat(self):
            try:
                if project.projectmodule.Tasks.Actions.Functions.is_trigger_start():
                    self.client.taskqueue_execute()
                else:
                    self.client.ACGIdle()
            except Exception,e:
                print self.client['userName']+ u' perform task, exception error!!!'
                print Exception,":",e
                gevent.sleep(60)
                self.client['userName'] = None
                self.client.reborn()
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(120)
                    res = eval(Login)
                self.client.ACG_COMMAND(u'createitem =10101052 =','PACKET_GC_NOTIFYEQUIP')
                gevent.sleep(2)
                self.client.ACGIdle()
                
                self.client.ACGUseEquip()
                gevent.sleep(2)
                self.client.ACGIdle()
