#coding=utf-8
import NetPackets
import Functions

class ACGENTERSCENE_huashan():
    def __init__(self, person):
        self.person = person        
        
    def run(self, sceneID, posX, posZ, enterType = 0):
        packet = NetPackets.PACKETS.PACKET_CG_ENTERSCENE(self.person)
        packet['enterType'] = enterType
        packet['sceneID'] = sceneID
        packet['posX'] = posX
        packet['posZ'] = posZ
        packet['m_AOIMaxCount'] = 30
        
        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_GC_ENTERSCENE",60)
        return res
    