# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/1/9 by ChengLongLong
-----------------------------------------------------------------------
Description:    获取道具列表总数量
-----------------------------------------------------------------------
History:   
2017/1/9 
=======================================================================
'''
import NetPackets
import Functions

class ACG_ASK_CONSIGNSALEPRODUCTTYPESDATA():
    def __init__(self, person):
        self.person = person

    def run(self, SearchClass, minLevel, maxLevel, ProductType, MainProductType, SubProductType, durtime=15):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_CONSIGNSALEPRODUCTTYPESDATA(self.person)

        packet['SearchClass'] = SearchClass
        packet['minLevel'] = minLevel
        packet['ProductType'] = ProductType
        packet['MainProductType'] = MainProductType
        packet['maxLevel'] = maxLevel
        packet['SubProductType'] = SubProductType

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_RET_CONSIGNSALEPRODUCTTYPESDATA', durtime)
        return res