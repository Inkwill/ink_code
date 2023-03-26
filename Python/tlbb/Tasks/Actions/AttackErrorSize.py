#coding= utf-8
import NetPackets
import random
import binascii
import struct
import Functions
import Users

class AttackErrorSize():
    def __init__(self, person):
        self.person = person        
        
    def run(self, account_startwith, client_version):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)  
   
        if self.person['userName'] == None:
            self.person['userName'] = u'R' + unicode(Users.User.getUserAccount(account_startwith))

        packet = NetPackets.PACKETS.PACKET_CL_Connect(self.person)
        packet['OpenID'] = self.person['userName']
        packet['AppId'] = u'NULL'
        packet['DeviceId'] = u'1f8574e75b59488ae12915f400ae4430'
        packet['RegChannel'] = 0
        packet['ClientVersion'] = unicode(client_version)
        packet['TelecomOper'] = u'中国移动'
        packet['InstallChannelId'] = 0
        packet['GameVersion'] = 0
        packet['ResFirstVersion'] = 3

        sendstream = '\x00' * 6
        size = int(random.random() * 100)
        sendstream += struct.pack("=HI", packet.getid(), size)
        sendstream += packet.getdatastream()
        
        self.person['socket'].send(sendstream)
        return (True,0,"Send error size login attack successfully.")