# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/1/10 by ChengLongLong
-----------------------------------------------------------------------
Description:    切出序章
-----------------------------------------------------------------------
History:   
2017/1/10 
=======================================================================
'''
import NetPackets
import Functions

class ACG_FIRSCENE_CHANGESCENE():
    def __init__(self, person):
        self.person = person

    def run(self,durtime=30):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_FIRSCENE_CHANGESCENE(self.person)

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NOTIFYCHANGESCENE', durtime)
        return res