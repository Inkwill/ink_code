import NetPackets
import Functions


class ACGReceiveRedPacket():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        if self.person['haobaols'] == []:
            return
        packet = NetPackets.PACKETS.PACKET_CG_GUILD(self.person)
        packet['m_Serial'] = 0
        packet['m_PacketType'] = 33
        packet['packet'] = NetPackets.PACKETS.CGReceiveRedPacket(self.person)
        packet1 = packet['packet']
        data = self.person['tmp_haobaols'].pop(0)
        packet1['m_guid'] = data
        packet1['data1'] = 0

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "GCReceiveRedPacket")
        return res
