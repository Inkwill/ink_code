#coding=utf-8
import NetPackets
import Functions

class ACLAskCharLogin():
    def __init__(self, person):
        self.person = person        
        
    def run(self):  
        packet = NetPackets.PACKETS.PACKET_CL_AskCharLogin(self.person)
        
        packet['GUID'] = self.person['m_Guid']
        packet['PlayerID'] = 0
        packet['SceneID'] = self.person['SceneID']
        packet['SzAccount'] = self.person['userName']
        packet['Name'] = self.person['userName']
        packet['Level'] = self.person['Level']
        
        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_LC_RetCharLogin")
#         if res[0] == False:
#             print self.person['userName'] + u' Error, ACLAskCharLogin'
        
        return res