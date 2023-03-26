import NetPackets
import Functions


class AGUILD_CGW_GUILDEVENT():
    def __init__(self, person):
        self.person = person

    def run(self, guildId = None):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GUILD(self.person)
        packet['m_Serial'] = 1
        packet['m_PacketType'] = 28
        packet1 = NetPackets.PACKETS.GUILD_CGW_GUILDEVENT(self.person)
        packet['packet'] = packet1
        packet1['m_GuildGUID'] = self.person['m_Guid']


        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILD")
        return res
