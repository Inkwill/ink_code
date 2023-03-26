#coding=utf-8
import NetPackets
import Functions

class ACG_USEITEM():
    def __init__(self, person):
        self.person = person

    def run (self, m_BagGUID,m_UseNum,m_BagTableIndex,m_BagIndex):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_USEITEM(self.person)

        packet['m_BagGUID'] = m_BagGUID  
        packet['m_UseNum'] = m_UseNum 
        packet['m_BagTableIndex'] = m_BagTableIndex 
        packet['m_BagIndex'] = m_BagIndex
        
        
        res = Functions.sendpacket(packet)

        return res