import random
import binascii
import Functions

class ALoginAttackRandom():
    def __init__(self, person):
        self.person = person        
        
    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)  
        
        packetsize = random.randint(0,100)
        sendbuf = ''
        for j in range(0,packetsize):
            randbyte = random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF')
            sendbuf += binascii.unhexlify(randbyte)
            
        self.person['socket'].send(sendbuf)         
        return (True,0,"Send random login attack successfully.")