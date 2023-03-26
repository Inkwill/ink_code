#coding=utf-8
import NetPackets
import Functions

class ACG_ASK_BALANCE():
    def __init__(self, person):
        self.person = person

    def run(self, type):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_BALANCE(self.person)

        packet['Type'] = 0
        packet['OpenId'] = self.person['userName']
        packet['Access_Token'] = "a" + self.person['userName']
        packet['Pay_Token'] = "pay" + self.person['userName']
        packet['pf'] = "ddpf" + self.person['userName']
        packet['pfKey'] = "dades" + self.person['userName']

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_Ret_BALANCE', timeout= 120)
        return res