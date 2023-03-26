#coding=utf-8
import NetPackets
import Functions

class ACGEventRequest():
    def __init__(self, person):
        self.person = person

    def run(self,nNpcId,nScriptId,nExIndex,iswait = True):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_EVENTREQUEST(self.person)

        packet['m_NpcID'] = nNpcId
        packet['m_IssueScriptID'] = -1
        packet['m_ScriptID'] = nScriptId
        packet['m_ExIndex'] = nExIndex

        res = Functions.sendpacket(packet)


        if iswait:
            res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NOTIFYCHANGESCENE", 30)
        else:
            res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_NETCHECK")

        return res
