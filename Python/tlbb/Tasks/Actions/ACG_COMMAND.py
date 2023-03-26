#coding=utf-8
import NetPackets
import Functions

class ACG_COMMAND():
    def __init__(self, person):
        self.person = person

    def run(self, context, waitpacket=''):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_COMMAND(self.person)

        packet['context'] = context

        if waitpacket == '':
            res = Functions.sendpacket(packet)
        else:
            Functions.sendpacket(packet)
            res = Functions.waitforpacket_with_heartbeat(self.person, waitpacket, timeout= 120)
        return res

