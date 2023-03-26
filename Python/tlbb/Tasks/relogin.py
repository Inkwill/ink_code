#coding=utf-8
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/09/19
-----------------------------------------------------------------------
Description:    
reloging task

-----------------------------------------------------------------------
History:   
2016/9/19 yaojun created
=======================================================================
'''
import Actions.Functions
import time

class relogin():
    def __init__(self, person):
        self.person = person  
              
    def run(self,server_ip,server_port,account_startwith,client_version):
        
        res = self.person.AConnectToServer(server_ip,server_port)
        if res[0] == False:
            return res
    
        res = self.person.ACL_Connect(account_startwith,client_version)
        if res[0] == False:
            return res
        
            
        res = self.person.AReCLAskLogin(218501)
        if res[0] == False:
            return res
        
        while True:
            Actions.Functions.handleinputstream(self.person)
            if self.person['Rev_LC_ReConnectData']!=None and self.person['Rev_LC_ReConnectData']==1:
                break
            elif self.person['Rev_LC_Status']!=None and self.person['Rev_LC_Status']==1:
                if self.person['LC_Status_smResult'] ==2 or self.person['LC_Status_smResult']==5:
                    break
                
        res = self.person.AConnectToServer(self.person['Scene_ServerIp'],self.person['Scene_ServerPort'])
        if res[0] == False:
            return res
        
        res = self.person.ACGConnect()
        if res[0] == False:
            return res
        
        res = self.person.ACGENTERSCENE()
        if res[0] == False:
            return res

        return res


        
        

