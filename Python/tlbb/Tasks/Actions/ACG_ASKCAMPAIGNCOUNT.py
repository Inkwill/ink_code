#coding=utf-8
import NetPackets
import Functions

class ACG_ASKCAMPAIGNCOUNT():
    def __init__(self, person):
        self.person = person

    def run(self, flag):
        packet = NetPackets.PACKETS.PACKET_CG_ASKCAMPAIGNCOUNT(self.person)

        packet['m_Flag'] = flag

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RETCAMPAIGNCOUNT')
        return res