#coding=utf-8
import NetPackets
import Functions

class ACGCharAskBaseAttrib():
    def __init__(self, person):
        self.person = person

    def run(self, nType):
        packet = NetPackets.PACKETS.PACKET_CG_CHARASKBASEATTRIB(self.person)

        packet['m_ObjID'] = self.person['m_ObjID']
        packet['m_nType'] = nType

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RETCAMPAIGNCOUNT')
        return res