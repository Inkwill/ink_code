#coding=utf-8
import NetPackets
import Functions

class ACGCharDefaultEvent():
    def __init__(self, person):
        self.person = person

    def run(self, nObjID):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_GC_CHARDEFAULTEVENT(self.person)

        packet['m_ObjID'] = nObjID
        packet['m_nIssuesScript'] = -1

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_SCRIPTCOMMAND")
        return res
