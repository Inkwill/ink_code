#coding=utf-8
import NetPackets
import Functions
import Users

class ACGAskChangeScene_huashan():
    def __init__(self, person):
        self.person = person

    def run(self,m_sourSceneID,m_destSceneID):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CGAskChangeScene(self.person)

        packet['m_sourSceneID'] = m_sourSceneID
        packet['m_destSceneID'] = m_destSceneID

        packet['m_memUsage'] = 0
        packet['m_iFreeLocalVideoMemory'] = 0
        packet['m_fAverageFPSInScene'] = 0.0
        packet['m_fVedioMemoryUsage'] = 0

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_RETCHANGESCENE")
        return res
