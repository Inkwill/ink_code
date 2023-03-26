import gevent

class tm_matching():
    def __init__(self, person):
        self.person = person

    def run(self):
        if self.person['matchstate'] == 'start':
            self.person.ACGOperPlatform()
            self.person.ACGIdle()
            self.person['matchstate'] = 'matching'
        elif self.person['matchstate'] == 'matching':
            self.person.ACGAskTeamInfo()
            self.person.ACGIdle()
        elif self.person['matchstate'] == 'end':
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGIdle()
            gevent.sleep(2)
            self.person.ACGTeamLeave()
            self.person['matchstate'] = 'start'




