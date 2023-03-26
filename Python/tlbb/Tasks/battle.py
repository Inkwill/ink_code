#coding=utf-8
import random
import math

class battle():
    def __init__(self, person):
        self.person = person

    def run(self, posx, posz, rd, sMonsterName = u''):
        if self.person['state'] == 'start':
            if len(self.person['monsterdic']) == 0:
                return
            self.person.m_objId = random.choice(self.person['monsterdic'].keys())
            if sMonsterName == '':
                self.person['state'] = 'walk'
            else:
                if self.person['monsterdic'][self.person.m_objId][3] != sMonsterName:
                    self.person['state'] = 'start'
                else:
                    self.person['state'] = 'walk'
        elif self.person['state'] == 'walk':
            if self.person.m_objId not in self.person['monsterdic']:
                self.person['state'] = 'start'
                return
            self.person.ACG_CHARMOVE(self.person['monsterdic'][self.person.m_objId][1],
                                     self.person['monsterdic'][self.person.m_objId][2])
            self.person['state'] = 'battle'
        elif self.person['state'] == 'battle':
            self.person.ACGIdle()
            if self.person.m_objId not in self.person['monsterdic']:
                self.person['state'] = 'walkback'
                return
            x = self.person['posx'] -self.person['monsterdic'][self.person.m_objId][1]
            y = self.person['posz'] -self.person['monsterdic'][self.person.m_objId][2]
            if math.sqrt(x*x + y*y)> 5:
                self.person['state'] = 'walk'
                return
            self.person.ACG_CHARUSESKILL(self.person['monsterdic'][self.person.m_objId][0], 300, self.person.m_objId,
                                         self.person['monsterdic'][self.person.m_objId][1],
                                         self.person['monsterdic'][self.person.m_objId][2])
        elif self.person['state'] == 'walkback':
            self.person.ACG_CHARMOVE(posx + random.random()*rd,
                                     posz + random.random()*rd)
            self.person['state'] = 'start'
        elif self.person['state'] == 'die':
            self.person.ACG_PLAYER_DIE_RESULT(2)
            self.person['state'] = 'start'




