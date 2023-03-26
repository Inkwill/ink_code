#coding=utf-8
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/11/9
-----------------------------------------------------------------------
Description:    
将person恢复成未登陆的初始状态,下次登陆将采用新帐号,person的任务队列将保留.
用于一次性任务的压测,当一次性任务完成后,旧帐号需要登出服务器,再将此person恢复成初始状态，再用新帐号登陆，继续做一遍一次性任务。

-----------------------------------------------------------------------
History:   
2016/11/9 luoyunpeng created
=======================================================================
'''

class reborn():
    def __init__(self, person):
        self.person = person  
              
    def run(self):

        self.person.cleanup_data()
            
        self.person['inputbuffer'] = ""
        self.person['socket'] = None
        self.person['is_packect_truncated'] = False
        
        self.person['userName'] = None
        self.person['posx'] = 0
        self.person['posz'] = 0
        self.person['SceneId'] = 0
        self.person['m_ObjID'] = 0
        self.person['m_Guid'] = 0
        self.person['targetmark'] = []
        self.person['monsterdic'] = {}
        
        return(True, 0, "person reborn!" )
        
        


        
        

