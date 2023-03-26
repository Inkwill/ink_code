# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/2/9 by ChengLongLong
-----------------------------------------------------------------------
Description:    占领帮会领地
-----------------------------------------------------------------------
History:   
2017/2/9 
=======================================================================
'''
import NetPackets
import Functions

class ACG_GuildTerritory():
    def __init__(self, person):
        self.person = person

    def run(self, GuildFightForTerritoryId,GuidH=0,GuidL=0,GuildId=0):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GuildTerritory(self.person)
        packet['GuildFightForTerritoryId'] = GuildFightForTerritoryId
        packet['GuidH'] = GuidH
        packet['GuidL'] = GuidL
        packet['GuildId'] = GuildId

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILD")
        return res