import Actions
import time
import gevent
import login

class disconnect():
    def __init__(self, person):
        self.person = person   
              
    def run(self,sec):
        self.person['socket'].close()
        gevent.sleep(sec)       
        return(True, 0, "disconnect+______________________________________________")