#coding=utf-8
import random
import math
import gevent
import time

import Actions

g_NpcObjId = 15
g_ScriptID = 1037
g_ExIndex = 1

class battle_banghuisouweizhan():
    def __init__(self, person):
        self.person = person

    def run(self, posx, posz, rd):
        if self.person['state'] == 'start':
            gevent.sleep(3)
            self.person.ACGIdle()
            self.person.ACG_CHARMOVE(self.person['posx'] + 1, self.person['posz'] + 1)
            self.person.ACGGMCommand(u"goto = %s, %s" %(posx, posz))
            gevent.sleep(3)
            #self.person.ACGIdle()

            self.person.ACG_CHARMOVE(posx + random.uniform(-1, 1) * rd, posz + random.uniform(-1, 1) * rd)
            gevent.sleep(3)
            self.person['state'] = 'battle'
            return
        elif self.person['state'] == 'battle':
            #self.person.ACG_CHARMOVE(posx + random.uniform(-1, 1) * rd, posz + random.uniform(-1, 1) * rd)
            #gevent.sleep(1)

            if self.person['state'] == 'battle':
                if time.time() - self.person['skillcd'] > 15:
                    self.person.ACG_CHARUSESKILL(0, 303)
                    self.person['skillcd'] = time.time()
                else:
                    self.person.ACG_CHARUSESKILL(self.person['m_Guid'], 304, self.person['m_ObjID'], self.person['posx'],
                                                 self.person['posz'])
            return
        elif self.person['state'] == 'die':
            gevent.sleep(5)
            self.person.ACGIdle()
            gevent.sleep(5)
            self.person.ACGIdle()
            self.person.ACG_PLAYER_DIE_RESULT(0, 'PACKET_GC_PLAYER_RELIVE')
            while self.person['state'] == "die":
                gevent.sleep(1)
                self.person.ACGIdle()
            self.person['state'] = 'start'
            return
        elif self.person['state'] == 'quit':
            self.person.ACGAskChangeScene()
            gevent.sleep(5)
            self.person.ACGIdle()
            self.person.ACGENTERSCENE(1)
            gevent.sleep(5)
            self.person.ACGIdle()
            gevent.sleep(5)
            self.person.ACGIdle()
            gevent.sleep(5)
            self.person.ACGIdle()
            gevent.sleep(5)
            self.person.ACGIdle()
            gevent.sleep(5)
            self.person.ACGIdle()
            gevent.sleep(5)
            self.person.ACGIdle()
            gevent.sleep(5)
            self.person.ACGIdle()

            self.person['state'] = 'stop'
            #self.enterSongliao()

            #self.person['state'] = 'start'
            return






