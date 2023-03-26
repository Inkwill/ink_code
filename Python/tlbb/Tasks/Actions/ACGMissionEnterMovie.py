#coding=utf-8
import NetPackets
import Functions
import Users

class ACGMissionEnterMovie():
    def __init__(self, person):
        self.person = person

    def run(self,nmovieId,isenterOrExit,nmissionId):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_MISSION_ENTER_MOVIE(self.person)
        
        packet['m_enterOrExit'] = isenterOrExit
        packet['m_missionId'] = nmissionId
        packet['m_movieId'] = nmovieId
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NETCHECK")
        return res
