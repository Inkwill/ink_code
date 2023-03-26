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
import traceback
#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"


#{原场景id:｛目标场景ID：[[传送点位置x,y]]， 目标场景Id:｝,}
scenedic={1:{31: [148.0, 14.0],},
          31:{1: [5.0, 84.0]}}
#{sceneId: [[move x, move_y],]}
movedic = {1: [[159.29, 22.96], [159.22, 35.01], [157.49, 30.87]],
           31:[[11.0,87.0],[17.45, 97.99],[20.91, 93.20],[21.35, 89.54]]}
#gm:[[GM到达场景ID, 到达x,到达y], [move位置[x,y],[x,y]], [传送点位置x,y, 是否首次传送需要确认(1:是，0：不是)], [返回move[x,y],[x,y], [返回位置x,y]]],
# ]
scenedic = [[[1, 158, 18], [[153.57, 17.12], [151.08, 16.26]], [148.0, 14.0, 1], [[9.96, 87.89],[8.46, 85.90]], [5.0, 84.0, 0]], #苏州-夜西湖
            #[[31, 53, 177], [[51.77, 177.27], [53.23, 178.38]], [50.0, 180.0], [[98.00, 181.60], [99.13, 182.85]], [97.0, 185.0]], #夜西湖-燕子屋
            #[[1, 34, 163], [[34.27, 164.65], [33.57,162.91]], [29.0, 166.0], [[7.29, 166.00], [7.73, 166.79]], [4.0, 170.0]], #苏州-聚贤庄
            #[[10, 232, 119], [[232.12, 117.55], [232.97, 118.66]], [237.0, 118.0], [[36.94, 11.70], [34.67, 10.70]], [36.0, 6.0]], #天龙寺-聚贤庄
            ]

COUNT = 0
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
        self.client.ACG_COMMAND(u'levelupallxiulian = 80')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'levelup = 80')
        gevent.sleep(2)
        self.client.ACGIdle()

        '''
        gevent.sleep(2)
        self.client.ACG_CHARMOVE(15.8369722366, 33.5553398132)
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACG_CHARMOVE(15.1706399918, 34.8082885742)
        gevent.sleep(2)
        self.client.ACGIdle()

        gevent.sleep(2)
        self.client['flag'] = 0
        self.client.ACG_COMMAND(u'goto = 158,18 = 1')
        self.client.ACGIdle()
        self.client.changescene()
        '''
        #for item in scenedic:
        global COUNT
        item = scenedic[COUNT% len(scenedic)]
        COUNT += 1
        self.client.changescreenposition(item[0][0],item[0][1],item[0][2])

        self.client.taskqueue_append("ACGIdle",70)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[1][0][0], item[1][0][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[1][1][0], item[1][1][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[2][0], item[2][1])
        self.client.taskqueue_append("changescene",0, item[2][2])
        self.client.taskqueue_append("ACGIdle",70)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[3][0][0], item[3][0][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[3][1][0], item[3][1][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[4][0], item[4][1])
        self.client.taskqueue_append("changescene",0, item[4][2])



        #self.client.taskqueue_append("ACGIdle",10)
        #self.client.taskqueue_append("ACG_CHARMOVE",0, 15.8369722366, 33.5553398132)
        #self.client.taskqueue_append("ACGIdle",8)
        #self.client.taskqueue_append("ACG_CHARMOVE",0, 15.1706399918, 34.8082885742)
        #self.client.taskqueue_append("ACGIdle",8)
        #self.client.taskqueue_append("ACG_CHARMOVE",0, 37.0711364746, 27.0720081329)
        #self.client.taskqueue_append("ACGIdle",8)



        #self.client['flag'] = 0
        #self.client.taskqueue_append("ACG_COMMAND",0, u'goto = 158,18 = 1')
        #self.client.taskqueue_append("ACGIdle",0)

        #self.client.ACG_COMMAND(u'goto = 158,18 = 1')
        #self.client.taskqueue_append("changescene",0)

        #self.client.taskqueue_append("ACGIdle",30)
        #self.client.changescene()

        #self.client.ACG_CHARMOVE(posx,posz)
        #self.client.ACGAskChangeScene()
        #self.client.ACGENTERSCENE()

        #self.client.ACG_COMMAND('userlevelup,41')



        #self.client.taskqueue_append("ACGChat",0,0,0)
        #self.client.taskqueue_append("ACGIdle",180)

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
                print self.client['userName']+ u' perform task, exception error!!!'
                traceback.print_exc()
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)
                
                global COUNT
                item = scenedic[COUNT% len(scenedic)]
                COUNT += 1
                self.client.changescreenposition(item[0][0],item[0][1],item[0][2])
                
                self.person['iscomfirm'] = None
                    
                    


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()