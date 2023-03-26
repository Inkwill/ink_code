import STAFMarshalling
import Defines
import logging
import struct
import PACKETS

class Packet():
    def __init__(self, person):
        self.person = person
        self.packpattern = []
        self.packdata = []
        self.packsize = []
        self.__data = {}
        
    def setdata (self, name, value):
        self.__data[name] = value
        return self.getdata(name)
    
    def getdata (self, name):
        if self.__data.has_key(name) and self.__data[name] != None:
            return self.__data[name]
        else:
            return None
        
    def __getitem__(self, name):
        return self.getdata(name)
    
    def __setitem__(self, name, value):
        return self.setdata(name, value)
        
    def getdatastream(self):
        return ''
        
    def filldatafromstream(self, buf):
        return False
   
    def getid(self):
        return Defines.ID_DEFINE(self.__class__.__name__)
    
    def getdatasize(self):
        return len(self.getdatastream())
            
    def dump(self):
        buf = STAFMarshalling.formatObject(self.__data)
        for key in self.__data.keys():
            if not (isinstance(self[key],int) or isinstance(self[key],float) or isinstance(self[key],str) or isinstance(self[key],long)):
                if isinstance(self[key],list) or isinstance(self[key],tuple):
                    buf += '\n' + key + ':[\n'
                    for v in self[key]:
                        if isinstance(v,int) or isinstance(v,float) or isinstance(v,str) or isinstance(v,long):
                            buf += str(v) + '\n'
                        elif isinstance(v,unicode):
                            buf += unicode(v) + '\n'
                        else:
                            try:
                                buf += v.dump() + '\n'
                            except Exception, info:
                                buf += str(v)
                    buf += ']'
                else:
                    if isinstance(self[key],unicode):
                        buf += '\n' + key + ':' + unicode(self[key])
                    else:
                        try:
                            buf += '\n' + key + ':' + self[key].dump()
                        except Exception, info:
                            buf += '\n' + str(key) + ':'

                    
        return buf

#     def handle(self):
#         pass
