#coding=utf-8
import NetPackets
import Functions

class ACG_RIDEBAGMOVEITEM():
    def __init__(self, person):
        self.person = person

    def run(self, index):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_RIDEBAGMOVEITEM(self.person)

        packet['index'] = index  

        res = Functions.sendpacket(packet)

        return res