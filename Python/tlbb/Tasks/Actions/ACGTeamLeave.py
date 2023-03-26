#coding=utf-8
import NetPackets
import Functions

class ACGTeamLeave():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_TEAM_LEAVE(self.person)

        packet['m_GUID64'] = self.person['m_Guid']

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_TEAM_RESULT")
        return res
