#coding=utf-8
import NetPackets
import Functions

class ACG_ONEKEY_GET_MAIL_APPEND():
    def __init__(self, person):
        self.person = person

    def run(self):
        if self.person['mailFlag'] == 0:
            return (True,0,"Do not send packet")
        self.person['mailFlag'] = 0

        packet = NetPackets.PACKETS.PACKET_CG_ONEKEY_GET_MAIL_APPEND(self.person)

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RET_MAIL_LIST', timeout= 120)
        return res