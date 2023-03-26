# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/9/14 by ��Ʒ��
-----------------------------------------------------------------------
Description:    切换场景 ,移动,排行榜,邮件
-----------------------------------------------------------------------
History:   
2016/09/14
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


#{ԭ����id:��Ŀ�곡��ID��[[���͵�λ��x,y]]�� Ŀ�곡��Id:��,}
scenedic={1:{31: [148.0, 14.0],},
          31:{1: [5.0, 84.0]}}
#{sceneId: [[move x, move_y],]}
movedic = {1: [[159.29, 22.96], [159.22, 35.01], [157.49, 30.87]],
           31:[[11.0,87.0],[17.45, 97.99],[20.91, 93.20],[21.35, 89.54]]}
#gm:[[GM���ﳡ��ID, ����x,����y], [moveλ��[x,y],[x,y]], [���͵�λ��x,y, �Ƿ��״δ�����Ҫȷ��(1:�ǣ�0������)], [����move[x,y],[x,y], [����λ��x,y]]],
# ]
scenedic = [[[1, 158, 18], [[153.57, 17.12], [151.08, 16.26]], [148.0, 14.0, 1], [[9.96, 87.89],[8.46, 85.90]], [5.0, 84.0, 0]], #����-ҹ����
            #[[31, 53, 177], [[51.77, 177.27], [53.23, 178.38]], [50.0, 180.0], [[98.00, 181.60], [99.13, 182.85]], [97.0, 185.0]], #ҹ����-������
            #[[1, 34, 163], [[34.27, 164.65], [33.57,162.91]], [29.0, 166.0], [[7.29, 166.00], [7.73, 166.79]], [4.0, 170.0]], #����-����ׯ
            #[[10, 232, 119], [[232.12, 117.55], [232.97, 118.66]], [237.0, 118.0], [[36.94, 11.70], [34.67, 10.70]], [36.0, 6.0]], #������-����ׯ
            ]

COUNT = 0
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
        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'levelupallxiulian = 80')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'levelup = 80')
        gevent.sleep(2)
        self.client.ACGIdle()
        
        self.client.ACGIdle()
        guidL, guidh = project.projectmodule.Tasks.Actions.NetPackets.TLSocket.DecodeUInt64(self.client['m_Guid'])
        self.client['mailFlag'] = 0


        #for item in scenedic:
        global COUNT
        item = scenedic[COUNT% len(scenedic)]
        COUNT += 1
        self.client.changescreenposition(item[0][0],item[0][1],item[0][2])
        

        

        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[1][0][0], item[1][0][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[1][1][0], item[1][1][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[2][0], item[2][1])
        self.client.taskqueue_append("ACGRequireRankList", 0 ,0, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,1, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,2, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,4, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,3, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,5, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,6, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_COMMAND",0, u'sendsystemmail = %s = "I just testing the mail system!" = 30000001' % guidL,'PACKET_GC_NOTIFY_MAIL_NEW')
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACG_ASK_MAIL_LIST", 0, 0)
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACG_ONEKEY_GET_MAIL_APPEND", 0)
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("changescene",0, item[2][2])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[3][0][0], item[3][0][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[3][1][0], item[3][1][1])
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_CHARMOVE",0, item[4][0], item[4][1])
        self.client.taskqueue_append("ACGRequireRankList", 0 ,0, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,1, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,2, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,4, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,3, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,5, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACGRequireRankList", 0 ,6, 1, 10 )
        self.client.taskqueue_append("ACGIdle",5)
        self.client.taskqueue_append("ACG_COMMAND",0, u'sendsystemmail = %s = "I just testing the mail system!" = 30000001' % guidL,'PACKET_GC_NOTIFY_MAIL_NEW')
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACG_ASK_MAIL_LIST", 0, 0)
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("ACG_ONEKEY_GET_MAIL_APPEND", 0)
        self.client.taskqueue_append("ACGIdle",10)
        self.client.taskqueue_append("changescene",0, item[4][2])



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
                traceback.print_exc()
                self.client.taskqueue_cleanup()
                self.client['socket'].close()
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(120)
                    res = eval(Login)
                    
                self.client.ACGIdle()
                guidL, guidh = project.projectmodule.Tasks.Actions.NetPackets.TLSocket.DecodeUInt64(self.client['m_Guid'])
                self.client['mailFlag'] = 0
                                    
                global COUNT
                item = scenedic[COUNT% len(scenedic)]
                COUNT += 1
                self.client.changescreenposition(item[0][0],item[0][1],item[0][2])
                
                self.person['iscomfirm'] = None
                
                self.client.taskqueue_cleanup()
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_CHARMOVE",0, item[1][0][0], item[1][0][1])
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_CHARMOVE",0, item[1][1][0], item[1][1][1])
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_CHARMOVE",0, item[2][0], item[2][1])
                self.client.taskqueue_append("ACGRequireRankList", 0 ,0, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,1, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,2, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,4, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,3, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,5, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,6, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_COMMAND",0, u'sendsystemmail = %s = "I just testing the mail system!" = 30000001' % guidL,'PACKET_GC_NOTIFY_MAIL_NEW')
                self.client.taskqueue_append("ACGIdle",10)
                self.client.taskqueue_append("ACG_ASK_MAIL_LIST", 0, 0)
                self.client.taskqueue_append("ACGIdle",10)
                self.client.taskqueue_append("ACG_ONEKEY_GET_MAIL_APPEND", 0)
                self.client.taskqueue_append("ACGIdle",10)
                self.client.taskqueue_append("changescene",0, item[2][2])
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_CHARMOVE",0, item[3][0][0], item[3][0][1])
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_CHARMOVE",0, item[3][1][0], item[3][1][1])
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_CHARMOVE",0, item[4][0], item[4][1])
                self.client.taskqueue_append("ACGRequireRankList", 0 ,0, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,1, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,2, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,4, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,3, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,5, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACGRequireRankList", 0 ,6, 1, 10 )
                self.client.taskqueue_append("ACGIdle",5)
                self.client.taskqueue_append("ACG_COMMAND",0, u'sendsystemmail = %s = "I just testing the mail system!" = 30000001' % guidL,'PACKET_GC_NOTIFY_MAIL_NEW')
                self.client.taskqueue_append("ACGIdle",10)
                self.client.taskqueue_append("ACG_ASK_MAIL_LIST", 0, 0)
                self.client.taskqueue_append("ACGIdle",10)
                self.client.taskqueue_append("ACG_ONEKEY_GET_MAIL_APPEND", 0)
                self.client.taskqueue_append("ACGIdle",10)
                self.client.taskqueue_append("changescene",0, item[4][2])
                    
                    


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()