#coding=utf-8
import NetPackets
import Functions

class ACGAskQuit():
    def __init__(self, person):
        self.person = person        
        
    def run(self):
        
        packet = NetPackets.PACKETS.PACKET_CG_ASK_QUIT(self.person)
        packet['Key'] = int(self.person['mServerKey'])

        res = Functions.sendpacket(packet)
        #Functions.waitforpacket(self.person, "PACKET_GC_KICK",30)
        return res