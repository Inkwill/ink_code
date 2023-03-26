#coding=utf-8
import NetPackets
import Functions

class ACG_PLAYER_DIE_RESULT():
    def __init__(self, person):
        self.person = person

    def run(self, type, waitpacket = None):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_PLAYER_DIE_RESULT(self.person)

        packet['m_ResultCode'] = type
        res = Functions.sendpacket(packet)
        if waitpacket == None:
            res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_CHARSKILL_SEND')
        else:
            res = Functions.waitforpacket_with_heartbeat(self.person, waitpacket)
        return res