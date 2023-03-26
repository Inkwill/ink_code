import random
import binascii

class AattackRandom():
    def __init__(self, person):
        self.person = person        
        
    def run(self):
        packetsize = random.randint(1,300)
        sendbuf = ''
        for j in range(0,packetsize):
            randbyte = random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF')
            sendbuf += binascii.unhexlify(randbyte)

        self.person['socket'].send(sendbuf)
        return (True,0,"Send random attack successfully.")