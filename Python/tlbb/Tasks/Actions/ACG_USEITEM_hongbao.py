#coding=utf-8
import NetPackets
import Functions

class ACG_USEITEM_hongbao():
    def __init__(self, person):
        self.person = person

    def run (self, m_BagTableIndex):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_USEITEM(self.person)

        if self.person['m_Item_guid'] is None:
            return

        packet['m_BagGUID'] = self.person['m_Item_guid']
        packet['m_UseNum'] = 1
        packet['m_BagTableIndex'] = m_BagTableIndex
        packet['m_BagIndex'] = self.person['GMItemBagIndex']

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_CHAT")

        return res