#coding=utf-8
import NetPackets
import Functions

class ACG_ASKCOPYSCENECOUNT():
    def __init__(self, person):
        self.person = person

    def run(self, m_Type):
        packet = NetPackets.PACKETS.PACKET_CG_ASKCOPYSCENECOUNT(self.person)

        packet['m_Type'] = m_Type

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RETCOPYSCENECOUNT')
        return res