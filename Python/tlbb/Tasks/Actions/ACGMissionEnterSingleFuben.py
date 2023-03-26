#coding=utf-8
import NetPackets
import Functions

class ACGMissionEnterSingleFuben():
    def __init__(self, person):
        self.person = person

    def run(self, npcId, nMissionIndex):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_MISSION_ENTERSINGLEFUBEN(self.person)

        packet['m_npcId'] = npcId
        packet['m_MissionIndex'] = nMissionIndex

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NOTIFYCHANGESCENE',30)
        return res