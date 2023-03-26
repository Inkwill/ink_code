#coding=utf-8
import NetPackets
import Functions

class ACG_CHARUSESKILL():
    def __init__(self, person):
        self.person = person

    def run(self, targetGuid, skillId, objId = -1, targetposx = 0.0, targetposz = 0.0 ,durtime=30):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_CHARUSESKILL(self.person)

        packet['TargetGuid'] = targetGuid
        packet['SkillDataId'] = skillId
        packet['ObjId'] = self.person['m_ObjID']
        packet['PosX'] = targetposx
        packet['PosY'] = targetposz
        packet['TargetObjId'] = objId
        packet['dir'] = 0.0

        Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_CHARSKILL_SEND',durtime)
        return res