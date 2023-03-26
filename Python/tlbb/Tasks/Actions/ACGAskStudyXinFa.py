#coding=utf-8
import NetPackets
import Functions

class ACGAskStudyXinFa():
    def __init__(self, person):
        self.person = person        
        
    def run(self,m_SkillCurLevel,m_SkillId,m_idXinfaType,m_WantLevel,m_Mode):  
        packet = NetPackets.PACKETS.PACKET_CG_ASKSTUDYXINFA(self.person)
        
        packet['m_SkillCurLevel'] = m_SkillCurLevel
        packet['m_SkillId'] = m_SkillId
        packet['m_idXinfaType'] = m_idXinfaType
        packet['m_WantLevel'] = m_WantLevel
        packet['m_Mode'] = m_Mode

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_STUDYXINFA")
        return res