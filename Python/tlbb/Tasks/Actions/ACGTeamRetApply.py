#coding=utf-8
import NetPackets
import Functions
import Users

class ACGTeamRetApply():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_TEAM_RET_APPLY(self.person)
        
        if self.person['m_SourGUID_List'] == None:
            print "m_SourGUID_List is None"
            return (False, 0, "m_SourGUID_List is Empty")
        if len(self.person['m_SourGUID_List']) == 0:
            print "m_SourGUID_List is 0"
            return (False, 0, "m_SourGUID_List is 0 len")

        for nSourGuid in self.person['m_SourGUID_List']:
            packet['m_uCheckKey'] = 0
            packet['m_SourGUID'] = nSourGuid
            packet['m_byReturn'] = 1
            Functions.sendpacket(packet)
            res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_TEAM_RESULT")
            
        #res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_TEAM_RESULT")
        return res
