# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/12/12 by ChengLongLong
-----------------------------------------------------------------------
Description:    获取拍卖物品列表
-----------------------------------------------------------------------
History:   
2016/12/12 
=======================================================================
'''

import NetPackets
import Functions


class ACGAskConsignSaleItemInfo():
    def __init__(self, person):
        self.person = person

    def run(self, sort, min, max, subtype, thirdtype, page=1, id=-1, isShow=0, EquipFiltrateIndex=9, durtime=15):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_CONSIGNSALEITEMINFO(self.person)

        packet['sort'] = sort
        packet['min'] = min
        packet['max'] = max
        packet['subtype'] = subtype
        packet['thirdtype'] = thirdtype
        packet['page'] = page
        packet['id'] = id
        packet['isShow'] = isShow
        packet['EquipFiltrateIndex'] = EquipFiltrateIndex

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RET_CONSIGNSALEITEMINFO', durtime)
        return res
