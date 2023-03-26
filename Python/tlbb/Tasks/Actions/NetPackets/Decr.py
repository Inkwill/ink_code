#coding=utf-8
'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        2016/12/26 by 鹿振宇 luzhenyu_ca@cyou.com
-----------------------------------------------------------------------
Description:    解密
-----------------------------------------------------------------------
History:   
2016/12/26 
2016/12/29 luzhenyu added
=======================================================================
'''



def decr(buf ,xor = 0xf0):
    retbuf = ''
    for buf1 in buf:
        retbuf += chr(ord(buf1) ^ xor)
    return retbuf
    

def encr(buf ,xor = 0xf0):
    retbuf = ''
    for buf1 in buf:
        retbuf += chr(ord(buf1) ^ xor)
    return retbuf


