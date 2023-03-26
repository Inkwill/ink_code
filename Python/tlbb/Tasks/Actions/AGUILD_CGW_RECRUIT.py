import NetPackets
import Functions


class AGUILD_CGW_RECRUIT():
    def __init__(self, person):
        self.person = person

    def run(self, proposerGuid):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GUILD(self.person)
        packet['m_Serial'] = self.person['m_Serial']
        packet['m_PacketType'] = 6
        packet1 = NetPackets.PACKETS.GUILD_CGW_RECRUIT(self.person)
        packet['packet'] = packet1
        packet1['m_ProposerGUID64'] = proposerGuid
        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILD_RETURN")
        return res
