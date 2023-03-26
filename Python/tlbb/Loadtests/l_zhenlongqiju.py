# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/12 by 粟品容
-----------------------------------------------------------------------
Description:    天龙八部  活动珍珑棋局
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
                gevent.sleep(600)
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
        
        self.client.ACG_COMMAND(u'levelup = 40')
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'iamgod')
        gevent.sleep(1)
        self.client.ACGIdle()

        self.client.changescreenposition(1,templist[0],templist[1])
        gevent.sleep(2)
        
        self.client.ACCTEAMINVITE()
        gevent.sleep(10)
        self.client.ACGIdle()
        
        # #测试用
        # self.client.ACGTeamRetApply()
        # gevent.sleep(5)
        # self.client.ACGIdle()
        #
        #
        self.client.ACGCharDefaultEvent(g_NpcObjId)
        gevent.sleep(3)
        self.client.ACGIdle()

        self.client.ACGMissionSubmit(g_NpcObjId,0,3100053,0,0)
        gevent.sleep(3)
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

        self.client['battle_path'] = []
        for i in range(1,16):
            self.client['battle_path'].append((4,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((8,4*i))
        for i in range(1,16):
            self.client['battle_path'].append((12,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((16,4*i))
        for i in range(1,16):
            self.client['battle_path'].append((20,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((24,4*i))
        for i in range(1,16):
            self.client['battle_path'].append((28,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((32,4*i))
        for i in range(1,16):
            self.client['battle_path'].append((36,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((40,4*i))
        for i in range(1,16):
            self.client['battle_path'].append((44,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((48,4*i))
        for i in range(1,16):
            self.client['battle_path'].append((52,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((56,4*i))
        for i in range(1,16):
            self.client['battle_path'].append((60,4*i))
        for i in range(16,1,-1):
            self.client['battle_path'].append((64,4*i))



        self.client['battle_monster'] = {}
        self.client['battle_path_index'] = 0



        # 暂时站到那里不动
        self.client.taskqueue_append("battle_path", 30)
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