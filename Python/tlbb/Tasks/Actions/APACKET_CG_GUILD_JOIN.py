import NetPackets
import Functions


class APACKET_CG_GUILD_JOIN():
    def __init__(self, person):
        self.person = person

    def run(self, guild_id):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GUILD_JOIN(self.person)
        packet['m_guid'] = self.person['m_Guid']
        packet['m_FromType'] = 0
        packet['m_GuildID'] = guild_id

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILD_RETURN")
        return res
