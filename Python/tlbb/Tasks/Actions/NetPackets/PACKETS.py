# -*- coding: utf-8 -*-

from Packet import Packet
import struct
from TLSocket import *
from GUILDPACKET import *


############################ yaojun start
class PACKET_CL_Connect(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['IsOpenTLog'] = True
        self['OpenID'] = u''
        #         self['AppId'] = u''
        self['PlatId'] = 0
        self['DeviceId'] = u''
        self['RegChannel'] = u''
        self['ClientVersion'] = u''
        self['TelecomOper'] = u''
        self['InstallChannelId'] = u''
        self['GameVersion'] = 0
        self['ResFirstVersion'] = 0
        self['ResSecondVersion'] = 0
        #         self['AppId_ACCOUNT'] = 32
        self['DeviceId_ACCOUNT'] = 64
        self['ClientVersion_ACCOUNT'] = 64
        self['TelecomOper_ACCOUNT'] = 64
        self['Channel_ACCOUNT'] = 64

    def getdatastream(self):
        buf = ''
        buf += WriteCharArray(self['OpenID'], 128, True)
        if self['IsOpenTLog']:
            #             buf += WriteCharArray(self['AppId'],self['AppId_ACCOUNT'],True)
            buf += WriteInt32(self['PlatId'])
            buf += WriteCharArray(self['DeviceId'], self['DeviceId_ACCOUNT'], True)
            buf += WriteCharArray(self['RegChannel'],self['Channel_ACCOUNT'],True)
            buf += WriteCharArray(self['ClientVersion'], self['ClientVersion_ACCOUNT'], True)
            buf += WriteCharArray(self['TelecomOper'], self['TelecomOper_ACCOUNT'], True)
            buf += WriteCharArray(self['InstallChannelId'],self['Channel_ACCOUNT'] ,True)
            buf += WriteInt32(self['GameVersion'])
            buf += WriteInt32(self['ResFirstVersion'])
        return buf

    def filldatafromstream(self, buf):
        (self['OpenID'],buf) = ReadCharArray(buf,128)
#         (self['AppId'],buf) = ReadCharArray(buf,self['AppId_ACCOUNT'])
        (self['PlatId'],buf) = ReadInt32(buf)
        (self['DeviceId'],buf) = ReadCharArray(buf,self['DeviceId_ACCOUNT'])
        (self['RegChannel'],buf) = ReadCharArray(buf,self['Channel_ACCOUNT'])
        (self['ClientVersion'],buf) = ReadCharArray(buf,self['ClientVersion_ACCOUNT'])
        (self['TelecomOper'],buf) = ReadCharArray(buf,self['TelecomOper_ACCOUNT'])
        (self['InstallChannelId'],buf) = ReadCharArray(buf,self['Channel_ACCOUNT'])
        (self['GameVersion'],buf) = ReadInt32(buf)
        (self['ResFirstVersion'],buf) = ReadInt32(buf)
        return (self,buf)

class PACKET_LC_RetConnect(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['mServerKey'] = 0
        self['result'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['result'])
        buf += WriteUInt32(self['mServerKey'])
        return buf

    def filldatafromstream(self, buf):
        (self['result'], buf) = ReadInt(buf)
        (self['mServerKey'], buf) = ReadUint(buf)
        return (self, buf)

    def handle(self):
        self.person['mServerKey'] = self['mServerKey']
        self.person['LC_mResult'] = self['result']
        pass


class PACKET_CL_AskLogin(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['OpenID'] = u''
        self['Version'] = 0
        self['KickUser'] = 0
        self['AccessToken'] = u''
        self['IsGuest'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteCharArray(self['OpenID'], 128, True);
        buf += WriteUInt32(self['Version'])
        buf += WriteInt32(self['KickUser'])
        buf += WriteCharArray(self['AccessToken'], 128, True);
        buf += WriteInt32(self['IsGuest'])
        return buf

    def filldatafromstream(self, buf):
        (self['OpenID'], buf) = ReadCharArray(buf, 128)
        (self['Version'], buf) = ReadUInt32(buf)
        (self['KickUser'], buf) = ReadInt32(buf)
        (self['AccessToken'], buf) = ReadCharArray(buf, 128)
        (self['IsGuest'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_LC_RetLogin(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['userAccount'] = ''
        self['m_CountTime'] = 0
        self['result'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteCharArray(self['userAccount'], 128, True);
        buf += WriteInt32(self['result'])
        buf += WriteInt16(self['m_CountTime'])
        return buf

    def filldatafromstream(self, buf):
        (self['userAccount'], buf) = ReadCharArray(buf, 128)
        (self['result'], buf) = ReadInt32(buf)
        (self['m_CountTime'], buf) = ReadShort(buf)
        return (self, buf)

    def handle(self):
        # self.person['mServerKey'] = self['mServerKey']
        # self.person['LC_mResult'] = self['result']
        pass


class PACKET_CL_AskCharList(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['OpenID'] = u''

    def getdatastream(self):
        buf = ''
        buf += WriteCharArray(self['OpenID'], 128, True);
        return buf

    def filldatafromstream(self, buf):
        (self['OpenID'], buf) = ReadCharArray(buf, 127)
        return (self, buf)


class DB_CHAR_BASE_INFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GUID'] = 0
        self['m_Sex'] = 0
        self['m_Name'] = ''
        self['m_Level'] = 0
        self['m_HairColor'] = 0
        self['m_HairModel'] = 0
        self['m_StartScene'] = 0
        self['m_Menpai'] = 0
        self['m_HeadID'] = 0
        self['m_nWeaponOpenFlag'] = 0
        self['m_MysticalWeaponLevel'] = 0
        self['m_DressId'] = 0
        self['m_Color'] = 0


class PACKET_LC_RetCharList(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['result'] = 0
        self['Count'] = 0
        self['szAccount'] = ''
        self['RoleList'] = []

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['result'], buf) = ReadInt32(buf)
        if self['result'] != 0:
            return (self, buf)
        (self['szAccount'], buf) = ReadCharArray(buf, 128)
        (self['Count'], buf) = ReadByte(buf)
        self['Count'] = ord(self['Count'])
        if self['Count'] > 0:
            for i in range(self['Count']):
                tempdata = DB_CHAR_BASE_INFO(None)
                hw = 0
                hl = 0
                (hw, buf) = ReadInt32(buf)
                (hl, buf) = ReadInt32(buf)
                tempdata['m_GUID'] = MakeGUID(hw, hl)
                (tempdata['m_Sex'], buf) = ReadInt32(buf)
                (tempdata['tmpName'], buf) = ReadCharArray(buf, 30)
                (tempdata['m_Level'], buf) = ReadInt32(buf)
                (tempdata['m_HairColor'], buf) = ReadUInt32(buf)
                (tempdata['m_HairModel'], buf) = ReadByte(buf)
                tempdata['m_HairModel'] = ord(tempdata['m_HairModel'])
                (tempdata['m_StartScene'], buf) = ReadShort(buf)
                (tempdata['m_Menpai'], buf) = ReadInt32(buf)
                (tempdata['m_HeadID'], buf) = ReadInt32(buf)
                (tempdata['m_nWeaponOpenFlag'], buf) = ReadByte(buf)
                tempdata['m_nWeaponOpenFlag'] = ord(tempdata['m_nWeaponOpenFlag'])
                (tempdata['m_MysticalWeaponLevel'], buf) = ReadInt32(buf)
                (tempdata['m_DressId'], buf) = ReadInt32(buf)
                (tempdata['m_Color'], buf) = ReadInt32(buf)
                self['RoleList'].append(tempdata)
        return (self, buf)

    def handle(self):
        self.person['RoleList'] = self['RoleList']
        if len(self['RoleList']) != 0:
            self.person['m_Guid'] = self['RoleList'][0]['m_GUID']
            self.person['menPai'] = self['RoleList'][0]['m_Menpai']
            self.person['sex'] = self['RoleList'][0]['m_Sex']
            self.person['SceneID'] = self['RoleList'][0]['m_StartScene']
            self.person['Level'] = self['RoleList'][0]['m_Level']
        pass


class PACKET_CL_AskCreateChar(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['CharName'] = ''
        self['Sex'] = 0
        self['MenPai'] = 0
        self['GUID'] = 0
        self['m_HairColor'] = 0
        self['m_HairModel'] = 0
        self['m_HeadID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteCharArray(self['CharName'], 30, True);
        buf += WriteInt32(self['Sex'])
        buf += WriteInt32(self['MenPai'])
        buf += WriteUInt64(self['GUID'])
        buf += WriteUInt32(self['m_HairColor'])
        buf += WriteByte(chr(self['m_HairModel']))
        buf += WriteInt32(self['m_HeadID'])
        return buf

    def filldatafromstream(self, buf):
        (self['CharName'], buf) = ReadCharArray(buf, 30)
        (self['Sex'], buf) = ReadInt32(buf)
        (self['MenPai'], buf) = ReadInt32(buf)
        (self['GUID'], buf) = ReadUInt64(buf)
        (self['m_HairColor'], buf) = ReadUInt32(buf)
        (self['m_HairModel'], buf) = ReadByte(buf)
        self['m_HairModel'] = ord(self['m_HairModel'])
        (self['m_HeadID'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_LC_RetCreateChar(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['result'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['result'])
        return buf

    def filldatafromstream(self, buf):
        (self['result'], buf) = ReadInt(buf)
        return (self, buf)

    def handle(self):
        self.person['LC_mResult'] = self['result']
        pass


class PACKET_CL_AskCharLogin(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['GUID'] = 0
        self['PlayerID'] = 0
        self['SceneID'] = 0
        self['SzAccount'] = u''
        self['Name'] = u''
        self['Level'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt64(self['GUID'])
        buf += WriteInt16(self['PlayerID'])
        buf += WriteInt16(self['SceneID'])
        buf += WriteCharArray(self['SzAccount'], 128, True);
        buf += WriteCharArray(self['Name'], 30, True);
        buf += WriteUInt32(self['Level'])
        return buf

    def filldatafromstream(self, buf):
        (self['GUID'], buf) = ReadUInt64(buf)
        (self['PlayerID'], buf) = ReadInt16(buf)
        (self['SceneID'], buf) = ReadInt16(buf)
        (self['SzAccount'], buf) = ReadCharArray(buf, 128)
        (self['Name'], buf) = ReadCharArray(buf, 30)
        (self['Level'], buf) = ReadUInt32(buf)
        return (self, buf)


class PACKET_LC_RetCharLogin(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        #         self['IP_SIZE'] = 24
        #         self['ServerIp'] = u''
        #         self['ServerPort'] = 0
        self['Key'] = 0
        self['WorldId'] = 0
        self['ZoonId'] = 0
        self['result'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['result'])

        #         buf += WriteUInt32(self['ServerPort'])
        #         buf += WriteCharArray(self['ServerIp'],self['IP_SIZE'],True)
        buf += WriteUInt32(self['Key'])
        buf += WriteByte(chr(self['WorldId']))
        buf += WriteUInt32(self['ZoonId'])
        return buf

    def filldatafromstream(self, buf):
        (self['result'], buf) = ReadInt(buf)
        #         (self['ServerPort'],buf) = ReadUint(buf)
        #         (self['ServerIp'],buf) = ReadCharArray(buf,self['IP_SIZE'])
        (self['Key'], buf) = ReadUint(buf)
        (self['WorldId'], buf) = ReadByte(buf)
        self['WorldId'] = ord(self['WorldId'])
        (self['ZoonId'], buf) = ReadUint(buf)
        return (self, buf)

    def handle(self):
        self.person['LC_mResult'] = self['result']
        self.person['ServerKey'] = self['Key']
        self.person['ZoonId'] = self['ZoonId']
        self.person['WorldId'] = self['WorldId']


# self.person['Scene_ServerIp'] = self['ServerIp']
#         self.person['Scene_ServerPort'] = self['ServerPort']

class PACKET_LC_Status(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['mTurnNumber'] = 0
        self['result'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt16(self['mTurnNumber'])
        buf += WriteInt32(self['result'])
        return buf

    def filldatafromstream(self, buf):
        (self['mTurnNumber'], buf) = ReadUShort(buf)
        (self['result'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        self.person['mTurnNumber'] = self['mTurnNumber']
        self.person['LC_Status_smResult'] = self['result']
        self.person['Rev_LC_Status'] = 1


class PACKET_LC_ReConnectData(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['IP_SIZE'] = 24
        self['ServerIp'] = u''
        self['ServerPort'] = 0
        self['Key'] = 0
        self['WorldId'] = 0
        self['ZoonId'] = 0
        self['ServerId'] = 0
        self['result'] = 0
        self['AccName'] = u''
        self['PlayerID'] = 0
        self['MenPai'] = 0
        self['UserKey'] = 0
        self['m_GUID'] = 0
        self['Sex'] = 0
        self['Level'] = 0

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['strAccName'], buf) = ReadCharArray(buf, 128)
        (self['PlayerID'], buf) = ReadShort(buf)

        (self['MenPai'], buf) = ReadInt(buf)
        (self['UserKey'], buf) = ReadUint(buf)
        (hw, buf) = ReadInt32(buf)
        (hl, buf) = ReadInt32(buf)
        self['m_GUID'] = MakeGUID(hw, hl)
        (self['Sex'], buf) = ReadUint(buf)
        (self['strAddress'], buf) = ReadCharArray(buf, self['IP_SIZE'])
        (self['ServerPort'], buf) = ReadUint(buf)
        (self['Key'], buf) = ReadUint(buf)
        (self['WorldId'], buf) = ReadByte(buf)
        self['WorldId'] = ord(self['WorldId'])
        (self['ZoonId'], buf) = ReadUint(buf)
        (self['ServerId'], buf) = ReadUint(buf)
        (self['Level'], buf) = ReadInt(buf)
        return (self, buf)

    def handle(self):
        self.person['LC_mResult'] = self['result']
        self.person['ServerKey'] = self['Key']
        self.person['ZoonId'] = self['ZoonId']
        self.person['WorldId'] = self['WorldId']
        self.person['Scene_ServerIp'] = self['strAddress']
        self.person['Scene_ServerPort'] = self['ServerPort']
        self.person['m_Guid'] = self['m_GUID']
        self.person['menPai'] = self['MenPai']
        self.person['sex'] = self['Sex']
        self.person['Level'] = self['Level']
        self.person['Rev_LC_ReConnectData'] = 1


class PACKET_CG_CGConnect(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['name'] = ''
        self['m_Guid'] = 0
        self['m_HW'] = 0
        self['m_HL'] = 0
        self['sex'] = 0
        self['IsReconnect'] = 0
        self['menPai'] = 0
        self['ZoonId'] = 0
        self['Key'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt32(self['Key'])
        buf += WriteUInt64(self['m_Guid'])
        buf += WriteUInt16(self['ZoonId'])
        buf += WriteCharArray(self['name'], 128, True);
        buf += WriteInt32(self['sex'])
        buf += WriteInt32(self['menPai'])
        buf += WriteInt32(0)
        buf += WriteInt32(0)
        buf += WriteInt32(0)
        buf += WriteInt32(self['IsReconnect'])
        buf += WriteInt32(0)
        buf += WriteInt32(0)
        buf += WriteInt32(0)
        buf += WriteInt32(0)
        return buf

    def filldatafromstream(self, buf):
        (self['Key'], buf) = ReadUInt32(buf)
        (self['m_Guid'], buf) = ReadUInt64(buf)
        (self['ZoonId'], buf) = ReadUInt16(buf)
        (self['name'], buf) = ReadCharArray(buf, 128);
        (self['sex'], buf) = ReadInt32(buf)
        (self['menPai'], buf) = ReadInt32(buf)
        temp = 0
        (temp, buf) = ReadInt32(buf)
        (temp, buf) = ReadInt32(buf)
        (temp, buf) = ReadInt32(buf)
        (self['IsReconnect'], buf) = ReadInt32(buf)
        (temp, buf) = ReadInt32(buf)
        (temp, buf) = ReadInt32(buf)
        (temp, buf) = ReadInt32(buf)
        (temp, buf) = ReadInt32(buf)
        return (self, buf)


class WorldPostion(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['x'] = 0
        self['z'] = 0


class PACKET_GC_GCConnect(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['SeverId'] = 0
        self['SceneId'] = 0
        self['Postion'] = WorldPostion(None)
        self['WhyFlag'] = 1

    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['SeverId'])
        buf += WriteInt16(self['SceneId'])
        buf += WriteSingle(self['Postion'].x)
        buf += WriteSingle(self['Postion'].z)
        buf += WriteInt16(self['WhyFlag'])

        return buf

    def filldatafromstream(self, buf):
        (self['SeverId'], buf) = ReadInt16(buf)
        (self['SceneId'], buf) = ReadInt16(buf)
        (self['Postion'].x, buf) = ReadSingle(buf)
        (self['Postion'].z, buf) = ReadSingle(buf)
        (self['WhyFlag'], buf) = ReadInt16(buf)
        return (self, buf)

    def handle(self):
        self.person['SceneId'] = self['SceneId']
        self.person['f_x'] = self['Postion'].x
        self.person['f_z'] = self['Postion'].z
        pass


################################## yaojun end


################################## luoyunpeng start
class PACKET_CG_HeartBeat(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_flag'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt16(self['m_flag'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_flag'], buf) = ReadUInt16(buf)
        return (self, buf)


################################## luoyunpeng end

###################### yaojun  start
class PACKET_CG_ENTERSCENE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['enterType'] = 0  # // 0??the first time enter scene after login. 1:changescene from other scene
        self['sceneID'] = 0
        self['posX'] = 0.0
        self['posZ'] = 0.0
        self['m_AOIMaxCount'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['sceneID'])
        buf += WriteByte(chr(self['enterType']))
        buf += WriteSingle(self['posX'])
        buf += WriteSingle(self['posZ'])
        buf += WriteInt32(self['m_AOIMaxCount'])
        return buf

    def filldatafromstream(self, buf):
        (self['sceneID'], buf) = ReadInt16(buf)
        (self['enterType'], buf) = ReadByte(buf)
        self['enterType'] = ord(self['enterType'])
        (self['posX'], buf) = ReadSingle(buf)
        (self['posZ'], buf) = ReadSingle(buf)
        (self['m_AOIMaxCount'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_ENTERSCENE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_byRet'] = 0  # 0: player can enter scene.
        self['m_nSceneID'] = 0
        self['m_nResID'] = 0
        self['m_posX'] = 0
        self['m_posZ'] = 0
        self['m_ObjID'] = 0
        self['m_bIsCity'] = 0
        self['m_nCityLevel'] = 0
        self['m_nPvpRuler'] = 0
        self['m_bIsKvkServer'] = 0
        self['m_nCamerFlag'] = 0
        self['m_nCamerPlay'] = 0
        self['m_bIsTServer'] = 0

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_byRet'], buf) = ReadByte(buf)
        self['m_byRet'] = ord(self['m_byRet'])
        (self['m_nSceneID'], buf) = ReadInt16(buf)
        (self['m_nResID'], buf) = ReadInt16(buf)
        (self['m_posX'], buf) = ReadSingle(buf)
        (self['m_posZ'], buf) = ReadSingle(buf)
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['m_bIsCity'], buf) = ReadByte(buf)
        self['m_bIsCity'] = ord(self['m_bIsCity'])
        (self['m_nCityLevel'], buf) = ReadByte(buf)
        self['m_nCityLevel'] = ord(self['m_nCityLevel'])
        (self['m_nPvpRuler'], buf) = ReadInt32(buf)
        (self['m_bIsKvkServer'], buf) = ReadInt32(buf)
        (self['m_nCamerFlag'], buf) = ReadInt32(buf)
        (self['m_nCamerPlay'], buf) = ReadByte(buf)
        self['m_nCamerPlay'] = ord(self['m_nCamerPlay'])
        (self['m_bIsTServer'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        if self.person['monsterdic'] != None:
            self.person['monsterdic'] = {}
        self.person['SceneId'] = self['m_nSceneID']
        self.person['m_nResID'] = self['m_nResID']
        self.person['m_ObjID'] = self['m_ObjID']
        self.person['posx'] = self['m_posX']
        self.person['posz'] = self['m_posZ']


###################### yaojun end

class PACKET_CG_CHARASKBASEATTRIB(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ObjID'] = 0
        self['m_nType'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_ObjID'])
        buf += WriteByte(chr(self['m_nType']))
        return buf

    def filldatafromstream(self, buf):
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['m_nType'], buf) = ReadByte(buf)
        self['m_nType'] = ord(self['m_nType'])
        return (self, buf)


class OWN_SETTING(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_SettingType'] = 0
        self['m_SettingData'] = 0


class PACKET_CG_MODIFYSETTING(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Value'] = OWN_SETTING(None)
        self['m_Type'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_Type']))
        buf += WriteByte(chr(self['m_Value']['m_SettingType']))
        buf += WriteInt32(self['m_Value']['m_SettingData'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_Type'], buf) = ReadByte(buf)
        self['m_Type'] = ord(self['m_Type'])

        (self['m_Value']['m_SettingType'], buf) = ReadByte(buf)
        self['m_Value']['m_SettingType'] = ord(self['m_Value']['m_SettingType'])

        (self['m_Value']['m_SettingData'], buf) = ReadInt32(buf)

        return (self, buf)


class PACKET_GC_RETSETTING(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Value'] = []

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        for i in range(111):
            temp = OWN_SETTING(None)
            (temp['m_SettingType'], buf) = ReadByte(buf)
            temp['m_SettingType'] = ord(temp['m_SettingType'])
            (temp['m_SettingData'], buf) = ReadInt32(buf)
            self['m_Value'].append(temp)

        return (self, buf)

    def handle(self):
        pass


class PACKET_CG_ASKMAIL(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['AskType'] = 0
        self['temp'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['AskType']))
        for i in range(22):
            buf += WriteByte(chr(self['temp']))
        return buf

    def filldatafromstream(self, buf):
        (self['AskType'], buf) = ReadByte(buf)
        self['AskType'] = ord(self['AskType'])
        for i in range(22):
            (self['temp'], buf) = ReadByte(buf)
            self['temp'] = ord(self['temp'])
        return (self, buf)


class PACKET_CG_CHAR_ASK_IMPACTLIST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ObjID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_ObjID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_ObjID'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_ASKSTUDYXINFA(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Mode'] = 0
        self['m_idXinfaType'] = 0
        self['m_SkillId'] = 0
        self['m_SkillCurLevel'] = 0
        self['m_WantLevel'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_Mode']))
        buf += WriteByte(chr(self['m_idXinfaType']))
        buf += WriteInt32(self['m_SkillId'])
        buf += WriteInt32(self['m_SkillCurLevel'])
        buf += WriteInt32(self['m_WantLevel'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_Mode'], buf) = ReadByte(buf)
        self['m_Mode'] = ord(self['m_Mode'])
        (self['m_idXinfaType'], buf) = ReadByte(buf)
        self['m_idXinfaType'] = ord(self['m_idXinfaType'])
        (self['m_SkillId'], buf) = ReadInt32(buf)
        (self['m_SkillCurLevel'], buf) = ReadInt32(buf)
        (self['m_WantLevel'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_CHARDEFAULTEVENT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ObjID'] = 0
        self['m_nIssuesScript'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_ObjID'])
        buf += WriteInt32(self['m_nIssuesScript'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['m_nIssuesScript'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_MISSION_ENTERSINGLEFUBEN(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_npcId'] = 0
        self['m_MissionIndex'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_npcId'])
        buf += WriteInt32(self['m_MissionIndex'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_npcId'], buf) = ReadInt32(buf)
        (self['m_MissionIndex'], buf) = ReadInt32(buf)
        return (self, buf)


class ScriptParam_MissionTips(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_strLen'] = 0
        self['m_Text'] = u''


class PACKET_GC_SCRIPTCOMMAND(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_CmdID'] = 0
        self['m_ParamMissionTips'] = ScriptParam_MissionTips(None)

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_CmdID'], buf) = ReadInt32(buf)
        if self['m_CmdID'] == 5:
            (self['m_ParamMissionTips']['m_strLen'], buf) = ReadInt16(buf)
            (self['m_ParamMissionTips']['m_Text'], buf) = ReadCharArray(buf, self['m_ParamMissionTips']['m_strLen'])
        return (self, buf)

    def handle(self):
        self.person['m_ParamMissionTips'] = self['m_ParamMissionTips']


class PACKET_CG_EVENTREQUEST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_NpcID'] = 0
        self['m_IssueScriptID'] = 0
        self['m_ScriptID'] = 0
        self['m_ExIndex'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_ScriptID'])
        buf += WriteInt32(self['m_ExIndex'])
        buf += WriteInt32(self['m_NpcID'])
        buf += WriteInt32(self['m_IssueScriptID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_ScriptID'], buf) = ReadInt32(buf)
        (self['m_ExIndex'], buf) = ReadInt32(buf)
        (self['m_NpcID'], buf) = ReadInt32(buf)
        (self['m_IssueScriptID'], buf) = ReadInt32(buf)
        return (self, buf)


# 属性没有加全，只写了自己需要的背包位置
class PACKET_GC_NOTIFYEQUIP(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_bagindex'] = 0
        self['m_ItemGUID_L'] = 0
        self['m_ItemGUID_H'] = 0

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_bagindex'], buf) = ReadUInt16(buf)
        (self['m_ItemGUID_H'], buf) = ReadInt32(buf)
        (self['m_ItemGUID_L'], buf) = ReadInt32(buf)
        guid = MakeGUID(self['m_ItemGUID_L'], self['m_ItemGUID_H'])
        # print '**************', guid
        return (self, buf)

    def handle(self):
        self.person['GMItemBagIndex'] = self['m_bagindex']
        guid = MakeGUID(self['m_ItemGUID_L'], self['m_ItemGUID_H'])
        # print '**************',guid
        self.person['m_Item_guid'] = guid


class PACKET_CG_USEEQUIP(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_BagIndex'] = 0
        self['m_EquipPoint'] = 0
        self['m_UseEquipType'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_BagIndex']))
        buf += WriteByte(chr(self['m_EquipPoint']))
        buf += WriteByte(chr(self['m_UseEquipType']))
        return buf

    def filldatafromstream(self, buf):
        (self['m_BagIndex'], buf) = ReadByte(buf)
        self['m_BagIndex'] = ord(self['m_BagIndex'])

        (self['m_EquipPoint'], buf) = ReadByte(buf)
        self['m_EquipPoint'] = ord(self['m_EquipPoint'])

        (self['m_UseEquipType'], buf) = ReadByte(buf)
        self['m_UseEquipType'] = ord(self['m_UseEquipType'])

        return (self, buf)


class PACKET_CG_MANIPULATEPETRET(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_objid'] = 0
        self['m_uPetGuid'] = 0
        self['m_type'] = 0
        self['m_nBagIndex'] = 0
        self['m_nReplaceSkillIndex'] = 0
        self['m_SecondPetGUID'] = 0
        self['m_nSkillID'] = 0

        self.m_type_dic = {'MANIPULATEPET_INVALID': -1, \
                           'MANIPULATEPET_CREATEPET': 0, \
                           'MANIPULATEPET_DELETEPET': 1, \
                           'MANIPULATEPET_FREEPET': 2, \
                           'MANIPULATEPET_ASKOFOTHERINFO': 3, \
                           'MANIPULATEPET_POSSESSIONPET': 4, \
                           'MANIPULATEPET_RESTOFPET': 5, \
                           'MANIPULATEPET_PETSKILLBOOKSTUDY': 6, \
                           'MANIPULATEPET_FORGETPETSKILL': 7, \
                           'MANIPULATEPET_PETSKILLLEVELUP': 8, \
                           'MANIPULATEPET_PETSKILLLREPLACE': 9, \
                           'MANIPULATEPET_PETPROCREATE': 10, \
                           'MANIPULATEPET_TAKEOUT': 11, \
                           'MANIPULATEPET_PETRETURNTOCHILD': 12, \
                           'MANIPULATEPET_PETGODOX': 13, \
                           'MANIPULATEPET_PETEXPITEM': 14, \
                           'MANIPULATEPET_PETRONGHEDU': 15, \
                           }

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_objid'])
        buf += WriteUInt64(self['m_uPetGuid'])
        buf += WriteInt32(self['m_type'])
        if (self['m_type'] == 6 or self['m_type'] == 12 or self['m_type'] == 14):
            buf += WriteInt32(self['m_nBagIndex'])
        if self['m_type'] == 9:
            buf += WriteInt32(self['m_nBagIndex'])
            buf += WriteInt32(self['m_nReplaceSkillIndex'])
        if (self['m_type'] == 10 or self['m_type'] == 11):
            buf += WriteUInt64(self['m_SecondPetGUID'])
        if self['m_type'] == 8:
            buf += WriteInt32(self['m_nBagIndex'])
            buf += WriteInt32(self['m_nReplaceSkillIndex'])
            buf += WriteInt32(self['m_nSkillID'])
        if self['m_type'] == 7:
            buf += WriteInt32(self['m_nSkillID'])

        return buf

    def filldatafromstream(self, buf):
        (self['m_objid'], buf) = ReadInt32(buf)
        (self['m_uPetGuid'], buf) = ReadInt32(buf)
        (self['m_type'], buf) = ReadInt32(buf)
        if (self['m_type'] == 6 or self['m_type'] == 12 or self['m_type'] == 14):
            (self['m_nBagIndex'], buf) = ReadInt32(buf)
        if self['m_type'] == 9:
            (self['m_nBagIndex'], buf) = ReadInt32(buf)
            (self['m_nReplaceSkillIndex'], buf) = ReadInt32(buf)
        if (self['m_type'] == 10 or self['m_type'] == 11):
            (self['m_SecondPetGUID'], buf) = ReadUInt64(buf)
        if self['m_type'] == 8:
            (self['m_nBagIndex'], buf) = ReadInt32(buf)
            (self['m_nReplaceSkillIndex'], buf) = ReadInt32(buf)
            (self['m_nSkillID'], buf) = ReadInt32(buf)
        if self['m_type'] == 7:
            (self['m_nSkillID'], buf) = ReadInt32(buf)
        return (self, buf)


###################yaojun  start
class PACKET_CC_TEAM_INVITE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_nSourObjID'] = 0
        self['m_byNameSize'] = 0
        self['m_szName'] = ''
        self['m_nDestZoneWorldId'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_nSourObjID'])
        buf += WriteByte(chr(self['m_byNameSize']))
        buf += WriteCharArray(self['m_szName'], self['m_byNameSize'], True)
        buf += WriteInt16(self['m_nDestZoneWorldId'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_nSourObjID'], buf) = ReadInt32(buf)
        (self['m_byNameSize'], buf) = ReadByte(buf)
        self['m_byNameSize'] = ord(self['m_byNameSize'])
        (self['m_szName'], buf) = ReadCharArray(buf, self['m_byNameSize'])
        (self['m_nDestZoneWorldId'], buf) = ReadInt16(buf)
        return (self, buf)


class PACKET_CG_TEAM_APPLY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_SourGUID'] = 0
        self['m_byDestNameSize'] = 0
        self['m_szDestName'] = ''
        self['m_nDestZoneWorldId'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt64(self['m_SourGUID'])
        buf += WriteByte(chr(self['m_byDestNameSize']))
        buf += WriteCharArray(self['m_szDestName'], self['m_byDestNameSize'], True)
        buf += WriteInt16(self['m_nDestZoneWorldId'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_SourGUID'], buf) = ReadInt64(buf)
        (self['m_byDestNameSize'], buf) = ReadByte(buf)
        self['m_byDestNameSize'] = ord(self['m_byDestNameSize'])
        (self['m_szDestName'], buf) = ReadCharArray(buf, self['m_byDestNameSize'])
        (self['m_nDestZoneWorldId'], buf) = ReadInt16(buf)
        return (self, buf)


class PACKET_CG_TEAM_LEAVE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GUID64'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt64(self['m_GUID64'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_GUID64'], buf) = ReadUInt64(buf)
        return (self, buf)


class PACKET_CG_ASK_TEAM_INFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_nObjID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_nObjID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_nObjID'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_ASK_TEAM_MEMBER_INFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_SceneID'] = 0
        self['m_GUID'] = 0
        self['m_nObjID'] = 0
        self['m_nTeamID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_nObjID'])
        (low, high) = DecodeUInt64(self['m_GUID'])
        buf += WriteInt32(low)
        buf += WriteInt32(high)
        buf += WriteInt16(self['m_SceneID'])
        buf += WriteInt16(self['m_nTeamID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_nObjID'], buf) = ReadInt32(buf)
        (G_L, buf) = ReadInt32(buf)
        (G_H, buf) = ReadInt32(buf)
        self['m_GUID'] = EncodeUInt64(G_H, G_L)
        (self['m_SceneID'], buf) = ReadInt16(buf)
        (self['m_nTeamID'], buf) = ReadInt16(buf)
        return (self, buf)


class PACKET_CG_TEAM_APPOINT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_SourGUID'] = 0
        self['m_DestGUID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt64(self['m_SourGUID'])
        buf += WriteUInt64(self['m_DestGUID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_SourGUID'], buf) = ReadUInt64(buf)
        (self['m_DestGUID'], buf) = ReadUInt64(buf)
        return (self, buf)


class PACKET_CG_TEAM_RET_APPLY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_byReturn'] = 0
        self['m_SourGUID'] = 0
        self['m_uCheckKey'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_byReturn']))
        buf += WriteUInt64(self['m_SourGUID'])
        buf += WriteUInt32(self['m_uCheckKey'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_byReturn'], buf) = ReadByte(buf)
        self['m_byReturn'] = ord(self['m_byReturn'])
        (self['m_SourGUID'], buf) = ReadUInt64(buf)
        (self['m_uCheckKey'], buf) = ReadUInt32(buf)
        return (self, buf)


class TEAM_LIST_ENTRY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GUID64'] = 0
        self['m_nSceneID'] = 0
        self['m_nSceneResID'] = 0
        self['m_ExtraID'] = 0
        self['m_NameSize'] = 0
        self['m_szName'] = 0
        self['m_nPortrait'] = 0
        self['m_uDataID'] = 0
        self['m_zoneWorldID'] = 0
        self['m_FightPoint'] = 0


class PACKET_GC_TEAM_LIST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_nEventID'] = 0
        self['m_nTeamID'] = 0
        self['m_nExpAllotMode'] = 0
        self['m_bIsTeamFollow'] = False
        self['m_byMemberCount'] = 0
        self['m_Members'] = []

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_nEventID'], buf) = ReadInt32(buf)
        (self['m_nTeamID'], buf) = ReadShort(buf)
        (self['m_nExpAllotMode'], buf) = ReadInt32(buf)
        (self['tempFollow'], buf) = ReadInt32(buf)
        (self['m_byMemberCount'], buf) = ReadByte(buf)
        self['m_byMemberCount'] = ord(self['m_byMemberCount'])
        for i in range(self['m_byMemberCount']):
            tempdata = TEAM_LIST_ENTRY(None)
            (G_L, buf) = ReadInt32(buf)
            (G_H, buf) = ReadInt32(buf)
            tempdata['m_GUID64'] = EncodeUInt64(G_H, G_L)
            (tempdata['m_nSceneID'], buf) = ReadInt16(buf)
            (tempdata['m_nSceneResID'], buf) = ReadInt16(buf)
            (tempdata['m_ExtraID'], buf) = ReadUInt32(buf)
            (tempdata['m_NameSize'], buf) = ReadByte(buf)
            tempdata['m_NameSize'] = ord(tempdata['m_NameSize'])
            (tempdata['m_szName'], buf) = ReadCharArray(buf, tempdata['m_NameSize'])
            (tempdata['m_nPortrait'], buf) = ReadInt32(buf)
            (tempdata['m_uDataID'], buf) = ReadUShort(buf)
            (tempdata['m_zoneWorldID'], buf) = ReadShort(buf)
            (tempdata['m_FightPoint'], buf) = ReadInt32(buf)
            self['m_Members'].append(tempdata)
        return (self, buf)

    def handle(self):
        self.person['m_nTeamID'] = self['m_nTeamID']
        if len(self['m_Members']) >= 2:
            self.person['notallmatchstate'] = "end"
        if len(self['m_Members']) == 5:
            self.person['matchstate'] = "end"


class PACKET_GC_TEAM_ASK_APPLY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_SourGUID'] = 0
        self['m_DestGUID'] = 0
        self['m_bySourNameSize'] = 0
        self['m_byDestNameSize'] = 0
        self['m_szSourName'] = ''
        self['m_szDestName'] = ''
        self['m_uFamily'] = 0
        self['m_Scene'] = 0
        self['m_Level'] = 0
        self['m_uDataID'] = 0
        self['m_nDefEquip'] = 0
        self['m_zoneWorldID'] = 0
        self['m_DetailFlag'] = 0
        self['m_FightPoint'] = 0
        self['m_nFashionID'] = 0
        self['m_uColorID'] = 0
        self['m_nWeaponLevel'] = 0
        self['m_uWeaponRank'] = 0
        self['m_nHairID'] = 0
        self['m_nHairColor'] = 0
        self['m_nHeadID'] = 0

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_SourGUID'], buf) = ReadUInt64(buf)
        (self['m_DestGUID'], buf) = ReadUInt64(buf)
        (self['m_bySourNameSize'], buf) = ReadByte(buf)
        self['m_bySourNameSize'] = ord(self['m_bySourNameSize'])
        (self['m_byDestNameSize'], buf) = ReadByte(buf)
        self['m_byDestNameSize'] = ord(self['m_byDestNameSize'])
        (self['m_szSourName'], buf) = ReadCharArray(buf, self['m_bySourNameSize'])
        (self['m_szDestName'], buf) = ReadCharArray(buf, self['m_byDestNameSize'])

        (self['m_uFamily'], buf) = ReadUInt32(buf)
        (self['m_Scene'], buf) = ReadShort(buf)
        (self['m_Level'], buf) = ReadInt32(buf)
        (self['m_DetailFlag'], buf) = ReadByte(buf)
        self['m_DetailFlag'] = ord(self['m_DetailFlag'])
        (self['m_uDataID'], buf) = ReadUShort(buf)
        (self['m_nDefEquip'], buf) = ReadInt32(buf)
        (self['m_zoneWorldID'], buf) = ReadShort(buf)
        (self['m_FightPoint'], buf) = ReadInt32(buf)

        (self['m_nFashionID'], buf) = ReadInt32(buf)
        (self['m_uColorID'], buf) = ReadInt32(buf)
        (self['m_nWeaponLevel'], buf) = ReadInt32(buf)
        (self['m_uWeaponRank'], buf) = ReadInt32(buf)

        (self['m_nHairID'], buf) = ReadUInt32(buf)
        (self['m_nHairColor'], buf) = ReadUInt32(buf)
        (self['m_nHeadID'], buf) = ReadUInt32(buf)

        return (self, buf)

    def handle(self):
        if self.person['m_SourGUID_List'] == None:
            self.person['m_SourGUID_List'] = []
        self.person['m_SourGUID_List'].append(self['m_SourGUID'])
        pass


class PACKET_GC_TEAM_RESULT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_byReturn'] = 0
        self['m_GUID64'] = 0
        self['m_TeamID'] = 0
        self['m_GUID64Ex'] = 0
        self['m_ObjID'] = 0
        self['m_SceneID'] = 0
        self['m_SceneResID'] = 0
        self['m_NameSize'] = 0
        self['m_Name'] = ''
        self['m_nPortrait'] = 0
        self['m_uDataID'] = 0
        self['m_zoneWorldID'] = 0

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_byReturn'], buf) = ReadByte(buf)
        self['m_byReturn'] = ord(self['m_byReturn'])

        (guid_low, buf) = ReadInt32(buf)
        (guid_high, buf) = ReadInt32(buf)
        self['m_GUID64'] = EncodeUInt64(guid_high, guid_low)

        (self['m_TeamID'], buf) = ReadShort(buf)

        (guid_low, buf) = ReadInt32(buf)
        (guid_high, buf) = ReadInt32(buf)
        self['m_GUID64Ex'] = EncodeUInt64(guid_high, guid_low)

        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['m_SceneID'], buf) = ReadShort(buf)
        (self['m_SceneResID'], buf) = ReadShort(buf)
        (self['m_NameSize'], buf) = ReadByte(buf)
        self['m_NameSize'] = ord(self['m_NameSize'])

        (self['m_Name'], buf) = ReadCharArray(buf, self['m_NameSize'])

        (self['m_nPortrait'], buf) = ReadInt32(buf)
        (self['m_uDataID'], buf) = ReadUShort(buf)
        (self['m_zoneWorldID'], buf) = ReadShort(buf)
        return (self, buf)

    def handle(self):
        pass


class PACKET_GC_RETURN_TEAMFOLLOW(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Return'] = 0
        self['m_GUID64'] = 0

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_Return'], buf) = ReadByte(buf)
        self['m_Return'] = ord(self['m_Return'])

        (guid_low, buf) = ReadInt32(buf)
        (guid_high, buf) = ReadInt32(buf)
        self['m_GUID64'] = EncodeUInt64(guid_high, guid_low)

        return (self, buf)

    def handle(self):
        pass


class PACKET_CG_CHAT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ChatType'] = 0
        self['m_DClientTime'] = 0
        self['m_ContexSize'] = 0
        self['m_Contex'] = u''
        self['m_TargetSize'] = 0
        self['m_TargetName'] = u''
        self['m_ActTargetSize'] = 0

        self['m_ActTargetName'] = u''
        self['m_TeamID'] = 0
        self['m_ChannelID'] = 0
        self['m_GuildID'] = 0
        self['m_GuildLeagueID'] = 0
        self['m_MenpaiID'] = 0
        self['m_IPRegion'] = 0

        self['m_ChatGroupID'] = 0
        self['m_TargetGuid'] = 0
        self['m_RaidID'] = 0
        self['m_RaidTeamID'] = 0
        self['m_TargetZoneWorldID'] = -1
        self['m_ClanID'] = 0
        self['m_TransferType'] = [0, 0]

        self['m_ItemGuid'] = 0
        self['m_PetGuid'] = 0

        self['m_FileIDSize'] = 0
        self['m_FileID'] = u''
        self['m_voiceDura'] = 0

        self.ChatType_dic = {
            'CHAT_TYPE_INVALID': -1, \
            'CHAT_TYPE_NORMAL': 0, \
            'CHAT_TYPE_TEAM': 1, \
            'CHAT_TYPE_SCENE': 2, \
            'CHAT_TYPE_TELL': 3, \
            'CHAT_TYPE_SYSTEM': 4, \
            'CHAT_TYPE_CHANNEL': 5, \
            'CHAT_TYPE_GUILD': 6, \
            'CHAT_TYPE_MENPAI': 7, \
            'CHAT_TYPE_SELF': 8, \
            'CHAT_TYPE_HELP': 9, \
            'CHAT_TYPE_SPEAKER': 10, \
            'CHAT_TYPE_IPREGION': 11, \
            'CHAT_TYPE_GUILD_LEAGUE': 12, \
            'CHAT_TYPE_RAID': 13, \
            'CHAT_TYPE_RAIDTEAM': 14, \
            'CHAT_TYPE_SUPERSPEAKER': 15, \
            'CHAT_TYPE_BIGWORLD': 16, \
            'CHAT_TYPE_CLAN': 17, \
            'CHAT_TYPE_ZHENGZHAO': 18, \
            'CHAT_TYPE_SECRETSPEAKER': 19, \
            'CHAT_TYPE_TBSPERKER': 20, \
            'CHAT_TYPE_NUMBER': 21, \
            'CHAT_TYPE_IMCHAT': 22, \
            'CHAT_TYPE_GROUPCHAT': 23, \
            'CHAT_TYPE_PET': 24, \
            'CHAT_TYPE_KVKSYSTEM': 25, \
            'CHAT_TYPE_SYSTEMEX': 26, \
            'CHAT_TYPE_TX_SYSTEMEX': 27}

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_ChatType']))
        buf += WriteUInt32(self['m_DClientTime'])
        self['m_ContexSize'] = GetStringBytesLen(self['m_Contex'], True)
        buf += WriteInt32(self['m_ContexSize'])
        buf += WriteCharArray(self['m_Contex'], self['m_ContexSize'], True)

        self['m_ActTargetSize'] = GetStringBytesLen(self['m_ActTargetName'], True)
        buf += WriteByte(chr(self['m_ActTargetSize']))
        buf += WriteCharArray(self['m_ActTargetName'], self['m_ActTargetSize'], True)
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_NORMAL']:
            buf += WriteInt16(self['m_TargetZoneWorldID'])

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_TELL']:
            self['m_TargetSize'] = GetStringBytesLen(self['m_TargetName'], True)
            buf += WriteByte(chr(self['m_TargetSize']))
            buf += WriteCharArray(self['m_TargetName'], self['m_TargetSize'], True)
            buf += WriteInt16(self['m_TargetZoneWorldID'])

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_TEAM']:
            buf += WriteInt16(self['m_TeamID'])
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_CHANNEL']:
            buf += WriteInt16(self['m_ChannelID'])
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GUILD']:
            buf += WriteInt16(self['m_GuildID'])
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GUILD_LEAGUE']:
            buf += WriteInt16(self['m_GuildLeagueID'])
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_MENPAI']:
            buf += WriteByte(chr(self['m_MenpaiID']))
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_IPREGION']:
            buf += WriteInt32(self['m_IPRegion'])
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_IMCHAT']:
            buf += WriteInt16(self['m_TeamID'])
        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GROUPCHAT']:
            buf += WriteInt16(self['m_TeamID'])
        for i in range(0, 2):
            buf += WriteByte(chr(self['m_TransferType'][i]))

        for i in range(0, 2):
            if self['m_TransferType'][i] == 1:
                buf += WriteUInt64(self['m_ItemGuid'][i])
            elif self['m_TransferType'][i] == 2:
                buf += WriteUInt64(self['m_PetGuid'][i])

        self['m_FileIDSize'] = GetStringBytesLen(self['m_FileID'], True)
        buf += WriteByte(chr(self['m_FileIDSize']))
        buf += WriteCharArray(self['m_FileID'], self['m_FileIDSize'], True)
        buf += WriteByte(chr(self['m_voiceDura']))
        return buf

    def filldatafromstream(self, buf):
        (self['m_ChatType'], buf) = ReadByte(buf)
        self['m_ChatType'] = ord(self['m_ChatType'])
        (self['m_DClientTime'], buf) = ReadUInt32(buf)
        (self['m_ContexSize'], buf) = ReadInt32(buf)
        (self['m_Contex'], buf) = ReadCharArray(buf, self['m_ContexSize'], True)
        (self['m_ActTargetSize'], buf) = ReadByte(buf)
        self['m_ActTargetSize'] = ord(self['m_ActTargetSize'])
        (self['m_ActTargetName'], buf) = ReadCharArray(buf, self['m_ActTargetSize'], True)

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_NORMAL']:
            (self['m_TargetZoneWorldID'], buf) = ReadInt16(buf)

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_TELL']:
            (self['m_TargetSize'], buf) = ReadByte(buf)
            self['m_TargetSize'] = ord(self['m_TargetSize'])
            (self['m_TargetName'], buf) = ReadCharArray(buf, self['m_TargetSize'], True)
            (self['m_TargetZoneWorldID'], buf) = ReadInt16(buf)

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_TEAM']:
            (self['m_TeamID'], buf) = ReadInt16(buf)
        elif self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_CHANNEL']:
            (self['m_ChannelID'], buf) = ReadInt16(buf)
        elif self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GUILD']:
            (self['m_GuildID'], buf) = ReadInt16(buf)
        elif self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GUILD_LEAGUE']:
            (self['m_GuildLeagueID'], buf) = ReadInt16(buf)
        elif self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_MENPAI']:
            (self['m_MenpaiID'], buf) = ReadByte(buf)
            self['m_MenpaiID'] = ord(self['m_MenpaiID'])
        elif self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_IPREGION']:
            (self['m_IPRegion'], buf) = ReadInt32(buf)
        elif self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_IMCHAT']:
            (self['m_TeamID'], buf) = ReadInt16(buf)
        elif self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GROUPCHAT']:
            (self['m_TeamID'], buf) = ReadInt16(buf)
        for i in range(0, 2):
            temp = 0
            (temp, buf) = ReadByte(buf)
            self['m_TransferType'][i] = ord(temp)

        for i in range(0, 2):
            if self['m_TransferType'][i] == 1:
                (self['m_ItemGuid'], buf) = ReadUInt64(buf)
            elif self['m_TransferType'][i] == 2:
                (self['m_PetGuid'], buf) = ReadUInt64(buf)

                #        (self['m_FileIDSize'],buf) = GetStringBytesLen(self['m_FileID'],True)
        (self['m_FileIDSize'], buf) = ReadByte(buf)
        self['m_FileIDSize'] = ord(self['m_FileIDSize'])
        (self['m_FileID'], buf) = ReadCharArray(buf, self['m_FileIDSize'], True)
        (self['m_voiceDura'], buf) = ReadByte(buf)
        self['m_voiceDura'] = ord(self['m_voiceDura'])
        return (self, buf)


class PACKET_GC_CHAT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ChatType'] = 0
        self['m_ChatBroadCastNoticeID'] = 0
        self['m_ContexSize'] = 0
        self['contents'] = u''
        self['m_Contex'] = u''
        self['m_SourNameSize'] = 0
        self['m_SourName'] = ""
        self['m_DestNameSize'] = 0
        self['m_DestName'] = ""
        self['m_SourID'] = 0
        self['m_uWroldChatID'] = 0
        self['m_IsFromSys'] = 0
        self['m_SourGuid'] = 0
        self['m_ChatGroupID'] = 0
        self['m_uMoodSize'] = 0
        self['m_uMood'] = ''
        self['m_SourZoneWorldID'] = 0
        self['m_TargetZoneWorldID'] = 0
        self['m_bIsGmTell'] = 0
        self['m_SecretSpeakerFlag'] = 0
        self['m_nHeadID'] = 0
        self['m_nLevel'] = 0
        self['m_nMenpai'] = 9
        self['m_CityNameSize'] = 0
        self['m_CityName'] = ''
        self['chatItem'] = None  #
        self['chatPet'] = None
        self['m_FileIDSize'] = 0
        self['m_FileID'] = ''
        self['m_voiceDura'] = 0
        self['m_TCNotice'] = ''

        self.ChatType_dic = {
            'CHAT_TYPE_INVALID': -1, \
            'CHAT_TYPE_NORMAL': 0, \
            'CHAT_TYPE_TEAM': 1, \
            'CHAT_TYPE_SCENE': 2, \
            'CHAT_TYPE_TELL': 3, \
            'CHAT_TYPE_SYSTEM': 4, \
            'CHAT_TYPE_CHANNEL': 5, \
            'CHAT_TYPE_GUILD': 6, \
            'CHAT_TYPE_MENPAI': 7, \
            'CHAT_TYPE_SELF': 8, \
            'CHAT_TYPE_HELP': 9, \
            'CHAT_TYPE_SPEAKER': 10, \
            'CHAT_TYPE_IPREGION': 11, \
            'CHAT_TYPE_GUILD_LEAGUE': 12, \
            'CHAT_TYPE_RAID': 13, \
            'CHAT_TYPE_RAIDTEAM': 14, \
            'CHAT_TYPE_SUPERSPEAKER': 15, \
            'CHAT_TYPE_BIGWORLD': 16, \
            'CHAT_TYPE_CLAN': 17, \
            'CHAT_TYPE_ZHENGZHAO': 18, \
            'CHAT_TYPE_SECRETSPEAKER': 19, \
            'CHAT_TYPE_TBSPERKER': 20, \
            'CHAT_TYPE_NUMBER': 21, \
            'CHAT_TYPE_IMCHAT': 22, \
            'CHAT_TYPE_GROUPCHAT': 23, \
            'CHAT_TYPE_PET': 24, \
            'CHAT_TYPE_KVKSYSTEM': 25, \
            'CHAT_TYPE_SYSTEMEX': 26, \
            'CHAT_TYPE_TX_SYSTEMEX': 27}

    def filldatafromstream(self, buf):


        (self['m_ChatType'], buf) = ReadByte(buf)
        self['m_ChatType'] = ord(self['m_ChatType'])
        (self['m_ContexSize'], buf) = ReadInt32(buf)

        if self['m_ContexSize'] > 0:
            if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_TX_SYSTEMEX']:
                (self['m_TCNotice'], buf) = ReadCharArray(buf, self['m_ContexSize'], True)
            else:
                (self['contents'], buf) = ReadBytes(buf, self['m_ContexSize'])


        #addby luzhenyu 避免后面出错，直接return掉
        return (self, buf)



        (self['m_SourNameSize'], buf) = ReadByte(buf)
        self['m_SourNameSize'] = ord(self['m_SourNameSize'])
        if self['m_SourNameSize'] > 0:
            (self['m_SourName'], buf) = ReadCharArray(buf, self['m_SourNameSize'], True)
        (self['m_DestNameSize'], buf) = ReadByte(buf)
        self['m_DestNameSize'] = ord(self['m_DestNameSize'])
        if self['m_DestNameSize'] > 0:
            (self['m_DestName'], buf) = ReadCharArray(buf, self['m_DestNameSize'], True)

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_NORMAL'] or self['m_ChatType'] == self.ChatType_dic[
            'CHAT_TYPE_PET']:
            (self['m_SourID'], buf) = ReadInt32(buf)
            (self['m_TargetZoneWorldID'], buf) = ReadInt16(buf)
        (self['m_uWroldChatID'], buf) = ReadUInt32(buf)
        (self['m_IsFromSys'], buf) = ReadByte(buf)
        self['m_IsFromSys'] = ord(self['m_IsFromSys'])

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_SYSTEMEX'] or self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GUILD']:
            (self['m_ChatBroadCastNoticeID'], buf) = ReadInt32(buf)

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_GROUPCHAT']:
            (self['m_ChatGroupID'], buf) = ReadInt32(buf)

        if self['m_ChatType'] == self.ChatType_dic['CHAT_TYPE_IPREGION']:
            (self['m_CityNameSize'], buf) = ReadByte(buf)
            self['m_CityNameSize'] = ord(self['m_CityNameSize'])
            if self['m_CityNameSize'] > 0:
                (self['m_CityName'], buf) = ReadCharArray(buf, self['m_CityNameSize'], True)

        (self['m_SourZoneWorldID'], buf) = ReadInt16(buf)
        (self['m_bIsGmTell'], buf) = ReadInt32(buf)
        print self['m_bIsGmTell']


        (self['m_SecretSpeakerFlag'], buf) = ReadByte(buf)
        self['m_SecretSpeakerFlag'] = ord(self['m_SecretSpeakerFlag'])
        (self['m_SourGuid'], buf) = ReadUInt64(buf)
        (self['m_nHeadID'], buf) = ReadInt16(buf)
        (self['m_nLevel'], buf) = ReadInt32(buf)
        (self['m_nMenpai'], buf) = ReadInt32(buf)
        (self['m_uMoodSize'], buf) = ReadByte(buf)
        self['m_uMoodSize'] = ord(self['m_uMoodSize'])
        if self['m_uMoodSize'] > 0:
            (self['m_uMood'], buf) = ReadCharArray(buf, self['m_uMoodSize'], True)
        (self['m_FileIDSize'], buf) = ReadByte(buf)
        self['m_FileIDSize'] = ord(self['m_FileIDSize'])
        if self['m_FileIDSize'] > 0:
            (self['m_FileID'], buf) = ReadCharArray(buf, self['m_FileIDSize'], True)
        (self['m_voiceDura'], buf) = ReadByte(buf)
        self['m_voiceDura'] = ord(self['m_voiceDura'])
        return (self, buf)

    def handle(self):
        if self['contents'].find('14403') != -1 and self['contents'].find('ExtraData') != -1:
            data = int(self['contents'].split('#ExtraData')[1].split(',')[0].strip())
            self.person['haobaols'].append(data)
            self.person['tmp_haobaols'].append(data)




class PACKET_CG_MISSION_MOVIE_END(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_movieId'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_movieId'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_movieId'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_MISSION_POS_CHANGE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_movieId'] = 0
        self['m_posX'] = 0.0
        self['m_posZ'] = 0.0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_movieId'])
        buf += WriteSingle(self['m_posX'])
        buf += WriteSingle(self['m_posZ'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_movieId'], buf) = ReadInt32(buf)
        (self['m_posX'], buf) = ReadSingle(buf)
        (self['m_posZ'], buf) = ReadSingle(buf)
        return (self, buf)


class PACKET_CG_MISSION_ENTER_MOVIE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_enterOrExit'] = 0
        self['m_missionId'] = 0
        self['m_movieId'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_enterOrExit'])
        buf += WriteInt32(self['m_missionId'])
        buf += WriteInt32(self['m_movieId'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_enterOrExit'], buf) = ReadInt32(buf)
        (self['m_missionId'], buf) = ReadInt32(buf)
        (self['m_movieId'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_MISSIONBANDON(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['index'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['index'])
        return buf

    def filldatafromstream(self, buf):
        (self['index'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_ASK_SERVER_TIME(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['AskType'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['AskType'])
        return buf

    def filldatafromstream(self, buf):
        (self['AskType'], buf) = ReadInt32(buf)

        return (self, buf)


class PACKET_CG_ASK_ACCEPT_MISSION(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_idNPC'] = 0
        self['m_idIssueScript'] = 0
        self['m_idScript'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_idNPC'])
        buf += WriteInt32(self['m_idIssueScript'])
        buf += WriteInt32(self['m_idScript'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_idNPC'], buf) = ReadInt32(buf)
        (self['m_idIssueScript'], buf) = ReadInt32(buf)
        (self['m_idScript'], buf) = ReadInt32(buf)
        return (self, buf)


guildtype = {45: "GW_LEAVE", 65: "GW_APPLY_CHIEFTAIN", 94: "GC_LISTWITHCITY", 14: "CG_BACK_CITY",
             86: "GC_LIST", 67: "GW_CRITE_PACKET", 89: "GC_APPOINT_INFO", 79: "WG_REFLASHEP", 11: "CG_DISMISS",
             96: "GC_YXSSINFO", 53: "GW_GET_POSITION_NAME", 0: "CG_ASKLIST", 78: "WG_LISTWITHCITY",
             66: "GW_BACK_CITY_BYGUILD", 19: "CG_REQUEST_POSITION_NAME", 8: "CG_WITHDRAW", 36: "GW_CREATE",
             99: "GC_GUILDINVITE", 76: "WG_NAMELIST", 10: "CG_LEAVE", 69: "GW_WG_SEPARATOR",
             63: "GW_ASKGUILDEVENT", 43: "GW_WITHDRAW", 27: "CG_QUICKEXPEL", 40: "GW_ADJUSTAUTHORITY",
             20: "CG_COM_MISS_COMPLETE", 33: "CG_REQ_PACKET", 83: "WG_GUILDINVITE", 15: "CG_LEAVEWORD",
             100: "GC_APPLY_CHIEFTAIN", 22: "CG_FIRSTMAN", 74: "WG_SELF_GUILD_INFO", 39: "GW_APPOINT",
             92: "GC_NAMELIST", 61: "GW_QUICKJOIN", 9: "CG_DEPOSIT", 60: "GW_FINDERGUILD",
             91: "GC_RETURN_POSITION_NAME", 44: "GW_DEPOSIT", 87: "GC_MEMBER_LIST", 4: "CG_APPOINT",
             13: "CG_CHANGEDESC", 38: "GW_ASKINFO", 25: "CG_FINDERGUILD", 35: "GW_ASKLIST",
             75: "WG_RETURN_POSITION_NAME", 42: "GW_EXPEL", 84: "WG_APPLY_CHIEFTAIN", 82: "WG_GUILDEVENT",
             29: "CG_GUILDINVITE", 6: "CG_RECRUIT", 88: "GC_GUILD_INFO", 12: "CG_DEMISE",
             18: "CG_GET_POSITION_NAME", 55: "GW_COM_MISS_COMPLETE", 58: "GW_ASKLISTWITHCITY",
             49: "GW_BACK_CITY", 24: "CG_REFLASHEP", 2: "CG_JOIN", 28: "CG_ASKGUILDEVENT",
             97: "GC_PAIHANGBANGINFO", 5: "CG_ADJUSTAUTHORITY", 16: "CG_PROMOTEA_CHIEF", 71: "WG_MEMBER_LIST",
             80: "WG_YXSSINFO", 51: "GW_PROMOTEA_CHIEF", 50: "GW_LEAVEWORD", 68: "GW_REQ_PACKET",
             54: "GW_REQUEST_POSITION_NAME", 95: "GC_REFLASHEP", 64: "GW_GUILDINVITE", 73: "WG_APPOINT_INFO",
             21: "CG_ASKNAMELIST", 7: "CG_EXPEL", 90: "GC_SELF_GUILD_INFO", -1: "GUILD_PACKET_INVALID",
             30: "CG_APPLY_CHIEFTAIN", 3: "CG_ASKINFO", 47: "GW_DEMISE", 70: "WG_LIST", 32: "CG_CRITE_PACKET",
             77: "WG_FIRSTMAN_NAME", 62: "GW_QUICKEXPEL", 37: "GW_JOIN", 57: "GW_FIRSTMAN",
             72: "WG_GUILD_INFO", 41: "GW_RECRUIT", 98: "GC_GUILDEVENT", 85: "WG_GC_SEPARATOR",
             26: "CG_QUICKJOIN", 17: "CG_MODIFY_POSITION_NAME", 31: "CG_BACK_CITY_BYGUILD",
             34: "CG_GW_SEPARATOR", 48: "GW_CHANGEDESC", 1: "CG_CREATE", 81: "WG_PAIHANGBANGINFO",
             46: "GW_DISMISS", 56: "GW_ASKNAMELIST", 23: "CG_ASKLISTWITHCITY", 59: "GW_REFLASHEP",
             93: "GC_FIRSTMAN_NAME", 52: "GW_MODIFY_POSITION_NAME", }


class PACKET_CG_GUILD(Packet):
    guildclass = {'CG_ASKLIST': 'GUILD_CGW_ASKLIST', 'CG_FINDERGUILD': 'GUILD_CGW_FINDER',
                  'CG_ASKINFO': 'GUILD_CGW_ASKINFO', 'CG_ASKGUILDEVENT': 'GUILD_CGW_GUILDEVENT',
                  'CG_RECRUIT': 'GUILD_CGW_RECRUIT', 'CG_REQ_PACKET': 'CGReceiveRedPacket'}

    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_PacketType'] = 0
        self['m_Serial'] = 0
        self['packet'] = None

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_PacketType']))
        buf += WriteUInt32(self['m_Serial'])

        if self['packet'] is not None:
            buf += self['packet'].getdatastream()
        return buf

    def filldatafromstream(self, buf):
        (self['m_PacketType'], buf) = ReadByte(buf)
        self['m_PacketType'] = ord(self['m_PacketType'])
        (self['m_Serial'], buf) = ReadUInt32(buf)
        try:
            typename = guildtype[self['m_PacketType']]
            classname = PACKET_CG_GUILD.guildclass[typename]
            self['packet'] = eval("%s(self.person)" % classname)
            (self['packet'], buf) = self['packet'].filldatafromstream(buf)
        except:
            if self.person.getloadflag() is False:
                print "self['m_PacketType'] :", self['m_PacketType']
                print "typename:", typename
        return (self, buf)


class CGReceiveRedPacket(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['data1'] = 0
        self['m_guid'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['data1'])
        (low, high) = DecodeUInt64(self['m_guid'])
        buf += WriteInt32(low)
        buf += WriteInt32(high)
        return buf

    def filldatafromstream(self, buf):
        (self['data1'], buf) = ReadInt32(buf)
        (low, buf) = ReadInt32(buf)
        (high, buf) = ReadInt32(buf)
        self['m_guid'] = EncodeUInt64(high, low)
        return (self, buf)


class GUILD_CGW_RECRUIT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ProposerGUID64'] = 0

    def getdatastream(self):
        buf = ''
        (low, high) = DecodeUInt64(self['m_ProposerGUID64'])
        buf += WriteInt32(low)
        buf += WriteInt32(high)
        return buf

    def filldatafromstream(self, buf):
        (low, buf) = ReadInt32(buf)
        (high, buf) = ReadInt32(buf)
        self['m_ProposerGUID64'] = EncodeUInt64(high, low)
        return (self, buf)


class GUILD_CGW_GUILDEVENT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GuildGUID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt64(self['m_GuildGUID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_GuildGUID'], buf) = ReadUInt64(buf)
        return (self, buf)


class GUILD_CGW_ASKINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GuildGUID'] = 0
        self['m_Type'] = 0
        self['m_IsOnLogin'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['m_GuildGUID'])
        buf += WriteByte(chr(self['m_Type']))
        buf += WriteByte(chr(self['m_IsOnLogin']))
        return buf

    def filldatafromstream(self, buf):
        (self['m_GuildGUID'], buf) = ReadInt16(buf)
        (self['m_Type'], buf) = ReadByte(buf)
        self['m_Type'] = ord(self['m_Type'])
        (self['m_IsOnLogin'], buf) = ReadByte(buf)
        self['m_IsOnLogin'] = ord(self['m_IsOnLogin'])
        return (self, buf)


class GUILD_CGW_FINDER(Packet):
    # id finder
    def __init__(self, person):
        Packet.__init__(self, person)
        self['type'] = 0
        self['m_GuildID'] = 0
        self['m_NameSize'] = 0
        self['guildName'] = 0
        self['m_Position'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['type']))
        if self['type'] == 1:
            buf += WriteInt16(self['m_GuildID'])
        elif self['type'] == 2:
            self['m_NameSize'] = GetStringBytesLen(self['guildName'], True)
            buf += WriteByte(chr(self['m_NameSize']))
            buf += WriteCharArray(self['guildName'], self['m_NameSize'], True)
            buf += WriteUInt32(self['m_Position'])

        return buf

    def filldatafromstream(self, buf):
        (self['type'], buf) = ReadByte(buf)
        self['type'] = ord(self['type'])
        if self['type'] == 1:
            (self['m_GuildID'], buf) = ReadInt16(buf)
        elif self['type'] == 2:
            (self['m_NameSize'], buf) = ReadByte(buf)
            self['m_NameSize'] = ord(self['m_NameSize'])
            (self['guildName'], buf) = ReadCharArray(buf, self['m_NameSize'], True)
            (self['m_Position'], buf) = ReadUInt32(buf)

        return (self, buf)


class GUILD_CGW_ASKLIST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_SortType'] = 0
        self['m_Start'] = 0
        self['m_QueryDiffWorld'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_SortType']))
        buf += WriteUInt16(self['m_Start'])
        buf += WriteByte(chr(self['m_QueryDiffWorld']))
        return buf

    def filldatafromstream(self, buf):
        (self['m_SortType'], buf) = ReadByte(buf)
        self['m_SortType'] = ord(self['m_SortType'])
        (self['m_Start'], buf) = ReadUInt16(buf)
        (self['m_QueryDiffWorld'], buf) = ReadByte(buf)
        self['m_QueryDiffWorld'] = ord(self['m_QueryDiffWorld'])
        return (self, buf)


class PACKET_GC_GUILD(Packet):
    guildclass = {'GC_GUILD_INFO': 'GUILD_WGC_GUILD_INFO', 'GC_MEMBER_LIST': 'GUILD_WGC_MEMBER_LIST',
                  'GC_SELF_GUILD_INFO': 'GUILD_WGC_SELF_GUILD_INFO'}

    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_PacketType'] = 0
        self['m_Serial'] = 0
        self['packet'] = None

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_PacketType'], buf) = ReadByte(buf)
        self['m_PacketType'] = ord(self['m_PacketType'])
        (self['m_Serial'], buf) = ReadUInt32(buf)
        if self['m_PacketType'] == 86:
            self['packet'] = GUILD_WGC_LIST(None)
            (self['packet'], buf) = self['packet'].filldatafromstream(buf)
        elif self['m_PacketType'] == 90:
            self['packet'] = GUILD_WGC_SELF_GUILD_INFO(None)
            # return (self,buf)
            (self['packet'], buf) = self['packet'].filldatafromstream(buf)
        else:
            try:
                typename = guildtype[self['m_PacketType']]
                classname = PACKET_GC_GUILD.guildclass[typename]
                self['packet'] = eval("%s(self.person)" % classname)
                (self['packet'], buf) = self['packet'].filldatafromstream(buf)
            except:
                if self.person.getloadflag() is False:
                    print "self['m_PacketType'] :", self['m_PacketType']
                    print "typename:", typename
        return (self, buf)

    def handle(self):
        if self['m_PacketType'] == 90:
            self.person['m_guildId'] = self['packet']['m_GuildID']
        if hasattr(self['packet'], 'handle'):
            self['packet'].handle()


class MemberInfo(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_NameChar'] = 0
        self['m_Guid64'] = 0
        self['m_Level'] = 0
        self['m_MenPaiID'] = 0
        self['m_CurContribute'] = 0
        self['m_CountributePerWeek'] = 0
        self['m_MaxContribute'] = 0
        self['m_JoinTime'] = 0
        self['m_LastLoginTime'] = 0
        self['m_LastLogoffTime'] = 0
        self['m_IsOnline'] = 0
        self['m_Position'] = 0
        self['m_IsOffLineLong'] = 0
        self['m_EquipPoint'] = 0
        self['m_ItemCount'] = 0
        self['m_ItemWeekCount'] = 0
        self['m_IsApplyChieftaion'] = 0
        self['m_Sex'] = 0
        self['m_HeaderID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteCharArray(self['m_NameChar'])
        (low, high) = DecodeUInt64(self['m_Guid64'])
        buf += WriteInt32(low)
        buf += WriteInt32(high)

        buf += WriteByte(chr(self['m_Level']))
        buf += WriteByte(chr(self['m_MenPaiID']))
        buf += WriteInt32(self['m_CurContribute'])
        buf += WriteInt32(self['m_CountributePerWeek'])
        buf += WriteInt32(self['m_MaxContribute'])
        buf += WriteInt32(self['m_JoinTime'])
        buf += WriteUInt32(self['m_LastLoginTime'])
        buf += WriteUInt32(self['m_LastLogoffTime'])
        buf += WriteByte(chr(self['m_IsOnline']))
        buf += WriteByte(chr(self['m_Position']))
        buf += WriteByte(chr(self['m_IsOffLineLong']))
        buf += WriteInt32(self['m_EquipPoint'])
        buf += WriteInt32(self['m_ItemCount'])
        buf += WriteInt32(self['m_ItemWeekCount'])
        buf += WriteByte(chr(self['m_IsApplyChieftaion']))
        buf += WriteByte(chr(self['m_Sex']))
        buf += WriteInt32(self['m_HeaderID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_NameChar'], buf) = ReadCharArray(buf, 30, True)
        (G_L, buf) = ReadInt32(buf)
        (G_H, buf) = ReadInt32(buf)
        self['m_Guid64'] = EncodeUInt64(G_H, G_L)

        (self['m_Level'], buf) = ReadByte(buf)
        self['m_Level'] = ord(self['m_Level'])
        (self['m_MenPaiID'], buf) = ReadByte(buf)
        self['m_MenPaiID'] = ord(self['m_MenPaiID'])
        (self['m_CurContribute'], buf) = ReadInt(buf)
        (self['m_CountributePerWeek'], buf) = ReadInt(buf)
        (self['m_MaxContribute'], buf) = ReadInt(buf)
        (self['m_JoinTime'], buf) = ReadInt(buf)
        (self['m_LastLoginTime'], buf) = ReadUint(buf)
        (self['m_LastLogoffTime'], buf) = ReadUint(buf)
        (self['m_IsOnline'], buf) = ReadByte(buf)
        self['m_IsOnline'] = ord(self['m_IsOnline'])
        (self['m_Position'], buf) = ReadByte(buf)
        self['m_Position'] = ord(self['m_Position'])
        (self['m_IsOffLineLong'], buf) = ReadByte(buf)
        self['m_IsOffLineLong'] = ord(self['m_IsOffLineLong'])
        (self['m_EquipPoint'], buf) = ReadInt(buf)
        (self['m_ItemCount'], buf) = ReadInt(buf)
        (self['m_ItemWeekCount'], buf) = ReadInt(buf)
        (self['m_IsApplyChieftaion'], buf) = ReadByte(buf)
        self['m_IsApplyChieftaion'] = ord(self['m_IsApplyChieftaion'])
        (self['m_Sex'], buf) = ReadByte(buf)
        self['m_Sex'] = ord(self['m_Sex'])
        (self['m_HeaderID'], buf) = ReadInt(buf)
        return (self, buf)


class GUILD_WGC_MEMBER_LIST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ValidMemberCount'] = 0
        self['m_MemberCount'] = 0
        self['m_MemberMax'] = 0
        self['m_Position'] = 0
        self['m_Access'] = 0
        self['m_GuildDesc'] = 0
        self['m_GuildName'] = 0
        self['m_GuildLeagueName'] = 0
        self['m_FirstManGUID'] = 0
        self['m_UI'] = 0
        self['m_GuildLevel'] = 0
        self['m_GuildMembers'] = []

    def getdatastream(self):
        buf = ''
        buf += WriteUInt16(self['m_ValidMemberCount'])
        buf += WriteUInt16(self['m_MemberCount'])
        buf += WriteUInt16(self['m_MemberMax'])
        buf += WriteByte(chr(self['m_Position']))
        buf += WriteByte(chr(self['m_Access']))
        buf += WriteCharArray(self['m_GuildDesc'], 100, True)
        buf += WriteCharArray(self['m_GuildName'], 24, True)
        buf += WriteCharArray(self['m_GuildLeagueName'], 32, True)

        (low, high) = DecodeUInt64(self['m_FirstManGUID'])
        buf += WriteInt32(low)
        buf += WriteInt32(high)

        buf += WriteByte(chr(self['m_UI']))
        buf += WriteByte(chr(self['m_GuildLevel']))
        # buf += WriteBuff(self['packet'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_ValidMemberCount'], buf) = ReadUInt16(buf)
        (self['m_MemberCount'], buf) = ReadUInt16(buf)
        (self['m_MemberMax'], buf) = ReadUInt16(buf)
        (self['m_Position'], buf) = ReadByte(buf)
        self['m_Position'] = ord(self['m_Position'])
        (self['m_Access'], buf) = ReadByte(buf)
        self['m_Access'] = ord(self['m_Access'])
        (self['m_GuildDesc'], buf) = ReadCharArray(buf, 100, True)
        (self['m_GuildName'], buf) = ReadCharArray(buf, 24, True)
        (self['m_GuildLeagueName'], buf) = ReadCharArray(buf, 32, True)

        (G_L, buf) = ReadInt32(buf)
        (G_H, buf) = ReadInt32(buf)
        self['m_FirstManGUID'] = EncodeUInt64(G_H, G_L)

        (self['m_UI'], buf) = ReadByte(buf)
        self['m_UI'] = ord(self['m_UI'])
        (self['m_GuildLevel'], buf) = ReadByte(buf)
        self['m_GuildLevel'] = ord(self['m_GuildLevel'])

        if 270 > self['m_MemberCount'] > 0:
            for i in range(self['m_MemberCount']):
                member = MemberInfo(self.person)
                self['m_GuildMembers'].append(member)
                (member, buf) = member.filldatafromstream(buf)
        return (self, buf)

    def handle(self):
        self.person['applylist'] = []
        for mem in self['m_GuildMembers']:
            if mem['m_JoinTime'] == 0:
                self.person['applylist'].append(mem['m_Guid64'])
        self.person['guildMembercount'] = self['m_MemberCount']


class GUILD_WGC_GUILD_INFO(Packet):
    pass


class PACKET_CG_GUILD_APPLY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['nameSize'] = 0
        self['descSize'] = 0
        self['_guildName'] = ''
        self['_guildDesc'] = ''
        self['m_guildName'] = ''

    def getdatastream(self):
        buf = ''
        self['nameSize'] = GetStringBytesLen(self['_guildName'], False)
        self['descSize'] = GetStringBytesLen(self['_guildDesc'], False)
        buf += WriteByte(chr(self['nameSize']))
        if self['nameSize'] <= 24:
            buf += WriteCharArray(self['_guildName'], self['nameSize'], True, False)
        buf += WriteByte(chr(self['descSize']))
        if self['descSize'] <= 100:
            buf += WriteCharArray(self['_guildDesc'], self['descSize'], True, False)
        return buf

    def filldatafromstream(self, buf):
        (self['nameSize'], buf) = ReadByte(buf)
        self['nameSize'] = ord(self['nameSize'])
        (self['_guildName'], buf) = ReadCharArray(buf, self['nameSize'])
        (self['descSize'], buf) = ReadByte(buf)
        self['descSize'] = ord(self['descSize'])
        (self['_guildDesc'], buf) = ReadCharArray(buf, self['descSize'])

        return (self, buf)


class PACKET_CG_RIDEBAGMOVEITEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['index'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['index'])
        return buf

    def filldatafromstream(self, buf):
        (self['index'], buf) = ReadInt32(buf)
        return (self, buf)


# It is so difficult!

class PACKET_CG_ASK_LAOSANHUAN(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_AskType'] = 0
        self['m_Difficulty'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_AskType']))
        #         buf += WriteByte(self['m_Difficulty'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_AskType'], buf) = ReadByte(buf)
        #         (self['m_Difficulty'],buf)= ReadByte(buf)
        return (self, buf)


class PACKET_GC_TEAMMATESCONDITION(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        return (self, buf)


class PACKET_CG_ASKCOPYSCENECOUNT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Type'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_Type']))
        return buf

    def filldatafromstream(self, buf):
        (self['m_Type'], buf) = ReadByte(buf)
        self['m_Type'] = ord(self['m_Type'])
        return (self, buf)


class PACKET_GC_RETCOPYSCENECOUNT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_aryCopySceneCount'] = []

    def getdatastream(self):
        buf = ''
        for i in range(0, 20):
            buf += WriteInt32(self['m_aryCopySceneCount'][i])
        return buf

    def filldatafromstream(self, buf):
        for i in range(0, 20):
            temp = 0
            (temp, buf) = ReadInt(buf)
            self['m_aryCopySceneCount'].append(temp)
        return (self, buf)


class PACKET_CG_FINDNPC(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_NpcNameLen'] = 0
        self['m_NpcName'] = ''

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['m_NpcNameLen'])
        buf += WriteCharArray(self['m_NpcName'], self['m_NpcNameLen'], True)
        return buf

    def filldatafromstream(self, buf):
        (self['m_NpcNameLen'], buf) = ReadByte(buf)
        (self['m_NpcName'], buf) = ReadCharArray(buf)
        return (self, buf)


class PACKET_GC_RETFINDNPC(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_DataId'] = 0
        self['m_fx'] = 0
        self['m_fz'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_DataId'])
        #         buf += WriteInt32(self['m_fx'])
        #         buf += WriteInt32(self['m_fz'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_DataId'], buf) = ReadInt(buf)
        #         (self['m_fx'],buf)= ReadInt(buf)
        #         (self['m_fz'],buf)= ReadInt(buf)
        return (self, buf)


class PACKET_CG_REQ_FURNACE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Count'] = 0
        self['BagIndex'] = []

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['Count'])
        for i in range(0, self['Count']):
            buf += WriteByte(self['BagIndex'][i])
        return buf

    def filldatafromstream(self, buf):
        (self['Count'], buf) = ReadByte(buf)
        for i in range(0, self['Count']):
            (self['BagIndex'][i], buf) = ReadByte(buf)
        return (self, buf)


class PACKET_CG_REQ_FURNACE_REWARD(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        return (self, buf)


class PACKET_GC_RESP_FURNACE_RESULT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Count'] = 0
        self['BagIndex'] = []
        self['CurFurnaceValue'] = -1

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['Count'])
        if self['Count'] <= 0:
            buf += WriteInt32(self['CurFurnaceValue'])
        for i in range(0, self['Count']):
            buf += WriteInt32(self['BagIndex'][i])
        buf += WriteInt32(self['CurFurnaceValue'])
        return buf

    def filldatafromstream(self, buf):
        (self['Count'], buf) = ReadInt32(buf)
        if self['Count'] <= 0:
            (self['CurFurnaceValue'], buf) = ReadInt32(buf)
        for i in range(0, self['Count']):
            (self['BagIndex'][i], buf) = ReadInt32(buf)
        (self['CurFurnaceValue'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_RESP_FURNACE_REWARD(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['ItemTableId'] = 0
        self['CurFurnaceValue'] = -1

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['ItemTableId'])
        if self['ItemTableId'] <= 0:
            buf += WriteInt32(self['CurFurnaceValue'])
        return buf

    def filldatafromstream(self, buf):
        (self['ItemTableId'], buf) = ReadInt(buf)
        if self['ItemTableId'] <= 0:
            (self['CurFurnaceValue'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_LIMITFASHIONTIMEOUT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Count'] = 0
        self['m_FashionId'] = []

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_Count'])
        if self['m_Count'] <= 256:
            for i in range(0, self['m_Count']):
                buf += WriteInt32(self['m_FashionId'][i])
        return buf

    def filldatafromstream(self, buf):
        (self['m_Count'], buf) = ReadInt32(buf)
        if self['m_Count'] <= 256:
            for i in range(0, self['m_Count']):
                (self['m_FashionId'][i], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_CHANGEFASHION(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_FashionId'] = 0
        self['m_ColorId'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_FashionId'])
        buf += WriteInt32(self['m_ColorId'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_FashionId'], buf) = ReadInt32(buf)
        (self['m_ColorId'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_FASHIONINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Ret'] = 0
        self['m_FashionId'] = 0
        self['m_ColorId'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['m_Ret'])
        buf += WriteInt32(self['m_FashionId'])
        buf += WriteInt32(self['m_ColorId'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_Ret'], buf) = ReadByte(buf)
        (self['m_FashionId'], buf) = ReadInt32(buf)
        (self['m_ColorId'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_FASHIONINFOS(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Count'] = 0
        self['m_FashionId'] = []
        self['m_ColorId'] = []
        self['m_TimeLimit'] = []

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_Count'])
        for i in range(0, self['m_Count']):
            buf += WriteInt32(self['m_FashionId'][i])
        for i in range(0, self['m_Count']):
            buf += WriteByte(self['m_ColorId'][i])
        for i in range(0, self['m_Count']):
            buf += WriteInt32(self['m_TimeLimit'][i])
        return buf

    def filldatafromstream(self, buf):
        (self['m_Count'], buf) = ReadByte(buf)
        for i in range(0, self['m_Count']):
            (self['m_FashionId'][i], buf) = ReadInt32(buf)
        for i in range(0, self['m_Count']):
            (self['m_ColorId'][i], buf) = ReadByte(buf)
        for i in range(0, self['m_Count']):
            (self['m_TimeLimit'][i], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_FASHIONCOLOR(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_FashionId'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_FashionId'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_FashionId'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_ASKFASHIONINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        return (self, buf)


class PACKET_GC_GETFASHION(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_FashionId'] = 0
        self['m_TimeLimit'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_FashionId'])
        buf += WriteInt32(self['m_TimeLimit'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_FashionId'], buf) = ReadInt32(buf)
        (self['m_TimeLimit'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_USESHOUHUN(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_TujianId'] = 0
        self['m_UseCount'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_TujianId'])
        buf += WriteByte(self['m_UseCount'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_TujianId'], buf) = ReadInt32(buf)
        (self['m_UseCount'], buf) = ReadByte(buf)
        return (self, buf)


class PACKET_CG_COMPOSE_GEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_TargetLevel'] = 0

    #         self['m_GemBagIdx'] = []

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['m_TargetLevel'])
        for i in range(0, 200):
            buf += WriteInt32(self['m_GemBagIdx'][i])
        return buf

    def filldatafromstream(self, buf):
        (self['m_TargetLevel'], buf) = ReadByte(buf)
        for i in range(0, 200):
            (self['m_GemBagIdx'][i], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_ASK_QUIT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Key'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteUInt32(self['Key'])
        return buf

    def filldatafromstream(self, buf):
        (self['Key'], buf) = ReadUInt32(buf)
        return (self, buf)


class PACKET_CG_ASK_PRIVATEINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_PlayerID'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_PlayerID'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_PlayerID'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_PRIVATEINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_IsMyself'] = 0
        self['m_InfoType'] = 0
        self['m_CharGUID64'] = 0
        self['m_Age'] = 0
        self['m_Sex'] = 0
        self['m_BloodType'] = 0
        self['m_YearAnimal'] = 0
        self['m_Consella'] = 0
        self['m_Province'] = 0

        self['m_SchoolInfoSize'] = 0
        self['m_SchoolInfo'] = 0
        self['m_JobInfoSize'] = 0
        self['m_JobInfo'] = ''
        self['m_CitySize'] = 0
        self['m_City'] = ''
        self['m_EmailInfoSize'] = 0
        self['m_EmailInfo'] = ''
        self['m_LuckWordSize'] = 0
        self['m_LuckWord'] = ''

        self['m_ConsortSize'] = 0
        self['m_Consort'] = ''
        self['m_WeddingTime'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['myselfTag'])
        buf += WriteByte(self['m_InfoType'])
        #         buf += WriteInt32(self['m_CharGUID64'])
        buf += WriteByte(self['m_Age'])
        buf += WriteByte(self['m_Sex'])
        buf += WriteByte(self['m_BloodType'])

        buf += WriteByte(self['m_YearAnimal'])
        buf += WriteByte(self['m_Consella'])
        buf += WriteByte(self['m_Province'])
        self['m_SchoolInfoSize'] = len(self['m_SchoolInfo'])
        buf += WriteByte(self['m_SchoolInfoSize'])
        self['m_JobInfoSize'] = len(self['m_JobInfo'])
        buf += WriteByte(self['m_JobInfoSize'])

        self['m_CitySize'] = len(self['m_City'])
        buf += WriteByte(self['m_CitySize'])
        self['m_EmailInfoSize'] = len(self['m_EmailInfo'])
        buf += WriteByte(self['m_EmailInfoSize'])
        self['m_LuckWordSize'] = len(self['m_LuckWord'])
        buf += WriteByte(self['m_LuckWordSize'])
        self['m_ConsortSize'] = len(self['m_Consort'])
        buf += WriteByte(self['m_ConsortSize'])

        return buf

    def filldatafromstream(self, buf):
        (self['myselfTag'], buf) = ReadByte(buf)
        (self['m_InfoType'], buf) = ReadByte(buf)
        #         (self['m_CharGUID64'],buf)= ReadByte(buf)
        (self['m_Age'], buf) = ReadByte(buf)
        (self['m_Sex'], buf) = ReadByte(buf)
        (self['m_BloodType'], buf) = ReadByte(buf)

        (self['m_YearAnimal'], buf) = ReadByte(buf)
        (self['m_Consella'], buf) = ReadByte(buf)
        (self['m_Province'], buf) = ReadByte(buf)
        self['m_SchoolInfoSize'] = len(self['m_SchoolInfo'])
        (self['m_SchoolInfoSize'], buf) = ReadByte(buf)
        self['m_JobInfoSize'] = len(self['m_JobInfo'])
        (self['m_JobInfoSize'], buf) = ReadByte(buf)

        self['m_CitySize'] = len(self['m_City'])
        (self['m_CitySize'], buf) = ReadByte(buf)
        self['m_EmailInfoSize'] = len(self['m_EmailInfo'])
        (self['m_EmailInfoSize'], buf) = ReadByte(buf)
        self['m_LuckWordSize'] = len(self['m_LuckWord'])
        (self['m_LuckWordSize'], buf) = ReadByte(buf)
        self['m_ConsortSize'] = len(self['m_Consort'])
        (self['m_ConsortSize'], buf) = ReadByte(buf)

        return (self, buf)


class PACKET_CG_APPLY_PRIVATEINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_InfoType'] = 0
        self['m_CharGUID64'] = 0
        self['m_Age'] = 0
        self['m_Sex'] = 0
        self['m_BloodType'] = 0
        self['m_YearAnimal'] = 0
        self['m_Consella'] = 0
        self['m_Province'] = 0
        self['m_SchoolInfoSize'] = 0
        self['m_SchoolInfo'] = ''
        self['m_dataSize'] = 0
        self['m_JobInfoSize'] = 0
        self['m_JobInfo'] = ''
        self['m_CitySize'] = 0
        self['m_City'] = ''
        self['m_EmailInfoSize'] = 0
        self['m_EmailInfo'] = ''
        self['m_LuckWordSize'] = 0
        self['m_LuckWord'] = ''
        self['m_ConsortSize'] = 0
        self['m_Consort'] = ''
        self['m_WeddingTime'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['m_type'])
        #         buf += WriteInt32(self['m_CharGUID64'])
        buf += WriteByte(self['m_Age'])
        buf += WriteByte(self['m_Sex'])
        buf += WriteByte(self['m_BloodType'])

        buf += WriteByte(self['m_YearAnimal'])
        buf += WriteByte(self['m_Consella'])
        buf += WriteByte(self['m_Province'])
        self['m_SchoolInfoSize'] = len(self['m_SchoolInfo'])
        buf += WriteByte(self['m_SchoolInfoSize'])
        self['m_JobInfoSize'] = len(self['m_JobInfo'])
        buf += WriteByte(self['m_JobInfoSize'])

        self['m_CitySize'] = len(self['m_City'])
        buf += WriteByte(self['m_CitySize'])
        self['m_EmailInfoSize'] = len(self['m_EmailInfo'])
        buf += WriteByte(self['m_EmailInfoSize'])
        self['m_LuckWordSize'] = len(self['m_LuckWord'])
        buf += ReadByte(self['m_LuckWordSize'])

        return buf

    def filldatafromstream(self, buf):
        (self['m_type'], buf) = ReadByte(buf)
        #         (self['m_CharGUID64'],buf)= ReadByte(buf)
        (self['m_Age'], buf) = ReadByte(buf)
        (self['m_Sex'], buf) = ReadByte(buf)
        (self['m_BloodType'], buf) = ReadByte(buf)

        (self['m_YearAnimal'], buf) = ReadByte(buf)
        (self['m_Consella'], buf) = ReadByte(buf)
        (self['m_Province'], buf) = ReadByte(buf)
        self['m_SchoolInfoSize'] = len(self['m_SchoolInfo'])
        (self['m_SchoolInfoSize'], buf) = ReadByte(buf)
        self['m_JobInfoSize'] = len(self['m_JobInfo'])
        (self['m_JobInfoSize'], buf) = ReadByte(buf)

        self['m_CitySize'] = len(self['m_City'])
        (self['m_CitySize'], buf) = ReadByte(buf)
        self['m_EmailInfoSize'] = len(self['m_EmailInfo'])
        (self['m_EmailInfoSize'], buf) = ReadByte(buf)
        self['m_LuckWordSize'] = len(self['m_LuckWord'])
        (self['m_LuckWordSize'], buf) = WriteByte(buf)

        return (self, buf)


class PACKET_CG_CGW_PACKET(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_type'] = 0
        self['m_dataSize'] = 0
        self['m_data'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_type']))
        buf += WriteInt32(self['m_dataSize'])
        #         buf += WriteInt32(self['m_data'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_type'], buf) = ReadByte(buf)
        self['m_type'] = ord(self['m_type'])
        (self['m_dataSize'], buf) = ReadUInt32(buf)
        #        (self['m_data'],buf)= ReadInt32(buf)
        return (self, buf)


class PACKET_GC_WGC_PACKET(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Type'] = 0
        self['m_DataSize'] = 0
        self['m_Data'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['m_type'])
        buf += WriteUInt32(self['m_dataSize'])
        #         buf += WriteInt32(self['m_data'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_type'], buf) = ReadByte(buf)
        (self['m_dataSize'], buf) = ReadUInt32(buf)
        #         (self['m_data'],buf)= ReadInt32(buf)
        return (self, buf)


class PACKET_CG_DISPEL_BUFF(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['n_SkillId'] = 0
        self['n_ImpactId'] = 0
        self['n_Sz'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['n_SkillId'])
        buf += WriteInt16(self['n_ImpactId'])
        buf += WriteInt32(self['n_Sz'])
        return buf

    def filldatafromstream(self, buf):
        (self['n_SkillId'], buf) = ReadInt16(buf)
        (self['n_ImpactId'], buf) = ReadInt16(buf)
        (self['n_Sz'], buf) = ReadInt32(buf)
        return (self, buf)


# supinrong
class PACKET_CG_CHARMOVE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ObjID'] = 0
        self['m_nHandleID'] = 0
        self['CurPostion'] = [0, 0]  # [x,y]
        self['m_yNumTargetPos'] = 0
        self['TargetPos'] = []  # [[x,y],[x.y]]
        self['m_bKeyboardMove'] = 0
        self['m_bDir'] = 0
        self['m_bIsStopMsg'] = 0

    def getdatastream(self):
        buf = ''
        if self['m_yNumTargetPos'] > 90:
            self['m_yNumTargetPos'] = 90
        if self['TargetPos'] == []:
            return buf
        buf += WriteInt32(self['m_nHandleID'])
        buf += WriteInt32(self['m_ObjID'])
        buf += WriteSingle(self['CurPostion'][0])
        buf += WriteSingle(self['CurPostion'][1])
        buf += WriteByte(chr(self['m_yNumTargetPos']))
        buf += WriteByte(chr(self['m_bKeyboardMove']))

        for i in range(self['m_yNumTargetPos']):
            buf += WriteSingle(self['TargetPos'][i][0])
            buf += WriteSingle(self['TargetPos'][i][1])

        buf += WriteInt32(self['m_bIsStopMsg'])
        buf += WriteSingle(self['m_bDir'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_nHandleID'], buf) = ReadInt32(buf)
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['CurPostion'][0], buf) = ReadSingle(buf)
        (self['CurPostion'][1], buf) = ReadSingle(buf)
        (self['m_yNumTargetPos'], buf) = ReadByte(buf)
        self['m_yNumTargetPos'] = ord(self['m_yNumTargetPos'])
        (self['m_bKeyboardMove'], buf) = ReadByte(buf)
        self['m_bKeyboardMove'] = ord(self['m_bKeyboardMove'])
        for i in range(self['m_yNumTargetPos']):
            self['TargetPos'].append([0, 0])
            (self['TargetPos'][i][0], buf) = ReadSingle(buf)
            (self['TargetPos'][i][1], buf) = ReadSingle(buf)

        (self['m_bIsStopMsg'], buf) = ReadInt32(buf)
        (self['m_bDir'], buf) = ReadSingle(buf)
        return (self, buf)


class PACKET_GC_NOTIFYCHANGESCENE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self.MAX_CHAR_LENGTH = 26
        self['m_CurrentSceneID'] = 0
        self['m_TargetSceneID'] = 0
        self['m_TargetPosX'] = 0
        self['m_TargetPosZ'] = 0
        self['m_TargetDir'] = 0
        self['m_nResID'] = 0
        self['m_CityNameChar'] = ""
        self['m_CityName'] = ""

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_CurrentSceneID'], buf) = ReadInt16(buf)
        (self['m_TargetSceneID'], buf) = ReadInt16(buf)
        (self['m_TargetPosX'], buf) = ReadSingle(buf)
        (self['m_TargetPosZ'], buf) = ReadSingle(buf)
        (self['m_TargetDir'], buf) = ReadFloat(buf)
        (self['m_nResID'], buf) = ReadInt16(buf)
        (self['m_CityNameChar'], buf) = ReadCharArray(buf, 26)

        if len(self['m_CityNameChar']) > 1:
            self['m_CityName'] = self['m_CityNameChar']
        # WriteCharArray(self['OpenID'],128,True)

        return (self, buf)

    def handle(self):
        self.person.m_CurrentSceneID = self['m_CurrentSceneID']
        self.person.m_TargetSceneID = self['m_TargetSceneID']
        self.person['SceneId'] = self['m_TargetSceneID']
        self.person['f_x'] = self['m_TargetPosX']
        self.person['f_z'] = self['m_TargetPosZ']

        self.person['flag'] = 1
        if self.person['state'] is not None:
            self.person['state'] = 'quit'


class PACKET_CGAskChangeScene(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_sourSceneID'] = 0
        self['m_destSceneID'] = 0
        self['m_memUsage'] = 0
        self['m_iFreeLocalVideoMemory'] = 0
        self['m_fAverageFPSInScene'] = 0
        self['m_fVedioMemoryUsage'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['m_sourSceneID'])
        buf += WriteInt16(self['m_destSceneID'])
        buf += WriteUInt32(self['m_memUsage'])
        buf += WriteUInt32(self['m_iFreeLocalVideoMemory'])
        buf += WriteSingle(self['m_fAverageFPSInScene'])
        buf += WriteUInt32(self['m_fVedioMemoryUsage'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_sourSceneID'], buf) = ReadInt16(buf)
        (self['m_destSceneID'], buf) = ReadInt16(buf)
        (self['m_memUsage'], buf) = ReadUInt32(buf)
        (self['m_iFreeLocalVideoMemory'], buf) = ReadUInt32(buf)
        (self['m_fAverageFPSInScene'], buf) = ReadSingle(buf)
        (self['m_fVedioMemoryUsage'], buf) = ReadUInt32(buf)
        return (self, buf)


class PACKET_GC_RETCHANGESCENE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self.IP_LENGTH = 24
        self.CHANGESCENE_RETURN = {"CSR_SUCCESS": 0, "CSR_SUCCESS_DIRRSERVER": 1, "CSR_ERROR": 2}
        self['m_IP'] = ""
        self['m_Port'] = 0
        self['m_Key'] = 0

    def filldatafromstream(self, buf):
        (result, buf) = ReadByte(buf)
        if ord(result) == 1:
            (self['m_IP'], buf) = ReadCharArray(buf, self.IP_LENGTH)
            (self['m_Port'], buf) = ReadUInt16(buf)

        (self['m_Key'], buf) = ReadUInt32(buf)
        return (self, buf)


class PACKET_CG_COMMAND(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['context'] = ""

    def getdatastream(self):
        buf = ''
        length = GetStringBytesLen(self['context'], True)
        buf += WriteByte(chr(length))
        buf += WriteCharArray(self['context'], length, True)
        return buf

    def filldatafromstream(self, buf):
        (length, buf) = ReadByte(buf)
        length = ord(length)
        (self['context'], buf) = ReadCharArray(buf, length)
        return (self, buf)


class PACKET_GC_CHARMOVE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_nObjID'] = 0
        self['m_uStartTime'] = 0
        self['m_nHandleID'] = 0
        self['m_nDir'] = 0
        self['m_nIsStopMsg'] = 0
        self['m_yNumTargetPos'] = 0
        self['TarPostion'] = []  # [x,y]
        self['m_UpdateFlagSize'] = 1
        self['m_Flags'] = 0
        self['m_nStopLogicCount'] = 0
        self['m_yStopNodeIndex'] = 0
        self['m_posStop'] = []  # [x, y]
        self['m_curPostion'] = []  # [x, y]
        self['m_vPosition'] = []  # [x, y]

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_nObjID'], buf) = ReadInt32(buf)
        (self['m_uStartTime'], buf) = ReadUInt32(buf)
        (self['m_nHandleID'], buf) = ReadInt32(buf)
        (self['m_nDir'], buf) = ReadSingle(buf)
        (self['m_nIsStopMsg'], buf) = ReadInt32(buf)
        (self['pFlags'], buf) = ReadCharArray(buf, 1, False)
        (self['m_yNumTargetPos'], buf) = ReadByte(buf)
        self['m_yNumTargetPos'] = ord(self['m_yNumTargetPos'])
        for i in range(self['m_yNumTargetPos']):
            self['TarPostion'].append([0, 0])
            (self['TarPostion'][i][0], buf) = ReadSingle(buf)
            (self['TarPostion'][i][1], buf) = ReadSingle(buf)
            self['m_vPosition'] = self['TarPostion'][i]
        self['m_curPostion'] = [0, 0]
        (self['m_curPostion'][0], buf) = ReadSingle(buf)
        (self['m_curPostion'][1], buf) = ReadSingle(buf)
        return (self, buf)

    def handle(self):
        if self['m_nObjID'] in self.person['monsterdic']:
            self.person['monsterdic'][self['m_nObjID']][1] = self['TarPostion'][-1][0]
            self.person['monsterdic'][self['m_nObjID']][2] = self['TarPostion'][-1][1]
        #added by luoyunpeng for battle_path
        if not self.person['battle_monster'] == None:
            if self['m_nObjID'] <= 9000 : #it's monster
                dis_x = self['TarPostion'][-1][0] - self.person['posx']
                dis_z = self['TarPostion'][-1][1] - self.person['posz']
                if -3 <= dis_x <= 3 and -3 <= dis_z <= 3:
                    self.person['battle_monster'][self['m_nObjID']] = (self['TarPostion'][-1][0],self['TarPostion'][-1][1])


class PACKET_GC_NEWMONSTER(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self.BUF_SIZE = 108
        self.PE_KEY_LENGTH = 48

        self['m_nObjID'] = 0
        self['m_GUID'] = 0
        self['m_PosWorld_x'] = 0.0
        self['m_PosWorld_z'] = 0.0
        self['m_Dir'] = 0.0
        self['m_MoveSpeed'] = 0.0
        self['m_UpdateVer'] = 0
        self['m_hp'] = 0
        self['m_maxHp'] = 0
        self['m_NameSize'] = 0
        self['m_Name'] = u''
        self['m_CampId'] = 0
        self['m_DataId'] = 0
        self['m_ReputationId'] = 0
        self['m_AIType'] = 0

    def filldatafromstream(self, buf):
        (self['m_nObjID'], buf) = ReadInt32(buf)
        (self['m_GUID'], buf) = ReadUInt64(buf)
        (self['m_PosWorld_x'], buf) = ReadSingle(buf)
        (self['m_PosWorld_z'], buf) = ReadSingle(buf)
        (self['m_Dir'], buf) = ReadSingle(buf)
        (self['m_MoveSpeed'], buf) = ReadSingle(buf)
        (self['m_UpdateVer'], buf) = ReadUInt32(buf)
        (self['m_hp'], buf) = ReadInt32(buf)
        (self['m_maxHp'], buf) = ReadInt32(buf)
        (self['m_NameSize'], buf) = ReadUInt32(buf)

        if self['m_NameSize'] > 0:
            (self['m_Name'], buf) = ReadCharArray(buf, self['m_NameSize'], True)

        (self['m_DataId'], buf) = ReadUInt32(buf)
        (self['m_CampId'], buf) = ReadInt16(buf)
        (self['m_ReputationId'], buf) = ReadInt16(buf)
        (self['m_AIType'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        if self['m_ReputationId'] in self.person['targetmark']:
            self.person['monsterdic'][self['m_nObjID']] = [self['m_GUID'], self['m_PosWorld_x'], self['m_PosWorld_z'],
                                                           self['m_Name']]
        # #add by luoyunpeng for battle_path
        # if self['m_CampId'] == 9 :  #is monster
        #     if self.person['all_monster_dic'] == None:
        #         self.person['all_monster_dic'] = []
        #         self.person['all_monster_dic'].append[self['m_nObjID']]
        #     else:
        #         self.person['all_monster_dic'].append[self['m_nObjID']]



class PACKET_GC_NEWMONSTER_MOVE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self.MAX_CHAR_PATH_NODE_NUMBER = 16

        self['m_nObjID'] = 0
        self['m_GUID'] = 0
        self['m_Pos'] = [0.0, 0.0]
        self['m_Dir'] = 0.0
        self['m_MoveSpeed'] = 0.0
        self['m_UpdateVer'] = 0
        self['m_LogicCount'] = 0
        self['m_BackMove'] = 0
        self['m_NumTargetPos'] = 0
        self['m_TargetPoses'] = []
        self['m_hp'] = 0
        self['m_maxHp'] = 0

    def filldatafromstream(self, buf):
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['m_GUID'], buf) = ReadInt64(buf)
        (self['m_Pos'][0], buf) = ReadSingle(buf)
        (self['m_Pos'][1], buf) = ReadSingle(buf)
        (self['m_Dir'], buf) = ReadSingle(buf)
        (self['m_MoveSpeed'], buf) = ReadSingle(buf)
        (self['m_UpdateVer'], buf) = ReadUInt32(buf)
        (self['m_LogicCount'], buf) = ReadInt32(buf)
        (self['m_BackMove'], buf) = ReadByte(buf)
        self['m_BackMove'] = ord(self['m_BackMove'])
        (self['m_NumTargetPos'], buf) = ReadByte(buf)
        self['m_NumTargetPos'] = ord(self['m_NumTargetPos'])
        for i in range(self['m_NumTargetPos']):
            self['m_TargetPoses'].append([0.0, 0.0])
            (self['m_TargetPoses'][i][0], buf) = ReadSingle(buf)
            (self['m_TargetPoses'][i][1], buf) = ReadSingle(buf)
        (self['m_hp'], buf) = ReadInt32(buf)
        (self['m_maxHp'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        if self['m_nObjID'] in self.person['monsterdic']:
            self.person['monsterdic'][self['m_nObjID']][1] = self['m_TargetPoses'][-1][0]
            self.person['monsterdic'][self['m_nObjID']][2] = self['m_TargetPoses'][-1][1]


class PACKET_CG_CHARUSESKILL(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['ObjId'] = 0
        self['SkillDataId'] = 0
        self['TargetGuid'] = 0
        self['TargetObjId'] = -1
        self['PosX'] = 0.0
        self['PosY'] = 0.0
        self['dir'] = 0.0

    def getdatastream(self):
        buf = ''
        buf += WriteSingle(self['dir'])
        buf += WriteInt16(self['SkillDataId'])
        buf += WriteUInt64(self['TargetGuid'])
        buf += WriteInt32(self['ObjId'])
        buf += WriteInt32(self['TargetObjId'])
        buf += WriteSingle(self['PosX'])
        buf += WriteSingle(self['PosY'])
        return buf

    def filldatafromstream(self, buf):
        (self['dir'], buf) = ReadSingle(buf)
        (self['SkillDataId'], buf) = ReadInt16(buf)
        (self['TargetGuid'], buf) = ReadUInt64(buf)
        (self['ObjId'], buf) = ReadInt32(buf)
        (self['TargetObjId'], buf) = ReadInt32(buf)
        (self['PosX'], buf) = ReadSingle(buf)
        (self['PosY'], buf) = ReadSingle(buf)
        return (self, buf)


class PACKET_GC_DELOBJECT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ObjID'] = 0
        self['m_SceneID'] = 0

    def filldatafromstream(self, buf):
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['m_SceneID'], buf) = ReadInt16(buf)
        return (self, buf)

    def handle(self):
        if self['m_ObjID'] in self.person['monsterdic']:
            self.person['monsterdic'].pop(self['m_ObjID'])


class PACKET_GC_PLAYER_DIE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_CanSpecialTreatmentRelive'] = 0
        self['m_CanSkillRelive'] = 0
        self['m_Time'] = 0
        self['m_PunishParam'] = DIE_PUNISH_PARAM(person)
        self['m_NotifyType'] = 0
        self['m_KillerGUID'] = 0
        self['m_ZoneWorldID'] = 0

    def filldatafromstream(self, buf):
        (self['m_CanSpecialTreatmentRelive'], buf) = ReadByte(buf)  # 1 can revive on the position
        self['m_CanSpecialTreatmentRelive'] = ord(self['m_CanSpecialTreatmentRelive'])
        (self['m_CanSkillRelive'], buf) = ReadInt32(buf)
        (self['m_Time'], buf) = ReadUInt32(buf)
        (self['m_KillerGUID'], buf) = ReadInt64(buf)
        (self['m_ZoneWorldID'], buf) = ReadInt16(buf)
        (self['m_PunishParam'], buf) = self['m_PunishParam'].filldatafromstream(buf)
        (self['notifyType'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        self.person['state'] = 'die'
        self.person['isDie'] = 'die'


class DIE_PUNISH_PARAM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_KilledSceneName'] = 0
        self['m_SceneNameLen'] = 0
        self['m_ExpLost'] = 0
        self['m_MonenyLost'] = 0
        self['m_ItemLosts'] = []
        self['m_ItemLostCount'] = 0
        self['m_KillerName'] = u''
        self.NPC_NAME_LEN = 32

    def filldatafromstream(self, buf):
        (self['m_SceneNameLen'], buf) = ReadInt16(buf)
        (self['m_KilledSceneName'], buf) = ReadCharArray(buf, self['m_SceneNameLen'])
        (self['m_ExpLost'], buf) = ReadUInt32(buf)
        (self['m_MonenyLost'], buf) = ReadUInt32(buf)
        (self['m_ItemLostCount'], buf) = ReadByte(buf)
        self['m_ItemLostCount'] = ord(self['m_ItemLostCount'])
        for i in range(self['m_ItemLostCount']):
            self['m_ItemLosts'].append(0)
            (self['m_ItemLosts'][i], buf) = ReadUInt32(buf)
        (self['m_KillerName'], buf) = ReadCharArray(buf, self.NPC_NAME_LEN)
        return (self, buf)


class PACKET_CG_PLAYER_DIE_RESULT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ResultCode'] = -1  # 0:释放灵魂，1：接受复活， 2：原地复活

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_ResultCode'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_ResultCode'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_EXECUTESCRIPT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Script'] = X_SCRIPT(person)

    def getdatastream(self):
        buf = ''
        buf += self['m_Script'].getdatastream()
        return buf

    def filldatafromstream(self, buf):
        (self['m_Script'], buf) = self['m_Script'].filldatafromstream(buf)
        return (self, buf)


class X_SCRIPT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self.MAX_FUNC_NAME_SIZE = 64
        self.MAX_INT_PARAM_COUNT = 6

        self['m_ScriptID'] = 0
        self['m_uFunNameSize'] = 0
        self['m_szFunName'] = u''
        self['m_uParamCount'] = 0
        self['m_aParam'] = []

    def getdatastream(self):
        buf = ''
        buf += Int32ConvertByte(self['m_ScriptID'])
        size = GetStringBytesLen(self['m_szFunName'], True)
        self['m_uFunNameSize'] = size
        buf += WriteByte(chr(size))
        buf += WriteCharArray(self['m_szFunName'], size, True)
        buf += WriteByte(chr(self['m_uParamCount']))
        for i in range(self['m_uParamCount']):
            buf += Int32ConvertByte(self['m_aParam'][i])
        return buf

    def filldatafromstream(self, buf):
        (self['m_ScriptID'], buf) = ByteConvertInt32(buf)
        (self['m_uFunNameSize'], buf) = ReadByte(buf)
        self['m_uFunNameSize'] = ord(self['m_uFunNameSize'])
        (self['m_szFunName'], buf) = ReadCharArray(buf, self['m_uFunNameSize'])
        (self['m_uParamCount'], buf) = ReadByte(buf)
        self['m_uParamCount'] = ord(self['m_uParamCount'])
        for i in range(self['m_uParamCount']):
            self['m_aParam'].append(0)
            (self['m_aParam'][i], buf) = ByteConvertInt32(buf)
        return (self, buf)


# 未完成
class PACKET_GC_MISSIONMODIFY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['missionIndex'] = 0
        self['isMissionAccept'] = 0
        self['m_byFlag'] = 0  # 0:修改mission  1:修改数据
        self['m_IsFinish'] = 0
        self['m_idMission'] = 0
        self['paramls'] = []

    def filldatafromstream(self, buf):
        (self['m_byFlag'], buf) = ReadByte(buf)
        self['m_byFlag'] = ord(self['m_byFlag'])

        if self['m_byFlag'] == 0:
            (self['missionIndex'], buf) = ReadInt32(buf)
            (self['m_idMission'], buf) = ReadInt32(buf)
            # if the mission id is exist
            (m_yFlags, buf) = ReadByte(buf)
            m_yFlags = ord(m_yFlags)
            paramls = []
            for i in range(8):
                (param, buf) = ReadInt32(buf)
                paramls.append(param)
            self['m_IsFinish'] = paramls[1]

            self['paramls'] = paramls
        return (self, buf)

    def handle(self):
        if self['m_byFlag'] == 0:
            self.person['mCurrentMission'] = self['m_idMission']
            self.person['MissionIsFinish'] = self['m_IsFinish']


class PACKET_CG_MISSIONSUBMIT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_idNPC'] = 0
        self['m_idScript'] = 0
        self['m_idSelectRadio'] = 0
        self['m_idIssueScript'] = 0
        self['m_validateData'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_idNPC'])
        buf += WriteInt32(self['m_idScript'])
        buf += WriteUInt32(self['m_idSelectRadio'])
        buf += WriteInt32(self['m_idIssueScript'])
        buf += WriteUInt32(self['m_validateData'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_idNPC'], buf) = ReadInt32(buf)
        (self['m_idScript'], buf) = ReadInt32(buf)
        (self['m_idSelectRadio'], buf) = ReadUInt32(buf)
        (self['m_idIssueScript'], buf) = ReadInt32(buf)
        (self['m_validateData'], buf) = ReadUInt32(buf)
        return (self, buf)


class CGRequireRankList(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['GUID_L'] = 0
        self['GUID_H'] = 0
        self['RankType'] = 0
        self['From'] = 0
        self['To'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['GUID_L'])
        buf += WriteInt32(self['GUID_H'])
        buf += WriteByte(chr(self['RankType']))
        buf += WriteByte(chr(self['From']))
        buf += WriteByte(chr(self['To']))
        return buf

    def filldatafromstream(self, buf):
        (self['GUID_L'], buf) = ReadInt32(buf)
        (self['GUID_H'], buf) = ReadInt32(buf)
        (self['RankType'], buf) = ReadByte(buf)
        self['RankType'] = ord(self['RankType'])
        (self['From'], buf) = ReadByte(buf)
        self['From'] = ord(self['From'])
        (self['To'], buf) = ReadByte(buf)
        self['To'] = ord(self['To'])
        return (self, buf)


class GCRequireRankList(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['GUID_L'] = 0
        self['GUID_H'] = 0
        self['RankType'] = 0
        self['Count'] = 0
        self['Total'] = 0
        self['MyRank'] = 0

    def filldatafromstream(self, buf):
        (self['GUID_L'], buf) = ReadInt32(buf)
        (self['GUID_H'], buf) = ReadInt32(buf)
        (self['RankType'], buf) = ReadByte(buf)
        self['RankType'] = ord(self['RankType'])
        (self['Count'], buf) = ReadByte(buf)
        self['Count'] = ord(self['Count'])
        (self['Total'], buf) = ReadByte(buf)
        self['Total'] = ord(self['Total'])
        (self['MyRank'], buf) = ReadByte(buf)
        self['MyRank'] = ord(self['MyRank'])
        return (self, buf)


class PACKET_GC_NOTIFY_MAIL_NEW(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_PlayerID'] = 0
        self['m_bNewMailFlag'] = 0
        self['m_bMailAppendFlag'] = 0

    def filldatafromstream(self, buf):
        (self['m_PlayerID'], buf) = ReadInt16(buf)
        (self['m_bNewMailFlag'], buf) = ReadInt32(buf)
        (self['m_bMailAppendFlag'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_ASK_MAIL_LIST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['myLGuid'] = 0
        self['myHGuid'] = 0
        self['myMailType'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['myLGuid'])
        buf += WriteInt32(self['myHGuid'])
        buf += WriteByte(chr(self['myMailType']))
        return buf

    def filldatafromstream(self, buf):
        (self['myLGuid'], buf) = ReadInt32(buf)
        (self['myHGuid'], buf) = ReadInt32(buf)
        (self['myMailType'], buf) = ReadByte(buf)
        self['myMailType'] = ord(self['myMailType'])
        return (self, buf)


class PACKET_GC_RET_MAIL_LIST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_PlayerID'] = 0
        self['m_ByCGMailType'] = 0
        self['m_MailCount'] = 0
        self['mybIsShowNew'] = 0
        self['mMailList'] = []

    def filldatafromstream(self, buf):
        (self['m_PlayerID'], buf) = ReadInt16(buf)
        (self['m_ByCGMailType'], buf) = ReadByte(buf)
        self['m_ByCGMailType'] = ord(self['m_ByCGMailType'])
        (self['m_MailCount'], buf) = ReadUInt32(buf)
        (self['mybIsShowNew'], buf) = ReadUInt32(buf)
        for i in range(self['m_MailCount']):
            (mailId, buf) = ReadUInt32(buf)
            (mailType, buf) = ReadByte(buf)
            mailType = ord(mailType)
            (guildL, buf) = ReadInt32(buf)
            (guildH, buf) = ReadInt32(buf)
            (senderName, buf) = ReadCharArray(buf, 31)
            (title, buf) = ReadCharArray(buf, 118)
            (viewFlag, buf) = ReadInt32(buf)
            (bReqMoney, buf) = ReadInt32(buf)
            (bIsHaveAppend, buf) = ReadInt32(buf)
            (leftTime, buf) = ReadUInt32(buf)
            (createTime, buf) = ReadUInt32(buf)
            if viewFlag == 0:
                self.person['mailFlag'] = 1
            temp = {"mailId": mailId,
                    "mailType": mailType,
                    "guildL": guildL,
                    "guildH": guildH,
                    "senderName": senderName,
                    "title": title,
                    "viewFlag": viewFlag,
                    "bReqMoney": bReqMoney,
                    "bIsHaveAppend": bIsHaveAppend,
                    "leftTime": leftTime,
                    "createTime": createTime}
            self['mMailList'].append(temp)
        return (self, buf)


class PACKET_CG_ASK_MAIL_NEW(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['myLGuid'] = 0
        self['myHGuid'] = 0
        self['myCGMailType'] = 0
        self['myMailType'] = 0
        self['myUMainId'] = 0
        self['myCreateTime'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['myLGuid'])
        buf += WriteInt32(self['myHGuid'])
        buf += WriteByte(chr(self['myCGMailType']))
        buf += WriteByte(chr(self['myMailType']))
        buf += WriteUInt32(self['myUMainId'])
        buf += WriteUInt32(self['myCreateTime'])
        return buf

    def filldatafromstream(self, buf):
        (self['myLGuid'], buf) = ReadInt32(buf)
        (self['myHGuid'], buf) = ReadInt32(buf)
        (self['myCGMailType'], buf) = ReadByte(buf)
        self['myCGMailType'] = ord(self['myCGMailType'])
        (self['myMailType'], buf) = ReadByte(buf)
        self['myMailType'] = ord(self['myMailType'])
        (self['myUMainId'], buf) = ReadUInt32(buf)
        (self['myCreateTime'], buf) = ReadUInt32(buf)
        return (self, buf)


class PACKET_GCSongLiaoBaseInfo(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['SongScore'] = 0
        self['LiaoScore'] = 0
        self['MyCamp'] = 0
        self['YunZhongState'] = 0
        self['YanMenState'] = 0
        self['DaiJunState'] = 0
        self['YunZhongValue'] = 0
        self['YanMenValue'] = 0
        self['DaiJunValue'] = 0

    def filldatafromstream(self, buf):
        (self['SongScore'], buf) = ReadInt32(buf)
        (self['LiaoScore'], buf) = ReadInt32(buf)
        (self['MyCamp'], buf) = ReadByte(buf)
        self['MyCamp'] = ord(self['MyCamp'])
        (self['YunZhongState'], buf) = ReadByte(buf)
        self['YunZhongState'] = ord(self['YunZhongState'])
        (self['YanMenState'], buf) = ReadByte(buf)
        self['YanMenState'] = ord(self['YanMenState'])
        (self['DaiJunState'], buf) = ReadByte(buf)
        self['DaiJunState'] = ord(self['DaiJunState'])
        (self['YunZhongValue'], buf) = ReadInt32(buf)
        (self['YanMenValue'], buf) = ReadInt32(buf)
        (self['DaiJunValue'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        self.person['camp'] = self['MyCamp']


class PACKET_CG_ASKCAMPAIGNCOUNT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Flag'] = 0  # 1 活动大厅：申请角色参加活动次数

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_Flag'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_Flag'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_WARPOSITIONMODIFY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_nSceneID'] = 0
        self['m_Guid_H'] = 0
        self['m_Guid_L'] = 0
        self['guid'] = 0
        self['m_nCampID'] = 0  # 0表示敌方，1表示已方
        self['m_bSycnType'] = 0
        self['m_nPositon_x'] = 0
        self['m_nPositon_y'] = 0

    def filldatafromstream(self, buf):
        (self['m_nSceneID'], buf) = ReadInt32(buf)
        (guid, buf) = ReadUInt64(buf)
        self['guid'] = guid
        self['m_Guid_L'], self['m_Guid_H'] = DecodeUInt64(guid)
        (self['m_nCampID'], buf) = ReadInt32(buf)
        (self['m_bSycnType'], buf) = ReadByte(buf)
        self['m_bSycnType'] = ord(self['m_bSycnType'])
        (self['m_nPositon_x'], buf) = ReadInt32(buf)
        (self['m_nPositon_y'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        flag = 0
        if self['guid'] in self.person['targetdic']:
            if self['m_nCampID'] == 1:
                flag = 1
        else:
            pass
            # print "guid:", self['guid'], 'not in new player move?'
        if flag == 1:
            self.person['targetdic'].pop(self['guid'])


class PACKET_GC_NEWPLAYER(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ObjID'] = 0
        self['m_GUID'] = 0
        self['m_PosWorld_x'] = 0
        self['m_PosWorld_z'] = 0
        self['m_Dir'] = 0
        self['m_MoveSpeed'] = 0
        self['m_UpdateVer'] = 0
        self['m_nCharFrameID'] = 0
        self['m_nIsFlyMove'] = 0
        self['m_bMountID'] = 0
        self['m_hp'] = 0
        self['m_maxHp'] = 0
        self['m_FashionID'] = 0
        self['m_ColorID'] = 0
        self['m_NameSize'] = 0
        self['m_Name'] = u''
        self['m_CampId'] = 0
        self['m_ReputationId'] = 0
        self['m_GuildId'] = 0

    def filldatafromstream(self, buf):
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (guid_l, buf) = ReadInt32(buf)
        (guid_H, buf) = ReadInt32(buf)
        self['m_GUID'] = EncodeUInt64(guid_H, guid_l)
        (self['m_PosWorld_x'], buf) = ReadSingle(buf)
        (self['m_PosWorld_z'], buf) = ReadSingle(buf)
        (self['m_Dir'], buf) = ReadSingle(buf)
        (self['m_MoveSpeed'], buf) = ReadSingle(buf)
        (self['m_UpdateVer'], buf) = ReadUInt32(buf)
        (self['m_nCharFrameID'], buf) = ReadInt32(buf)
        (self['m_nIsFlyMove'], buf) = ReadInt32(buf)
        (self['m_bMountID'], buf) = ReadInt32(buf)
        if True:
            (self['m_hp'], buf) = ReadInt32(buf)
            (self['m_maxHp'], buf) = ReadInt32(buf)
        (self['m_FashionID'], buf) = ReadInt32(buf)
        (self['m_ColorID'], buf) = ReadInt32(buf)
        (self['m_NameSize'], buf) = ReadUInt32(buf)
        if self['m_NameSize'] > 0:
            (self['m_Name'], buf) = ReadCharArray(buf, self['m_NameSize'])
        (self['m_CampId'], buf) = ReadInt16(buf)
        (self['m_ReputationId'], buf) = ReadInt16(buf)
        (self['m_GuildId'], buf) = ReadInt16(buf)
        return (self, buf)

    def handle(self):
        self.person['tarGUID'] = self['m_GUID']
        self.person['tarOBJID'] = self['m_ObjID']
        if self['m_CampId'] > 0:
            self.person['targetdic'][self['m_GUID']] = [self['m_ObjID'], [self['m_PosWorld_x'], self['m_PosWorld_z']]]


class PACKET_GC_NEWPLAYER_MOVE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_ObjID'] = 0
        self['m_GUID'] = 0
        self['m_Pos'] = [0, 0]
        self['m_Dir'] = 0
        self['m_MoveSpeed'] = 0
        self['m_UpdateVer'] = 0
        self['m_nCharFrameID'] = 0
        self['m_LogicCount'] = 0
        self['m_BackMove'] = 0
        self['m_NumTargetPos'] = 0
        self['m_TargetPoses'] = []
        self['m_bIsFlyMove'] = 0
        self['m_nMount'] = 0
        self['m_hp'] = 0
        self['m_maxHp'] = 0
        self['m_FashionID'] = 0
        self['m_ColorID'] = 0

    def filldatafromstream(self, buf):
        (self['m_ObjID'], buf) = ReadInt32(buf)
        (self['m_GUID'], buf) = ReadInt64(buf)
        (self['m_Pos'][0], buf) = ReadSingle(buf)
        (self['m_Pos'][1], buf) = ReadSingle(buf)
        (self['m_Dir'], buf) = ReadSingle(buf)
        (self['m_MoveSpeed'], buf) = ReadSingle(buf)
        (self['m_UpdateVer'], buf) = ReadUInt32(buf)
        (self['m_nCharFrameID'], buf) = ReadInt32(buf)
        (self['m_LogicCount'], buf) = ReadInt32(buf)
        (self['m_BackMove'], buf) = ReadByte(buf)
        self['m_BackMove'] = ord(self['m_BackMove'])
        (self['m_NumTargetPos'], buf) = ReadByte(buf)
        self['m_NumTargetPos'] = ord(self['m_NumTargetPos'])
        for i in range(self['m_NumTargetPos']):
            temp = [0, 0]
            (temp[0], buf) = ReadSingle(buf)
            (temp[1], buf) = ReadSingle(buf)
            self['m_TargetPoses'].append(temp)
        (self['m_bIsFlyMove'], buf) = ReadInt32(buf)
        (self['m_nMount'], buf) = ReadInt32(buf)
        if True:
            (self['m_hp'], buf) = ReadInt32(buf)
            (self['m_maxHp'], buf) = ReadInt32(buf)
        (self['m_FashionID'], buf) = ReadInt32(buf)
        (self['m_ColorID'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        self.person['targetdic'][self['m_GUID']] = [self['m_ObjID'], self['m_TargetPoses'][-1]]
        self.person['tarGUID'] = self['m_GUID']
        self.person['tarOBJID'] = self['m_ObjID']


# 未完成
class PACKET_GC_DETAIL_HEALS_AND_DAMAGES(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['DirtyFlags'] = 0  # 未完成
        self['ReceiverObjId'] = 0
        self['skillDataId'] = 0
        self['hitRate'] = 0
        self['SenderObjId'] = 0
        self['SenderLogicCount'] = 0
        self['HpChange'] = 0
        self['oldHp'] = 0
        self['MpChange'] = 0
        self['EnergyChange'] = 0
        self['RageChange'] = 0
        self['StrikePointChange'] = 0
        self['IsCriticalHit'] = 0
        self['IsEnhanceDamage'] = 0
        self['realSize'] = 0

    def filldatafromstream(self, buf):
        (self['DirtyFlags'], buf) = ReadCharArray(buf, 1, False)
        (self['ReceiverObjId'], buf) = ReadInt32(buf)
        (self['SenderObjId'], buf) = ReadInt32(buf)
        (self['SenderLogicCount'], buf) = ReadInt32(buf)
        if 0 != (ord(self['DirtyFlags'][0]) & 1):
            (self['HpChange'], buf) = ReadInt32(buf)
            (self['oldHp'], buf) = ReadInt32(buf)

        # (self['SenderLogicCount'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        if self['oldHp'] != 0 and (self['oldHp'] + self['HpChange'] < 0):
            self.person['death_objId'] = self['ReceiverObjId']
            if self.person['death_objId'] == self.person['m_ObjID']:
                pass
                # self.person['state'] = "die"
            
            #add by luoyunpeng for battle_path
            if not self.person['battle_monster'] == None:
                if self.person['battle_monster'].has_key(self['ReceiverObjId']):
                    del self.person['battle_monster'][self['ReceiverObjId']]
            


class PACKET_GC_PLAYER_RELIVE(Packet):
    def handle(self):
        self.person['state'] = 'alive'


class PACKET_GC_USEEQUIPRESULT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Result'] = 0  # 1为成功

    def filldatafromstream(self, buf):
        (self['m_Result'], buf) = ReadByte(buf)
        self['m_Result'] = ord(self['m_Result'])
        return (self, buf)


class PACKET_CG_ASK_BALANCE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Type'] = 0  # 余额请求类型:0登陆请求玩家账户余额~1支付完成之后请求余额~2：刷新玩家票据
        self['OpenId'] = 0
        self['Access_Token'] = 0
        self['Pay_Token'] = 0
        self['pf'] = 0
        self['pfKey'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['Type']))
        buf += WriteCharArray(self['OpenId'], 128, True)
        buf += WriteCharArray(self['Access_Token'], 128, True)
        buf += WriteCharArray(self['Pay_Token'], 128, True)
        buf += WriteCharArray(self['pf'], 128, True)
        buf += WriteCharArray(self['pfKey'], 128, True)
        return buf

    def filldatafromstream(self, buf):
        (self['Type'], buf) = ReadByte(buf)
        self['Type'] = ord(self['Type'])
        (self['OpenId'], buf) = ReadCharArray(buf, 128)
        (self['Access_Token'], buf) = ReadCharArray(buf, 128)
        (self['Pay_Token'], buf) = ReadCharArray(buf, 128)
        (self['pf'], buf) = ReadCharArray(buf, 128)
        (self['pfKey'], buf) = ReadCharArray(buf, 127)
        return (self, buf)


class PACKET_GC_Ret_BALANCE(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['result'] = 0  # 0:支付成功
        self['balance'] = 0  # --游戏币个数（包含了赠送游戏币）
        self['gen_Balance'] = 0  # -绑定元宝（其实是米大师返回的赠送元宝，但是由于绑定元宝也
        self['first_save'] = 0  # 是否满足首次充值，1：满足，0：不满足。
        self['save_amt'] = 0  # 累计充值金额的游戏币数量

    def filldatafromstream(self, buf):
        (self['result'], buf) = ReadInt32(buf)
        (self['balance'], buf) = ReadInt32(buf)
        (self['gen_Balance'], buf) = ReadInt32(buf)
        (self['first_save'], buf) = ReadInt32(buf)
        (self['save_amt'], buf) = ReadInt32(buf)
        return (self, buf)


# supinrong end



# lua packet **************start***************

class PACKET_CG_OPER_PLATFORM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Guid_H'] = 0
        self['m_Guid_L'] = 0
        self['m_szActiveName'] = u''
        self['m_bOperType'] = 0
        self['m_nActiveID'] = 0
        self['m_nSubClassID'] = 0

    def getdatastream(self):
        buf = ''
        guid = EncodeUInt64(self['m_Guid_H'], self['m_Guid_L'])
        buf += WriteUInt64(guid)
        length = GetStringBytesLen(self['m_szActiveName'], True)
        buf += WriteByte(chr(length))
        buf += WriteCharArray(self['m_szActiveName'], length, True)

        buf += WriteInt32(self['m_bOperType'])
        buf += WriteInt32(self['m_nActiveID'])
        buf += WriteByte(chr(self['m_nSubClassID']))

        return buf

    def filldatafromstream(self, buf):
        guid = 0
        (guid, buf) = ReadUInt64(buf)
        self['m_Guid_L'], self['m_Guid_H'] = DecodeUInt64(guid)
        (length, buf) = ReadByte(buf)
        length = ord(length)
        (self['m_szActiveName'], buf) = ReadCharArray(buf, length)
        (self['m_bOperType'], buf) = ReadInt32(buf)
        (self['m_nActiveID'], buf) = ReadInt32(buf)
        (self['m_nSubClassID'], buf) = ReadByte(buf)
        self['m_nSubClassID'] = ord(self['m_nSubClassID'])
        return (self, buf)


class PACKET_GC_RET_PLATFORM_RESULT(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Guid_H'] = 0
        self['m_Guid_L'] = 0
        self['m_GuidString'] = u''
        self['m_nActiveID'] = 0
        self['m_nSubClassID'] = 0
        self['m_nResult'] = 0

    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (guid, buf) = ReadUInt64(buf)
        self['m_Guid_L'], self['m_Guid_H'] = DecodeUInt64(guid)
        self['m_GuidString'] = str(EncodeUInt64(self['m_Guid_H'], self['m_Guid_L']))
        (self['m_nActiveID'], buf) = ReadInt32(buf)
        (self['m_nSubClassID'], buf) = ReadByte(buf)
        self['m_nSubClassID'] = ord(self['m_nSubClassID'])
        (self['m_nResult'], buf) = ReadInt32(buf)
        return (self, buf)

    def handle(self):
        pass


class PACKET_CG_CREATE_PLATFORM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_Guid_H'] = 0
        self['m_Guid_L'] = 0
        self['m_szActiveName'] = u''
        self['m_nActiveID'] = 0
        self['m_nSubClassID'] = 0
        self['m_nLowLevel'] = 0
        self['m_nUpperLevel'] = 0
        self['m_bMatchType'] = 0
        self['m_bAutoMatch'] = 0

    def getdatastream(self):
        buf = ''
        guid = EncodeUInt64(self['m_Guid_H'], self['m_Guid_L'])
        buf += WriteUInt64(guid)
        length = GetStringBytesLen(self['m_szActiveName'], True)
        buf += WriteByte(chr(length))
        buf += WriteCharArray(self['m_szActiveName'], length, True)

        buf += WriteInt32(self['m_nActiveID'])
        buf += WriteByte(chr(self['m_nSubClassID']))

        buf += WriteInt32(self['m_nLowLevel'])
        buf += WriteInt32(self['m_nUpperLevel'])
        buf += WriteInt32(self['m_bMatchType'])
        buf += WriteInt32(self['m_bAutoMatch'])

        return buf

    def filldatafromstream(self, buf):
        guid = 0
        (guid, buf) = ReadUInt64(buf)
        self['m_Guid_L'], self['m_Guid_H'] = DecodeUInt64(guid)
        (length, buf) = ReadByte(buf)
        length = ord(length)
        (self['m_szActiveName'], buf) = ReadCharArray(buf, length)

        (self['m_nActiveID'], buf) = ReadInt32(buf)
        (self['m_nSubClassID'], buf) = ReadByte(buf)
        self['m_nSubClassID'] = ord(self['m_nSubClassID'])
        (self['m_nLowLevel'], buf) = ReadInt32(buf)
        (self['m_nUpperLevel'], buf) = ReadInt32(buf)
        (self['m_bMatchType'], buf) = ReadInt32(buf)
        (self['m_bAutoMatch'], buf) = ReadInt32(buf)

        return (self, buf)


# 上架物品
class PACKET_CG_CONSIGNSALEITEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        # self['guid_L'] = 0
        # self['guid_H'] = 0

        self['guid'] = 0
        self['count'] = 0
        self['price'] = 0
        self['curpage'] = 1

    def getdatastream(self):
        buf = ''
        # guid = EncodeUInt64(self['guid_L'],self['guid_H'])
        # buf += WriteUInt64(guid)

        buf += WriteUInt64(self['guid'])
        buf += WriteInt32(self['count'])
        buf += WriteInt32(self['price'])
        buf += WriteInt32(self['curpage'])
        return buf

    def filldatafromstream(self, buf):
        # guid = 0
        # (guid, buf) = ReadUInt64(buf)
        # self['guid_L'],self['guid_H'], = DecodeUInt64(guid)
        # gid = MakeGUID(self['guid_L'],self['guid_H'])
        # print gid
        # self['guid'] = gid
        (self['guid'], buf) = ReadUInt64(buf)
        (self['count'], buf) = ReadInt32(buf)
        (self['price'], buf) = ReadInt32(buf)
        (self['curpage'], buf) = ReadInt32(buf)
        return (self, buf)


# 下架物品
class PACKET_CG_CANCELCONSIGNSALEITEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['guid'] = 0
        self['curpage'] = 1

    def getdatastream(self):
        buf = ''
        buf += WriteUInt64(self['guid'])
        buf += WriteInt32(self['curpage'])
        return buf

    def filldatafromstream(self, buf):
        (self['guid'], buf) = ReadUInt64(buf)
        (self['curpage'], buf) = ReadInt32(buf)
        return (self, buf)


# 获取自己的上架商品列表
class PACKET_CG_ASK_MYCONSIGNSALEITEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['index'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['index'])
        return buf

    def filldatafromstream(self, buf):
        (self['index'], buf) = ReadInt32(buf)
        return (self, buf)


# 返回自己的上架商品列表
class PACKET_GC_RET_MYCONSIGNSALEITEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        # self['index'] = 0
        self['max'] = 0

        self['saleItems'] = []

        # self['guid_L'] = 0
        # self['guid_H'] = 0

        self['CurSaleCount'] = 0
        self['MaxSaleCount'] = 0

    def getdatastream(self):
        buf = ''
        # buf += WriteInt16(self['index'])
        buf += WriteInt16(self['max'])
        for i in range(self['index']):
            buf += WriteByte(chr(self['saleItems'][i][0]))
            buf += WriteUInt32(self['saleItems'][i][1])
            buf += WriteByte(chr(self['saleItems'][i][2]))
            buf += WriteByte(chr(self['saleItems'][i][3]))
            buf += WriteInt16(self['saleItems'][i][4])
            buf += WriteByte(chr(self['saleItems'][i][5]))
            buf += WriteUInt64(self['saleItems'][i][6])
            buf += WriteInt16(self['saleItems'][i][7])
            buf += WriteInt16(self['saleItems'][i][8])
            buf += WriteUInt32(self['saleItems'][i][9])
        buf += WriteInt16(self['CurSaleCount'])
        buf += WriteInt16(self['MaxSaleCount'])
        return buf

    def filldatafromstream(self, buf):
        # (self['index'], buf) = ReadInt(buf)
        (self['max'], buf) = ReadInt(buf)
        # print self['index']

        for i in range(self['max']):
            self['saleItems'].append([' ', 0, ' ', ' ', 0, ' ', 0, 0, 0, 0])
            (self['saleItems'][i][0], buf) = ReadByte(buf)
            self['saleItems'][i][0] = ord(self['saleItems'][i][0])
            (self['saleItems'][i][1], buf) = ReadUint(buf)
            (self['saleItems'][i][2], buf) = ReadByte(buf)
            self['saleItems'][i][2] = ord(self['saleItems'][i][2])
            (self['saleItems'][i][3], buf) = ReadByte(buf)
            self['saleItems'][i][3] = ord(self['saleItems'][i][3])
            (self['saleItems'][i][4], buf) = ReadInt32(buf)
            (self['saleItems'][i][5], buf) = ReadByte(buf)
            self['saleItems'][i][5] = ord(self['saleItems'][i][5])
            (self['guid_H'], buf) = ReadInt32(buf)
            (self['guid_L'], buf) = ReadInt32(buf)
            # print self['guid_L']
            # print self['guid_H']
            # gid = MakeGUID(self['guid_L'],self['guid_H'])
            # print gid
            self['saleItems'][i][6] = MakeGUID(self['guid_L'], self['guid_H'])

            (self['saleItems'][i][7], buf) = ReadInt(buf)
            (self['saleItems'][i][8], buf) = ReadInt(buf)
            (self['saleItems'][i][9], buf) = ReadUint(buf)
        (self['CurSaleCount'], buf) = ReadInt(buf)
        (self['MaxSaleCount'], buf) = ReadInt(buf)
        return (self, buf)


# 获取拍卖物品列表
class PACKET_CG_ASK_CONSIGNSALEITEMINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self.sort = {
            'Equip': 0,
            'Gem': 1,
            'Pet': 2,
            'Other': 3,
            'All': 4
        }
        self.SortClass = {
            'Quality': 0,
            'Level': 1,
            'Count': 2,
            'Price': 3,
            'TableID': 4
        }
        self.SortType = {
            'UP': 0,
            'DOWN': 1
        }
        self['sort'] = 0
        self['subtype'] = 0
        self['thirdtype'] = 0
        self['quality'] = 0
        self['sortclass'] = self.SortClass['Price']
        self['sorttype'] = self.SortType['UP']
        self['keyword'] = u""
        self['page'] = 1
        self['id'] = -1
        self['min'] = 0
        self['max'] = 0
        self['isShow'] = 0
        self['EquipFiltrateIndex'] = 9

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['sort'])
        buf += WriteInt32(self['subtype'])
        buf += WriteInt32(self['thirdtype'])
        buf += WriteInt32(self['quality'])
        buf += WriteInt32(self['sortclass'])
        buf += WriteInt32(self['sorttype'])
        buf += WriteInt32(self['page'])
        if self['id'] > 0:
            buf += WriteInt32(self['id'])
        else:
            buf += WriteInt32(self['min'])
            buf += WriteInt32(self['max'])
        buf += WriteInt32(self['isShow'])
        buf += WriteInt32(self['EquipFiltrateIndex'])
        return buf

    def filldatafromstream(self, buf):
        (self['sort'], buf) = ReadInt32(buf)
        (self['subtype'], buf) = ReadInt32(buf)
        (self['thirdtype'], buf) = ReadInt32(buf)
        (self['quality'], buf) = ReadInt32(buf)
        (self['sortclass'], buf) = ReadInt32(buf)
        (self['sorttype'], buf) = ReadInt32(buf)
        (self['page'], buf) = ReadInt32(buf)
        if self['id'] > 0:
            (self['id'], buf) = ReadInt32(buf)
        else:
            (self['min'], buf) = ReadInt32(buf)
            (self['max'], buf) = ReadInt32(buf)
        (self['isShow'], buf) = ReadInt32(buf)
        (self['EquipFiltrateIndex'], buf) = ReadInt32(buf)
        return (self, buf)


# 返回拍卖物品列表
class PACKET_GC_RET_CONSIGNSALEITEMINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['max'] = 0

        self['Buy_RightTwoItem'] = []

        self['ItemPage'] = 0
        self['ItemPageMax'] = 0
        self['sum'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['max'])
        for i in range(self['index']):
            buf += WriteByte(chr(self['Buy_RightTwoItem'][i][0]))
            buf += WriteUInt32(self['Buy_RightTwoItem'][i][1])
            buf += WriteByte(chr(self['Buy_RightTwoItem'][i][2]))
            buf += WriteByte(chr(self['Buy_RightTwoItem'][i][3]))
            buf += WriteInt16(self['Buy_RightTwoItem'][i][4])
            buf += WriteByte(chr(self['Buy_RightTwoItem'][i][5]))
            buf += WriteUInt64(self['Buy_RightTwoItem'][i][6])
            buf += WriteInt16(self['Buy_RightTwoItem'][i][7])
            buf += WriteInt16(self['Buy_RightTwoItem'][i][8])
            buf += WriteUInt32(self['Buy_RightTwoItem'][i][9])
        buf += WriteInt16(self['ItemPage'])
        buf += WriteInt16(self['ItemPageMax'])
        buf += WriteInt16(self['sum'])
        return buf

    def filldatafromstream(self, buf):
        (self['max'], buf) = ReadInt(buf)
        for i in range(self['max']):
            self['Buy_RightTwoItem'].append([' ', 0, ' ', ' ', 0, ' ', 0, 0, 0, 0])
            (self['Buy_RightTwoItem'][i][0], buf) = ReadByte(buf)
            self['Buy_RightTwoItem'][i][0] = ord(self['Buy_RightTwoItem'][i][0])
            (self['Buy_RightTwoItem'][i][1], buf) = ReadUint(buf)
            (self['Buy_RightTwoItem'][i][2], buf) = ReadByte(buf)
            self['Buy_RightTwoItem'][i][2] = ord(self['Buy_RightTwoItem'][i][2])
            (self['Buy_RightTwoItem'][i][3], buf) = ReadByte(buf)
            self['Buy_RightTwoItem'][i][3] = ord(self['Buy_RightTwoItem'][i][3])
            (self['Buy_RightTwoItem'][i][4], buf) = ReadInt(buf)
            (self['Buy_RightTwoItem'][i][5], buf) = ReadByte(buf)
            self['Buy_RightTwoItem'][i][5] = ord(self['Buy_RightTwoItem'][i][5])
            (self['guid_H'], buf) = ReadInt32(buf)
            (self['guid_L'], buf) = ReadInt32(buf)
            self['Buy_RightTwoItem'][i][6] = MakeGUID(self['guid_L'], self['guid_H'])
            (self['Buy_RightTwoItem'][i][7], buf) = ReadInt(buf)
            (self['Buy_RightTwoItem'][i][8], buf) = ReadInt(buf)
            (self['Buy_RightTwoItem'][i][9], buf) = ReadUint(buf)
        (self['ItemPage'], buf) = ReadInt(buf)
        (self['ItemPageMax'], buf) = ReadInt(buf)
        (self['sum'], buf) = ReadInt(buf)
        return (self, buf)

    def handle(self):
        self.person['ItemPageMax'] = self['ItemPageMax']
        self.person['Buy_RightTwoItem'] = self['Buy_RightTwoItem']


# 购买商品
class PACKET_CG_BUY_CONSIGNSALEITEMINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self.sort = {
            'Equip': 0,
            'Gem': 1,
            'Pet': 2,
            'Other': 3,
            'All': 4
        }
        self.SortClass = {
            'Quality': 0,
            'Level': 1,
            'Count': 2,
            'Price': 3,
            'TableID': 4
        }
        self.SortType = {
            'UP': 0,
            'DOWN': 1
        }
        self['sort'] = 0
        self['subtype'] = 0
        # self['thirdtype'] = 0
        self['quality'] = 0
        self['sortclass'] = self.SortClass['Price']
        self['sorttype'] = self.SortType['UP']
        self['page'] = 1
        self['id'] = -1
        self['min'] = 0
        self['max'] = 0
        self['EquipFiltrateIndex'] = 9
        self['guid'] = 0
        self['count'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['sort'])
        buf += WriteInt32(self['subtype'])
        # buf += WriteInt32(self['thirdtype'])
        buf += WriteInt32(self['quality'])
        buf += WriteInt32(self['sortclass'])
        buf += WriteInt32(self['sorttype'])
        buf += WriteInt32(self['page'])
        if self['id'] > 0:
            buf += WriteInt32(self['id'])
        else:
            buf += WriteInt32(self['min'])
            buf += WriteInt32(self['max'])
        buf += WriteInt32(self['EquipFiltrateIndex'])
        buf += WriteInt64(self['guid'])
        buf += WriteInt32(self['count'])
        return buf

    def filldatafromstream(self, buf):
        (self['sort'], buf) = ReadInt32(buf)
        (self['subtype'], buf) = ReadInt32(buf)
        # (self['thirdtype'], buf) = ReadInt32(buf)
        (self['quality'], buf) = ReadInt32(buf)
        (self['sortclass'], buf) = ReadInt32(buf)
        (self['sorttype'], buf) = ReadInt32(buf)
        (self['page'], buf) = ReadInt32(buf)
        if self['id'] > 0:
            (self['id'], buf) = ReadInt32(buf)
        else:
            (self['min'], buf) = ReadInt32(buf)
            (self['max'], buf) = ReadInt32(buf)
        (self['EquipFiltrateIndex'], buf) = ReadInt32(buf)

        (self['guid_L'], buf) = ReadInt32(buf)
        (self['guid_H'], buf) = ReadInt32(buf)
        # print self['guid_L']
        # print self['guid_H']
        self['guid'] = MakeGUID(self['guid_L'], self['guid_H'])
        # (self['guid'], buf) = ReadInt64(buf)
        (self['count'], buf) = ReadInt32(buf)
        return (self, buf)


# 获取道具列表总数量
class PACKET_CG_ASK_CONSIGNSALEPRODUCTTYPESDATA(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['SearchClass'] = 0
        self['MainProductType'] = 0
        self['SubProductType'] = 0
        self['ProductType'] = 0
        self['minLevel'] = 0
        self['maxLevel'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['SearchClass'])
        buf += WriteInt32(self['MainProductType'])
        buf += WriteInt32(self['SubProductType'])
        buf += WriteInt32(self['ProductType'])
        buf += WriteInt32(self['minLevel'])
        buf += WriteInt32(self['maxLevel'])
        return buf

    def filldatafromstream(self, buf):
        (self['SearchClass'], buf) = ReadInt32(buf)
        (self['MainProductType'], buf) = ReadInt32(buf)
        (self['SubProductType'], buf) = ReadInt32(buf)
        (self['ProductType'], buf) = ReadInt32(buf)
        (self['minLevel'], buf) = ReadInt32(buf)
        (self['maxLevel'], buf) = ReadInt32(buf)
        return (self, buf)


# 返回道具列表总数量
class PACKET_GC_RET_CONSIGNSALEPRODUCTTYPESDATA(Packet):
    pass


# 兑换货币
class PACKET_CG_ASK_EXCHANGEMONEY(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['activeType'] = 1
        self['exchangeType'] = 0
        self['exchangeNum'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['activeType']))
        buf += WriteByte(chr(self['exchangeType']))
        buf += WriteInt32(self['exchangeNum'])
        return buf

    def filldatafromstream(self, buf):
        (self['activeType'], buf) = ReadByte(buf)
        self['activeType'] = ord(self['activeType'])
        (self['exchangeType'], buf) = ReadByte(buf)
        self['exchangeType'] = ord(self['exchangeType'])
        (self['exchangeNum'], buf) = ReadInt32(buf)
        return (self, buf)


# 元宝商城
class PACKET_CGYBShopBuy(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['TableId'] = 0
        self['BuyNum'] = 0
        self['Type'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['TableId'])
        buf += WriteInt32(self['BuyNum'])
        buf += WriteByte(chr(self['Type']))
        return buf

    def filldatafromstream(self, buf):
        (self['TableId'], buf) = ReadInt32(buf)
        (self['BuyNum'], buf) = ReadInt32(buf)
        (self['Type'], buf) = ReadByte(buf)
        self['Type'] = ord(self['Type'])
        return (self, buf)


class PACKET_GCYBShopBuy(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Result'] = 0
        self['BuyType'] = 0
        self['ItemId'] = 0
        self['BuyNum'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['Result']))
        buf += WriteByte(chr(self['BuyType']))
        buf += WriteInt32(self['ItemId'])
        buf += WriteInt32(self['BuyNum'])
        return buf

    def filldatafromstream(self, buf):
        (self['Result'], buf) = ReadByte(buf)
        self['Result'] = ord(self['Result'])
        (self['BuyType'], buf) = ReadByte(buf)
        self['BuyType'] = ord(self['BuyType'])
        (self['ItemId'], buf) = ReadInt32(buf)
        (self['BuyNum'], buf) = ReadInt32(buf)
        return (self, buf)


# luzhenyu added


class CGBankSwapItem(Packet):
    pass


class PACKET_GC_TEAMFOLLOW_ERROR(Packet):
    pass


class PACKET_GC_HIDDENWEAPONOPT(Packet):
    pass


class PACLET_GC_DIE(Packet):
    pass


class PACKET_CG_ANTAGONIST_REQ(Packet):
    pass


class PACKET_GC_STUDYXINFA(Packet):
    pass


class GCShopBuy(Packet):
    pass


class PACKET_GC_TARGET_LIST_AND_HIT_FLAGS(Packet):
    pass


class CGDailyPackInfo(Packet):
    pass


class PACKET_GC_TEAM_ASK_INVITE(Packet):
    pass


class PACKET_GC_REMOVEPET(Packet):
    pass


class PACKET_GC_LEVELUPRESULT(Packet):
    pass


class PACKET_CG_TEAM_RET_INVITE(Packet):
    pass


class PACKET_GC_CHAR_BUFF(Packet):
    pass


class PACKET_CG_PICKITEMBOX(Packet):
    pass


class PACKET_CG_RET_TEAMFOLLOW_RESULT(Packet):
    pass


class PACKET_GC_NEWPET_SKILLCHANNEL(Packet):
    pass


class CGShopBuy(Packet):
    pass


class PACKET_CG_ASKDETAILEQUIPLIST(Packet):
    pass


class PACKET_GC_TEAM_LEADER_ASK_INVITE(Packet):
    pass


class PACKET_CG_ACHIEVEMENT(Packet):
    pass


class PACKET_GC_CHANGEDIRECTION(Packet):
    pass


class PACKET_CG_PETPROCREATEREGISTERUI(Packet):
    pass


class PACKET_CG_GUILD_ASKMEMBERINFO(Packet):
    pass


class PACKET_CG_TEAM_LEADER_RET_INVITE(Packet):
    pass


class PACKET_GC_NEWPLAYER_DEATH(Packet):
    pass


class PACKET_CG_CITYASKATTR(Packet):
    pass


class PACKET_CL_AskDeleteChar(Packet):
    pass


class PACKET_GC_GMCHAT(Packet):
    pass


class PACKET_CG_ASKMYBAGSIZECHANGE(Packet):
    pass


class GCResponseCarryStore(Packet):
    pass


class CGAskItemInfo(Packet):
    pass


class CGBankAcquireList(Packet):
    pass


class PACKET_GC_OPERATE_RESULT(Packet):
    pass


class PACKET_GC_CHAR_STOPACTION(Packet):
    pass


class PACKET_GC_CHARSKILL_GATHER(Packet):
    pass


class PACKET_GC_DETAILSKILLLIST(Packet):
    pass


class PACKET_GC_NEWSPECIAL(Packet):
    pass


class PACKET_CG_RELATION(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['type'] = 0
        self['m_From'] = 0        
        self['m_TargetGUIDLow'] = -1
        self['m_TargetGUIDHigh'] = -1
        self['m_TargetWorldID'] = -1
        self['m_NameSize'] = ''
        self['name'] = ''
        self['m_RelationType'] = ''
        self['m_Group'] = ''
        self['m_uMoodSize'] = ''        
        self['m_szMood'] = ''        
        self['m_Count'] = '' 
        self['m_GUIDList64'] = []                
        self['m_Sign'] = ''
        self['m_TeamId'] = 0
        self['m_ActivityId'] = 0        
        
                        
        self.type_dic = {                           
                           'REQ_NONE':0, \
                           'REQ_RELATIONLIST':1, \
                           'REQ_RELATIONINFO':2, \
                           'REQ_VIEWPLAYER':3, \
                           'REQ_ADDFRIEND':4, \
                           'REQ_ADDTOBLACKLIST':5, \
                           'REQ_TEMPFRIEND_TO_FRIEND':6, \
                           'REQ_TEMPFRIEND_ADDTO_BLACKLIST':7, \
                           'REQ_TRANSITION':8, \
                           'REQ_DELFRIEND':9, \
                           'REQ_DELFROMBLACKLIST':10, \
                           'REQ_NEWGOODFRIEND':11, \
                           'REQ_RELATIONONLINE':12, \
                           'REQ_MODIFYMOOD':13, \
                           'REQ_MODIFYSETTINGS':14, \
                           'REQ_NOTIFY_ADDTEMPFRIEND':15, \
                           'REQ_NOTIFY_MARRY':16, \
                           'REQ_DRAW_SWEAR':17, \
                           'REQ_CHANGE_SWEAR':18, \
                           'REQ_CHANGE_PERSONAL_SWEAR':19, \
                           'REQ_CHANGE_USERNAME':20, \
                           'REQ_CHANGE_GUILDNAME':21, \
                           'REQ_ADDENEMY':22, \
                           'REQ_DELENEMY':23, \
                           'REQ_ENEMY_TRANSTO_FRIEND':24, \
                           'REQ_ADDTRUSTFRIEND':25, \
                           'REQ_DELTRUSTFRIEND':26, \
                           'REQ_MODIFYGROUPINGNAME':27, \
                           'REQ_CHANGENAME':28, \
                           'REQ_ADDTOFOE':29, \
                           'REQ_ADDINHIBIT':30, \
                           'REQ_DELFOE':31, \
                           'REQ_FOELISTINHIBIT':32, \
                           'REQ_ADDBGFRIEND':33, \
                           'REQ_RELATIONOFFLINE':34, \
                           'REQ_RELATIONBEONLINE':35, \
                           'REQ_FEIXINUIDCHANGE':36, \
                           'REQ_FEIXINUID':37, \
                           'REQ_SGM_CHANGE_USERNAME':38, \
                           'REQ_MODIFY_REMARK':39, \
                           'REQ_REFRESHFOETITLE':40, \
                           'REQ_ADDFRIEND_BATCH':42, \
                           'REQ_ADDFRIEDNBYPROPELLINE':43\
                           }

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['type'])
        buf += WriteInt32(self['m_From'])        
        if self['type'] == self.type_dic['REQ_RELATIONLIST']:
            pass
        
        if self['type'] == self.type_dic['REQ_RELATIONINFO']:        
            buf += WriteInt32(self['m_TargetGUIDLow'])
            buf += WriteInt32(self['m_TargetGUIDHigh'])
            buf += WriteByte(self['m_NameSize'])
            buf += WriteCharArray(self['name'], self['m_NameSize'], False)            
            buf += WriteInt16(self['m_TargetWorldID'])         
        
        if self['type'] == self.type_dic['REQ_VIEWPLAYER'] or self['type'] == self.type_dic['REQ_NOTIFY_ADDTEMPFRIEND']:
#        if self['type'] == self.type_dic['REQ_NOTIFY_ADDTEMPFRIEND']:         
            buf += WriteByte(self['m_NameSize'])                  
            buf += WriteInt16(self['m_TargetWorldID'])         
            buf += WriteCharArray(self['name'], self['m_NameSize'], True)                     
            buf += WriteByte(self['m_Sign'])
        
        if self['type'] == self.type_dic['REQ_DELFROMBLACKLIST'] or self['type'] == self.type_dic['REQ_DELENEMY']:
#        if self['type'] == self.type_dic['REQ_DELENEMY']:            
            buf += WriteInt32(self['m_TargetGUIDLow'])
            buf += WriteInt32(self['m_TargetGUIDHigh'])            
            buf += WriteInt16(self['m_TargetWorldID'])             
        
        if self['type'] == self.type_dic['REQ_ADDFRIEND'] or self['type'] == self.type_dic['REQ_TEMPFRIEND_TO_FRIEND'] or self.type_dic['REQ_ENEMY_TRANSTO_FRIEND']:            
#        if self['type'] == self.type_dic['REQ_TEMPFRIEND_TO_FRIEND']:                         
#        if self['type'] == self.type_dic['REQ_ENEMY_TRANSTO_FRIEND']:
            buf += WriteInt32(self['m_TargetGUIDLow'])
            buf += WriteInt32(self['m_TargetGUIDHigh'])            
            buf += WriteInt16(self['m_TargetWorldID'])            
            buf += WriteByte(self['m_NameSize'])             
            buf += WriteCharArray(self['name'], self['m_NameSize'], False)            
            buf += WriteByte(self['m_RelationType'])            
            buf += WriteByte(self['m_Group'])  
        
        if self['type'] == self.type_dic['REQ_ADDTOBLACKLIST'] or self['type'] == self.type_dic['REQ_TEMPFRIEND_ADDTO_BLACKLIST']:                         
#        if self['type'] == self.type_dic['REQ_TEMPFRIEND_ADDTO_BLACKLIST']:            
            buf += WriteInt32(self['m_TargetGUIDLow'])
            buf += WriteInt32(self['m_TargetGUIDHigh'])            
            buf += WriteInt16(self['m_TargetWorldID'])            
            buf += WriteByte(self['m_NameSize'])             
            buf += WriteCharArray(self['name'], self['m_NameSize'], False)            
            buf += WriteByte(self['m_RelationType'])             
        if self['type'] == self.type_dic['REQ_ADDENEMY']:                         
            buf += WriteInt32(self['m_TargetGUIDLow'])
            buf += WriteInt32(self['m_TargetGUIDHigh'])            
            buf += WriteInt16(self['m_TargetWorldID']) 
        if self['type'] == self.type_dic['REQ_TRANSITION']:            
            buf += WriteInt32(self['m_TargetGUIDLow'])
            buf += WriteInt32(self['m_TargetGUIDHigh'])              
            buf += WriteInt16(self['m_TargetWorldID'])            
            buf += WriteByte(self['m_RelationType'])            
            buf += WriteByte(self['m_Group']) 
        if self['type'] == self.type_dic['REQ_MODIFYMOOD']: 
            buf += WriteByte(self['m_uMoodSize'])            
            buf += WriteCharArray(self['m_szMood'], self['m_uMoodSize'], True)             
        if self['type'] == self.type_dic['REQ_ADDTRUSTFRIEND'] or self['type'] == self.type_dic['REQ_DELTRUSTFRIEND']:            
#        if self['type'] == self.type_dic['REQ_DELTRUSTFRIEND']:                                   
            buf += WriteInt32(self['m_TargetGUIDLow'])
            buf += WriteInt32(self['m_TargetGUIDHigh'])              
            buf += WriteInt16(self['m_TargetWorldID'])            
        if self['type'] == self.type_dic['REQ_ADDFRIEND_BATCH']:
            for i in range(0, self['m_Count']):
                buf += WriteByte(chr(self['m_GUIDList64'][i]))    
        if self['type'] == self.type_dic['REQ_ADDFRIEDNBYPROPELLINE']:
            for i in range(0, self['m_Count']):                 
                buf += WriteByte(self['m_Group'])                 
                buf += WriteInt32(self['m_TargetGUIDLow'])
                buf += WriteInt32(self['m_TargetGUIDHigh'])              
                buf += WriteInt16(self['m_TargetWorldID'])                 
                buf += WriteByte(self['m_NameSize'])             
                buf += WriteCharArray(self['name'], self['m_NameSize'], False) 
                buf += WriteByte(self['m_RelationType'])                 
                buf += WriteInt32(self['m_TeamId']) 
                buf += WriteInt32(self['m_ActivityId'])                                                        
        return buf

    def filldatafromstream(self, buf):
        (self['type'], buf) = ReadByte(buf)
        self['type'] = ord(self['type'])
        (self['m_From'], buf) = ReadInt32(buf)
                
        if self['type'] == self.type_dic['REQ_RELATIONLIST']:
            pass
        
        if self['type'] == self.type_dic['REQ_RELATIONINFO']:
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)       
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf)       
            (self['m_NameSize'], buf) = ReadByte(buf)
            self['m_NameSize'] = ord(self['m_NameSize'])                       
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)          
            (self['name'], buf) = ReadCharArray(buf, self['m_NameSize'], False)
            
        if self['type'] == self.type_dic['REQ_VIEWPLAYER'] or self['type'] == self.type_dic['REQ_NOTIFY_ADDTEMPFRIEND']:               
            (self['m_NameSize'], buf) = ReadByte(buf)
            self['m_NameSize'] = ord(self['m_NameSize'])          
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)          
            (self['name'], buf) = ReadCharArray(buf, self['m_NameSize'], True)        
            (self['m_Sign'], buf) = ReadByte(buf)
            self['m_Sign'] = ord(self['m_Sign'])   
                   
        if self['type'] == self.type_dic['REQ_DELFROMBLACKLIST'] or self['type'] == self.type_dic['REQ_DELENEMY']:           
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)       
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf) 
            (self['m_TargetWorldID'], buf) = ReadInt16(buf) 
                       
        if self['type'] == self.type_dic['REQ_DELFRIEND']: 
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)       
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf) 
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)   
                      
        if self['type'] == self.type_dic['REQ_ADDFRIEND'] or self['type'] == self.type_dic['REQ_TEMPFRIEND_TO_FRIEND'] or self['type'] == self.type_dic['REQ_ENEMY_TRANSTO_FRIEND']:                                   
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)       
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf)
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)  
            (self['m_NameSize'], buf) = ReadByte(buf)
            self['m_NameSize'] = ord(self['m_NameSize'])              
            (self['name'], buf) = ReadCharArray(buf, self['m_NameSize'], False)            
            (self['m_RelationType'], buf) = ReadByte(buf)
            self['m_RelationType'] = ord(self['m_RelationType'])              
            (self['m_Group'], buf) = ReadByte(buf)
            self['m_Group'] = ord(self['m_Group'])  
                        
        if self['type'] == self.type_dic['REQ_ADDTOBLACKLIST'] or self['type'] == self.type_dic['REQ_TEMPFRIEND_ADDTO_BLACKLIST']:                          
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)        
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf)
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)
            (self['m_NameSize'], buf) = ReadByte(buf)
            self['m_NameSize'] = ord(self['m_NameSize'])              
            (self['name'], buf) = ReadCharArray(buf, self['m_NameSize'], False)            
            (self['m_RelationType'], buf) = ReadByte(buf)
            self['m_RelationType'] = ord(self['m_RelationType'])  
                        
        if self['type'] == self.type_dic['REQ_ADDENEMY']: 
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)     
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf)
            (self['m_TargetWorldID'], buf) = ReadInt16(buf) 
                      
        if self['type'] == self.type_dic['REQ_TRANSITION']:             
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)       
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf)
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)
            (self['m_RelationType'], buf) = ReadByte(buf)
            self['m_RelationType'] = ord(self['m_RelationType'])             
            (self['m_Group'], buf) = ReadByte(buf)
            self['m_Group'] = ord(self['m_Group'])    
                     
        if self['type'] == self.type_dic['REQ_MODIFYMOOD']:             
            (self['m_uMoodSize'], buf) = ReadByte(buf)
            self['m_uMoodSize'] = ord(self['m_szMood'])             
            (self['name'], buf) = ReadCharArray(buf, self['m_szMood'], True)            

        if self['type'] == self.type_dic['REQ_ADDTRUSTFRIEND'] or self['type'] == self.type_dic['REQ_DELTRUSTFRIEND']:                                     
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)       
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf)
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)

        if self['type'] == self.type_dic['REQ_ADDFRIEND_BATCH']:             
            (self['m_Count'], buf) = ReadByte(buf)
            self['m_Count'] = ord(self['m_Count'])            
            for i in range(0,self['m_Count']):            
                temp = 0
                (temp, buf) = ReadInt32(buf)
                self['m_GUIDList64'].m_LGuid.append(temp)
                self['m_GUIDList64'].m_HGuid.append(temp)
                
        if self['type'] == self.type_dic['REQ_ADDFRIEDNBYPROPELLINE']: 
            (self['m_Group'], buf) = ReadByte(buf)
            self['m_Group'] = ord(self['m_Group'])   
            (self['m_TargetGUIDLow'], buf) = ReadInt32(buf)      
            (self['m_TargetGUIDHigh'], buf) = ReadInt32(buf)
            (self['m_TargetWorldID'], buf) = ReadInt16(buf)           
            (self['m_NameSize'], buf) = ReadByte(buf)
            self['m_NameSize'] = ord(self['m_NameSize'])             
            (self['name'], buf) = ReadCharArray(buf, self['m_NameSize'], False)            
            (self['m_RelationType'], buf) = ReadByte(buf)
            self['m_RelationType'] = ord(self['m_RelationType'])             
            (self['m_TeamId'], buf) = ReadInt32(buf)                                        
            (self['m_ActivityId'], buf) = ReadInt32(buf)                                                
        return (self, buf)




class PAKCET_CG_CHAR_STOP_LOGIC(Packet):
    pass


class PACKET_GC_NTP(Packet):
    pass


class PACKET_GC_CHAR_DETAIL_BUFF(Packet):
    pass


class GUID64_t(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_HGuid'] = 0
        self['m_LGuid'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['m_LGuid'])
        buf += WriteInt32(self['m_HGuid'])
        return buf

    def filldatafromstream(self, buf):
        (self['m_LGuid'], buf) = ReadInt32(buf)
        (self['m_HGuid'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_CG_GUILD_JOIN(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GuildID'] = 0
        self['m_FromType'] = 0
        self['m_guid'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['m_GuildID'])
        buf += WriteByte(chr(self['m_FromType']))

        (low, high) = DecodeUInt64(self['m_guid'])
        buf += WriteInt32(low)
        buf += WriteInt32(high)
        return buf

    def filldatafromstream(self, buf):
        (self['m_GuildID'], buf) = ReadInt16(buf)
        (self['m_FromType'], buf) = ReadByte(buf)
        self['m_FromType'] = ord(self['m_FromType'])

        (low, buf) = ReadInt32(buf)
        (high, buf) = ReadInt32(buf)
        self['m_guid'] = EncodeUInt64(high, low)

        return (self, buf)


class PACKET_CG_PACKUP_PACKET(Packet):
    pass


class PACKET_GC_GUILD_LIST(Packet):
    pass


class PACKET_CG_CHARASKDETAILATTRIB(Packet):
    pass


class PACKET_CG_ASKMYBAGLIST(Packet):
    pass


class PACKET_GC_PACKUP_PACKET(Packet):
    pass


class CGTitleList(Packet):
    pass


class PACKET_CG_USEITEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_BagIndex'] = 1
        self['m_BagTableIndex'] = 0
        self['m_BagGUID'] = 0
        self['m_UseNum'] = 0
        self['m_TargetObj'] = 0
        self['m_TargetPos.x'] = 0
        self['m_TargetPos.z'] = 0
        self['m_Dir'] = 0
        self['m_TargetPetGUID'] = 0
        self['m_TargetItemIndex'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['m_BagIndex']))
        buf += WriteInt32(self['m_BagTableIndex'])

        (low, high) = DecodeUInt64(self['m_BagGUID'])

        buf += WriteInt32(high)
        buf += WriteInt32(low)

        buf += WriteByte(chr(self['m_UseNum']))
        buf += WriteInt32(self['m_TargetObj'])
        buf += WriteSingle(self['m_TargetPos.x'])
        buf += WriteSingle(self['m_TargetPos.z'])
        buf += WriteSingle(self['m_Dir'])
        buf += WriteUInt64(self['m_TargetPetGUID'])
        buf += WriteByte(chr(self['m_TargetItemIndex']))
        return buf

    def filldatafromstream(self, buf):
        (self['m_BagIndex'], buf) = ReadByte(buf)
        self['m_BagIndex'] = ord(self['m_BagIndex'])

        (self['m_BagTableIndex'], buf) = ReadInt32(buf)
        (self['m_BagGUID'], buf) = ReadUInt64(buf)
        (self['m_UseNum'], buf) = ReadByte(buf)
        self['m_UseNum'] = ord(self['m_UseNum'])

        (self['m_TargetObj'], buf) = ReadInt32(buf)
        (self['m_TargetPos.x'], buf) = ReadSingle(buf)
        (self['m_TargetPos.z'], buf) = ReadSingle(buf)
        (self['m_Dir'], buf) = ReadSingle(buf)
        (self['m_TargetPetGUID'], buf) = ReadUInt64(buf)
        (self['m_TargetItemIndex'], buf) = ReadByte(buf)

        self['m_TargetItemIndex'] = ord(self['m_TargetItemIndex'])

        return (self, buf)


class GCBankRemoveItem(Packet):
    pass


class PACKET_GC_RIDEBAGINFO(Packet):
    pass


class PACKET_GC_ASKDETAILXIULIAN(Packet):
    pass


class PACKET_GC_RIDEBAGMOVEITEMRESULT(Packet):
    pass


class PACKET_CG_PACKAGE_SWAPITEM(Packet):
    pass


class CGBankRemoveItem(Packet):
    pass


class PACKET_GC_CHARDETAILATTRIB(Packet):
    pass


class PACKET_GC_NEWPET_MOVE(Packet):
    pass


class PACKET_GC_NEWPLAYER_SKILLCHANNEL(Packet):
    pass


class PACKET_GC_ADDSKILL(Packet):
    pass


class PACKET_GC_CHAR_DOACTION(Packet):
    pass


class PACKET_GC_PETPOSSBUFINFO(Packet):
    pass


class PACKET_GC_MISSIONLIST(Packet):
    pass


class PACKET_GC_MISSIONREMOVE(Packet):
    pass


class GCBankSwapItem(Packet):
    pass


class PACKET_GC_PACKAGE_SWAPITEM(Packet):
    pass


class PACKET_CG_STOP_TEAMFOLLOW(Packet):
    pass


class GCBagList(Packet):
    pass


class PACKET_GC_CHARBASEATTRIB(Packet):
    pass


class PACKET_GC_CHARSKILL_SEND(Packet):
    pass


class PACKET_CG_TEAM_KICK(Packet):
    pass


class PACKET_CG_FINGER(Packet):
    pass


class PACKET_GC_PICKRESULT(Packet):
    pass


class PACKET_GC_NEWITEMBOX(Packet):
    pass


class PACKET_CG_CHANGE_PK_MODE_REQ(Packet):
    pass


class PACKET_CG_ASKDETAILSKILLLIST(Packet):
    pass


class PACKET_GC_FINGER(Packet):
    pass


class GCDailyPackInfo(Packet):
    pass


class PACKET_LC_RetDeleteChar(Packet):
    pass


class PACKET_CG_USE_GEM(Packet):
    pass


class PACKET_CG_MISSIONHAVEDONEFLAG(Packet):
    pass


class PACKET_GC_HeartBeat(Packet):
    pass


'''
class CGReceiveRedPacket(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_PacketType'] = 1
        self['m_Serial'] = 0
        self['m_2'] = 0
        self['m_3'] = 0
        self['m_Guid'] = 0


    def getdatastream(self):
        buf = ''
        buf += WriteByte(33)
        buf += WriteUInt32(0)
        buf += WriteInt32(0)
        buf += WriteInt32(0)
        (low,high) = DecodeUInt64(self['m_Guid'])
        buf += WriteInt32(low)
        buf += WriteInt32(high)
        return buf

    def filldatafromstream(self, buf):
        (self['m_PacketType'],buf) = ReadByte(buf)
        self['m_PacketType'] = ord(self['m_PacketType'])
        (self['m_Serial'],buf) = ReadUInt32(buf)
        (self['m_2'],buf) = ReadInt32(buf)
        (self['m_3'],buf) = ReadInt32(buf)
        (low,buf) = ReadInt32(buf)
        (high,buf) = ReadInt32(buf)
        self['m_Guid'] = EncodeUInt64(high, low)

        return (self,buf)
'''


class PACKET_GC_SETCURPOINT(Packet):
    pass


class PACKET_CG_GMCHAT(Packet):
    pass


class PACKET_GC_UNEQUIPRESULT(Packet):
    pass


class PACKET_GC_OTHER_ASK_TEAMFOLLOW(Packet):
    pass


class CGShopSell(Packet):
    pass


class PACKET_GC_ARRIVE(Packet):
    pass


class PACKET_GC_CITYATTR(Packet):
    pass


class PACKET_GC_NEWMONSTER_SKILLCHANNEL(Packet):
    pass


class PACKET_CG_SET_PETATTRIB(Packet):
    pass


class PACKET_GC_UPDATE_ACHIEVEMENT(Packet):
    pass


class PACKET_GC_MANIPULATEPETRET(Packet):
    pass


class PACKET_CG_NTP(Packet):
    pass


class PACKET_CG_ASKSETTING(Packet):
    pass


class PACKET_GC_TEAM_MEMBER_INFO(Packet):
    pass


class PACKET_GC_CHARMODIFYACTION(Packet):
    pass


class GCCharSkillConditionCheckInvalid(Packet):
    pass


class PACKET_GC_CHARSKILL_DEPLETE_REFIX(Packet):
    pass


class PACKET_GC_CHARSKILL_LEAD(Packet):
    pass


class PACKET_CG_OPENITEMBOX(Packet):
    pass


class PACKET_GC_USEITEMRESULT(Packet):
    pass


class PACKET_GC_GUILD_AUTHORITY(Packet):
    pass


class PACKET_CG_ASKDETAILXIULIAN(Packet):
    pass


class PACKET_GC_COOLDOWN_UPDATE(Packet):
    pass


class PACKET_GC_NEWMONSTER_DEATH(Packet):
    pass


class PACKET_GC_RETCAMPAIGNCOUNT(Packet):
    pass


class PACKET_GC_NETCHECK(Packet):
    pass


class PACKET_GC_DETAILATTRIB_PET(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_uPetGuid'] = 0

    def getdatastream(self):
        buf = ''

        (low, high) = DecodeUInt64(self['m_GUID'])

        return buf

    def filldatafromstream(self, buf):
        (G_L, buf) = ReadInt32(buf)
        (G_H, buf) = ReadInt32(buf)
        self['m_uPetGuid'] = EncodeUInt64(G_H, G_L)

        return (self, buf)

    def handle(self):
        self.person['m_uPetGuid'] = self['m_uPetGuid']

        pass


class PACKET_GC_DELALLOBJ(Packet):
    pass


class PACKET_CG_MAIL_DEL_OR_BACK(Packet):
    pass


class PACKET_GC_LEVELUP(Packet):
    pass


class CGGMCommand(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['msg'] = u""

    def getdatastream(self):
        buf = ''
        length = GetStringBytesLen(self['msg'], True)
        buf += WriteByte(chr(length))
        buf += WriteCharArray(self['msg'], length, True)
        return buf

    def filldatafromstream(self, buf):
        (length, buf) = ReadByte(buf)
        length = ord(length)

        (self['msg'], buf) = ReadCharArray(buf, length, True)
        return (self, buf)


class PACKET_GC_BOXITEMLIST(Packet):
    pass


class PACKET_CG_ASKRIDEBAGINFO(Packet):
    pass


class PACKET_GC_CHARSKILL_MISSED(Packet):
    pass


class PACKET_GC_GUILD_APPLY(Packet):
    pass


class PACKET_CG_ASKMISSIONLIST(Packet):
    pass


class PACKET_GC_ITEMINFO(Packet):
    pass


class PACKET_CG_ASKSETCURPOINT(Packet):
    pass


class PACKET_CL_AskQuitQuene(Packet):
    pass


class PACKET_GC_ASK_SERVER_TIME(Packet):
    pass


class PACKET_CG_TEAM_DISSMISS(Packet):
    pass


class PACKET_GC_CHAR_DIRECT_IMPACT(Packet):
    pass


class PACKET_CG_ASK_GEM_CONTAINER(Packet):
    pass


class PACKET_GC_BAGSIZECHANGE(Packet):
    pass


class PACKET_GC_DETAIL_IMPACT_LIST_UPDATE(Packet):
    pass


class PACKET_GC_UICOMMAND(Packet):
    pass


class PACKET_GC_GUILD_ERROR(Packet):
    pass


class GCBankAddItem(Packet):
    pass


class GCTitleList(Packet):
    pass


class PACKET_GC_DETAILEQUIPLIST(Packet):
    pass


class PACKET_GC_RELATION(Packet):
    pass


class PACKET_GC_RET_MAIL_NEW(Packet):
    pass


class PACKET_GC_GUILD_RETURN(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['msa'] = GUILD_RETURN(person)

    def filldatafromstream(self, buf):
        (self['msa'], buf) = self['msa'].filldatafromstream(buf)
        return (self, buf)

    def handle(self):
        if hasattr(self['msa'], "handle"):
            self['msa'].handle()


guildreturn = {27: "BACK_CITY_BYGUID", 34: "MEMBER_LOGOFF", 14: "FOUND", 25: "DELETE_LUOYANGCITY",
               22: "SETLEAVEWORD", 12: "LEAVE", 19: "CITY_CREATE", 29: "CREATE_RED_PACKET", 4: "DEMOTE",
               24: "BATTLE_GUILDS", 26: "FIRSTMAN", 0: "CREATE", 15: "DISMISS", 23: "MODLEAVEWORD",
               18: "BACK_CITY", 3: "PROMOTE", 21: "NOTIFY", 33: "XUETU2MEMBER", 7: "RECRUIT", -1: "INVALID",
               9: "DEMISE", 32: "JOIN_XUETU_BRODCAST", 16: "CHANGEDESC", 1: "RESPONSE", 5: "AUTHORIZE",
               31: "QUICK_JOIN", 28: "FEED_BACK", 2: "JOIN", 17: "NAME", 8: "EXPEL", 30: "XUETU_JOIN_RETURN",
               6: "DEPRIVE_AUTHORITY", 10: "WITHDRAW", 13: "REJECT", 20: "CITY_DESTORY", 11: "DEPOSIT"}


def read_GUID64_t(buf):
    (G_L, buf) = ReadInt32(buf)
    (G_H, buf) = ReadInt32(buf)
    guid = EncodeUInt64(G_H, G_L)
    return (guid, buf)


def write_GUID64_t(guid):
    buf = ''
    (low, high) = DecodeUInt64(guid)
    buf += WriteInt32(low)
    buf += WriteInt32(high)
    return buf


class GUILD_RETURN(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['returnType'] = 0
        self['m_Serial'] = 0
        self['m_GuildID'] = 0

    def filldatafromstream(self, buf):
        (self['returnType'], buf) = ReadByte(buf)
        self['returnType'] = ord(self['returnType'])

        try:
            name = guildreturn[self['returnType']]
            if name == 'CREATE' or name == 'JOIN' or name == 'XUETU_JOIN_RETURN':
                (self['m_Serial'], buf) = ReadUint(buf)
                (self['m_GuildID'], buf) = ReadInt16(buf)
                (self['m_GuildNameSize'], buf) = ReadByte(buf)
                self['m_GuildNameSize'] = ord(self['m_GuildNameSize'])

                (self['m_GuildName']) = ReadCharArray(buf, self['m_GuildNameSize'], True)
                (self['m_FromType'], buf) = ReadByte(buf)
                self['m_FromType'] = ord(self['m_FromType'])
            elif name == 'RECRUIT':
                (self['m_Serial'], buf) = ReadUint(buf)
                (self['m_GuildID'], buf) = ReadInt16(buf)
                (self['m_GUID'], buf) = read_GUID64_t(buf)
                (self['m_GUIDChanged'], buf) = read_GUID64_t(buf)
                (self['m_SourNameSize'], buf) = ReadByte(buf)
                self['m_SourNameSize'] = ord(self['m_SourNameSize'])
                (self['m_DestNameSize'], buf) = ReadByte(buf)
                self['m_DestNameSize'] = ord(self['m_DestNameSize'])
                (self['m_GuildNameSize'], buf) = ReadByte(buf)
                self['m_GuildNameSize'] = ord(self['m_GuildNameSize'])
                (self['m_PositionNameSize'], buf) = ReadByte(buf)
                self['m_PositionNameSize'] = ord(self['m_PositionNameSize'])
                (self['m_JoinTime'], buf) = ReadInt(buf)
                (self['m_IsOnLine'], buf) = ReadByte(buf)
                self['m_IsOnLine'] = ord(self['m_IsOnLine'])
                (self['m_SourName'], buf) = ReadCharArray(buf, self['m_SourNameSize'], True)
                (self['m_DestName'], buf) = ReadCharArray(buf, self['m_DestNameSize'], True)
                (self['m_GuildName'], buf) = ReadCharArray(buf, self['m_GuildNameSize'], True)
                (self['m_PositionName'], buf) = ReadCharArray(buf, self['m_PositionNameSize'], True)
        except:
            if self.person.getloadflag() is False:
                print "name:", name
        return (self, buf)

    def handle(self):
        if self['m_Serial'] != 0:
            self.person['m_Serial'] = self['m_Serial']


class PACKET_CG_UNEQUIP(Packet):
    pass


class PACKET_GC_OBJ_TELEPORT(Packet):
    pass


class PACKET_GC_CHAR_IMPACT_LIST_UPDATE(Packet):
    pass


class PACKET_GC_MISSIONADD(Packet):
    pass


class PACKET_CG_GET_MAIL_APPEND(Packet):
    pass


class PACKET_GC_NEWPET(Packet):
    pass


class PACKET_GC_BankAcquireList(Packet):
    pass


class PACKET_MAX(Packet):
    pass


class CGTitleOperate(Packet):
    pass


class PACKET_CG_HIDDENWEAPONOPT(Packet):
    pass


class GCShopSell(Packet):
    pass


class PACKET_GC_CHARMOVERESULT(Packet):
    pass


class PACKET_CG_TEAMLEADER_ASK_TEAMFOLLOW(Packet):
    pass


class PACKET_GC_SPECIAL_OBJ_FADE_OUT(Packet):
    pass


class PACKET_CG_TRANSPORT(Packet):
    pass


class PACKET_GC_TEAM_ERROR(Packet):
    pass


class PACKET_GC_SPECIAL_OBJ_ACTIVE(Packet):
    pass


class PACKET_GC_GEM_CONTAINER(Packet):
    pass


class PACKET_GC_CHAR_CHARGE(Packet):
    pass


class CGBankAddItem(Packet):
    pass


class PACKET_GC_RET_MAIL_NEW_OPT(Packet):
    pass


class PACKET_GC_HEROTRIALSSWEEPS(Packet):
    pass


class PACKET_CG_ASK_DAHUNLUAN(Packet):
    pass


class PACKET_GC_DAHUNLUAN_SCORE(Packet):
    pass


class PACKET_GC_DAHUNLUAN_ENTER(Packet):
    pass


class PACKET_CG_GODWEAPONUPGRADE(Packet):
    pass


class PACKET_GC_GODWEAPONUPGRADERESULT(Packet):
    pass


class PACKET_CG_ASKMONTHLYSIGNLIST(Packet):
    pass


class PACKET_GC_MONTHLYSIGNLIST(Packet):
    pass


class PACKET_CG_SIGNORRESIGN(Packet):
    pass


class PACKET_GC_SIGNORRESIGNRESULT(Packet):
    pass


class PACKET_CG_MYSTICALWEAPON_SKILL_ACTIVED(Packet):
    pass


class PACKET_GC_MYSTICALWEAPON_SKILL_ACTIVED_RESULT(Packet):
    pass


class PACKET_CG_CHANGESCENEBYMAP(Packet):
    pass


class PACKET_CG_MISSION_GUIDE_END(Packet):
    pass


class PACKET_CG_GODWEAPONCAST(Packet):
    pass


class PACKET_GC_GODWEAPONCASTRESULT(Packet):
    pass


class PACKET_CG_SHIMEN_ASKHELP(Packet):
    pass


class PACKET_CG_SHIMEN_HELP_LIST(Packet):
    pass


class PACKET_GC_SHIMEN_ASK_HELP(Packet):
    pass


class PACKET_CG_MISSION_DELIVERY(Packet):
    pass


class PACKET_GC_RIDE_OVERTIMELISTINFO(Packet):
    pass


class PACKET_CGW_TEAM_UPDATE_NUM(Packet):
    pass


class PACKET_CG_MISSIONREWARD(Packet):
    pass


class PACKET_CG_EQUIPSLOTENHANCE(Packet):
    pass


class PACKET_GC_EQUIPSLOTINFO(Packet):
    pass


class PACKET_CG_ASKEQUIPSLOTINFO(Packet):
    pass


class PACKET_CG_UPDATELIVINGSKILL(Packet):
    pass


class PACKET_GC_UPDATELIVINGSKILL(Packet):
    pass


class PACKET_CG_USELIVINGSKILL(Packet):
    pass


class PACKET_GC_USELIVINGSKILL(Packet):
    pass


class PACKET_CG_CHATVOICE(Packet):
    pass


class PACKET_GC_CHATVOICE(Packet):
    pass


class PACKET_GC_GEM_OPERATE_RESULT(Packet):
    pass


class PACKET_CG_ASKPETTUJIANINFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['index'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['index'])
        return buf

    def filldatafromstream(self, buf):
        (self['index'], buf) = ReadInt32(buf)
        return (self, buf)


class PACKET_GC_RETASKPETTUJIANINFO(Packet):
    pass


class PACKET_CG_CHATVOICETOSTR(Packet):
    pass


class PACKET_GC_CHATVOICETOSTR(Packet):
    pass


class PACKET_CG_CITYLOCATION(Packet):
    pass


class CGAskExpandBank(Packet):
    pass


class GCRetExpandBank(Packet):
    pass


class PACKET_CG_HEROCARD_INFO(Packet):
    pass


class PACKET_GC_HEROCARD_INFO(Packet):
    pass


class PACKET_CG_ACTIVE_HERO(Packet):
    pass


class PACKET_GC_MATERIAL_LIST(Packet):
    pass


class PACKET_CG_HERO_LEVELUP(Packet):
    pass


class PACKET_CG_ASKDRAWCARDINITDATA(Packet):
    pass


class PACKET_GC_RETDRAWCARDINITDATA(Packet):
    pass


class PACKET_CG_ASKDRAWCARD(Packet):
    pass


class PACKET_GC_RETDRAWCARD(Packet):
    pass


class PACKET_CG_CHARJUMPFLY(Packet):
    pass


class PACKET_GC_CHARJUMPFLY(Packet):
    pass


class PACKET_LC_RETNOTICE(Packet):
    pass


class PACKET_CL_ASKNOTICE(Packet):
    pass


class CGRequestCarryStore(Packet):
    pass


class PACKET_GC_ASKEXAMBASEDATA(Packet):
    pass


class PACKET_CG_EXAMANSWERQUESTION(Packet):
    pass


class PACKET_GC_EXAMANSWERQUSERIONRESULT(Packet):
    pass


class PACKET_GC_EXAMTOPDATA(Packet):
    pass


class PACKET_GC_EXAMISWRIGHTBROADCASE(Packet):
    pass


class PACKET_CG_ASKTAKEREWARD(Packet):
    pass


class PACKET_GC_RETTAKEREWARD(Packet):
    pass


class PACKET_CG_ASKEXAMTOPDATA(Packet):
    pass


class PACKET_CG_GUIDEFLOW(Packet):
    pass


class PACKET_CG_ASK_BLACK_MARKET(Packet):
    pass


class PACKET_GC_BLACK_MARKET_LIST(Packet):
    pass


class PACKET_CG_BLACKMARKET_BUY(Packet):
    pass


class PACKET_GC_BLACKMARKET_REFRESH(Packet):
    pass


class PACKET_CG_CGAskQuestion(Packet):
    pass


class PACKET_GC_GCAskQuestion(Packet):
    pass


class PACKET_GC_EXAMUICLOSENOTICE(Packet):
    pass


class GCAddRedPacket(Packet):
    pass


class GCDelRedPacket(Packet):
    pass


class GCUpdateRedPacket(Packet):
    pass


class GCRedPacketList(Packet):
    pass


class PACKET_CG_NPCTRANSFER(Packet):
    pass


class PACKET_CG_ASKCOMPOSE(Packet):
    pass


class Packet_GC_RETCOMPOSE(Packet):
    pass


class PACKET_CGAskYBXGList(Packet):
    pass


class GCAskYBXGList(Packet):
    pass


class PACKET_CG_JIAOCHANGCHALLENGE(Packet):
    pass


class PACKET_GC_JIAOCHANGCHALLENGE(Packet):
    pass


class PACKET_GC_JIAOCHANGCHALLENGEDATA(Packet):
    pass


class PACKET_CG_JIAOCHANGCHALLENGEHANDLE(Packet):
    pass


class PACKET_GC_JIAOCHANGCHALLENGEHANDLE(Packet):
    pass


class PACKET_GC_JIAOCHANGCHALLENGENOTICE(Packet):
    pass


class PACKET_CG_HAIROPERATE(Packet):
    pass


class PACKET_GC_HAIROPERATERETURN(Packet):
    pass


class PACKET_CG_ASKKILLERLOG(Packet):
    pass


class PACKET_GC_RETKILLERLOG(Packet):
    pass


class PACKET_GC_HAIRCOLORCHANGE(Packet):
    pass


class PACKET_CG_LUA_COMMON(Packet):
    pass


class PACKET_GC_LUA_COMMON(Packet):
    pass


class PACKET_CGW_REQ_LASTRELATIONINFO(Packet):
    pass


class PACKET_WGC_RET_LASTRELATIONINFO(Packet):
    pass


class PACKET_CG_ASK_BANGPAIGONGZI(Packet):
    pass


class PACKET_GC_SEND_BANGPAIGONGZI(Packet):
    pass


class CGServerLevelInfo(Packet):
    pass


class GCServerLevelInfo(Packet):
    pass


class PACKET_CGCommonShopBuy(Packet):
    pass


class PACKET_GCCommonShopBuy(Packet):
    pass


class GCSongLiaoBaseInfo(Packet):
    pass


class CGSongLiaoDetailInfo(Packet):
    pass


class GCSongLiaoDetailInfo(Packet):
    pass


class PACKET_GC_GUILDCITYDEFENDINFO(Packet):
    pass


class PACKET_CG_GUILDCITYDEFENDINFO(Packet):
    pass


class PACKET_CG_ASK_PLATFORM_LIST(Packet):
    pass


class PACKET_GC_RET_PLATFORM_INFO(Packet):
    pass


class PACKET_GC_BANGPAISHOPINFO(Packet):
    pass


class PACKET_CG_BANGPAISHOPBUY(Packet):
    pass


class PACKET_GC_BANGPAISHOPBUYRETURN(Packet):
    pass


class PACKET_GC_GUILDACTIVITYDRINK(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)

        self['Type'] = 0
        self['leftTime'] = 0
        self['gainExp'] = 0
        self['answerLeftTime'] = 0
        self['answerCount'] = 0
        self['rollLeftTime'] = 0
        self['rollCount'] = 0
        self['curRollPieceNum'] = 0
        self['dealType'] = 0
        self['joinNum'] = 0
        self['expAdd'] = 0
        self['QuestionType'] = 0
        self['TableID'] = 0
        self['Qtype1'] = 0
        self['Qtype2'] = 0
        self['Qtype3'] = 0
        self['QValue1'] = 0
        self['QValue2'] = 0
        self['QValue3'] = 0
        self['Qanswer1'] = 0
        self['Qanswer2'] = 0
        self['Qanswer3'] = 0
        self['Qanswer4'] = 0
        self['leftSeconds'] = 0
        self['curNum'] = 0
        self['curRollPieceNum'] = 0
        self['AwardNum'] = 0
        self['MyAnswer'] = 0
        self['TableID'] = 0
        self['QuestionType'] = 0
        self['RightAnswer'] = 0
        self['OverTime'] = 0
        self['curRollPieceNum'] = 0
        self['RightNum'] = 0
        self['num'] = 0
        self['playerName'] = 0
        self['RightNum'] = 0
        self['curRollPieceNum'] = 0
        self['killerGuidL'] = 0
        self['killerGuidH'] = 0
        self['userName'] = 0
        self['DiceNum'] = 0
        self['Lv'] = 0
        self['Menpai'] = 0
        self['Sex'] = 0
        self['HeadId'] = 0
        self['killerGuidL2'] = 0
        self['killerGuidH2'] = 0
        self['userName2'] = 0
        self['DiceNum2'] = 0
        self['Lv2'] = 0
        self['Menpai2'] = 0
        self['Sex2'] = 0
        self['HeadId2'] = 0

    def filldatafromstream(self, buf):
        (self['Type'], buf) = ReadByte(buf)
        self['Type'] = ord(self['Type'])
        (self['Type'], buf) = ReadByte(buf)
        self['Type'] = ord(self['Type'])
        if self['Type'] == 2:  #RetAskBase
            (self['leftTime'], buf) = ReadInt(buf)
            (self['gainExp'], buf) = ReadInt(buf)
            (self['answerLeftTime'], buf) = ReadInt(buf)
            (self['answerCount'], buf) = ReadByte(buf)
            self['answerCount'] = ord(self['answerCount'])
            (self['rollLeftTime'], buf) = ReadInt(buf)
            (self['rollCount'], buf) = ReadByte(buf)
            self['rollCount'] = ord(self['rollCount'])
            (self['curRollPieceNum'], buf) = ReadByte(buf)
            self['curRollPieceNum'] = ord(self['curRollPieceNum'])
            (self['dealType'], buf) = ReadByte(buf)
            self['dealType'] = ord(self['dealType'])
            (self['joinNum'], buf) = ReadInt(buf)
            (self['expAdd'], buf) = ReadByte(buf)
            self['expAdd'] = ord(self['expAdd'])
        elif self['Type'] == 4:  #RetAskQuestion
            (self['QuestionType'], buf) = ReadByte(buf)
            self['QuestionType'] = ord(self['QuestionType'])
            (self['TableID'], buf) = ReadInt(buf)
            (self['Qtype1'], buf) = ReadByte(buf)
            self['Qtype1'] = ord(self['Qtype1'])
            (self['Qtype2'], buf) = ReadByte(buf)
            self['Qtype2'] = ord(self['Qtype2'])
            (self['Qtype3'], buf) = ReadByte(buf)
            self['Qtype3'] = ord(self['Qtype3'])
            (self['QValue1'], buf) = ReadInt(buf)
            (self['QValue2'], buf) = ReadInt(buf)
            (self['QValue3'], buf) = ReadInt(buf)

            (self['Qanswer1'], buf) = ReadCharArray(buf,31)
            (self['Qanswer2'], buf) = ReadCharArray(buf, 31)
            (self['Qanswer3'], buf) = ReadCharArray(buf, 31)
            (self['Qanswer4'], buf) = ReadCharArray(buf, 31)

            (self['leftSeconds'], buf) = ReadInt(buf)
            (self['curNum'], buf) = ReadByte(buf)
            self['curNum'] = ord(self['curNum'])
            (self['curRollPieceNum'], buf) = ReadByte(buf)
            self['curRollPieceNum'] = ord(self['curRollPieceNum'])
            (self['AwardNum'], buf) = ReadByte(buf)
            self['AwardNum'] = ord(self['AwardNum'])
        elif self['Type'] == 6:  #RetAskAnswer
            (self['MyAnswer'], buf) = ReadByte(buf)
            self['MyAnswer'] = ord(self['MyAnswer'])
            (self['TableID'], buf) = ReadInt(buf)
            (self['QuestionType'], buf) = ReadByte(buf)
            self['QuestionType'] = ord(self['QuestionType'])
            (self['RightAnswer'], buf) = ReadByte(buf)
            self['RightAnswer'] = ord(self['RightAnswer'])
            (self['OverTime'], buf) = ReadByte(buf)
            self['OverTime'] = ord(self['OverTime'])
            (self['curRollPieceNum'], buf) = ReadByte(buf)
            self['curRollPieceNum'] = ord(self['curRollPieceNum'])
            (self['RightNum'], buf) = ReadByte(buf)
            self['RightNum'] = ord(self['RightNum'])
        elif self['Type'] == 8:  #RetAskRoll
            (self['num'], buf) = ReadByte(buf)
            self['num'] = ord(self['num'])
        elif self['Type'] == 9:  #RetAddRollPiece
            (self['playerName'], buf) = ReadCharArray(buf, 31)
            (self['RightNum'], buf) = ReadByte(buf)
            self['RightNum'] = ord(self['RightNum'])
            (self['curRollPieceNum'], buf) = ReadByte(buf)
            self['curRollPieceNum'] = ord(self['curRollPieceNum'])
        elif self['Type'] == 12:  #RetClearInfo
            (self['killerGuidL'], buf) = ReadInt32(buf)
            (self['killerGuidH'], buf) = ReadInt32(buf)
            (self['userName'], buf) = ReadCharArray(buf, 31)
            (self['DiceNum'], buf) = ReadByte(buf)
            self['DiceNum'] = ord(self['DiceNum'])
            (self['Lv'], buf) = ReadInt(buf)
            (self['Menpai'], buf) = ReadByte(buf)
            self['Menpai'] = ord(self['Menpai'])
            (self['Sex'], buf) = ReadUInt32(buf)
            (self['HeadId'], buf) = ReadInt(buf)

            (self['killerGuidL2'], buf) = ReadInt32(buf)
            (self['killerGuidH2'], buf) = ReadInt32(buf)
            (self['userName2'], buf) = ReadCharArray(buf, 31)
            (self['DiceNum2'], buf) = ReadByte(buf)
            self['DiceNum2'] = ord(self['DiceNum2'])
            (self['Lv2'], buf) = ReadInt(buf)
            (self['Menpai2'], buf) = ReadByte(buf)
            self['Menpai2'] = ord(self['Menpai2'])
            (self['Sex2'], buf) = ReadUInt32(buf)
            (self['HeadId2'], buf) = ReadInt(buf)
        return (self,buf)

    def handle(self):
        if self['Type'] == 4:
            self.person['TableID'] = self['TableID']
            self.person['QuestionType'] = self['QuestionType']
        if self['Type'] == 2:
            self.person['answerLeftTime'] = self['answerLeftTime']
            self.person['rollLeftTime'] = self['rollLeftTime']
        if self['Type'] == 12:
            self.person['finished'] = 0



class PACKET_CG_GUILDACTIVITYDRINK(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Type'] = 0
        self['guildId'] = 0
        self['sceneId'] = 0
        self['TableId'] = 0
        self['QuestionType'] = 0
        self['answerIndex'] = 0
        self['AskType'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(chr(self['Type']))
        if self['Type'] == 1111: #AskGuildUserInfo
            buf += WriteByte(chr(self['Type']))
            buf += WriteInt32(self['guildId'])
            buf += WriteInt32(self['sceneId'])
        elif self['Type'] == 5: #AskAnswer
            buf += WriteByte(chr(self['Type']))
            buf += WriteInt32(self['TableId'])
            buf += WriteByte(chr(self['QuestionType']))
            buf += WriteByte(chr(self['answerIndex']))
        elif self['Type'] == 1: #AskBasic
            buf += WriteByte(chr(self['Type']))
            buf += WriteByte(chr(self['AskType']))
        else:
            buf += WriteByte(chr(self['Type']))
        return buf

    def filldatafromstream(self, buf):
        (self['Type'], buf) = ReadByte(buf)
        self['Type'] = ord(self['Type'])
        if self['Type'] == 1111: #AskGuildUserInfo
            (self['Type'], buf) = ReadByte(buf)
            self['Type'] = ord(self['Type'])
            (self['guildId'], buf) = ReadInt32(buf)
            (self['sceneId'], buf) = ReadInt32(buf)
        elif self['Type'] == 5: #AskAnswer
            (self['Type'], buf) = ReadByte(buf)
            self['Type'] = ord(self['Type'])
            (self['TableId'], buf) = ReadInt32(buf)
            (self['QuestionType'], buf) = ReadByte(buf)
            self['QuestionType'] = ord(self['QuestionType'])
            (self['answerIndex'], buf) = ReadByte(buf)
            self['answerIndex'] = ord(self['answerIndex'])
        elif self['Type'] == 1: #AskBasic
            (self['Type'], buf) = ReadByte(buf)
            self['Type'] = ord(self['Type'])
            (self['AskType'], buf) = ReadByte(buf)
            self['AskType'] = ord(self['AskType'])
        else:
            (self['Type'], buf) = ReadByte(buf)
            self['Type'] = ord(self['Type'])
        return (self,buf)



class PACKET_CG_SWORN_BROTHER_INFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['myLGuid'] = 0
        self['myHGuid'] = 0
        self['myBrother_H_Guid'] = 0        
        self['myBrother_L_Guid'] = 0        
        
    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['myLGuid'])
        buf += WriteInt32(self['myHGuid'])
        buf += WriteInt32(self['myBrother_H_Guid'])
        buf += WriteInt32(self['myBrother_L_Guid'])                
        return buf

    def filldatafromstream(self, buf):
        (self['myLGuid'], buf) = ReadInt32(buf)
#        self['myLGuid'] = ord(self['myLGuid'])
        (self['myHGuid'], buf) = ReadInt32(buf)
#        self['myHGuid'] = ord(self['myHGuid'])        
        (self['myBrother_H_Guid'], buf) = ReadInt32(buf)
#        self['myBrother_H_Guid'] = ord(self['myBrother_H_Guid'])
        (self['myBrother_L_Guid'], buf) = ReadInt32(buf)
#        self['myBrother_L_Guid'] = ord(self['myBrother_L_Guid'])        
        
        
        return (self, buf)


class PACKET_GC_SWORN_BROTHER_INFO(Packet):
    pass


class PACKET_CG_BROTHER_MATTERS(Packet):
    pass


class PACKET_GC_BROTHER_MATTERS(Packet):
    pass


class PACKET_CG_ASK_TEAMGOAL(Packet):
    pass


class PACKET_GC_RET_TEAMGOAL(Packet):
    pass


class PACKET_CG_CALL_BROTHER(Packet):
    pass


class PACKET_GC_CALL_BROTHER(Packet):
    pass


class CGLineData(Packet):
    pass


class CGRequestTimeLimitAchievement(Packet):
    pass


class GCRequestTimeLimitAchievement(Packet):
    pass


class CGRequestTimeLimitAchievementReward(Packet):
    pass


class PACKET_GC_SWORN_UPDATE_VOTER_DATA(Packet):
    pass


class PACKET_GC_KICK(Packet):
    pass


class PACKET_CG_TSS_DATA(Packet):
    pass


class PACKET_GC_TSS_DATA(Packet):
    pass


class CGRequestYueKaInfo(Packet):
    pass


class GCRequestYueKaInfo(Packet):
    pass


class CGRequestYueKaReward(Packet):
    pass


class GCRequestYueKaReward(Packet):
    pass


class PACKET_CG_YEWAIBOSS_MAPINFO(Packet):
    pass


class PACKET_GC_RET_YEWAIBOSS_MAPINFO(Packet):
    pass


class GCTitleUpdate(Packet):
    pass


class GCTitleOperate(Packet):
    pass


class GCRequestChangeLine(Packet):
    pass


class GCLineData(Packet):
    pass


class PACKET_CG_SETSYSTEMDATA(Packet):
    pass


class PACKET_CG_ASKSYSTEMDATA(Packet):
    pass


class PACKET_GC_SENDSYSTEMDATA(Packet):
    pass


class PACKET_GC_FINDRES(Packet):
    pass


class PACKET_CG_ASKFINDRES(Packet):
    pass


class PACKET_GC_FINDRESLIST(Packet):
    pass


class PACKET_CG_ASKCONSIGNSALEITEMBASEPRICE(Packet):
    pass


class CGOutLine(Packet):
    pass


class PACKET_GC_QUERY_ITEM_BASE_PRICE_MSG(Packet):
    pass


class PACKET_GC_CONSIGNSALE_RECORD_LIST(Packet):
    pass


class PACKET_CG_ASK_CONSIGNSALE_ITEM_DETATL(Packet):
    pass


class PACKET_CG_EXAMBASEINFO(Packet):
    pass


class PACKET_GC_EXAMBASEINFO(Packet):
    pass


class PACKET_CG_ASKHELPFORMGUILD(Packet):
    pass


class PACKET_GC_ASKHELPFORMGUILD(Packet):
    pass


class PACKET_CG_SENDEXAMHELPTOGUILD(Packet):
    pass


class PACKET_GC_SENDEXAMHELPTOGUILD(Packet):
    pass


class PACKET_CGW_CHECKQUESTIONANSERED(Packet):
    pass


class PACKET_WGC_CHECKQUESTIONANSERED(Packet):
    pass


class PACKET_WGC_SOMEONEANSERED(Packet):
    pass


class PACKET_WGC_ACCESSHUISHI(Packet):
    pass


class PACKET_CG_ONEKEY_GET_MAIL_APPEND(Packet):
    pass


class GCReceiveRedPacket(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['type'] = 0
        self['data'] = 0
        self['guid'] = 0
        self['Result'] = 0

    def filldatafromstream(self, buf):
        (self['type'], buf) = ReadByte(buf)
        self['type'] = ord(self['type'])
        (self['data'], buf) = ReadUInt32(buf)
        (self['guid'], buf) = ReadUInt64(buf)
        (self['Result'], buf) = ReadInt32(buf)

        return (self, buf)


class GCSceneMapping(Packet):
    pass


class PACKET_WGC_EXAMSTYSTEMNOTICE(Packet):
    pass


class PACKET_CG_MASTER(Packet):
    pass


class PACKET_GC_MASTER(Packet):
    pass


class PACKET_CG_ASKBREAKOUTLEVEL(Packet):
    pass


class PACKET_CG_ASKEXPPOOLDATA(Packet):
    pass


class PACKET_GC_ASKEXPPOOLDATA(Packet):
    pass


class PACKET_CG_ASK_REBELPOSITION(Packet):
    pass


class PACKET_GC_RET_REBELPOSITIONDATA(Packet):
    pass


class PACKET_CG_BANGPAISHOPOPEN(Packet):
    pass


class PACKET_GC_RETBREAKOUTLEVEL(Packet):
    pass


class PACKET_CG_PICSHAREDONE(Packet):
    pass


class PACKET_CG_ASK_GUILDRESEARCHlIST(Packet):
    pass


class PACKET_GC_ASK_GUILDRESEARCHlIST(Packet):
    pass


class PACKET_CG_ASK_UPGRADEGUILDRESEARCH(Packet):
    pass


class GCCollectionInfo(Packet):
    pass


class CGRequestCollectionSkillLevelUp(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['index'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['index'])
        return buf

    def filldatafromstream(self, buf):
        (self['index'], buf) = ReadByte(buf)
        self['index'] = ord(self['index'])
        return (self, buf)


class PACKET_CG_SWORN_CHANGE_MINGHAO(Packet):
    pass


class PACKET_CG_MODIFY_JIANGHUZIHAO(Packet):
    pass


class PACKET_CG_PAOHUAN_HELP(Packet):
    pass


class PACKET_GC_PAOHUAN_HELP(Packet):
    pass


class PACKET_CG_ASK_TEAMFOLLOW(Packet):
    pass


class PACKET_GC_RET_TEAMFOLLOW(Packet):
    pass


class PACKET_CG_Upload_Log(Packet):
    pass


class PACKET_CG_ASKAUCTIONSHOPITEM(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Asktype'] = 0
        self['Type'] = 0
        self['SubType'] = 0
        self['Page'] = 1        
        
    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['Asktype'])
        if self['Asktype'] == 1: 
            buf += WriteByte(self['Type'])        
            buf += WriteByte(self['SubType'])        
            buf += WriteInt32(self['Page'])                
        return buf

    def filldatafromstream(self, buf):
        (self['index'],buf) = ReadByte(buf)
        self['index'] = ord(self['index'])
        if self['Asktype'] == 1:        
            (self['Type'],buf) = ReadByte(buf)
            self['Type'] = ord(self['index'])        
            (self['SubType'],buf) = ReadByte(buf)
            self['SubType'] = ord(self['SubType']) 
            (self['Page'],buf) = ReadInt32(buf)
            self['Page'] = ord(self['Page'])                    
        return (self,buf)







class PACKET_GC_RETAUCTIONSHOPITEM(Packet):
    pass


class PACKET_CG_ASKAUCTIONITEM(Packet):
    pass


class PACKET_CG_ASKBUYNOWPRICEITEM(Packet):
    pass


class PACKET_GC_RETAUCTIONSHOPRECORDLIST(Packet):
    pass


class PACKET_GC_RETAUCTIONSHOPREDPOINT(Packet):
    pass


class PACKET_CG_HUASHAN_SWORD_RANK(Packet):
    pass


class PACKET_GC_HUASHAN_SWORD_RANK(Packet):
    pass


class PACKET_GC_CLOSELOADINGUI(Packet):
    pass


class PACKET_GC_HUASHAN_MAIN(Packet):
    pass


class PACKET_CG_HUASHAN_MAIN(Packet):
    pass


class PACKET_GC_HUASHAN_COMBAT_REPORT(Packet):
    pass


class PACKET_GC_HUASHAN_RESULT(Packet):
    pass


class PACKET_GC_HUASHAN_ICON(Packet):
    pass


class PACKET_CG_GODWEAPONOPEN(Packet):
    pass


class PACKET_GC_GODWEAPONOPEN(Packet):
    pass


class PACKET_CG_FIRSCENE_FINISH(Packet):
    pass


class PACKET_CG_FIRSCENE_CHANGESCENE(Packet):
    pass


# luzhenyu 1/18/2017 added

class PACKET_GC_IDIPSHOWWARNING(Packet):
    pass


class PACKET_CG_MISSION_QUETIONS(Packet):
    pass


class PACKET_CG_ANSWER_MISSION_QUETIONS(Packet):
    pass


class PACKET_GC_ANSWER_MISSION_QUETIONS(Packet):
    pass


class PACKET_GC_MISSION_QUETIONS(Packet):
    pass


class PACKET_GC_ASK_SHAXINGRANKINFO(Packet):
    pass


class PACKET_GC_ASK_SHAXINGFUBENINFO(Packet):
    pass


class PACKET_CG_ASK_SHAXINGRANKINFO(Packet):
    pass


class PACKET_GC_CHAR_BUFFUPDATE(Packet):
    pass


class PACKET_CG_ASKADDSKILLLIST(Packet):
    pass


class PACKET_GC_ADDSKILLLIST(Packet):
    pass


#帮派领地
class PACKET_CG_GuildTerritory(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['GuidH'] = 0
        self['GuidL'] = 0
        self['GuildId'] = 0
        self['GuildFightForTerritoryId'] = -1

    def getdatastream(self):
        buf = ''
        buf += WriteInt32(self['GuidH'])
        buf += WriteInt32(self['GuidL'])
        buf += WriteInt16(self['GuildId'])
        buf += WriteInt16(self['GuildFightForTerritoryId'])
        return buf

    def filldatafromstream(self, buf):
        (self['GuidH'], buf) = ReadInt32(buf)
        (self['GuidL'], buf) = ReadInt32(buf)
        (self['GuildId'], buf) = ReadInt16(buf)
        (self['GuildFightForTerritoryId'], buf) = ReadInt16(buf)
        return (self, buf)

class PACKET_GC_GuildTerritory(Packet):
    pass

class PACKET_CG_AskGuildTerritoryInfo(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['Type'] = 0

    def getdatastream(self):
        buf = ''
        buf += WriteByte(self['Type'])
        return buf

    def filldatafromstream(self, buf):
        (self['Type'], buf) = ReadByte(buf)
        self['Type'] = ord(self['Type'])
        return (self, buf)


class PACKET_GC_BackGuildTerritoryInfo(Packet):
    pass


class PACKET_GC_CHATMESSAGECLEAR(Packet):
    pass


class CGRequestShaXingRankInfo(Packet):
    pass


class GCRequestShaXingRankInfo(Packet):
    pass


class GCMessageBall(Packet):
    pass
