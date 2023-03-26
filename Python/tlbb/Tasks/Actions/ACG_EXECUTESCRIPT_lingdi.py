# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/2/13 by ChengLongLong
-----------------------------------------------------------------------
Description:    
-----------------------------------------------------------------------
History:   
2017/2/13 
=======================================================================
'''
import NetPackets
import Functions


class ACG_EXECUTESCRIPT_lingdi():
    def __init__(self, person):
        self.person = person

    def run(self, scriptId, funName, param, m_uFunNameSize=15,durtime=40):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_EXECUTESCRIPT(self.person)

        item = packet['m_Script']
        item['m_ScriptID'] = scriptId
        item['m_szFunName'] = funName
        item['m_aParam'] = param
        item['m_uParamCount'] = len(item['m_aParam'])
        item['m_uFunNameSize'] = m_uFunNameSize

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NOTIFYCHANGESCENE',durtime)
        while res[0] == False:
            self.person.ACGIdle()
            res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NOTIFYCHANGESCENE",durtime)
        return res