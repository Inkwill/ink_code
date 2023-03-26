
import gevent
import random

class battle_path():
    def __init__(self, person):
        self.person = person

    def run(self):
        gevent.sleep(0.5)
        self.person.ACGIdle()
        gevent.sleep(0.5)
        self.person.ACGIdle()
        if len(self.person['battle_monster']) == 0:
            res = self.person.ACG_CHARMOVE(self.person['battle_path'][self.person['battle_path_index']][0],
                                     self.person['battle_path'][self.person['battle_path_index']][1])

            self.person['posx'] = self.person['battle_path'][self.person['battle_path_index']][0]
            self.person['posz'] = self.person['battle_path'][self.person['battle_path_index']][1]


            
            self.person['battle_path_index'] = self.person['battle_path_index'] + 1
            if self.person['battle_path_index'] == len(self.person['battle_path']):
                self.person['battle_path_index'] = 0
                self.person['battle_path'].reverse()
            return res
        else:
            monster_id = self.person['battle_monster'].keys()[0]
            posx = self.person['posx']
            posz = self.person['posz']
            self.person.ACG_CHARMOVE(posx + random.randint(-1,1), posz + random.randint(-1,1))
            res = self.person.ACG_CHARUSESKILL(-1, 300, monster_id, self.person['battle_monster'][monster_id][0], self.person['battle_monster'][monster_id][1])
            self.person.ACG_CHARMOVE(posx, posz)

            return res


