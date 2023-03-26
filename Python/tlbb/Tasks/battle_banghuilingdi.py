# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/2/9 by ChengLongLong
-----------------------------------------------------------------------
Description:    帮会领地战斗
-----------------------------------------------------------------------
History:   
2017/2/9 
=======================================================================
'''
import gevent
import random

import Actions


class battle_banghuilingdi():
    def __init__(self, person):
        self.person = person

    def run(self):
        if self.person['state_lingdi'] == 'start':
            gevent.sleep(2)
            self.person.ACGIdle()
            temp = self.person['SceneId']
            # 移动到传送点，进入战斗场景
            self.person.ACGGMCommand(u"goto = 47, 17")
            gevent.sleep(2)
            self.person.ACGIdle()
            # print '**********',temp,self.person['SceneId']
            while self.person['SceneId'] == temp:
                self.person.ACGIdle()
                self.person.ACG_CHARMOVE(44, 17)
                gevent.sleep(2)
                self.person.ACGIdle()
                self.person.ACG_CHARMOVE(47, 17)
                gevent.sleep(2)
                self.person.ACGIdle()

            self.person.ACGAskChangeScene()
            gevent.sleep(2)
            self.person.ACGIdle()
            self.person.ACGENTERSCENE(1)
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            #缥缈峰
            if self.person['SceneId'] == 306:
                self.battle_scene(137, 59)
                return
            #擂鼓山
            if self.person['SceneId'] == 307:
                self.battle_scene(54, 41)
                return
            #少室山
            if self.person['SceneId'] == 308:
                self.battle_scene(88, 79)
                return
            #玄武岛
            if self.person['SceneId'] == 309:
                self.battle_scene(94, 102)
                return
            #夜西湖
            if self.person['SceneId'] == 310:
                self.battle_scene(135, 162)
                return
            #燕子坞
            if self.person['SceneId'] == 311:
                self.battle_scene(108, 37)
                return
            #天龙寺
            if self.person['SceneId'] == 312:
                self.battle_scene(83, 130)
                return
            #聚贤庄
            if self.person['SceneId'] == 313:
                self.battle_scene(142,38)
                return
            return

        elif self.person['state_lingdi'] == 'battle':
            # print self.person['userName'], ':battle'
            gevent.sleep(1)
            self.person.ACGIdle()
            if self.p_die() == 1:
                return
            self.person.ACG_CHARUSESKILL(0, 303, -1, 0, 0)
            for i in range(15):
                gevent.sleep(1)
                self.person.ACGIdle()
                if self.p_die() == 1:
                    return
            return

        elif self.person['state_lingdi'] == 'quitscene':
            self.person.ACGIdle()
            gevent.sleep(2)
            # print self.person['userName'], ':quitscene',self.person['SceneId']
            self.person.ACGAskChangeScene()
            gevent.sleep(2)
            self.person.ACGIdle()
            self.person.ACGENTERSCENE(1)
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person['state_lingdi'] = 'start'
            return

    def battle_scene(self, x_pos, z_pos):
        self.person.ACGGMCommand(u"goto = %s, %s" % (x_pos, z_pos))
        gevent.sleep(1)
        self.person.ACGIdle()
        if self.p_die() == 1:
            return
        self.person.ACG_CHARMOVE(random.random() * 3 + x_pos, z_pos + random.random() * 3)
        gevent.sleep(1)
        self.person.ACGIdle()
        if self.p_die() == 1:
            return
        self.person.ACG_CHARMOVE(random.random() * 3 + x_pos, z_pos + random.random() * 3)
        gevent.sleep(1)
        self.person.ACGIdle()
        if self.p_die() == 1:
            return
        self.person.ACG_COMMAND(u'sendimpacttounit =%s =110' % (self.person['tarOBJID']))
        gevent.sleep(1)
        self.person.ACGIdle()
        if self.p_die() == 1:
            return
        # print self.person['userName'], ':battle_scene'
        self.person['state_lingdi'] = 'battle'

    def p_die(self):
        if self.person['isDie'] == 'die':
            # print self.person['userName'], 'die'
            Actions.Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NOTIFYCHANGESCENE", 20)
            self.person['isDie'] = ''
            self.person['state_lingdi'] = 'quitscene'
            return 1
