# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/01/05 by luzhenyu
-----------------------------------------------------------------------
Description:    综合跑动
-----------------------------------------------------------------------
History:   
2017/01/05 luzhenyu created
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
#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version,True)"



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



        gevent.sleep(3)
        self.client.ACGIdle()
        
        #选项list
        
        #坐骑
        zuoqi_list = [11000020,11000025,11000040,11000045,11000050,11000055,11000060,11000065,11000070,11000080]
        
        #宠物
        chongwu_list = [50009,50109,50209,50309,50409,50509,52109,52209,52309,52619,52809,52909]
        
        #时装
        shizhuang_list = [40012006,40012012,40012024,40012042]
        
        #称号
        chenghao_list = [12,22,33,43,54]



        
        self.client.ACG_COMMAND(u'levelup = 50')
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

        PosList = [[147, 146], [150, 147], [150, 143], [143, 142], [141, 147], [143, 152],[146,149]]

        templist = PosList[random.randint(0, 6)]

        self.client.changescreenposition(27, templist[0],templist[1])

        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()
        gevent.sleep(2)
        self.client.ACGIdle()

#        备用代码，用于在列表中取值
#         list[random.randint(0,len(list)-1)]
 

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
        self.client.ACG_RIDEBAGMOVEITEM(1)
        gevent.sleep(2)
        self.client.ACGIdle()

        if self.client['m_ObjID'] != None:
            self.client.ACG_CHARUSESKILL(0,5)
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

        # self.client.taskqueue_append("ACG_CHARMOVE", 0, 156, random.randint(75, 156))
        # self.client.taskqueue_append("ACGIdle", 6)
        # self.client.taskqueue_append("ACG_CHARMOVE", 0, 156, random.randint(75, 156))
        self.client.taskqueue_append("ACGIdle", 6)

        
        

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
                raise 




if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()


