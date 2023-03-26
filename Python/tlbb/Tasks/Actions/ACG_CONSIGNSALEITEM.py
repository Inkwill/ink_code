# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/12/12 by ChengLongLong
-----------------------------------------------------------------------
Description:    玩家商店 上架物品
-----------------------------------------------------------------------
History:   
2016/12/12 
=======================================================================
'''
import NetPackets
import Functions


class ACG_CONSIGNSALEITEM():
    def __init__(self, person):
        self.person = person

    def run(self, guid, count, price,durtime=15):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_CONSIGNSALEITEM(self.person)

        packet['guid'] = guid
        packet['count'] = count
        packet['price'] = price
        packet['curpage'] = 1

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RET_MYCONSIGNSALEITEM', durtime)
        return res
