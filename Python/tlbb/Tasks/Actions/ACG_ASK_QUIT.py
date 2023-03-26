#coding=utf-8
import NetPackets
import Functions

class ACG_ASK_QUIT():
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = NetPackets.PACKETS.PACKET_CG_ASK_QUIT(self.person)

        packet['Key'] = self.person['ServerKey']

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NETCHECK')
        return res