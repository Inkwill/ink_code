# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/09 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部  杀星副本
-----------------------------------------------------------------------
History:   
2016/10/09：姚俊创建
=======================================================================
'''
import project
from locust import Locust, task, TaskSet
import socket
import TestParam
import random
import gevent
import traceback

#visit http://127.0.0.1:8089/ for loadtest testing

Login = "self.client.login(TestParam.login_ip,TestParam.login_port,TestParam.server_ip, TestParam.server_port, TestParam.account_startwith, TestParam.client_version)"

COUNT = 0
# count/50 : [guildId, count]
guildIdDic = {}
posLs = [
    [101, 122],  # 天元
    [97, 118],  # 雁门
    [93, 121],  # 云中
    [97, 126]
]
Membercount = 100


class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__(*args, **kwargs)
        self.client = project.projectmodule.person(True)

        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName']) + ' login, socket error!!!'
            self.client['socket'].close()
            raise


        self.client.ACG_COMMAND(u'levelup = 39')
        gevent.sleep(5)
        self.client.ACGIdle()

        self.client.ACG_COMMAND(u'addmoney = 500000')
        gevent.sleep(5)
        self.client.ACGIdle()

        self.client.changescreenposition(0, 149, 180)
        gevent.sleep(5)
        self.client.ACGIdle()

        # 戴帽子
        self.client.ACG_COMMAND(u'createitem = 10101052 = =1')
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
        if self.client['GMItemBagIndex'] is None:
            self.client.ACGGMCommand(u'iamgod')
        else:
            self.client.ACGUseEquip()
        gevent.sleep(2)
        self.client.ACGIdle()

        # 没有帮会的玩家打开帮会页面
        self.client.AGUILD_CGW_ASKLIST()
        gevent.sleep(5)
        self.client.ACGIdle()

        global COUNT
        global guildIdDic
        count = COUNT / Membercount
        master = COUNT % Membercount
        COUNT += 1

        guildName = u'guildr' + str(count)
        if master == 0:
            self.client['guildMembercount'] = 0
            self.client['applylist'] = []
            self.client['m_guildId'] = -1
            # 创建帮会, 创建后，获得了帮会Id： self.client['m_guildId']

            # self.client.ACGGuildApply(guildName)
            self.client.ACGGuildApply()
            gevent.sleep(5)
            self.client.ACGIdle()

            while self.client['m_guildId'] < 0:
                gevent.sleep(5)
                self.client.ACGIdle()
            guildid = self.client['m_guildId']

            guildIdDic[count] = [self.client['m_guildId'], self.client['guildMembercount']]

            # 有帮会的玩家，打开帮会界面. 这是帮主的
            # type = 1, 0 表示帮众信息或者帮会信息
            # 帮会成员信息，会返回申请列表的成员消息。
            # self.client['applylist']
            self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 1)
            self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 0)

            self.client.APACKET_CG_CGW_PACKET()
            # 帮会事件 该包有问题。 最后发现这是传的玩家的guid ?
            self.client.AGUILD_CGW_GUILDEVENT()
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()

        else:

            while count not in guildIdDic:
                gevent.sleep(5)
                self.client.ACGIdle()
            guildid = guildIdDic[count][0]
            memcount = guildIdDic[count][1]
            guildIdDic[count][1] += 1
            if memcount == (Membercount - 1):
                guildIdDic.pop(count)

            # guildid = 0

            # 没有帮会的玩家打开帮会页面
            self.client.AGUILD_CGW_ASKLIST()
            gevent.sleep(5)
            self.client.ACGIdle()
            # 按ID查找帮会
            self.client.AGUILD_CGW_FINDER(1, guildid)
            # self.client.AGUILD_CGW_FINDER(2, guildName = guildName)
            self.client.AGUILD_CGW_ASKLIST()
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()

            # 申请加入帮会，ID查找后申请
            self.client.APACKET_CG_GUILD_JOIN(guildid)
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()

        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(5)
        self.client.ACGIdle()

        self.client.ACGAskServerTime()
        gevent.sleep(5)
        self.client.ACGIdle()

        # 打开帮会界面
        self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 1)
        self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 0)
        self.client.APACKET_CG_CGW_PACKET()
        self.client.AGUILD_CGW_GUILDEVENT()
        # 回到帮会
        self.client.ACG_CHARUSESKILL(0, 14)
        res = project.projectmodule.Tasks.Actions.Functions.waitforpacket_with_heartbeat(self.client,
                                                                                         "PACKET_GC_NOTIFYCHANGESCENE",
                                                                                         60)
        while res[0] == False:
            self.client.ACGIdle()
            res = project.projectmodule.Tasks.Actions.Functions.waitforpacket_with_heartbeat(self.client,
                                                                                             "PACKET_GC_NOTIFYCHANGESCENE",
                                                                                             60)
        self.client.ACGIdle()
        self.client.ACGAskChangeScene()
        gevent.sleep(5)
        self.client.ACGIdle()
        gevent.sleep(5)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)
        self.client.ACGIdle()
        gevent.sleep(3)

        # 到达npc的位置 枯荣大师
        self.client.ACG_CHARMOVE(89, 130)
        gevent.sleep(5)
        self.client.ACGIdle()

        # 打开npc界面
        self.client.ACGCharDefaultEvent(32)
        gevent.sleep(3)
        self.client.ACGIdle()
        self.client.ACGEventRequest(32, 900019, 1)
        gevent.sleep(3)
        self.client.ACGIdle()
        gevent.sleep(3)
        self.client.ACGIdle()

        # 进入场景
        self.client.ACGAskChangeScene()
        gevent.sleep(10)
        self.client.ACGIdle()
        self.client.ACGENTERSCENE(1)

        self.client['battle_monster'] = {}
        self.client['battle_path'] = [(49, 46),(50, 47)]
        self.client['battle_path_index'] = 0

        self.client.taskqueue_append("battle_path", 300)
        self.client.taskqueue_append("ACGIdle", 1)


class Testclient(GameLocust):
    min_wait = 800
    max_wait = 1200

    class task_set(TaskSet):
        @task(10)
        def laosanhuan(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName'] + u' perform task, exception error!!!'
                traceback.print_exc()
                gevent.sleep(600)
                res = eval(Login)
                while (res[0] == False):
                    gevent.sleep(600)
                    res = eval(Login)


if __name__ == '__main__':
    aa = GameLocust()
    while 1:
        aa.client.taskqueue_execute()


