#coding=utf-8
import NetPackets
import Functions

class AReCLAskLogin():
    def __init__(self, person):
        self.person = person        
        
    def run(self,Version):
        
        packet = NetPackets.PACKETS.PACKET_CL_AskLogin(self.person)
        packet['OpenID'] = self.person['userName']
        packet['Version'] = Version
        packet['KickUser'] = 0
        packet['IsGuest'] = 0

        res = Functions.sendpacket(packet)
        #res = Functions.waitforpacket(self.person, "PACKET_LC_ReConnectData",15)
        return res