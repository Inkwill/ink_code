# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/09 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部  燕子坞副本
-----------------------------------------------------------------------
History:   
2016/10/09：姚俊创建
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import random
import gevent
import traceback

#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"
g_NpcObjId = 12
g_ScriptID = 900014
g_ExIndex = 1
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
            

        PosList = [[246,214],[247,216],[248,213],[249,215],[248,216],[247,214]]
        
        
        templist = PosList[random.randint(0,5)]
        
        self.client.ACG_COMMAND(u'levelup = 40')
        gevent.sleep(2)
        self.client.changescreenposition(1,templist[0],templist[1])
        gevent.sleep(2)
        
        self.client.ACCTEAMINVITE()
        gevent.sleep(5)
        self.client.ACGIdle()
        self.client.ACGCharDefaultEvent(g_NpcObjId)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACGEventRequest(g_NpcObjId,g_ScriptID,g_ExIndex)
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACGAskChangeScene()
        gevent.sleep(10)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)
        gevent.sleep(5)
        self.client.ACGIdle()
        gevent.sleep(5)
        self.client.ACGIdle()
        gevent.sleep(5)
        self.client.ACGIdle()
        gevent.sleep(5)
        self.client.ACGIdle()


        self.client['all_monster_dic'] = []

        self.client['battle_monster'] = {}
        self.client['battle_path'] = [(80,10),(75,10),(69,12), (62, 12)
            ,(50, 14)
            , (15, 32), (13, 36),  (16, 33), (21, 42), (30, 48)
            ,(34, 57)
            ,(87, 56), (94, 55), (100, 54), (104, 52), (104, 53)
            , (104, 49), (104, 48), (106, 49), (105, 58)
            , (102, 64), (98, 68), (95, 74), (91, 76)
            , (84, 79), (77, 80), (70, 80), (63, 80)
            , (55, 81), (49, 81), (44, 80), (41, 86)
            , (39, 92), (39, 99), (38, 105), (37, 111)]
        self.client['battle_path_index'] = 0

        self.client.taskqueue_append("battle_path", 300)
        self.client.taskqueue_append("ACGIdle", 1)
        

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
                traceback.print_exc()
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)

                gevent.sleep(2)
                self.client.ACGIdle()
                gevent.sleep(2)
                self.client.ACGIdle()
                gevent.sleep(2)
                self.client.ACGIdle()


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()
