#coding=utf-8
import NetPackets
import Functions
from datetime import datetime

class ACGChat():
    def __init__(self, person):
        self.person = person        
        
    def run(self, chatType):
        packet = NetPackets.PACKETS.PACKET_CG_CHAT(self.person)
        
        packet['m_ChatType'] = chatType
        packet['m_Contex'] = u'' + self.person['userName'] + " is speaking!"
        packet['m_DClientTime'] = datetime.now().second
        packet['m_TeamID'] = self.person['m_nTeamID']

        res = Functions.sendpacket(packet)
        #res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_CHAT")

        return res