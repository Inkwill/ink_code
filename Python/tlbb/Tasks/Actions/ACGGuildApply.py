#coding=utf-8
import NetPackets
import Functions
import Users

class ACGGuildApply():
    def __init__(self, person):
        self.person = person

    def run(self, guildName = None):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GUILD_APPLY(self.person)
        if guildName is None:
            packet['_guildName'] = 'g' + self.person['userName']
        else:
            packet['_guildName'] = guildName
        packet['_guildDesc'] = self.person['userName']

        Functions.sendpacket(packet)        
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_CHAT",40)
        return res
