#coding=utf-8
import NetPackets
import Functions

class ACG_ASKAUCTIONSHOPITEM():
    def __init__(self, person):
        self.person = person

    def run(self):
        packet = NetPackets.PACKETS.PACKET_CG_ASKAUCTIONSHOPITEM(self.person)

        packet['Type'] = '0'
        packet['Asktype'] = '0'
        packet['Page'] = 1        
        packet['index'] = 1        
        packet['SubType'] = '0'       
        
        Functions.sendpacket(packet)

        res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_NETCHECK')
        return res