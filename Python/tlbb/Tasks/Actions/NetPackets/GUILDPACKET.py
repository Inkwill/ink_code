# -*- coding: utf-8 -*-
from  TLSocket import *
from Packet import Packet

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
        (self['m_SortType'],buf)= ReadByte(buf)
        self['m_SortType'] = ord(self['m_SortType'])
        (self['m_Start'],buf)= ReadUInt16(buf)  
        (self['m_QueryDiffWorld'],buf)= ReadByte(buf)
        self['m_QueryDiffWorld'] = ord(self['m_QueryDiffWorld'])
        return (self,buf)

class Officer(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GUID'] = 0
        self['HighValue'] = 0
        self['LowValue'] = 0
        self['m_Name'] = ''
        self['m_Level'] = 0
        self['m_MenpaiID'] = 0
        self['m_IsOnline'] = 0
        self['m_Position'] = 0
        self['m_Sex'] = 0
        self['m_HeaderID'] = 0
           
    def getdatastream(self):
        buf = ''
        return buf

    def filldatafromstream(self, buf):
        (self['m_GUID'],buf)= ReadInt64(buf)
        self['LowValue'],self['HighValue'] = DecodeUInt64(self['m_GUID'])
        (self['m_NameChars'],buf)= ReadCharArray(buf,30) 
        
        (self['m_Level'],buf)= ReadByte(buf) 
        self['m_Level'] = ord(self['m_Level'])
        (self['m_MenpaiID'],buf)= ReadByte(buf) 
        self['m_MenpaiID'] = ord(self['m_MenpaiID'])
        (self['m_IsOnline'],buf)= ReadByte(buf) 
        self['m_IsOnline'] = ord(self['m_IsOnline'])
        (self['m_Position'],buf)= ReadByte(buf) 
        self['m_Position'] = ord(self['m_Position'])
        (self['m_Sex'],buf)= ReadByte(buf) 
        self['m_Sex'] = ord(self['m_Sex'])
        (self['m_HeaderID'],buf)= ReadInt(buf)
        
        return (self,buf)
        
class GuildInfo(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['OFFICER_COUNT'] = 3
        self['m_GuildID'] = 0
        self['m_ChiefName'] = ''
        self['m_GuildName'] = ''
        self['m_GuildDesc'] = ''
        self['m_CityName'] = ''
        self['m_GuildLeagueName'] = ''
        self['m_PortSceneID'] = 0
        self['m_GuildStatus'] = 0
        self['m_GuildUserCount'] = 0
        self['m_GuildLevel'] = 0
        self['m_FoundedTime'] = 0
        self['m_BoomValue'] = 0
        self['m_BattleWeekScore'] = 0
        self['m_Battle4WeekScore'] = 0
        self['m_YvXueValue'] = 0
        self['m_AllEquipPoint'] = 0
        self['m_MaxGuildUserCount'] = 0
        self['m_IsMeApply'] = 0
        self['m_Officers'] = []
         
    def getdatastream(self):
        buf = ''
        return buf
    
    def filldatafromstream(self, buf):
        (self['m_GuildID'],buf)= ReadShort(buf)
        (self['m_ChiefName'],buf)= ReadCharArray(buf,30) 
        (self['m_GuildName'],buf)= ReadCharArray(buf,25) 
        (self['m_GuildDesc'],buf)= ReadCharArray(buf,101) 
        (self['m_CityName'],buf)= ReadCharArray(buf,26) 
        (self['m_GuildLeagueName'],buf)= ReadCharArray(buf,32) 
        (self['m_PortSceneID'],buf)= ReadInt(buf) 
        (self['m_GuildStatus'],buf)= ReadByte(buf) 
        self['m_GuildStatus'] = ord(self['m_GuildStatus'])
        (self['m_GuildUserCount'],buf)= ReadInt(buf) 
        (self['m_GuildLevel'],buf)= ReadByte(buf)
        self['m_GuildLevel'] = ord(self['m_GuildLevel'])
        (self['m_FoundedTime'],buf)= ReadInt(buf) 
        (self['m_BoomValue'],buf)= ReadInt(buf) 
        (self['m_BattleWeekScore'],buf)= ReadInt(buf) 
        (self['m_Battle4WeekScore'],buf)= ReadInt(buf) 
        (self['m_YvXueValue'],buf)= ReadInt(buf) 
        (self['m_AllEquipPoint'],buf)= ReadInt(buf) 
        (self['m_MaxGuildUserCount'],buf)= ReadInt(buf)
        (self['m_IsMeApply'],buf)= ReadByte(buf)
        self['m_IsMeApply'] = ord(self['m_IsMeApply'])
               
        for i in range(self['OFFICER_COUNT']):
            temp = Officer(None)
            (temp,buf) = temp.filldatafromstream(buf)
            self['m_Officers'].append(temp)
        
        return (self,buf)


class GUILD_WGC_LIST(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_StartIndex'] = 0
        self['m_GuildCount'] = 0
        self['m_GuildListCount'] = 0
        self['m_Guilds'] = []
        
    def getdatastream(self):
        buf = ''
        return buf
    
    def filldatafromstream(self, buf):
        (self['m_StartIndex'],buf)= ReadUShort(buf)
        (self['m_GuildCount'],buf)= ReadUShort(buf)  
        (self['m_GuildListCount'],buf)= ReadByte(buf)
        self['m_GuildListCount'] = ord(self['m_GuildListCount'])
        if self['m_GuildListCount']>0 and self['m_GuildListCount']<=128:
            temp = GuildInfo(None)
            (temp,buf) = temp.filldatafromstream(buf)
            self['m_Guilds'].append(temp)
            pass
        
        return (self,buf)


class BattleGuild_t(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GuildID'] = 0
        self['m_LeftTime'] = 0
        
    def getdatastream(self):
        buf = ''
        buf += WriteInt16(self['m_GuildID'])
        buf += WriteUInt32(self['m_LeftTime'])
        return buf
    
    def filldatafromstream(self, buf):
        (self['m_GuildID'],buf)= ReadInt16(buf)
        (self['m_LeftTime'],buf)= ReadUInt32(buf)
        return (self,buf)
    
class GUILD_WGC_SELF_GUILD_INFO(Packet):
    def __init__(self, person):
        Packet.__init__(self, person)
        self['m_GuildID'] = 0
        self['m_GuildNameSize'] = 0
        self['m_GuildName'] = ''
        self['m_PositionNameSize'] = 0
        self['m_PositionName'] = ''
        self['m_GuildLeagueNameSize'] = 0
        self['m_GuildLeagueName'] = ''
        self['m_GuildPosition'] = 0
        self['m_GuildContri'] = 0
        self['m_GuildContriPerWeek'] = 0
        self['m_MaxGuildCountri'] = 0
        self['m_CityID'] = 0
        self['m_LeaveWordSize'] = 0
        self['m_GuildLeaveWord'] = ''
        self['m_GuildDescSize'] = 0
        self['m_GuildDesc'] = ''
        self['m_GuildLevel'] = 0
        self['m_GuildTime'] = 0
        self['m_BattleGuildList'] = []
        self['m_BattleNum'] = 0
        self['m_HostillityNum'] = 0
        self['m_AppointTime'] = 0
        self['m_ProposerCount'] = 0
        self['m_DiffWorldBattleGuild'] = None
        self['m_DiffWorldBattleGuildZoneWorldID'] = 0
        self['m_ChieftainApplyStutas'] = 0
        self['m_ChieftainApplyCd'] = 0
    
    def getdatastream(self):
        buf = ''
        return buf
    
    def filldatafromstream(self, buf):

        (self['m_GuildID'],buf)= ReadShort(buf)
        (self['m_GuildNameSize'],buf)= ReadByte(buf)
        self['m_GuildNameSize'] = ord(self['m_GuildNameSize'])
        (self['m_GuildName'],buf)= ReadCharArray(buf,self['m_GuildNameSize'])
        (self['m_PositionNameSize'],buf)= ReadByte(buf)
        self['m_PositionNameSize'] = ord(self['m_PositionNameSize'])
        (self['m_PositionName'],buf)= ReadCharArray(buf,self['m_PositionNameSize']) 
        (self['m_GuildLeagueNameSize'],buf)= ReadByte(buf)
        self['m_GuildLeagueNameSize'] = ord(self['m_GuildLeagueNameSize'])
        (self['m_GuildLeagueName'],buf)= ReadCharArray(buf,self['m_GuildLeagueNameSize'])
        (self['m_GuildPosition'],buf)= ReadByte(buf)
        self['m_GuildPosition'] = ord(self['m_GuildPosition'])
        
        (self['m_GuildContri'],buf)= ReadInt(buf)
        (self['m_GuildContriPerWeek'],buf)= ReadInt(buf)
        (self['m_MaxGuildCountri'],buf)= ReadInt(buf)
        
        (self['m_CityID'],buf)= ReadShort(buf)
        
        (self['m_LeaveWordSize'],buf)= ReadUint(buf)
        (self['m_GuildLeaveWord'],buf)= ReadCharArray(buf,self['m_LeaveWordSize'])
        
        (self['m_GuildDescSize'],buf)= ReadByte(buf)
        self['m_GuildDescSize'] = ord(self['m_GuildDescSize'])
        (self['m_GuildDesc'],buf)= ReadCharArray(buf,self['m_GuildDescSize'])
        
        (self['m_GuildLevel'],buf)= ReadInt(buf)
        (self['m_GuildTime'],buf)= ReadInt(buf)
        return (self,buf)
        for i in range(3):
            temp = BattleGuild_t(None)
            (temp,buf) = temp.filldatafromstream(buf)
            self['m_BattleGuildList'].append(temp)
        
        (self['m_BattleNum'],buf)= ReadInt(buf)
        (self['m_HostillityNum'],buf)= ReadInt(buf)
        (self['m_AppointTime'],buf)= ReadUint(buf)
        (self['m_ProposerCount'],buf)= ReadInt(buf)
        temp = BattleGuild_t(None)
        (self['m_DiffWorldBattleGuild'],buf) = temp.filldatafromstream(buf)
        (self['m_DiffWorldBattleGuildZoneWorldID'],buf) = ReadShort(buf)
        (self['m_ChieftainApplyStutas'],buf) = ReadByte(buf)
        self['m_ChieftainApplyStutas'] = ord(self['m_ChieftainApplyStutas'])
        (self['m_ChieftainApplyCd'],buf)= ReadInt(buf)
        
        return (self,buf)