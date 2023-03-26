# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/31 by 粟品容
-----------------------------------------------------------------------
Description:    tlbb 邮件
-----------------------------------------------------------------------
History:
2016/10/31：粟品容创建
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

posls = [[32, 145],[33, 126],[63, 128],[65, 147], [47, 144]]
COUNT = 0
class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        self.client['menpails'] = [2,4,7,8]
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
        self.client.ACG_COMMAND(u'levelupallxiulian = 68')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'levelup = 68')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.changescreenposition(1, 113,167)
        self.client.ACGIdle()
        gevent.sleep(2)


        self.client.ACG_COMMAND(u'addmission = 3100084')
        self.client['MissionIsFinish'] = 0
        gevent.sleep(2)
        self.client.ACGIdle()



        #self.client['mCurrentMission'] = self['m_idMission']
        #self.client['MissionIsFinish'] = self['m_IsFinish']
        #3100054
        self.client.ACGCharDefaultEvent(36)
        while self.client['MissionIsFinish'] != 1:
            self.client.ACGIdle()
        self.client.ACGMissionSubmit(36, 0, self.client['mCurrentMission'], 0, 0)
        self.client['MissionIsFinish'] = 0

        self.client.ACGAskAcceptMission(0, 0, 3100055)
        #3100081
        self.client.ACGCharDefaultEvent(36)
        while self.client['MissionIsFinish'] != 1:
            self.client.ACGIdle()
        self.client.ACGMissionSubmit(36, 0, self.client['mCurrentMission'], 0, 0)
        self.client['MissionIsFinish'] = 0

        #3100084
        self.client.ACGCharDefaultEvent(36)
        while self.client['MissionIsFinish'] != 1:
            self.client.ACGIdle()
        self.client.ACGMissionSubmit(36, 0, self.client['mCurrentMission'], 0, 0)
        self.client['MissionIsFinish'] = 0



        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.changescreenposition(0, 87, 66)
        self.client.ACGIdle()
        gevent.sleep(2)

        self.client.ACG_COMMAND(u'addmission = 3100025')
        self.client['MissionIsFinish'] = 0
        gevent.sleep(2)
        self.client.ACGIdle()

        #3100084
        self.client.ACGCharDefaultEvent(8)
        while self.client['MissionIsFinish'] != 1:
            self.client.ACGIdle()
        self.client.ACGMissionSubmit(8, 0, self.client['mCurrentMission'], 0, 0)
        self.client['MissionIsFinish'] = 0

        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACGUseEquip(17)

        #到秦皇地宫
        self.client.ACGIdle()
        gevent.sleep(2)
        global COUNT
        pos = posls[COUNT % len(posls)]
        COUNT += 1
        self.client.changescreenposition(21, pos[0], pos[1])

        self.client['monsterdic'] = {}
        self.client['targetmark'] = [17]
        self.client['state'] = "start"
        self.client.ACGIdle()
        gevent.sleep(2)


        self.client.taskqueue_append("battle_digong",10)
        self.client.taskqueue_append("ACG_COMMAND",0 , u"full")




        '''
        self.client['mailFlag'] = 0
        self.client.taskqueue_append("ACGIdle",35)
        self.client.taskqueue_append("ACG_COMMAND",0, u'sendsystemmail = %s = "I just testing the mail system!" = 30000001' % guidL,'PACKET_GC_NOTIFY_MAIL_NEW')
        self.client.taskqueue_append("ACGIdle",30)
        self.client.taskqueue_append("ACG_ASK_MAIL_LIST", 0, 0)
        self.client.taskqueue_append("ACGIdle",30)
        self.client.taskqueue_append("ACG_ONEKEY_GET_MAIL_APPEND", 0)
        self.client.taskqueue_append("ACGIdle",25)
        '''
        #self.client.taskqueue_append("ACGIdle",25)


class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200

    class task_set(TaskSet):
        @task(10)
        def chat(self):
            try:
                self.client.taskqueue_execute()

            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
                #traceback.print_exc()
                print Exception
                print e
                self.client.taskqueue_cleanup()
                self.client['socket'].close()
                print "self.buf:", self.client['inputbuffer']
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