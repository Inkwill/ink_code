#coding=utf-8
import NetPackets
import Functions

class ACG_MANIPULATEPETRET():
    def __init__(self, person):
        self.person = person

    def run(self, m_nSkillID,m_SecondPetGUID,m_type,m_nReplaceSkillIndex,m_objid,m_uPetGuid,m_nBagIndex ):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_MANIPULATEPETRET(self.person)

        packet['m_nSkillID'] = m_nSkillID  
        packet['m_SecondPetGUID'] = m_SecondPetGUID 
        packet['m_type'] = m_type 
        packet['m_nReplaceSkillIndex'] = m_nReplaceSkillIndex 
        packet['m_objid'] = m_objid 
        packet['m_uPetGuid'] = m_uPetGuid 
        packet['m_nBagIndex'] = m_nBagIndex 

        res = Functions.sendpacket(packet)

        return res