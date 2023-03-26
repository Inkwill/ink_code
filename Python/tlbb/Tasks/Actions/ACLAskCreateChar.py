#coding=utf-8
import NetPackets
import Functions
import random

class ACLAskCreateChar():
    def __init__(self, person):
        self.person = person        
        
    def run(self,isRandom = False):  
        packet = NetPackets.PACKETS.PACKET_CL_AskCreateChar(self.person)      
        
        packet['CharName'] = self.person['userName']
        
        
        if not isRandom:
            packet['Sex'] = 1
            packet['m_HairModel'] = 15
            packet['m_HeadID'] = 1
            if self.person['menpails'] is not None:
                packet['MenPai'] = random.choice(self.person['menpails'])
            else:
                packet['MenPai'] = 4
        else:
            packet['Sex'] = random.choice([0,1])
            if packet['Sex'] == 0:
                packet['m_HairModel'] = 16
                packet['m_HeadID'] = 15
            else:
                packet['m_HairModel'] = 15
                packet['m_HeadID'] = 1
            if self.person['menpails'] is not None:
                packet['MenPai'] = random.choice(self.person['menpails'])
            else:
                packet['MenPai'] = random.choice([2,4,7,8])
            
        
        self.person['menpai'] = packet['MenPai']
        packet['GUID'] = 0
        packet['m_HairColor'] = 0

        
        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_LC_RetCharList")
        if res[0] == False:
            print self.person['userName'] + u' Error, ACLAskCreateChar'
        return res