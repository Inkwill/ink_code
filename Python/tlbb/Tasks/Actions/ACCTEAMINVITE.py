#coding=utf-8
import NetPackets
import Functions
import Users

class ACCTEAMINVITE():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CC_TEAM_INVITE(self.person)

        packet['m_nSourObjID'] = self.person['m_ObjID']
        packet['m_byNameSize'] = len(self.person['userName'])+1
        packet['m_szName'] = self.person['userName']
        packet['m_nDestZoneWorldId'] = -1

        if self.person['m_SourGUID_List'] != None:
            self.person['m_SourGUID_List'] = None
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_TEAM_LIST", 40)
        return res
