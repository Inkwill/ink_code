#coding=utf-8
import NetPackets
import Functions


class ACGCreatePlatfrom():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_CREATE_PLATFORM(self.person)
        
        guid = self.person['m_Guid']
        
        packet['m_Guid_L'], packet['m_Guid_H'] = NetPackets.TLSocket.DecodeUInt64(guid)
        
        packet['m_szActiveName'] = u'夺宝马贼'
        
        packet['m_nActiveID'] = 6
        packet['m_nSubClassID'] = 1
        packet['m_nLowLevel'] = 20
        packet['m_nUpperLevel'] = 100
        packet['m_bMatchType'] = 1
        packet['m_bAutoMatch'] = 1  
        

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RET_PLATFORM_RESULT')
        return res