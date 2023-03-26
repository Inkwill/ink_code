# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/12/12 by ChengLongLong
-----------------------------------------------------------------------
Description:    
-----------------------------------------------------------------------
History:   
2016/12/12 
=======================================================================
'''

import NetPackets
import Functions


class ACG_ASK_EXCHANGEMONEY():
    def __init__(self, person):
        self.person = person

    def run(self, exchangeNum, exchangeType, activeType=1):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_EXCHANGEMONEY(self.person)

        packet['exchangeNum'] = exchangeNum
        packet['exchangeType'] = exchangeType
        packet['activeType'] = activeType


        res = Functions.sendpacket(packet)
        return res
