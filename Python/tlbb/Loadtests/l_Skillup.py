# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/22 by wuqiongȻ��wuqiong_yd@cyou-inc.com)
-----------------------------------------------------------------------
Description:    tlbb Skill_levelup 

-----------------------------------------------------------------------
History:   
2016/09/20: 吴琼创建

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
        
        
        self.client.ACG_COMMAND(u'levelup = 50')
        self.client.ACG_COMMAND(u'addmoney = 999999')
        
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,301,1,2,2)   
        self.client.taskqueue_append("ACGIdle",60)
        self.client.taskqueue_append("ACGAskStudyXinFa",0,2,301,1,49,2) 
        self.client.taskqueue_append("ACGIdle",60)  
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,302,1,42,2)  
        self.client.taskqueue_append("ACGIdle",60) 
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,303,1,42,2)  
        self.client.taskqueue_append("ACGIdle",60)  
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,304,1,42,2)  
        self.client.taskqueue_append("ACGIdle",60) 
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,309,2,41,2)    
        self.client.taskqueue_append("ACGIdle",60)
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,310,2,41,2)   
        self.client.taskqueue_append("ACGIdle",60)
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,311,2,41,2)   
        self.client.taskqueue_append("ACGIdle",60)
        self.client.taskqueue_append("ACGAskStudyXinFa",0,1,312,2,41,2)   
        self.client.taskqueue_append("ACGIdle",60) 
        
        self.client.taskqueue_append("AFreezeToAction",0,"ACGIdle",0)

        

class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
        
    
    class task_set(TaskSet):
        @task(1)
        #random
        def login(self):
            try:
                if project.projectmodule.Tasks.Actions.Functions.is_trigger_start():
                    self.client.taskqueue_execute()
                else:
                    self.client.ACGIdle()

            except Exception, e:
                print str(self.client['account'])+' perform task, exception error!!!'
                self.client.taskqueue_cleanup()
                self.client['socket'].close()
                logging.exception(e)
                raise
