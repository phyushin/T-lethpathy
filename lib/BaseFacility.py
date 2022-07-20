# this file contains all the different base facilities
# this gets saved when we call BaseItem.file_save() so we will need to return layouts ar somepoint

class BaseLayout():
    start_offset = 0xDA
    end_offset = 0xFD
    data={}
    layout={}

    def __init__(self, layout_stream):
        self.data=bytearray(layout_stream[self.start_offset:self.end_offset])

    def load_layout(self):
        i = 0
        while i < 6:
            self.layout[i]=self.data[i*6:((i+1)*6)]
            i += 1

        print(self.layout)

    def get_start_offset(self):
        return self.start_offset

    def get_end_offset(self):
        return self.end_offset

    def build_facilites(self):
        pass

    def get_data(self):
        return self.data


class BuildTimeLayout(BaseLayout):
   start_offset = 0xFE
   end_offset = 0x121

   def build_facilities(self):
       self.data= "/x00" * len(self.data)

class Facility():
    x_pos = 0 # X but we're taking top left as the sub pen has 4 parts and is special
    y_pos = 0

    def __init__(self):
        self.val = "\xff"

    def get_value(self):
        return self.val

    def get_x(self):
        return self.x

    def get_y(self):
        return y

    def check_if_space_avail(self, data):
        ret_val = False
        if data[x_pos][x_pos] == "\xff":
            ret_val = True
        return ret_val

    def build_facility(self, x_pos, y_pos, base_layout):
        self.x_pos = x_pos
        self.y_pos = y_pos
        if check_if_space_avail(base_layout):
            print("we can build here")
        else:
            print("we cannot build here")


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

