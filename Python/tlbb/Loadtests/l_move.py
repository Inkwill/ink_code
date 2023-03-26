# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/14 by 粟品容
-----------------------------------------------------------------------
Description:    英雄王座 传送功能
-----------------------------------------------------------------------
History:   
2016/09/14：粟品容创建
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


#{原场景id:｛目标场景ID：[[传送点位置x,y]]， 目标场景Id:｝,}
scenedic={1:{31: [148.0, 14.0],},
          31:{1: [5.0, 84.0]}}
#{sceneId: [[move x, move_y],]}
langfang = [[15.8369722366, 33.5553398132], [15.1706399918, 34.8082885742],[37.0711364746, 27.0720081329],
            [53.6416435242, 35.2674789429],
            [50.5798492432,30.1448516846], [60.9219741821, 34.9331321716], [86.8266983032, 32.2625656128]]
movedic = {1: [[159.29, 22.96], [159.22, 35.01], [157.49, 30.87]],
           31:[[11.0,87.0],[17.45, 97.99],[20.91, 93.20],[21.35, 89.54]],
           2:langfang}

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




        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()


        '''
        self.client.ACG_CHARMOVE(15.8369722366, 33.5553398132)
        self.client.ACGIdle()
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACG_CHARMOVE(15.1706399918, 34.8082885742)
        gevent.sleep(3)
        self.client.ACG_CHARMOVE(37.0711364746, 27.0720081329)
        '''

        #self.client.ACGAskChangeScene()
        #self.client.ACGENTERSCENE()


        self.client.ACG_CHARMOVE(self.client['posx']+1, self.client['posz']+1)
        gevent.sleep(2)
        self.client.ACGIdle()


        self.client.ACG_COMMAND(u'levelup = 50')
        gevent.sleep(3)
        self.client.ACGIdle()
        self.client.changescreenposition(1,153,153)
        gevent.sleep(5)
        self.client.ACGIdle()

        

#         length = len(langfang)
#         for i in range(length):
#             self.client.taskqueue_append("ACG_CHARMOVE",0,langfang[i][0],langfang[i][1])
#             self.client.taskqueue_append("ACGIdle",8)
# 
#         for i in range(length):
#             self.client.taskqueue_append("ACG_CHARMOVE",0,langfang[length-i-1][0],langfang[length - i -1][1])
#             self.client.taskqueue_append("ACGIdle",8)
        self.client.taskqueue_append("ACG_CHARMOVE",0,156,156)
        self.client.taskqueue_append("ACGIdle",15)
        self.client.taskqueue_append("ACG_CHARMOVE",0,156,238)
        self.client.taskqueue_append("ACGIdle",15)        

        #self.client.taskqueue_append("ACGIdle",30)

class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def chat(self):
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


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()