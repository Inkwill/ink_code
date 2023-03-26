# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/10/18 by 姚俊
-----------------------------------------------------------------------
Description:    天龙八部   创建帮会 且帮会人数加到上限
-----------------------------------------------------------------------
History:   
2016/10/18：姚俊创建
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
class GameLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GameLocust, self).__init__( *args, **kwargs)
        self.client = project.projectmodule.person(False)
        
        try:
            res = eval(Login)
            while (res[0] == False):
                gevent.sleep(600)
                res = eval(Login)
        except socket.error, info:
            print str(self.client['userName'])+' login, socket error!!!'
            self.client['socket'].close()
            raise
            

        PosList = [[204,147],[204,148],[204,149],[203,149],[203,147],[203,147]]
        
        
        templist = PosList[random.randint(0,5)]
        
        self.client.ACG_COMMAND(u'levelup = 49')
        gevent.sleep(5)
        self.client.ACGIdle()
        
        self.client.ACG_COMMAND(u'addmoney = 500000')
        gevent.sleep(5)
        self.client.ACGIdle()

        self.client.changescreenposition(0, 149, 180)
        gevent.sleep(5)
        self.client.ACGIdle()

        #没有帮会的玩家打开帮会页面
        self.client.AGUILD_CGW_ASKLIST()
        gevent.sleep(5)
        self.client.ACGIdle()

        '''
        #有帮会的玩家，打开帮会界面. 这是帮主的
        #type = 1, 0 表示帮众信息或者帮会信息
        #帮会成员信息，会返回申请列表的成员消息。
        #self.client['applylist']
        self.client.AGUILD_CGW_ASKINFO(guild_id=2, type=1)
        self.client.AGUILD_CGW_ASKINFO(guild_id =2, type=0)
        #帮会事件 该包有问题。
        self.client.AGUILD_CGW_GUILDEVENT(guildId = 591381130397311112)


        #帮会收人 self.client['applylist']中guild
        self.client.AGUILD_CGW_RECRUIT(proposerGuid = 0)

        #帮主
        self.client['guildMembercount'] = 0
        self.client['applylist'] = []
        while self.client['guildMembercount'] < 50:
            self.client.AGUILD_CGW_ASKINFO(m_GuildId=2, m_Type=1)
            self.client.AGUILD_CGW_ASKINFO(m_GuildId =2, m_Type=0)
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()
            for guid in self.client['applylist']:
                self.client.AGUILD_CGW_RECRUIT(guid)
        '''



        global COUNT
        global guildIdDic
        count = COUNT /50
        master = COUNT % 50
        COUNT += 1

        self.client['m_Serial'] = 0
        if master == 0:
            self.client['guildMembercount'] = 0
            self.client['applylist'] = []
            self.client['m_guildId'] = -1
            #创建帮会, 创建后，获得了帮会Id： self.client['m_guildId']
            self.client.ACGGuildApply()
            gevent.sleep(5)
            self.client.ACGIdle()

            while self.client['m_guildId'] < 0:
                gevent.sleep(5)
                self.client.ACGIdle()
            guildid = self.client['m_guildId']

            guildIdDic[count] = [self.client['m_guildId'], self.client['guildMembercount']]

            #有帮会的玩家，打开帮会界面. 这是帮主的
            #type = 1, 0 表示帮众信息或者帮会信息
            #帮会成员信息，会返回申请列表的成员消息。
            #self.client['applylist']
            self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 1)
            self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 0)

            self.client.APACKET_CG_CGW_PACKET()
            #帮会事件 该包有问题。 最后发现这是传的玩家的guid ?
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


            while self.client['guildMembercount'] < 50:
                self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 1)
                self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 0)
                self.client.APACKET_CG_CGW_PACKET()
                self.client.AGUILD_CGW_GUILDEVENT()
                gevent.sleep(5)
                self.client.ACGIdle()
                gevent.sleep(5)
                self.client.ACGIdle()
                gevent.sleep(5)
                self.client.ACGIdle()

                guilLs = self.client['applylist']
                self.client['applylist'] = []
                for guid in guilLs:
                    self.client.AGUILD_CGW_RECRUIT(guid)
                    gevent.sleep(0)
                    self.client.ACGIdle()
                    self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 1)
                    self.client.AGUILD_CGW_ASKINFO(self.client['m_guildId'], 0)
                    self.client.APACKET_CG_CGW_PACKET()
                    self.client.AGUILD_CGW_GUILDEVENT()
                    gevent.sleep(0)
                    self.client.ACGIdle()
            guildIdDic.pop(count)

        else:

            while count not in guildIdDic:
                gevent.sleep(5)
                self.client.ACGIdle()
            guildid = guildIdDic[count][0]
            #guildid = 0

            #没有帮会的玩家打开帮会页面
            self.client.AGUILD_CGW_ASKLIST()
            gevent.sleep(5)
            self.client.ACGIdle()
            #按ID查找帮会
            self.client.AGUILD_CGW_FINDER(1, guildid)
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()

            #申请加入帮会，ID查找后申请
            self.client.APACKET_CG_GUILD_JOIN(guildid)
            gevent.sleep(5)
            self.client.ACGIdle()
            gevent.sleep(5)
            self.client.ACGIdle()


        self.client.ACGAskServerTime()
        gevent.sleep(5)
        self.client.ACGIdle()

        #self.client.taskqueue_append("AGUILD_CGW_ASKINFO", 0, guildid, 1)
        #self.client.taskqueue_append("ACGIdle",5)
        #self.client.taskqueue_append("AGUILD_CGW_ASKINFO", 0, guildid, 0)
        #self.client.taskqueue_append("ACGIdle",5)
        #self.client.taskqueue_append("AGUILD_CGW_GUILDEVENT", 0, guildid)
        self.client.taskqueue_append("ACGIdle",60)
        

class Testclient(GameLocust):
    min_wait = 800
    max_wait = 1200
    
    class task_set(TaskSet):
        @task(10)    
        def laosanhuan(self):
            try:
                self.client.taskqueue_execute()
            except Exception, e:
                print self.client['userName']+ u' perform task, exception error!!!'
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
