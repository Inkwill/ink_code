#coding=utf-8
import NetPackets
import Functions
import Users

class ACL_Connect():
    def __init__(self, person):
        self.person = person        
        
    def run(self,account_startwith,client_version):
        if self.person['userName'] == None:
            self.person['userName'] = u'R' + unicode(Users.User.getUserAccount(account_startwith))
        
        packet = NetPackets.PACKETS.PACKET_CL_Connect(self.person)
        packet['OpenID'] = self.person['userName']
        packet['AppId'] = u'NULL'
        packet['DeviceId'] = u'1f8574e75b59488ae12915f400ae4430'
        packet['RegChannel'] = u''
        packet['ClientVersion'] = unicode(client_version)
        packet['TelecomOper'] = u'中国移动'
        packet['InstallChannelId'] = u''
        packet['GameVersion'] = 0
        packet['ResFirstVersion'] = 3
        

        Functions.sendpacket(packet)
        res = Functions.waitforpacket(self.person, "PACKET_LC_RetConnect")
        return res