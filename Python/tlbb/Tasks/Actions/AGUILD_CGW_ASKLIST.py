#coding=utf-8
import NetPackets
import Functions

class AGUILD_CGW_ASKLIST():
    def __init__(self, person):
        self.person = person        
        
    def run(self):  
        packet = NetPackets.PACKETS.PACKET_CG_GUILD(self.person)
        packet['m_PacketType'] = 0
        packet['m_Serial'] = 0

        packet['packet'] = NetPackets.PACKETS.GUILD_CGW_ASKLIST(self.person)
        packet1 = packet['packet']
        packet1['m_QueryDiffWorld'] = 0
        packet1['m_QueryDiffWorld'] = 0
        packet1['m_QueryDiffWorld'] = 0

        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_GC_GUILD")
        return res