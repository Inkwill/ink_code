#coding=utf-8
import NetPackets
import Functions

class ACG_ASK_MAIL_LIST():
    def __init__(self, person):
        self.person = person

    def run(self, mailtype):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_MAIL_LIST(self.person)

        packet['myLGuid'], packet['myHGuid'] = NetPackets.TLSocket.DecodeUInt64(self.person['m_Guid'])  #get it when enterscene
        packet['myMailType'] = mailtype

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RET_MAIL_LIST', timeout = 120)
        return res