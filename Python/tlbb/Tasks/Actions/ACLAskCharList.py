#coding=utf-8
import NetPackets
import Functions

class ACLAskCharList():
    def __init__(self, person):
        self.person = person        
        
    def run(self):  
        packet = NetPackets.PACKETS.PACKET_CL_AskCharList(self.person)
        
        packet['OpenID'] = self.person['userName']

        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_LC_RetCharList")
        return res