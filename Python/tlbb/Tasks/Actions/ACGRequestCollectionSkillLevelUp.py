#coding=utf-8
import NetPackets
import Functions

class ACGRequestCollectionSkillLevelUp():
    def __init__(self, person):
        self.person = person

    def run(self,index):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.CGRequestCollectionSkillLevelUp(self.person)

        packet['index'] = index  

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NETCHECK')
        return res