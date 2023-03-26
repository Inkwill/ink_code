# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/12 by 罗运鹏
-----------------------------------------------------------------------
Description:    天龙八部  活动珍珑棋局 ,完成后,切换帐号,继续珍珑棋局
-----------------------------------------------------------------------
History:   
2016/10/12：粟品容
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import random
import gevent
#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"
g_NpcObjId = 5
g_ScriptID = 900008
g_ExIndex = 1
class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        
        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(120)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise
            

        self.client['monsterdic'] ={}
        self.client['targetmark'] = [17]
        self.client['state'] = "start"
        PosList = [[147,146],[147,147],[147,148],[146,147],[146,148],[147,149]]
        
        templist = PosList[random.randint(0,5)]
        
        self.client.taskqueue_append("ACG_COMMAND",0,u'levelup = 40')
        self.client.taskqueue_append("ACGIdle",3)
        self.client.taskqueue_append("ACG_COMMAND",0,u'createitem =10101052 =','PACKET_GC_NOTIFYEQUIP')
        self.client.taskqueue_append("ACGIdle",3)
        self.client.taskqueue_append("ACGUseEquip")
        self.client.taskqueue_append("ACGIdle",3)
        
        self.client.taskqueue_append("changescreenposition",0,1,templist[0],templist[1])
        self.client.taskqueue_append("ACGIdle",2)
        
        self.client.taskqueue_append("ACCTEAMINVITE",0)
        self.client.taskqueue_append("ACGIdle",10)
        
        #测试用
        self.client.taskqueue_append("ACGTeamRetApply",0)
        self.client.taskqueue_append("ACGIdle",5)
        
        
        self.client.taskqueue_append("ACGCharDefaultEvent",0,g_NpcObjId)
        self.client.taskqueue_append("ACGIdle",4)
        self.client.taskqueue_append("ACGMissionSubmit",0,g_NpcObjId,0,3100053,0,0)
        self.client.taskqueue_append("ACGIdle",4)
        
        self.client.taskqueue_append("ACGCharDefaultEvent",0,g_NpcObjId)
        self.client.taskqueue_append("ACGIdle",5)
        
        self.client.taskqueue_append("ACGEventRequest",0,g_NpcObjId,g_ScriptID,g_ExIndex)
        self.client.taskqueue_append("ACGIdle",5)
        
        self.client.taskqueue_append("ACGAskChangeScene",0)
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACGENTERSCENE",0,1)
        self.client.taskqueue_append("ACGIdle",5)
             
        self.client.taskqueue_append("battle_fuben",1800)
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGAskQuit",0)
        self.client.taskqueue_append("reborn",0)
        self.client.taskqueue_append("login",0,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)
        self.client.taskqueue_append("ACGIdle",3)

class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def laosanhuan(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
                print Exception,":",e
                gevent.sleep(60)
                self.client['userName'] = None
                self.client.reborn()
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(120)
                    res = eval(Login)