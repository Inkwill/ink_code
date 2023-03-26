import NetPackets
import Functions


class AGUILD_CGW_ASKINFO():
    def __init__(self, person):
        self.person = person

    def run(self, m_GuildId, m_Type, m_Serial=0):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GUILD(self.person)
        packet['m_Serial'] = m_Serial
        packet['m_PacketType'] = 3
        packet1 = NetPackets.PACKETS.GUILD_CGW_ASKINFO(self.person)
        packet['packet'] = packet1
        packet1['m_GuildGUID'] = m_GuildId
        packet1['m_Type'] = m_Type
        packet1['m_IsOnLogin'] = 0

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILD")
        return res
