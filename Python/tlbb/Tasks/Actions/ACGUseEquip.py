#coding=utf-8
import NetPackets
import Functions

class ACGUseEquip():
    def __init__(self, person):
        self.person = person

    def run(self, m_EquipPoint = 1):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_USEEQUIP(self.person)

        packet['m_BagIndex'] = self.person['GMItemBagIndex']
        packet['m_EquipPoint'] = m_EquipPoint
        packet['m_UseEquipType'] = 1

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_USEEQUIPRESULT')
        return res