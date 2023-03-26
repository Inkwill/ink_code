#coding=utf-8
import NetPackets
import Functions
import Users

class ACG_CHARMOVE():
    def __init__(self, person):
        self.person = person

    def run(self, posx, posz):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        packet = NetPackets.PACKETS.PACKET_CG_CHARMOVE(self.person)

        packet['m_ObjID'] = self.person['m_ObjID']  #get it when enterscene
        packet['CurPostion'] = [self.person['posx'], self.person['posz']] #[x,z]
        #packet['TargetPos'] = [[self.person['posx'], self.person['posz']], [posx, posz]] #[[x,z],[x.z]]
        packet['TargetPos'] = [[posx, posz]]
        packet['m_yNumTargetPos'] = len(packet['TargetPos'])

        packet['m_nHandleID'] = 0
        packet['m_bKeyboardMove'] = 0
        packet['m_bDir'] = -1.0
        packet['m_bIsStopMsg'] = -1

        self.person['posx'] = posx
        self.person['posz'] = posz

        res = Functions.sendpacket(packet)
#         if res[0] == False:
#             print self.person['userName'] + u' Error, ACG_CHARMOVE'
#             raise Exception("ACG_CHARMOVE Failed")
        #if waitforpacket is not None:
        #    res = Functions.waitforpacket(self.person, waitforpacket)
        #res = Functions.waitforpacket(self.person, 'PACKET_GC_CHARMOVE')
        #res = Functions.waitforpacket_with_heartbeat(self.person, 'PACKET_GC_CHARMOVE',5)
        return res