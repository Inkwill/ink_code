# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/12/12 by ChengLongLong
-----------------------------------------------------------------------
Description:    玩家商店  商品下架
-----------------------------------------------------------------------
History:   
2016/12/12 
=======================================================================
'''

import NetPackets
import Functions

class ACG_SWORN_BROTHER_INFO():
    def __init__(self, person):
        self.person = person

    def run(self, guid, durtime=15):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_SWORN_BROTHER_INFO(self.person)

        packet['myHGuid'] = -1
        packet['myBrother_H_Guid'] = 0
        packet['myHGuid'] = -1
        packet['myBrother_H_Guid'] = 0
        
        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NETCHECK')
        return res