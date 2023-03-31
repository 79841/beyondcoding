class Human:
    def breathe(self):
        raise NotImplementedError


class FootballPlayer(Human):
    def breathe(self):
        print("hoo ha")


Son = FootballPlayer()
Son.breathe()
