#coding=utf-8
import NetPackets
import Functions

class ACG_CHAR_ASK_IMPACTLIST():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_CHAR_ASK_IMPACTLIST(self.person)

        packet['m_ObjID'] = self.person['m_ObjID']  

        res = Functions.sendpacket(packet)
        return res