#coding=utf-8
import NetPackets
import Functions

class ACGSIGNORRESIGN():
    def __init__(self, person):
        self.person = person        
        
    def run(self,m_mode,m_Index):  
        packet = NetPackets.PACKETS.PACKET_CG_SIGNORRESIGN(self.person)
        
        packet['m_mode'] = m_mode
        packet['m_Index'] = m_Index

        res = Functions.sendpacket(packet)
#         res = Functions.waitforpacket_with_heartbeat(self.person, "")
        return res