# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/12/13 by ChengLongLong
-----------------------------------------------------------------------
Description:    购买玩家商店物品
-----------------------------------------------------------------------
History:   
2016/12/13 
=======================================================================
'''
import NetPackets
import Functions

class ACG_BUY_CONSIGNSALEITEMINFO():
    def __init__(self, person):
        self.person = person

    def run(self, sort, min, max, subtype, guid, count, page=1, EquipFiltrateIndex=9, id=-1, durtime=15):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_BUY_CONSIGNSALEITEMINFO(self.person)

        packet['sort'] = sort
        packet['min'] = min
        packet['max'] = max
        packet['subtype'] = subtype
        packet['guid'] = guid
        packet['count'] = count
        packet['page'] = page
        packet['EquipFiltrateIndex'] = EquipFiltrateIndex
        packet['id'] = id


        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_SCRIPTCOMMAND', durtime)
        return res