# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/02/07 by luzhenyu
-----------------------------------------------------------------------
Description:    yingxiongshilian
-----------------------------------------------------------------------
History:
2017/02/07 luzhenyu created
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
import random

# visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"


class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__(*args, **kwargs)
        self.client = project.projectmodule.person(True)
        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName']) + ' login, socket error!!!'
            self.client['socket'].close()
            raise

        gevent.sleep(2)

        # 升级
        self.client.ACG_COMMAND(u'levelup = 15')
        gevent.sleep(2)
        self.client.ACGIdle()

        # 戴帽子
        self.client.ACG_COMMAND(u'createitem = 10101052 = =1')
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACGUseEquip()
        gevent.sleep(2)
        self.client.ACGIdle()


        # 转场到苏州百晓生旁
        self.client.changescreenposition(1, 163, 130)
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()

        # # 向百晓生申请试炼 这个没有卵用
        # self.client.ACGEventRequest(6,900011,1)
        # gevent.sleep(2)
        # self.client.ACGIdle()
        # gevent.sleep(2)
        # self.client.ACGIdle()


        #申请生成场景
        self.client.ACG_EXECUTESCRIPT(900011, u'HeroTrials', [1,1])
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()

        #进入场景中
        self.client.ACGAskChangeScene()
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()

        #开始打
        self.client.taskqueue_append("ACG_CHARMOVE", 0, random.randint(30, 36), random.randint(30, 36))
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACG_CHARMOVE", 0, random.randint(30, 36), random.randint(30, 36))
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACG_CHARMOVE", 0, random.randint(30, 36), random.randint(30, 36))
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACG_CHARMOVE", 0, 33, 33)
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACG_CHARUSESKILL", 0, 0, 303, -1, 0, 0)  # AOE
        self.client.taskqueue_append("ACGIdle", 1)
        self.client.taskqueue_append("ACG_EXECUTESCRIPT", 0, 900011, u'HeroTrials', [2, 0])
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACGIdle", 3)
        self.client.taskqueue_append("ACGIdle", 3)



class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200

    class task_set(TaskSet):
        @task(10)
        def chat(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName'] + u' perform task, exception error!!!'
                traceback.print_exc()
                self.client.taskqueue_cleanup()
                self.client['socket'].close()
                raise


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()