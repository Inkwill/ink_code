#coding=utf-8
import NetPackets
import Functions

class ACGAskMail():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASKMAIL(self.person)

        packet['AskType'] = 0
        packet['temp'] = 0
        
        res = Functions.sendpacket(packet)

        #res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_MISSIONMODIFY",30)
        return res
