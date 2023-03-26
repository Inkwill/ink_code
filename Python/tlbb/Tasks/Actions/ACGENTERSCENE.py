#coding=utf-8
import NetPackets
import Functions

class ACGENTERSCENE():
    def __init__(self, person):
        self.person = person        
        
    def run(self, enterType = 0):
        packet = NetPackets.PACKETS.PACKET_CG_ENTERSCENE(self.person)
        packet['enterType'] = enterType
        packet['sceneID'] = self.person['SceneId']
        packet['posX'] = self.person['f_x']
        packet['posZ'] = self.person['f_z']
        packet['m_AOIMaxCount'] = 30
        
        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_GC_ENTERSCENE",60)
        return res
    