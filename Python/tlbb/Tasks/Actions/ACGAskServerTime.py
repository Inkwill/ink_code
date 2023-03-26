#coding=utf-8
import NetPackets
import Functions

class ACGAskServerTime():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_SERVER_TIME(self.person)

        packet['AskType'] = 0

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_ASK_SERVER_TIME")
        return res
