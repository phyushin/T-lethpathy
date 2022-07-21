from lib.SaveGameFile import SaveGameFile
from os import path

class Rank():

    def terrorist(self):
        return "\x07"

    def soldier(self):
        return "\x06"

    def squad_leader(self):
        return "\x05"

    def technician(self):
        return "\x04"

    def medic(self):
        return "\x03"

    def navigator(self):
        return "\x02"

    def commander(self):
        return "\x01"

class AlienContainment(SaveGameFile):
    _start_offset = 0x00
    _end_offset = 0x0C
    data={}
    layout={}

    def __init__(self, file_path):
        self.file_name="ASTORE.DAT"
        self.file_path=path.join(file_path, self.file_name)
        self.load_file()

    def get_containment(self):
        return self.data

    def capture_alien(self, position, alien, base_no):
        base_idx = base_no -1
        _start_pos = (position-1)*12

        print(_start_pos)
        print(alien.get_data())

        _captured = alien.get_data() + base_idx.to_bytes(1, 'little') + "\x00".encode(encoding=self.encoding)*12
        _captured = _captured[0:12]
        print(_captured)
        self.data[_start_pos:_start_pos+12] = _captured
        self.save_file()


class Alien(): ## 12 bytes between each capture
    encoding='UTF-8'
    def __init__(self):
        self.race = "\x00"
        self.rank = "\x00"
        self.base = "\x00"

    def get_data(self):
        return self.race.encode(encoding=self.encoding) + self.rank.encode(encoding=self.encoding)

    def capture(self, containmentspot, rank):
        containmentspot = self.race + self.rank

    def set_rank(self, rank):
        self.rank = rank

class Aquatoid(Alien):
    def __init__(self):
        self.race = "\x01"
        self.rank = "\x06" #soldier

class Gill_man(Alien):
    def __init__(self):
        self.race = "\x02"
        self.rank = "\x06" #soldier

class Lobster_man(Alien):
    def __init__(self):
        self.race = "\x03"
        self.rank = "\x06" #soldier

class Tasoth(Alien):
    def __init__(self):
        self.race = "\x04"
        self.rank = "\x06" #soldier

class Calcinite(Alien):
    def __init__(self):
        self.race = "\x05"
        self.rank = "\x07"

class DeepOne(Alien):
    def __init__(self):
        self.race = "\x06"
        self.rank = "\x07"

class Bio_Drone(Alien):
    def __init__(self):
        self.race = "\x07"
        self.rank = "\x07"

class Tentaculat(Alien):
    def __init__(self):
        self.race = "\x08"
        self.rank = "\x07"

class Triscene(Alien):
    def __init__(self):
        self.race = "\x09"
        self.rank = "\x07"

class Hallucinoid(Alien):
    def __init__(self):
        self.race = "\x0a"
        self.rank = "\x07"

class Xarquid(Alien):
    def __init__(self):
        self.race = "\x0b"
        self.rank = "\x07"
