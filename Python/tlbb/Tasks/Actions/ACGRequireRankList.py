#coding=utf-8
import NetPackets
import Functions

class ACGRequireRankList():
    def __init__(self, person):
        self.person = person

    def run(self, rankType, start, end):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.CGRequireRankList(self.person)

        packet['GUID_L'], packet['GUID_H'] = NetPackets.TLSocket.DecodeUInt64(self.person['m_Guid'])  #get it when enterscene
        packet['RankType'] = rankType
        packet['From'] = start
        packet['To'] = end

        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'GCRequireRankList')
        return res