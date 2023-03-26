# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/1/10 by ChengLongLong
-----------------------------------------------------------------------
Description:    标记序章完成
-----------------------------------------------------------------------
History:   
2017/1/10 
=======================================================================
'''
import NetPackets
import Functions

class ACG_FIRSCENE_FINISH():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_FIRSCENE_FINISH(self.person)

        res = Functions.sendpacket(packet)
        return res