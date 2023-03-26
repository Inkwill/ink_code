import Functions


class ACGIdle():
    def __init__(self, person):
        self.person = person

    def run(self):
        Functions.handleinputstream(self.person)
        Functions.heartbeat(self.person)

        return (True, 0, "Adle action performed.")

