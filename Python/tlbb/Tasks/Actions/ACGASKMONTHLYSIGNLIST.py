#coding=utf-8
import NetPackets
import Functions

class ACGASKMONTHLYSIGNLIST():
    def __init__(self, person):
        self.person = person        
        
    def run(self,m_mode):  
        packet = NetPackets.PACKETS.PACKET_CG_ASKMONTHLYSIGNLIST(self.person)
        
        packet['m_mode'] = m_mode

        res = Functions.sendpacket(packet)
#         res = Functions.waitforpacket_with_heartbeat(self.person, "")
        return res