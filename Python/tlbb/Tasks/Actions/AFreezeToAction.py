
class AFreezeToAction():
    def __init__(self, person):
        self.person = person        
        
    def run(self,*args):
        self.person.taskqueue_cleanup()
        self.person.taskqueue_append(*args)

        return (True, 0, "AFreezeAction action performed.")
        