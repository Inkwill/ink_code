#coding=utf-8
import pytlbb
import binascii
import struct


def ReadUInt64(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadUInt64(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])

def ReadInt64(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadInt64(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])

def ReadUInt32(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadUInt32(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])

def ReadUint(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadUint(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])

def ReadInt32(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadInt32(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])

def ReadInt(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadInt(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])

def ReadSingle(buf):
    (value,index) = pytlbb.ReadSingle(buf)
    return (value,buf[index:])

def ReadFloat(buf):
    (value,index) = pytlbb.ReadFloat(buf)
    return (value,buf[index:])

def ReadDouble(buf):
    (value,index) = pytlbb.ReadDouble(buf)
    return (value,buf[index:])

def ReadUInt16(buf):
    (value,index) = pytlbb.ReadUInt16(buf)
    return (value,buf[index:])

def ReadUShort(buf):
    (value,index) = pytlbb.ReadUShort(buf)
    return (value,buf[index:])

def ReadInt16(buf):
    (value,index) = pytlbb.ReadInt16(buf)
    return (value,buf[index:])

def ReadShort(buf):
    (value,index) = pytlbb.ReadShort(buf)
    return (value,buf[index:])


def ReadBool(buf):
    (value,index) = pytlbb.ReadBool(buf)
    if value == 1:
        return (True,buf[index:])
    else:
        return (False,buf[index:])
    

def ReadByte(buf):
    if len(buf) == 0:
        return ('','')
    elif len(buf) == 1:
        return (buf[0],'')
    else:
        return (buf[0],buf[1:])

def ReadBytes(buf,length):
    return (buf[:length],buf[length:])



def WriteUInt64(value, bIsVarintCode = True):
    return pytlbb.WriteUInt64(value,ChangeBoolToInt(bIsVarintCode))

def WriteInt64(value, bIsVarintCode = True):
    return pytlbb.WriteInt64(value,ChangeBoolToInt(bIsVarintCode))

def WriteUInt32(value, bIsVarintCode = True):
    return pytlbb.WriteUInt32(value,ChangeBoolToInt(bIsVarintCode))

def WriteInt32(value, bIsVarintCode = True):
    return pytlbb.WriteInt32(value,ChangeBoolToInt(bIsVarintCode))

def WriteSingle(value):
    return pytlbb.WriteSingle(value)

def WriteDouble(value):
    return pytlbb.WriteDouble(value)

def WriteUInt16(value):
    return pytlbb.WriteUInt16(value)

def WriteInt16(value):
    return pytlbb.WriteInt16(value)

def WriteBool(value):
    if value == True:
        return pytlbb.WriteBool(1)
    else:
        return pytlbb.WriteBool(0)

def WriteByte(value):
    return value

def ReadCharArray(buf, length, bConvertEncoding = True):
    if bConvertEncoding:
        (value,index) = pytlbb.ReadCharArray(buf, length, ChangeBoolToInt(bConvertEncoding))
    else:
        (value,index) = pytlbb.ReadCharArray_Byte(buf, length, ChangeBoolToInt(bConvertEncoding))
    return (value,buf[index:])

def WriteCharArray(value, length, bConvertEncoding, AddTerminator = True):
    if bConvertEncoding:
        return pytlbb.WriteCharArray(value, length, ChangeBoolToInt(bConvertEncoding), ChangeBoolToInt(AddTerminator) )
    else:
        return pytlbb.WriteCharArray_Byte(value, length, ChangeBoolToInt(bConvertEncoding), ChangeBoolToInt(AddTerminator) )
    
    
def MakeGUID(LowWord,HighWord):
    Lbyte = struct.pack("=i", LowWord) 
    Hbyte = struct.pack("=i", HighWord)
    (value,) = struct.unpack("=Q",(Lbyte + Hbyte))
    return value

def EncodeUInt64(HighWord,LowWord):
    Hbyte = struct.pack("=i", HighWord)
    Lbyte = struct.pack("=i", LowWord) 
    (value,) = struct.unpack("=Q",(Lbyte + Hbyte))
    return value

def DecodeUInt64(value):
    valuebyte = struct.pack("=Q", value)
    low,high = struct.unpack("=2i",valuebyte)
    return (low,high)
    
    
def GetStringBytesLen(inputstring,AddTerminator):
    #input AddTerminator for True or False
    return pytlbb.GetStringBytesLen(inputstring, ChangeBoolToInt(AddTerminator) )   

def UInt32ConvertByte(value, bIsVarintCode = True):
    return pytlbb.WriteUInt32(value,ChangeBoolToInt(bIsVarintCode))

def Int32ConvertByte(value, bIsVarintCode = True):
    return pytlbb.WriteInt32(value,ChangeBoolToInt(bIsVarintCode))

def ByteConvertUInt32(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadUInt32(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])

def ByteConvertInt32(buf, bIsVarintCode = True):
    (value,index) = pytlbb.ReadInt32(buf, ChangeBoolToInt(bIsVarintCode))
    return (value,buf[index:])
        

def ChangeBoolToInt(boolvalue):
    if boolvalue == True:
        return 1
    else:
        return 0
    

    
    
if __name__ == "__main__":
    aaa = GetStringBytesLen(u'畅游天下',True)
    print aaa
    bbb = GetStringBytesLen(u'abc',True)
    print bbb  
    
    bbb = "324534645"
    #aaa = MakeGUID(122,1)
    #print aaa
    ###########Test  
    #bbb = WriteInt32(3456,False)
    #bbb = WriteSingle(7.00)
    #bbb = WriteUInt64(4235235234523523,False)
    #bbb = WriteInt64(32454355555,True)
    #bbb = WriteUInt32(234423)
    #bbb = WriteDouble(45.55555444123)
    #bbb = WriteInt16(-4434)
    #bbb = WriteBool(False)
    #bbb = WriteByte('p')
    #bbb = WriteCharArray('abc', 7, False)
#     bbb = WriteCharArray(u'畅游', 7, True)
#     print binascii.hexlify(bbb)
#     print "length: " + str(len(bbb))
#     bbb += '1234567890'
#     
#     str1 = binascii.hexlify(bbb)
#     j = 0
#     str2 = ''
#     for i in range(2,len(str1)+2,2):
#         str2 += str1[j:i] + ' '
#         j = i
#     print str2
#     
#     print "start read!!!"
    
    #(value,index) = ReadInt32(bbb,False)
    #(value,index) = ReadSingle(bbb)
    #(value,index) = ReadFloat(bbb)
    #(value,index) = ReadUInt64(bbb,False)
    #(value,index) = ReadInt64(bbb,True)
    #(value,index) = ReadUInt32(bbb)
    #(value,index) = ReadDouble(bbb)
    #(value,index) = ReadInt16(bbb)
    #(value,index) = ReadBytes(bbb,3)
    #(value,index) = ReadCharArray(bbb,7,False)
#     (value,index) = ReadCharArray(bbb,7,True)
#     
#     print len(value)
#     print value
#     print "after buffer :" + index



