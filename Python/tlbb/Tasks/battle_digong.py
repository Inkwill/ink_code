#coding=utf-8
import random
import math
import gevent

skillls = {2:100, 4:300, 7:200, 8:400}
class battle_digong():
    def __init__(self, person):
        self.person = person

    def run(self):
        #print "self.person['monsterdic']:", self.person['monsterdic']
        if self.person['state'] == 'start':
            self.person['controlnum'] = 0
            if len(self.person['monsterdic']) == 0:
                return
            self.person['monster_guid'] = random.choice(self.person['monsterdic'].keys())
            self.person['state'] = 'walk'

        elif self.person['state'] == 'walk':
            self.person.ACGIdle()
            if self.person.m_objId not in self.person['monsterdic']:
                self.person['state'] = 'start'
                return

            xj = self.person['posx'] -self.person['monsterdic'][self.person['monster_guid']][1]
            yj = self.person['posz'] -self.person['monsterdic'][self.person['monster_guid']][2]
            ndistance = math.sqrt(xj*xj + yj*yj)

            self.person.ACG_CHARMOVE(self.person['monsterdic'][self.person.m_objId][1],
                                     self.person['monsterdic'][self.person.m_objId][2])

            times = int(ndistance /8.0) + 2
            for i in range(times):
                gevent.sleep(2)
                self.person.ACGIdle()
            self.person['state'] = 'battle'

        elif self.person['state'] == 'battle':
            self.person.ACGIdle()
            if self.person.m_objId not in self.person['monsterdic']:
                self.person['state'] = 'start'
                return
            x = self.person['posx'] -self.person['monsterdic'][self.person.m_objId][1]
            y = self.person['posz'] -self.person['monsterdic'][self.person.m_objId][2]

            if math.sqrt(x*x + y*y)> 5:
                self.person['state'] = 'walk'
                return
            self.person.ACG_CHARUSESKILL(self.person['monsterdic'][self.person.m_objId][0], skillls[self.person['menPai']], self.person.m_objId,
                                         self.person['monsterdic'][self.person.m_objId][1],
                                         self.person['monsterdic'][self.person.m_objId][2],5)
        elif self.person['state'] == 'die':
            self.person.ACG_PLAYER_DIE_RESULT(2)
            self.person['state'] = 'start'

