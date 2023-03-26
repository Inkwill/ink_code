#coding=utf-8
import NetPackets
import Functions

class ACG_EXECUTESCRIPT():
    def __init__(self, person):
        self.person = person

    def run(self, scriptId, funName, param):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_EXECUTESCRIPT(self.person)

        item = packet['m_Script']
        item['m_ScriptID'] = scriptId
        item['m_szFunName'] = funName
        item['m_aParam'] = param
        item['m_uParamCount'] = len(item['m_aParam'])

        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NETCHECK')
        return res