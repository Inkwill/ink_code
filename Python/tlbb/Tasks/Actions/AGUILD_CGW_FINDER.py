import NetPackets
import Functions


class AGUILD_CGW_FINDER():
    def __init__(self, person):
        self.person = person

    def run(self, type, m_guid= None, guildName = None):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)


        packet = NetPackets.PACKETS.PACKET_CG_GUILD(self.person)
        packet['m_Serial'] = 0
        packet['m_PacketType'] = 25

        packet['packet'] = NetPackets.PACKETS.GUILD_CGW_FINDER(self.person)
        packet1 = packet['packet']
        packet1['type'] = type
        if type == 1:
            packet1['m_GuildID'] = m_guid
        elif type == 2:
            packet1['guildName'] = guildName
            packet1['m_Position'] = 0



        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILD")
        return res
