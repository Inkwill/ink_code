#coding= utf-8
import NetPackets
import random
import binascii
import struct
import Functions

class AttackErrorContent():
    def __init__(self, person):
        self.person = person        
        
    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)  

        Ids = [355, 426, 711]
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