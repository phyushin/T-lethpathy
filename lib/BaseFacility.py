class Facility():
    def __init__(self):
        self.val = "\xff"

    def build(self, layout, time, x, y, force):
        if (not force and self.check_not_building_over(layout, x , y)): #thot how you do and in an if in python ?!?! idk xD
            layout[x-1][y-1] = self.val
            time[x-1][y-1] = "\x00"
        else:
            print("We can't build here")

    def check_not_building_over(self, layout, x, y):
        return (layout[x-1][y-1] == "\xff")

class LivingQuaters(Facility):
    def __init__(self):
        self.val = "\x01"

class Lab(Facility):
    def __init__(self):
        self.val = "\x02"

class Workshop(Facility):
    def __init__(self):
        self.val ="\x03"

class Standard_Sonar(Facility):
    def __init__(self):
        self.val ="\x04"

class Wide_Array_Sonar(Facility):
    def __init__(self):
        self.val ="\x05"

class Torpedo_Defences(Facility):
    def __init__(self):
        self.val ="\x06"

class General_Store(Facility):
    def __init__(self):
        self.val ="\x07"

class Alien_Contain(Facility):
    def __init__(self):
        self.val ="\x08"

class Gauss_Defences(Facility):
    def __init__(self):
        self.val ="\x09"

class Sonic_Defences(Facility):
    def __init__(self):
        self.val ="\x0a"

class PWT_Defences(Facility):
    def __init__(self):
        self.val ="\x0b"

class Bombardment_Shield(Facility):
    def __init__(self):
        self.val ="\x0c"

class MC_Generator(Facility):
    def __init__(self):
        self.val ="\x0d"

class MC_Lab(Facility):
    def __init__(self):
        self.val ="\x0e"

class Transmission_Resolver(Facility):
    def __init__(self):
        self.val ="\x0f"

class SubPen(Facility):
    def __init__(self):
        self.val = "\x10" #top left

    def build(self, layout, time, x, y, force):
        if (not force and self.check_not_building_over(layout, x, y)):
            layout[x-1][y-1] = "\x10"     # top left
            layout[x-1][y] = "\x11"   # top right
            layout[x][y-1] = "\x12"   # bottom left
            layout[x][y] = "\x13" # bottom left
            time[x][y] = "\x00"
            time[x][y-1] = "\x00"
            time[x-1][y] = "\x00"
            time[x-1][y-1] = "\x00"
        else:
            print("I can't build here")

    def check_not_building_over(self, layout, x, y):
        if ((layout[x-1][y-1] == "\xff") and (layout[x-1][y] == "\xff") and (layout[x][y-1] == "\xff") and (layout[x][y] == "\xff")):
            return True # bottom left

