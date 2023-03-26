#coding=utf-8
import NetPackets
import Functions

class ACLAskLogin():
    def __init__(self, person):
        self.person = person        
        
    def run(self,Version, chongzhi_flag = None):
        
        packet = NetPackets.PACKETS.PACKET_CL_AskLogin(self.person)
        packet['OpenID'] = self.person['userName']
        packet['Version'] = Version
        packet['KickUser'] = 0
        packet['IsGuest'] = 0
        if chongzhi_flag is not None:
            packet['AccessToken'] = "a" + self.person['userName']

        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_LC_Status",60)
        # if res[0] == False:
        #     # print self.person['userName'] + u' Error, ACLAskLogin'
        return res

