import NetPackets
import random
import binascii
import struct
import Functions

class ALoginAttackWrongContent():
    def __init__(self, person):
        self.person = person        
        
    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)  

        packet = NetPackets.PACKETS.PACKET_CG_CHARMOVE(self.person)

        packet['m_ObjID'] = 32  #get it when enterscene
        packet['CurPostion'] = [self.person['posx'], self.person['posz']] #[x,z]
        packet['TargetPos'] = [[15.8369722366, 33.5553398132]]
        packet['m_yNumTargetPos'] = len(packet['TargetPos'])

        packet['m_nHandleID'] = 0
        packet['m_bKeyboardMove'] = 8
        packet['m_bDir'] = 3
        packet['m_bIsStopMsg'] = 9

        self.person['posx'] = 15.8369722366
        self.person['posz'] = 33.5553398132
        
        Functions.sendpacket(packet)
        return (True,0,"Send wrong content login attack successfully.")