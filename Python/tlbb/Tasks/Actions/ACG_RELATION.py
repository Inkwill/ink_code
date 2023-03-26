#coding=utf-8
import NetPackets
import Functions

class ACG_RELATION():
    def __init__(self, person):
        self.person = person

    def run(self, type, waitpacket = None):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_RELATION(self.person)
        packet['m_TargetWorldID'] = -1
        packet['m_NameSize'] = ''
        packet['name'] = ''
        packet['m_szMood'] = ''
        packet['m_TargetGUIDHigh'] = -1        
        packet['m_Count'] = ''
        packet['m_uMoodSize'] = ''
        packet['m_RelationType'] = ''
        packet['m_TargetGUIDLow'] = -1
        packet['type'] = '1' 
        packet['m_GUIDList64'] = []
        packet['m_Group'] = ''       
        packet['m_Sign'] = ''          
       
        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NETCHECK')
        return res