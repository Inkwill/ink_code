#coding=utf-8
import NetPackets
import Functions

class ACGAskTeamInfo():
    def __init__(self, person):
        self.person = person        
        
    def run(self):  
        packet = NetPackets.PACKETS.PACKET_CG_ASK_TEAM_INFO(self.person)
        
        packet['m_nObjID'] = self.person['m_ObjID']
        
        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_TEAM_LIST",40)
        return res