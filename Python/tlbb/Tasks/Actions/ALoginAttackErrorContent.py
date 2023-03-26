import NetPackets
import random
import binascii
import struct
import Functions

class ALoginAttackErrorContent():
    def __init__(self, person):
        self.person = person        
        
    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)  

        Ids = [163, 277, 359, 418, 481, 487, 547, 714, 729, 772, 799, 907, 925, 964, 1179, 1187, 1361, 1370, 1442,
               1563, 1689, 1691, 1719, 1741, 9998, 188, 524, 746, 912, 1690, 1738]
        #Ids = NetPackets.Defines.PACKET_DIC.keys()
        id = Ids[int(random.random()*len(Ids))]

        print "id:", id
        if id not in NetPackets.Defines.PACKET_DIC:
            print "id:", id
        packetname = NetPackets.Defines.PACKET_DIC[id]
        while packetname == "":
            id = Ids[int(random.random()*len(Ids))]
            packetname = NetPackets.Defines.PACKET_DIC[id]

        print "packetname:", packetname
        packet = eval("NetPackets.PACKETS.%s(self.person)"%(packetname))

        sendstream = '\x00' * 6
        sendstream += struct.pack("=HI", packet.getid(), packet.getdatasize())
        size = packet.getdatasize()
        content = ""
        for i in range(size):
            content = random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF')

        sendstream += binascii.unhexlify(content)

        self.person['socket'].send(sendstream)
        return (True,0,"Send error content login attack successfully.")