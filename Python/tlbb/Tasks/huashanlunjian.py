# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/1/22 by ChengLongLong
-----------------------------------------------------------------------
Description:    华山论剑
-----------------------------------------------------------------------
History:   
2017/1/22 
=======================================================================
'''
import gevent
import random
import Actions


class huashanlunjian():
    def __init__(self, person):
        self.person = person

    def run(self):
        if self.person['state_huashan'] == 'start':
            self.person.ACGIdle()
            self.person.ACG_CHARMOVE(random.random() * 2 + 18, 32 + random.random() * 2)
            gevent.sleep(2)
            # print self.person['SceneId'] == 59 or self.person['SceneId'] == 58 or self.person['SceneId'] == 57

            if self.person['SceneId'] == 59 or self.person['SceneId'] == 58 or self.person['SceneId'] == 57:
                self.person['state_huashan'] = 'start'
                return
            else:
                # print self.person['userName'], self.person['SceneId']
                self.person.ACGIdle()
                gevent.sleep(1)
                self.person['state_huashan'] = 'enterhuashan'

        elif self.person['state_huashan'] == 'enterhuashan':
            # print self.person['userName'], '--enterhuashan'
            # self.person.ACGIdle()
            self.person.ACGAskChangeScene()
            self.person.ACGIdle()
            self.person.ACGENTERSCENE(1)
            self.person.ACGIdle()
            self.person.ACG_CHARMOVE(33, 33)
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            self.person.ACG_COMMAND(u'sendimpacttounit =%s =110' % (self.person['tarOBJID']))
            self.person.ACGIdle()
            self.person['state_huashan'] = 'battle'
            return

        elif self.person['state_huashan'] == 'battle':
            self.person.ACGIdle()
            self.person.ACG_CHARUSESKILL(0, 303, -1, 0, 0)
            for i in range(8):
                gevent.sleep(2)
                self.person.ACGIdle()
                if self.person['SceneId'] == 59 or self.person['SceneId'] == 58 or self.person['SceneId'] == 57:
                    gevent.sleep(2)
                    self.person.ACGIdle()
                    # print self.person['userName'], self.person['SceneId']
                    self.person['state_huashan'] = 'quitscene'
                    return
            return

        elif self.person['state_huashan'] == 'quitscene':
            self.person.ACGIdle()
            gevent.sleep(2)
            # print self.person['userName'],':quitscene'
            self.person.ACGAskChangeScene()
            gevent.sleep(2)
            self.person.ACGIdle()
            self.person.ACGENTERSCENE(1)
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            self.person.ACGTeamLeave()
            gevent.sleep(2)
            self.person.ACGIdle()
            self.person.ACCTEAMINVITE()
            gevent.sleep(2)
            self.person.ACGIdle()
            self.person['state_huashan'] = 'start'
            return


