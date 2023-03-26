#coding=utf-8
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/08/04
-----------------------------------------------------------------------
Description:    
loging task

-----------------------------------------------------------------------
History:   
2016/9/13 luoyunpeng created
2016/9/18 yaojun added
=======================================================================
'''
import Actions.Functions
import gevent

class login_pass_xuzhang():
    def __init__(self, person):
        self.person = person  
              
    def run(self,login_ip,login_port,server_ip,server_port,account_startwith,client_version):
        
        res = self.person.AConnectToServer(login_ip,login_port)
        if res[0] == False:
            return res
    
        res = self.person.ACL_Connect(account_startwith,client_version)#get
        if res[0] == False:
            return res
        
        #res = Actions.Functions.sendstream(self.person, 1753, 0, '')
        #if res[0] == False:
        #    return res
        
        #res = Actions.Functions.waitforpacket(self.person, "PACKET_LC_RetLogin",5)

        
        
        res = self.person.ACLAskLogin(218501)#get
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
         
#         res = self.person.AConnectToServer("115.159.28.139",1231)
#         if res[0] == False:
#             return res

         
        res = self.person.AConnectToServer(server_ip,server_port)
        if res[0] == False:
            return res
         
        res = self.person.ACGConnect()#get
        if res[0] == False:
            return res
        
        res = self.person.ACGENTERSCENE()#get
        if res[0] == False:
            return res
        
    
        gevent.sleep(1)        
        res = self.person.ACGIdle()#get
        if res[0] == False:
            return res

        if self.person['SceneID'] == 4:
            print '===================', self.person['SceneID']
            res = self.person.pass_xuzhang()
            if res[0] == False:
                return res
            print '******************',self.person.m_CurrentSceneID
            print '%%%%%%%%%%%%%%%%%%',self.person.m_TargetSceneID
            res = self.person.ACGAskChangeScene()
            print '===================ACGAskChangeScene'
            if res[0] == False:
                return res
            res = self.person.ACGIdle()
            if res[0] == False:
                return res

            res = self.person.ACGENTERSCENE(1)
            print '===================enter scene'
            if res[0] == False:
                return res
            res = self.person.ACGIdle()
            if res[0] == False:
                return res

        return res

