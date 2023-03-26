#coding=utf-8
import NetPackets
import Functions
import Users

class ACGMissionMovieEnd():
    def __init__(self, person):
        self.person = person

    def run(self,nmovieId):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_MISSION_MOVIE_END(self.person)

        
        packet['m_movieId'] = nmovieId
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_MISSIONMODIFY",30)
        return res
