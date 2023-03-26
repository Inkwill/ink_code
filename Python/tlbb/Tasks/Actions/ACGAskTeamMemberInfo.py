#coding=utf-8
import NetPackets
import Functions
import Users

class ACGAskTeamMemberInfo():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_TEAM_MEMBER_INFO(self.person)
             
        packet['m_SceneID'] = self.person['SceneId']
        packet['m_GUID'] = self.person['m_Guid']
        packet['m_nObjID'] = self.person['m_ObjID']
        packet['m_nTeamID'] = self.person['m_nTeamID']
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_TEAM_MEMBER_INFO")
        return res
