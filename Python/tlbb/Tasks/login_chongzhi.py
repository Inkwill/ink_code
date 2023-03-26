#coding=utf-8
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/11/18
-----------------------------------------------------------------------
Description:    
loging task

-----------------------------------------------------------------------
History:   
2016/9/13 luoyunpeng created
2016/9/18 yaojun added
2016/11/18 supinrong added
=======================================================================
'''
import Actions.Functions
import time

class login_chongzhi():
    def __init__(self, person):
        self.person = person  
              
    def run(self,server_ip,server_port,account_startwith,client_version):
        
        res = self.person.AConnectToServer(server_ip,server_port)
        if res[0] == False:
            return res
    
        res = self.person.ACL_Connect(account_startwith,client_version)
        if res[0] == False:
            return res

        
        res = self.person.ACLAskLogin(218501, 1)
        if res[0] == False:
            return res
        
        while self.person['LC_Status_smResult'] !=2:
            res = Actions.Functions.waitforpacket(self.person, "PACKET_LC_Status",60)
            if res[0] == False:
                return res
        
        res = self.person.ACLAskCharList()
        if res[0] == False:
            return res
        if len(self.person['RoleList'])==0:
            res = self.person.ACLAskCreateChar()
            if res[0] == False:
                return res
        
        res = self.person.ACLAskCharLogin()
        if res[0] == False:
            return res
        
        res = self.person.AConnectToServer("115.159.28.139",1231)
        if res[0] == False:
            return res
        
        res = self.person.ACGConnect()
        if res[0] == False:
            return res
        
        res = self.person.ACGENTERSCENE()
        if res[0] == False:
            return res
        return res


