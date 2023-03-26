'''
=======================================================================
AutoTest Team Source File.
Copyright(C), Changyou.com
-----------------------------------------------------------------------
Created:        
-----------------------------------------------------------------------
Description:    Functions.py
-----------------------------------------------------------------------
History:
=======================================================================
'''

import struct
import NetPackets
import select
import time
import logging
import socket
import binascii
import os
import platform
import gevent


def sendstream(person,packetid,packetsize,stream):
    logger = logging.getLogger('Function sendstream')
    sendstream = binascii.unhexlify('000000000000')
    sendstream += struct.pack("=HI", packetid, packetsize)
    sendstream += stream
    logger.debug('packetid : ' + str(packetid))
    logger.debug('packetsize : ' + str(packetsize))
    logger.debug('stream : ' + binascii.hexlify(stream)) 
    try:
        person['socket'].send(sendstream)
    except socket.error, info:
        (errno, errmsg) = info
        logger.debug( "Sendpacket failed. Socket errno= %d, errmsg = %s" % (errno, errmsg))
        return (False,0,"Sendpacket failed. Socket errno= %d, errmsg = %s" % (errno, errmsg))
    return (True,0,"Sendpacket successfully.")

def sendpacket(packet):
    logger = logging.getLogger('Function sendpacket')


    sendstream = NetPackets.Decr.encr( struct.pack("=I", packet.person['packet_id_index']) + '\x00' * 2)
    packet.person['packet_id_index'] = packet.person['packet_id_index'] + 1



    sendstream += NetPackets.Decr.encr(struct.pack("=HI", packet.getid(), packet.getdatasize()))
    sendstream += NetPackets.Decr.encr(packet.getdatastream())
    if packet.person.getloadflag() == False:
        logger.debug('sendpacket : ' + packet.__class__.__name__ + packet.dump())
        logger.debug('packet stream : ' + binascii.hexlify(sendstream))

    try:
        packet.person['socket'].send(sendstream)
    except socket.error, info:
        (errno, errmsg) = info
        logger.debug( "Sendpacket failed. Socket errno= %d, errmsg = %s" % (errno, errmsg))
        print packet.person['userName']
        print "sendpacket socket error : " + packet.__class__.__name__
        print ("Sendpacket failed. Socket errno= %d, errmsg = %s" % (errno, errmsg))
        raise Exception("sendpacket Failed")        
        #return (False,0,"Sendpacket failed. Socket errno= %d, errmsg = %s" % (errno, errmsg))
    return (True,0,"Sendpacket %s successfully." %(packet.__class__.__name__))

def getpacket(person):
    logger = logging.getLogger('Functions getpacket')
    try:
        buf_len = len(person['inputbuffer'])
        if buf_len < 6 or person['is_packect_truncated'] == True:  

            if person['packet_rec_time'] == 1:
                person['packet_rec_time'] = 0
                return None
            
            recbuf = ''
            with gevent.Timeout(10, False) as timeout:
                recbuf = NetPackets.Decr.decr(person['socket'].recv(655360))
            if len(recbuf) > 0:
                person['inputbuffer'] = person['inputbuffer'] + recbuf
            
            if person['packet_rec_time'] == 0 or person['packet_rec_time'] == None:
                person['packet_rec_time'] = 1

            if person['is_packect_truncated'] == True:
                person['is_packect_truncated'] = False
                    
                    
        buf_len = len(person['inputbuffer'])
        if buf_len >= 6:
            packetid, packetsize = struct.unpack("=HI", person['inputbuffer'][:6])
            packetsize = packetsize & 0xffffff
            packetclass = ""

            if buf_len < (packetsize + 6):
                person['is_packect_truncated'] = True
                return None
            try:                
                packetclass = NetPackets.Defines.PACKET_DEFINE(packetid)
                
            except KeyError, info:            
                logger.debug('Error! Packet is not defined! Packet ID:' + str(packetid))
                logger.debug('ErrorPacket stream:' + binascii.hexlify(person['inputbuffer']))
                person['inputbuffer'] = person['inputbuffer'][packetsize+6:]
                return None
            
            
            if buf_len >= (packetsize + 6):
                if person.getloadflag() == False:
                    logger.debug('Receive packet: ' + packetclass)
                    logger.debug('Receive packet stream : ' + binascii.hexlify(person['inputbuffer']))
                # print ('********: ' + packetclass)
                # print ('********: ' + binascii.hexlify(person['inputbuffer']))
                
                packet = eval('NetPackets.PACKETS.' + packetclass + "(person)")
                
                if person.getloadflag() == False:                
                    packetbuf = person['inputbuffer'][6:packetsize+6]
                    try:
                        packet.filldatafromstream(packetbuf)
                    except:
                        print ('Error! packet.filldatafromstream error :'  + packetclass + " " + binascii.hexlify(person['inputbuffer']))
                    try:
                        logger.debug('packet data : ' + packet.dump())
                    except TypeError,info:
                        print ('Error! Packet dump error :' + str(info) + " " + packetclass + " " + binascii.hexlify(person['inputbuffer']))
                        
                elif hasattr(packet,'handle'):
                    packetbuf = person['inputbuffer'][6:packetsize+6]
                    try:
                        packet.filldatafromstream(packetbuf)
                    except:
                        print ('Error! packet.filldatafromstream error :'  + packetclass + " " + binascii.hexlify(person['inputbuffer']))    
                        
                        
                person['inputbuffer'] = person['inputbuffer'][packetsize+6:]
                return packet 
            else:
                person['is_packect_truncated'] = True
                return None
        else:
            return None
    except  Exception, e:
        print person['userName']
        print Exception
        print e
        raise
   
def handlepacket(packet):
    if hasattr(packet,'handle'):
        packet.handle()
    

def handleinputstream(person):
    while 1:
        packet = getpacket(person)
        if packet == None:
            break
        handlepacket(packet)

def heartbeat(person):
    if not person['heartbeat_time'] == None:
        total_time = int((time.time() - person['heartbeat_time']) * 1000)
        if total_time > 5 * 1000:
        #send heartbeat
            packet = NetPackets.PACKETS.PACKET_CG_HeartBeat(person)
            packet['m_flag'] = 0
            sendpacket(packet)
            person['heartbeat_time'] = time.time()
    else:
        person['heartbeat_time'] = time.time()


        
def waitforpacket(person, packetname, timeout=15):
    logger = logging.getLogger('Functions waitforpacket')
    logger.debug('Wait for packet: ' + packetname)
    latesttime = time.time()
    gevent.sleep(0)
    while 1:
        packet = getpacket(person)
        if packet == None:  
            #print person['inputbuffer']          
            total_time = int((time.time() - latesttime) * 1000)
            if total_time > timeout*1000:
                break
            else:
                gevent.sleep(0)
                continue
        if packet.__class__.__name__ == packetname:
            total_time = int((time.time() - latesttime) * 1000)
            handlepacket(packet)
            return (True, total_time, "Successfully get packet " + packetname)
        else:
            handlepacket(packet)
    return (False, total_time, "Failed get packet " + packetname)

def waitforpacket_with_heartbeat(person, packetname, timeout=15):
    logger = logging.getLogger('Functions waitforpacket')
    logger.debug('Wait for packet: ' + packetname)
    latesttime = time.time()
    gevent.sleep(0)
    while 1:        
        packet = getpacket(person)        
        if packet == None:  
            #print person['inputbuffer']          
            total_time = int((time.time() - latesttime) * 1000)
            if total_time > timeout*1000:
                break
            else:
                gevent.sleep(0)
                heartbeat(person)
                continue
        if packet.__class__.__name__ == packetname:
            total_time = int((time.time() - latesttime) * 1000)
            handlepacket(packet)
            return (True, total_time, "Successfully get packet " + packetname)
        else:
            handlepacket(packet)
    return (False, total_time, "Failed get packet " + packetname)


def get_account_startnumber(startnumber,endnumber):
    sysstr = platform.system()
    if(sysstr =="Windows"):
        tempfile = os.environ["TMP"] + '/locusttempnumber.txt'
    else:
        tempfile = '/tmp/locusttempnumber.txt'
    try:
        outputfile = open(tempfile,'r')
        cur_number = int(outputfile.readline())
        if cur_number >= endnumber:
            next_number = startnumber
        elif cur_number < startnumber:
            next_number = startnumber
        else:
            next_number = cur_number + 1
        outputfile.close()
        outputfile = open(tempfile,'w')
        outputfile.write(str(next_number))
        outputfile.close()
        return next_number
    except IOError:
        outputfile = open(tempfile,'w')
        outputfile.write(str(startnumber))
        outputfile.close()
        return int(startnumber)
    
TRIGGER_INDEX = False
TRIGGER_FILE = ''
if(platform.system() =="Windows"):
    TRIGGER_FILE = os.environ["TMP"] + '/locusttemptrigger.txt'
else:
    TRIGGER_FILE = '/tmp/locusttemptrigger.txt'
if os.path.exists(TRIGGER_FILE):
    os.remove(TRIGGER_FILE)
    
def is_trigger_start():
    global TRIGGER_INDEX
    global TRIGGER_FILE
    if TRIGGER_INDEX == False:
        if os.path.exists(TRIGGER_FILE):
            TRIGGER_INDEX = True
            return True
        else:
            return False
    else:
        return True





