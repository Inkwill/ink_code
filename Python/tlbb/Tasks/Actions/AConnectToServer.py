import socket
import logging
import time
import gevent

class AConnectToServer():
    def __init__(self, person):
        self.person = person        
        
    def run(self, ip, port):
        logger = logging.getLogger('AConnectToServer')
        self.person['socket'] = gevent.socket.socket()
        self.person['socket'].connect((ip,port))
        gevent.sleep(5)
        logger.debug("AConnectToServer successfully. Connet IP = %s, port = %d" % (ip, port))        
        self.person['packet_id_index'] = 0
        return(True, 0, "AConnectToServer successfully. Connet IP = %s, port = %d" % (ip, port))