import NetPackets
import Functions


class ACGGMCommand():
    def __init__(self, person):
        self.person = person

    def run(self, msg):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.CGGMCommand(self.person)
        packet['msg'] = msg

        res = Functions.sendpacket(packet)
        #res = Functions.waitforpacket_with_heartbeat(self.person, "kSCHeartbeatAck")
        return res
