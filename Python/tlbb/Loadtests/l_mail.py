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
        guidL, guidh = project.projectmodule.Tasks.Actions.NetPackets.TLSocket.DecodeUInt64(self.client['m_Guid'])


        '''
        self.client.ACG_COMMAND(u'sendsystemmail = %s = "I just testing the mail system!" = 30000001' % guidL, 'PACKET_GC_NOTIFY_MAIL_NEW')
        self.client.ACGIdle()
        self.client.ACG_ASK_MAIL_LIST(0)
        self.client.ACGIdle()
        self.client.ACG_ONEKEY_GET_MAIL_APPEND()
        '''
        self.client['mailFlag'] = 0
        self.client.taskqueue_append("ACGIdle",35)
        self.client.taskqueue_append("ACG_COMMAND",0, u'sendsystemmail = %s = "I just testing the mail system!" = 30000001' % guidL,'PACKET_GC_NOTIFY_MAIL_NEW')
        self.client.taskqueue_append("ACGIdle",30)
        self.client.taskqueue_append("ACG_ASK_MAIL_LIST", 0, 0)
        self.client.taskqueue_append("ACGIdle",30)
        self.client.taskqueue_append("ACG_ONEKEY_GET_MAIL_APPEND", 0)
        self.client.taskqueue_append("ACGIdle",25)



class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def chat(self):
            try:
#                if project.projectmodule.Tasks.Actions.Functions.is_trigger_start():
                self.client.taskqueue_execute()
#                else:
#                    self.client.ACGIdle()
            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
                traceback.print_exc()
                print "self.buf:", self.client['inputbuffer']
                print e
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