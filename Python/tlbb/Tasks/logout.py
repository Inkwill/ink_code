#coding=utf-8
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/02/13
-----------------------------------------------------------------------
Description:    
reloging task

-----------------------------------------------------------------------
History:   
2017/2/13 anran created
=======================================================================
'''
import Actions.Functions
import time

class logout():
    def __init__(self, person):
        self.person = person  
              
    def run(self,m_Type):
        
        res = self.person.ACG_ASKCOPYSCENECOUNT(m_Type)
        if res[0] == False:
            return res
    
        res = self.person.ACG_ASK_QUIT()
        if res[0] == False:
            return res

        return res


        