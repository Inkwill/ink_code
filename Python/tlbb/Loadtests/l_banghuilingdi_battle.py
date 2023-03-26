# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/2/9 by ChengLongLong
-----------------------------------------------------------------------
Description:    帮会领地--战斗
-----------------------------------------------------------------------
History:   
2017/2/9 
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import random
import gevent
import traceback

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"

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
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.changescreenposition(0, 111, 155)
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.AGUILD_CGW_ASKINFO(-1,3,1)
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 1,2)
        self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 0,2)

        self.client.APACKET_CG_CGW_PACKET()
        gevent.sleep(2)
        self.client.ACGIdle()

        #进入营地
        self.client.ACG_EXECUTESCRIPT_lingdi(880004,u'AskEnterBattle',[])
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACGAskChangeScene()
        gevent.sleep(3)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)
        gevent.sleep(3)
        self.client.ACGIdle()

        self.client['state_lingdi'] = 'start'

        self.client.taskqueue_append("battle_banghuilingdi", 0)
        self.client.taskqueue_append("ACGIdle", 0.2)


class TestPerson(GameLocust):
    max_wait = 600
    min_wait = 500

    class task_set(TaskSet):
        @task(10)
        def lingdi_ballte(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName'] + u' perform task, exception error!!!'
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)

if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()
