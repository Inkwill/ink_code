#coding=utf-8
import NetPackets
import Functions
import Users

class ACGAskAcceptMission():
    def __init__(self, person):
        self.person = person

    def run(self,NpcId,IssueScriptId,ScriptId):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_ASK_ACCEPT_MISSION(self.person)

        packet['m_idNPC'] = NpcId
        packet['m_idIssueScript'] = IssueScriptId
        packet['m_idScript'] = ScriptId
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_MISSIONMODIFY",40)
        return res
