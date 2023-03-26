# -*- coding: utf-8 -*-

'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/19 by luoyunpeng
-----------------------------------------------------------------------
Description:
-----------------------------------------------------------------------
History:   
2016/09/16
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
#[[sceneId, posx, poxy, 可随机的位置长度， [怪物的配置相关ID]],]]=
battledic = [[2,54.38, 50.69, 3, [17]], [2, 151.95, 33.29, 3, [17]]]
COUNT = 0
class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        #{objId:[guid, posx, posy]}
        self.client['monsterdic'] = {}

        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise

        self.client.ACG_COMMAND(u'levelup = 20')

        # start, walk, battle
        self.client['state'] = "start"

        global COUNT
        item = battledic[COUNT% len(battledic)]
        COUNT += 1
        self.client['targetmark'] = item[4]
        self.client.changescreenposition(item[0], item[1], item[2])
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()

        #self.client.taskqueue_append("ACGIdle",30)
        self.client.taskqueue_append("battle",0,item[1], item[2], item[3])
        self.client.taskqueue_append("ACGIdle",3)
                                           
class TestPerson(GameLocust):
    min_wait = 500
    max_wait = 600
    
    class task_set(TaskSet):
        @task(10)    
        def chat(self):
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
                    
                self.client['state'] = "start"

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