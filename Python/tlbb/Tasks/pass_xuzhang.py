# -*- coding: utf-8 -*-
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2017/1/10 by ChengLongLong
-----------------------------------------------------------------------
Description:    跳过序章
-----------------------------------------------------------------------
History:   
2017/1/10 
=======================================================================
'''
import Actions
import gevent

class pass_xuzhang():
    def __init__(self, person):
        self.person = person

    def run(self):
        gevent.sleep(2)
        self.person.ACGIdle()
        res = self.person.ACG_FIRSCENE_FINISH()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        if res[0] == False:
            return res
        res = self.person.ACG_FIRSCENE_CHANGESCENE()
        gevent.sleep(2)
        self.person.ACGIdle()
        gevent.sleep(2)
        self.person.ACGIdle()
        if res[0] == False:
            return res
        return res
