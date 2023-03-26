import NetPackets
import Functions
import gevent
import random

class ACG_GUILDACTIVITYDRINK():
    def __init__(self, person):
        self.person = person

    def run(self, type, guildId = None, sceneId = None, AskType = None):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_GUILDACTIVITYDRINK(self.person)
        packet['Type'] = type

        if type == 1111: #AskGuildUserInfo
            packet['guildId'] = guildId
            packet['sceneId'] = sceneId
        elif type == 5: #AskAnswer
            while self.person['QuestionType'] is None:
                Functions.handleinputstream(self.person)
                Functions.heartbeat(self.person)
                gevent.sleep(2)
            packet['QuestionType'] = self.person['QuestionType']
            packet['TableId'] = self.person['TableID']
            answerIndex = random.choice([0,1])
            packet['answerIndex'] = answerIndex
            self.person['QuestionType'] = None
            self.person['TableID'] = None
        elif type == 1: #AskBasic
            packet['AskType'] = AskType
        res = Functions.sendpacket(packet)
        res = Functions.waitforpacket_with_heartbeat(self.person, "PACKET_GC_GUILDACTIVITYDRINK")
        return res
