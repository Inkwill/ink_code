# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/2/9 by ChengLongLong
-----------------------------------------------------------------------
Description:    
-----------------------------------------------------------------------
History:   
2017/2/9 
=======================================================================
'''
import NetPackets
import Functions

class ACG_AskGuildTerritoryInfo():
    def __init__(self, person):
        self.person = person

    def run(self, Type='0'):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_AskGuildTerritoryInfo(self.person)
        packet['Type'] = Type

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_BackGuildTerritoryInfo")
        return res