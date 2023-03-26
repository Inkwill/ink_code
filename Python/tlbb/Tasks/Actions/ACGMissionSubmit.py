#coding=utf-8
import NetPackets
import Functions
import Users

class ACGMissionSubmit():
    def __init__(self, person):
        self.person = person

    def run(self,NpcId,IssueScriptId,ScriptId,SelectRadioId,validateData):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_MISSIONSUBMIT(self.person)

        
        packet['m_idNPC'] = NpcId
        packet['m_idScript'] = ScriptId
        packet['m_idSelectRadio'] = SelectRadioId
        packet['m_idIssueScript'] = IssueScriptId
        packet['m_validateData'] = validateData
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_MISSIONMODIFY",30)
        return res
