import NetPackets
import Functions


class APACKET_CG_CGW_PACKET():
    def __init__(self, person):
        self.person = person

    def run(self, m_dataSize=4, m_type=2):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_CGW_PACKET(self.person)
        packet['m_dataSize'] = m_dataSize
        #packet['m_data'] = 0
        packet['m_type'] = m_type

        res = Functions.sendpacket(packet)
        #res = Functions.waitforpacket_with_heartbeat(self.person, "kSCHeartbeatAck")
        return res
