# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/2/8 by ChengLongLong
-----------------------------------------------------------------------
Description:    
-----------------------------------------------------------------------
History:   
2017/2/8 
=======================================================================
'''
import NetPackets
import Functions


class AGC_CHARDEFAULTEVENT():
    def __init__(self, person):
        self.person = person

    def run(self,m_ObjID,iswait = True):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_GC_CHARDEFAULTEVENT(self.person)

        packet['m_ObjID'] = m_ObjID
        packet['m_IssueScriptID'] = -1

        res = Functions.sendpacket(packet)


        if iswait:
            res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_SCRIPTCOMMAND", 30)
        else:
            res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NETCHECK")

        return res