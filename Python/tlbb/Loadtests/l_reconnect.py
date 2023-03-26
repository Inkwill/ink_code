# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/27
-----------------------------------------------------------------------
Description:    tlbb  断线重连

-----------------------------------------------------------------------
History:   
2016/10/27  粟品容

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
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise

        while 1:
            gevent.sleep(3)
            #self.client.ACG_COMMAND(u'levelup = 20')
            #gevent.sleep(3)
            self.client.ACG_CHARMOVE(13.8997402191,38.984954834)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACG_CHARMOVE(11.741771698,37.3592605591)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACG_CHARMOVE(10.4629402161,39.2045898438)
            self.client.ACGIdle()

            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()

            #print 'began to recconnect'
            self.client['socket'].close()
            #self.client['inputbuffer'] = ""
            res = self.client.AConnectToServer("115.159.28.139",1231)
            while (res[0] == False):
                print "connect to server failed."
                res = self.client.AConnectToServer("115.159.28.139",1231)
            sceneId = self.client['SceneId']
            self.client.ACGConnect(1)
            self.client.ACGIdle()
            self.client.ACGIdle()
            self.client['f_x'] = self.client['posx']
            self.client['f_z'] = self.client['posz']
            self.client['SceneId'] = sceneId
            self.client.ACGENTERSCENE()

            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()
            gevent.sleep(3)
            self.client.ACGIdle()

        '''
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACG_CHARMOVE",0,13.8997402191,38.984954834)
        self.client.taskqueue_append("ACGIdle",12)
        self.client.taskqueue_append("ACG_CHARMOVE",0,11.741771698,37.3592605591)
        self.client.taskqueue_append("ACGIdle",12)
        self.client.taskqueue_append("ACG_CHARMOVE",0,10.4629402161,39.2045898438)
        self.client.taskqueue_append("ACGIdle",12)
        self.client.taskqueue_append("ACG_CHARMOVE",0,11.8052043915,40.9342956543)
        self.client.taskqueue_append("ACGIdle",12)
        '''



class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
        
    
    class task_set(TaskSet):
        @task(1)
        def login(self):
            try:
                self.client.taskqueue_execute() 
            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
                self.client['socket'].close()
                raise
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()