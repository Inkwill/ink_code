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
import random
import math
#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"

g_NpcObjId = 15
g_ScriptID = 1037
g_ExIndex = 1
COUNT = 0
#camp = 0 宋， camp=1 辽
#[宋[[代郡], []]]
walkls = [[
        [[164.942962646,28.2548599243],[132.601119995,41.7026596069],[129.645553589,80.5891876221],[131.723693848,113.523635864],
        [152.745315552,115.776901245],[155.728225708,116.096633911]], #代郡
        [[164.843048096,28.1891555786],[132.581497192,41.710105896],[128.814483643,83.6268310547],[99.6057510376,90.4715118408],
        [96.6848754883,91.1559829712]], #雁门
        [[163.661987305,29.7613639832],[149.127883911,33.2916259766],[42.0933265686,37.0946769714],[35.3963699341,75.5153884888],
        [34.8812179565,78.4708251953]], #云中
    ], #宋
    [
        [[29.7598495483,166.788421631],[56.3308486938,160.107788086],[147.525268555,155.191589355],[155.093719482,120.219787598],
        [155.728210449,117.287979126]],#代郡
        [[29.3431930542,165.597076416],[55.6859436035,157.042572021],[63.6199188232,105.789916992],[94.3249969482,92.714302063],
        [97.0841827393,91.536819458]], #雁门
        [[29.3431930542,166.578491211],[57.081905365,154.827819824],[57.8430938721,76.9627075195],[37.0678787231,80.025428772],
        [34.0999908447,80.4629592896]]#云中
          ]]#辽

posLs = [
    #[157, 117], #代郡
    #[95, 93], #雁门
    [34, 79],  #云中
]

class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        #{guid:[objId,[x, y]]}
        self.client['targetdic'] = {}
        self.client['death_objId'] = 0

        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise

        #选项list

        #坐骑
        zuoqi_list = [11000020,11000025,11000040,11000045,11000050,11000055,11000060,11000065,11000070,11000080]
        #宠物
        chongwu_list = [50009,50109,50209,50309,50409,50509,52109,52209,52309,52619,52809,52909]
        #时装
        shizhuang_list = [40012006,40012012,40012024,40012042]
        #称号
        chenghao_list = [12,22,33,43,54]


        gevent.sleep(2)
        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'levelupallxiulian = 100')
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'levelup = 100')
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.changescreenposition(0, 149, 180)
        self.client.ACGIdle()
        gevent.sleep(2)
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()


        self.client.ACG_COMMAND(u'createitem =30300000 = = 1')#称号
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_COMMAND(u'settitle =%d' % chenghao_list[random.randint(0,len(chenghao_list)-1)])
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACG_COMMAND(u'openmysticalweapon =1')#神器
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACG_COMMAND(u'createpettomyself = %d' % chongwu_list[random.randint(0,len(chongwu_list)-1)] ) #珍兽
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
        if self.client['m_uPetGuid'] != None:
            self.client.ACG_MANIPULATEPETRET(0,0,0,0,0,self.client['m_uPetGuid'],0)
        gevent.sleep(2)
        self.client.ACGIdle()

        self.client.ACG_COMMAND(u'createitem = %d == 1' % zuoqi_list[random.randint(0,len(zuoqi_list)-1)] )#坐骑
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_RIDEBAGMOVEITEM(1)
        gevent.sleep(2)
        self.client.ACGIdle()
        self.client.ACG_CHARUSESKILL(0,5,-1,0,0)
        gevent.sleep(2)
        self.client.ACGIdle()

        tempId =  shizhuang_list[random.randint(0,len(shizhuang_list)-1)]

        self.client.ACG_COMMAND(u'createitem =%d = =1' % tempId)#时装
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        if self.client['m_Item_guid'] != None:
            self.client.ACG_USEITEM(self.client['m_Item_guid'],1,tempId,1)
        gevent.sleep(2)
        self.client.ACGIdle()


        #到达npc处
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
        self.client['camp'] = None
        res = project.projectmodule.Tasks.Actions.Functions.waitforpacket_with_heartbeat(self.client, "PACKET_GC_NOTIFYCHANGESCENE",60)
        while res[0] == False:
            self.client.ACGIdle()
            res = project.projectmodule.Tasks.Actions.Functions.waitforpacket_with_heartbeat(self.client, "PACKET_GC_NOTIFYCHANGESCENE",60)

        self.client.ACGIdle()
        self.client.ACGAskChangeScene()
        gevent.sleep(5)
        self.client.ACGIdle()
        gevent.sleep(5)
        self.client.ACGIdle()

        self.client['targetdic'] = {}

        self.client.ACGENTERSCENE(1)
        self.client.ACGIdle()
        gevent.sleep(3)
        '''
        self.client.ACGCharAskBaseAttrib(3)
        self.client.ACGIdle()


        #ask team info
        self.client.ACGIdle()
        self.client.ACGAskTeamInfo()
        self.client.ACGIdle()
        #get into the camp's time.
        self.client.ACG_ASKCAMPAIGNCOUNT(1)
        '''
        self.client['state'] = 'start'
        self.client['skillcd'] = 0
        pos = random.choice(posLs)
        self.client.taskqueue_append("battle_songliaodazhan", 0, pos[0], pos[1], 4)
        self.client.taskqueue_append("ACGIdle",0)
                                           
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
                raise
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()