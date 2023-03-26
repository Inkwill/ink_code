#coding=utf-8
import NetPackets
import Functions
import Users

class ACGTeamApply():
    def __init__(self, person):
        self.person = person

    def run(self,szDesName):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_TEAM_APPLY(self.person)
        
        packet['m_SourGUID'] = self.person['m_Guid']
        packet['m_byDestNameSize'] = len(szDesName)+1
        packet['m_szDestName'] = szDesName
        packet['m_nDestZoneWorldId'] = -1
        
        res = Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_TEAM_RESULT")
        return res
