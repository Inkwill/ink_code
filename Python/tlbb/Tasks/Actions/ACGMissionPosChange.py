#coding=utf-8
import NetPackets
import Functions

class ACGMissionPosChange():
    def __init__(self, person):
        self.person = person

    def run(self, nMovieId,nx,ny):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_MISSION_POS_CHANGE(self.person)

        packet['m_movieId'] = nMovieId
        packet['m_posX'] = nx
        packet['m_posZ'] = ny

        res = Functions.sendpacket(packet)
        #res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_CHAR_STOPACTION')
        return res