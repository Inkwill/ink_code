#coding=utf-8
import NetPackets
import Functions
import Users
from NetPackets.GUILDPACKET import *

class ACGGuild():
    def __init__(self, person):
        self.person = person

    def run(self,packettype,serial):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GUILD(self.person)
        
        packet['m_PacketType'] = packettype
        packet['m_Serial'] = serial
        if packettype == 0:
            packet['packet'] = GUILD_CGW_ASKLIST(None)
            packet['packet']['m_SortType'] = 0
            packet['packet']['m_Start'] = 0
            packet['packet']['m_QueryDiffWorld'] = 0
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILD")
        return res
