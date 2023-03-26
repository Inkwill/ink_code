import gevent
import Actions

class changescene():
    def __init__(self, person):
        self.person = person

    def run(self, isComfirm):

        #self.person.changescene = 0
        #res = self.person.ACG_COMMAND('goto = 158,18 = 1')
        #if res[0] == False:
        #    return res

        #while self.person['flag'] != 1:
            #res = self.person.ACG_COMMAND(u'goto = 158,18 = 1')
            #if res[0] == True:
            #    break
            #gevent.sleep(5)
            #self.person.ACGIdle()
        #print "flag:", self.person['flag']
        #self.person['flag'] = 0
        if isComfirm == 1 and self.person['iscomfirm'] is None:
            self.person['iscomfirm'] = 1
            self.person.ACG_EXECUTESCRIPT(400999, u'EnterAreaWithConfirm', [-1, 22, 22])

        res = Actions.Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NOTIFYCHANGESCENE",60)
        if res[0] == False:
            return res

        res = self.person.ACGAskChangeScene()
        if res[0] == False:
            return res

        res = self.person.ACGENTERSCENE(1)
        if res[0] == False:
            return res
        #print "finished changescene!!!!"
        return res
