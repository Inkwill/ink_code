import gevent

class tm_notallmatching():
    def __init__(self, person):
        self.person = person

    def run(self):
        if self.person['notallmatchstate'] == 'start':
            self.person.ACGOperPlatform()
            self.person.ACGIdle()
            self.person['notallmatchstate'] = 'matching'
        elif self.person['notallmatchstate'] == 'matching':
            self.person.ACGAskTeamInfo()
            gevent.sleep(2)
            self.person.ACGIdle()
        elif self.person['notallmatchstate'] == 'end':
            #self.person.ACGIdle()
            self.person.ACGTeamLeave()
            self.person['notallmatchstate'] = 'start'