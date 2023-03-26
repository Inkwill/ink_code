# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:
-----------------------------------------------------------------------
Description:    采集功能
-----------------------------------------------------------------------
History:   
2017/1/17：安然创建
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
        self.client.ACG_COMMAND(u'goto =167,167 =1')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'addjiaozi = 1000000')
        gevent.sleep(2)
        self.client.ACGIdle()               
        self.client.ACG_COMMAND(u'createitem =30201301 = =1000')
        gevent.sleep(2)
        self.client.ACGIdle()        
        
        self.client.taskqueue_append('ACG_CHARMOVE',0,157,131)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)    
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)    
        self.client.taskqueue_append('ACG_CHAR_ASK_IMPACTLIST',0)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACG_CHARMOVE',0,178,46)
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACGCharDefaultEvent',0)        
        self.client.taskqueue_append("ACGIdle",1)
        self.client.taskqueue_append('ACGEventRequest',0,43,900133,0)         
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        self.client.taskqueue_append('ACGRequestCollectionSkillLevelUp',0,1) 
        self.client.taskqueue_append("ACGIdle",5)        
        
        

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