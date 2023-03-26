# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/12/13 by ChengLongLong
-----------------------------------------------------------------------
Description:    玩家商店
-----------------------------------------------------------------------
History:   
2016/12/13 
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import gevent
import random
import logging
import traceback
#visit http://127.0.0.1:8089/ for loadtest testing
Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"
class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(True)
        res = eval(Login)
        while (res[0] == False):
            gevent.sleep(10)
            res = eval(Login)
        # self.client.ACG_CHARMOVE(11 + random.randint(-5, 5), 38 + random.randint(-5, 5))
        other_account = self.client['userName'][1:] + 'a'
        other_person = project.projectmodule.person(True)
        res = other_person.login(TestParam.login_ip,TestParam.login_port, TestParam.server_ip, TestParam.server_port,other_account, TestParam.client_version)
        while (res[0] == False):
            self.client.ACGIdle()
            res = other_person.login(TestParam.login_ip,TestParam.login_port, TestParam.server_ip, TestParam.server_port,other_account, TestParam.client_version)

        self.client['other_person'] = other_person
        self.client['person_set'] = project.projectmodule.personset()

        self.client.changescreenposition(0, 111 + random.random(), 155 + random.random())
        gevent.sleep(2)
        self.client.ACGIdle()
        other_person.ACGIdle()

        other_person.changescreenposition(0, 111 + random.random(), 155 + random.random())
        gevent.sleep(2)
        self.client.ACGIdle()
        other_person.ACGIdle()

        #第一个person添加GM
        self.client.ACG_COMMAND(u'levelup = 50')
        gevent.sleep(1)
        self.client.ACGIdle()
        other_person.ACGIdle()
        self.client.ACG_COMMAND(u'clearbag')
        gevent.sleep(1)
        self.client.ACGIdle()
        other_person.ACGIdle()
        self.client.ACG_COMMAND(u'addmoney =99999999')
        gevent.sleep(1)
        self.client.ACGIdle()
        other_person.ACGIdle()
        self.client.ACG_COMMAND(u'addyuanbao =99999999')
        gevent.sleep(1)
        self.client.ACGIdle()
        other_person.ACGIdle()
        self.client.ACG_ASK_EXCHANGEMONEY(999999, 2, 1)
        gevent.sleep(1)
        self.client.ACGIdle()
        other_person.ACGIdle()
        self.client.ACG_COMMAND(u'createitem =30201000 =2 =1')
        gevent.sleep(1)
        self.client.ACGIdle()
        other_person.ACGIdle()

        #第二个person添加GM
        other_person.ACG_COMMAND(u'levelup = 50')
        gevent.sleep(1)
        other_person.ACGIdle()
        self.client.ACGIdle()
        other_person.ACG_COMMAND(u'clearbag')
        gevent.sleep(1)
        other_person.ACGIdle()
        self.client.ACGIdle()
        other_person.ACG_COMMAND(u'addmoney =99999999')
        gevent.sleep(1)
        other_person.ACGIdle()
        self.client.ACGIdle()
        other_person.ACG_COMMAND(u'addyuanbao =99999999')
        gevent.sleep(1)
        other_person.ACGIdle()
        self.client.ACGIdle()
        other_person.ACG_ASK_EXCHANGEMONEY(999999, 2, 1)
        gevent.sleep(1)
        other_person.ACGIdle()
        self.client.ACGIdle()

        #第一个人查阅玩家商店
        #查询45级老虎
        self.client['person_set'].taskqueue_append(self.client, "ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA", 0, 2, 36, 45, 0, -1, -1)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGAskConsignSaleItemInfo", 0, 2, 36, 45, 14, 0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        #查询 忘无石
        self.client['person_set'].taskqueue_append(self.client, "ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA", 0, 3, -1, -1, 0, 2, 2)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGAskConsignSaleItemInfo", 0, 3, 30000305, 0, 999,0,1,30000305)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        #查询 培养材料--装备强化--地煞
        self.client['person_set'].taskqueue_append(self.client, "ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA", 0, 3,-1,-1,0,3,0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGAskConsignSaleItemInfo", 0, 3,30000001,0,999,0,1,30000001)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        # 查询 任务道具--采集物--兽牙
        self.client['person_set'].taskqueue_append(self.client, "ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA", 0, 3, -1, -1, 0,4, 0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGAskConsignSaleItemInfo", 0, 3, 30201212, 0, 999,0, 1,30201212)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        # 查询 珍兽技能--手动技--附身
        self.client['person_set'].taskqueue_append(self.client, "ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA", 0, 3, -1, -1, 0,5, 0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGAskConsignSaleItemInfo", 0, 3, 40001008, 0, 999, 0,1,40001008)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)

        # 第一个人上架物品
        self.client['person_set'].taskqueue_append(self.client, "ACG_CONSIGNSALEITEM", 0, self.client['m_Item_guid'], 1, 200)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACG_CANCELCONSIGNSALEITEM", 0, self.client['m_Item_guid'])
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACG_CONSIGNSALEITEM", 0, self.client['m_Item_guid'], 1,200)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)

        #第二个人买物品
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA", 0, 3,-1,-1,0,6,0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGAskConsignSaleItemInfo", 0, 3, 30201000, 0, 999, 0, 1, 30201000)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACG_BUY_CONSIGNSALEITEMINFO", 0, 3,1,30201000,999,self.client['m_Item_guid'],1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)

        #第二个人上架物品
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACG_CONSIGNSALEITEM", 0, self.client['m_Item_guid'], 1, 200)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)

        #第一个人买物品
        self.client['person_set'].taskqueue_append(self.client, "ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA", 0, 3,-1,-1,0,6,0)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGAskConsignSaleItemInfo", 0, 3, 30201000, 0, 999, 0, 1, 30201000)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACG_BUY_CONSIGNSALEITEMINFO", 0, 3,1,30201000,999,self.client['m_Item_guid'],1)
        self.client['person_set'].taskqueue_append(self.client['other_person'], "ACGIdle", 1)
        self.client['person_set'].taskqueue_append(self.client, "ACGIdle", 1)


class TestPerson(GameLocust):
    min_wait = 800
    max_wait = 1200

    class task_set(TaskSet):
        @task(10)
        def playershop(self):
            try:
                self.client['person_set'].taskqueue_execute()
            except socket.error, info:
                print self.client['userName'] + u' perform task, exception error!!!'
                traceback.print_exc()
                self.client['socket'].close()
                self.client['other_person']['socket'].close()
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(10)
                    res = eval(Login)

                other_account = self.client['userName'][1:] + 'a'

                res = self.client['other_person'].login(TestParam.login_ip,TestParam.login_port, TestParam.server_ip, TestParam.server_port,other_account, TestParam.client_version)
                while (res[0] == False):
                    self.client.ACGIdle()
                    self.client['other_person'].login(TestParam.login_ip,TestParam.login_port, TestParam.server_ip, TestParam.server_port,other_account, TestParam.client_version)




