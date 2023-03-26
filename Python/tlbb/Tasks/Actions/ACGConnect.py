#coding=utf-8
import NetPackets
import Functions

class ACGConnect():
    def __init__(self, person):
        self.person = person        
        
    def run(self, isReconnect = 0):
        packet = NetPackets.PACKETS.PACKET_CG_CGConnect(self.person)
        
        packet['name'] = self.person['userName']
        packet['m_Guid'] = self.person['m_Guid']
        packet['m_HW'] = 0
        packet['m_HL'] = 0
        packet['sex'] = self.person['sex']
        packet['IsReconnect'] = isReconnect
        packet['menPai'] = self.person['menPai']
        packet['ZoonId'] = self.person['ZoonId']
        packet['Key'] = self.person['ServerKey']
        
        Functions.sendpacket(packet)
        #if isReconnect == 1:
        #    res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GCConnect", timeout= 180)
        #    return res
        res = Functions.waitforpacket(self.person, "PACKET_GC_GCConnect", timeout = 180)
        return res