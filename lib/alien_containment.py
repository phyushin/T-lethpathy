class Alien():
    def _init__(self):
        self.race = "\x00"
        self.rank = "\x00"

    def capture(self, containmentspot, rank):
        containmentspot = self.race + self.rank

class Terrorist(Alien):
    def __init__(self):
        self.race = "\x05"
        self.rank = "\x07"

class Aquatoid(Alien):
    def __init__(self):
        self.race = "\x01"
        self.rank = "\x06" #soldier

    def capture_soldier(self, containmentspot):
        self.capture(containmentspot, "\x06")

    def capture_squad_leader(self, containmentspot):
        self.capture(containmentspot, "\x05")
    
    def capture_technician(self, containmentspot):
        self.capture(containmentspot, "\x04")
    
    def capture_medic(self, containmentspot):
        self.capture(containmentspot, "\x03")
    
    def capture_navigator(self, containmentspot):
        self.capture(containmentspot, "\x02")
    
    def capture_commander(self, containmentspot):
        self.capture(containmentspot, "\x01")

class Gill_man(Alien):
    def __init__(self):
        self.race = "\x02"
        self.rank = "\x06" #soldier

    def capture_soldier(self, containmentspot):
        self.capture(containmentspot, "\x06")

    def capture_squad_leader(self, containmentspot):
        self.capture(containmentspot, "\x05")
    
    def capture_technician(self, containmentspot):
        self.capture(containmentspot, "\x04")
    
    def capture_commander(self, containmentspot):
        self.capture(containmentspot, "\x01")

class Lobster_man(Alien):
    def __init__(self):
        self.race = "\x03"
        self.rank = "\x06" #soldier

    def capture_soldier(self, containmentspot):
        self.capture(containmentspot, "\x06")

    def capture_squad_leader(self, containmentspot):
        self.capture(containmentspot, "\x05")
    
    def capture_technician(self, containmentspot):
        self.capture(containmentspot, "\x04")
    
    def capture_navigator(self, containmentspot):
        self.capture(containmentspot, "\x02")
    
    def capture_commander(self, containmentspot):
        self.capture(containmentspot, "\x01")

class Tasoth(Alien):
    def __init__(self):
        self.race = "\x04"
        self.rank = "\x06" #soldier

    def capture_soldier(self, containmentspot):
        self.capture(containmentspot, "\x06")

    def capture_squad_leader(self, containmentspot):
        self.capture(containmentspot, "\x05")


class Calcinite(Terrorist):
    def __init__(self):
        self.race = "\x05"

class Deep_one(Terrorist):
    def __init__(self):
        self.race = "\x06"

class Bio_Drone(Terrorist):
    def __init__(self):
        self.race = "\x07"

class Tentaculat(Terrorist):
    def __init__(self):
        self.race = "\x08"

class Triscene(Terrorist):
    def __init__(self):
        self.race = "\x09"

class Hallucinoid(Terrorist):
    def __init__(self):
        self.race = "\x0a"

class Xarquid(Terrorist):
    def __init__(self):
        self.race = "\x0b"