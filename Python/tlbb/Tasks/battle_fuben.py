#coding=utf-8
import random
import math
import gevent

class battle_fuben():
    def __init__(self, person):
        self.person = person

    def run(self, sMonsterName = u''):
        #print "self.person['monsterdic']:", self.person['monsterdic']
        if self.person['state'] == 'start':
            self.person.ACGIdle()
            self.person['controlnum'] = 0
            if len(self.person['monsterdic']) == 0:
                return
            self.person.m_objId,self.person.m_distance = self.getNearMonster()
            if sMonsterName == '':
                self.person['state'] = 'walk'
            else:
                if self.person['monsterdic'][self.person.m_objId][3] != sMonsterName:
                    self.person['state'] = 'start'
                else:
                    self.person['state'] = 'walk'
        elif self.person['state'] == 'walk':
            self.person['controlnum'] = 0
            if self.person.m_objId not in self.person['monsterdic']:
                self.person['state'] = 'start'
                return
            self.person.ACG_CHARMOVE(self.person['monsterdic'][self.person.m_objId][1],
                                     self.person['monsterdic'][self.person.m_objId][2])
            if self.person.m_distance/3 > 1:
                gevent.sleep(self.person.m_distance/3)
            else:
                gevent.sleep(1)
            self.person['state'] = 'battle'
        elif self.person['state'] == 'battle':
            if self.person['controlnum'] == None:
                self.person['controlnum'] = 1
            else:
                self.person['controlnum'] = self.person['controlnum'] + 1
            self.person.ACGIdle()
            if self.person.m_objId not in self.person['monsterdic']:
                self.person['state'] = 'start'
                return
            x = self.person['posx'] -self.person['monsterdic'][self.person.m_objId][1]
            y = self.person['posz'] -self.person['monsterdic'][self.person.m_objId][2]
            
            if math.sqrt(x*x + y*y)> 5:
                self.person['state'] = 'walk'
                return
            self.person.ACG_CHARUSESKILL(self.person['monsterdic'][self.person.m_objId][0], 300, self.person.m_objId,
                                         self.person['monsterdic'][self.person.m_objId][1],
                                         self.person['monsterdic'][self.person.m_objId][2],5)
        elif self.person['state'] == 'die':
            self.person['controlnum'] = 0
            self.person.ACG_PLAYER_DIE_RESULT(2)
            self.person['state'] = 'start'

    def getNearMonster(self):
        keylist = self.person['monsterdic'].keys() 
        resultobj = keylist[0]
        ndistance = 0
        for objt in keylist:
            xi = self.person['posx'] -self.person['monsterdic'][resultobj][1]
            yi = self.person['posz'] -self.person['monsterdic'][resultobj][2]
            xj = self.person['posx'] -self.person['monsterdic'][objt][1]
            yj = self.person['posz'] -self.person['monsterdic'][objt][2]
            if math.sqrt(xi*xi + yi*yi)> math.sqrt(xj*xj + yj*yj):
                    resultobj = objt
                    ndistance = math.sqrt(xj*xj + yj*yj)
        return (resultobj,ndistance)

