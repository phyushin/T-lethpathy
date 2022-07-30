from lib.SaveGameFile import SaveGameFile
# from lib.Stores import BaseStores as Stores
from lib.BaseFacility import Facility, BaseLayout, BuildTimeLayout

# This class will handle per base manipulation
class BaseItem(SaveGameFile):

    def __init__(self, base_no, data):
        self.base_no = base_no
        self.base_index = base_no -1
        self.base_data = bytearray(data)
        self.technician_count = 0
        self.scientist_count = 0
        self.layout = {}
        self.build_times = {}
        self.stores = {}

### base
    def __get_staff__(self, is_scientist):
        if is_scientist:
            return list(self.base_data[291:292])[0]
        else:
            return list(self.base_data[290:291])[0]

    def __set_staff__(self, is_scientist, count):
        count = count % 256
        count = count.to_bytes(1,'little')
        if is_scientist:
            self.base_data[291:292] = count
        else:
            self.base_data[291:292] = count

    def get_name(self):
        return bytes(self.base_data[0:12])

    def set_name(self, name):
        filler = "\x00"
        name = f"{name}{filler*12}" # don't ask xD
        trunc_name = name[0:12] #base names can be 12 chars max so truncate.
        self.base_data[0:12] = trunc_name.encode(encoding=self.encoding)
        print(f"Base renamed to: {trunc_name}")

    def get_base_no(self):
        return self.base_no

    def get_scientist_count(self):
        return self.__get_staff__(True)

    def get_technician_count(self):
        return self.__get_staff__(False)

    def set_scientist_count(self, count):
        print(f"Setting scientist count to: {count}")
        self.__set_staff__(True, count)

    def set_technician_count(self, count):
        self.__set_staff__(False, count)

#### BASE LAYOUT

    def load_layout(self):
        # base layout is a 6x6 grid
        # starting at 218 bytes in and then 36 bytes later ... the build times for each of these items is listed
        self.layout = BaseLayout(self.base_data)
        self.build_times = BuildTimeLayout(self.base_data)

    def save_layout(self):
        self.base_data[self.layout.get_start_offset():self.layout.get_end_offset()] = self.layout.get_layout()
        self.base_data[self.build_times.get_start_offset():self.build_times.get_end_offset()]= self.build_times.get_layout()

    def get_layout(self):
        return self.layout.get_data()

    def get_data(self):
        return self.base_data

    def get_construction_time_layout(self):
        return self.build_times.get_data()

    def build_facility(self, x_pos, y_pos, facility): # this logic needs to go the other way to normal grid ref we need to know which row we're on before cols (x before y)
        _start_offset = self.layout.get_start_offset()
        _end_offset = self.layout.get_end_offset()

        self.load_layout() # ensure base layout and times are loaded
        self.layout.load_grid()
        _layout = self.layout.get_grid()
        # perhaps we need to do it bit by bit?
        _row = list(_layout[y_pos-1])
        _row[x_pos-1] = int.from_bytes(facility.get_value(), 'little') # the first row in each of these will be the index so that isn't right
        _layout[y_pos-1] = bytearray(_row)
        self.layout.set_grid(_layout)
        self.base_data[_start_offset:_end_offset] = self.layout.get_data()
        self.build_facilities()

    def build_facilities(self): ## just mark everything as fully built
        new_build_times = "\x00"*35
        _start_offset = self.build_times.get_start_offset()
        _end_offset = self.build_times.get_end_offset()
        self.base_data[_start_offset:_end_offset] = bytearray(new_build_times.encode(encoding=self.encoding))
        print("removed build times")

    def set_base_data(self, base_data):
        self.base_data = base_data

    def get_stores(self):
        return self.stores

    def set_stores(self, items):
        for item in items:
            _start_pos = item.get_location()
            self.base_data[_start_pos:_start_pos+2] =item.get_qty()

    def get_info(self):
        base_info = f"Base No:{self.get_base_no()}\nName: {self.get_name().decode(encoding=self.encoding)}\n"
        base_info = f"{base_info}Scientists: {self.get_scientist_count()}\n"
        base_info = f"{base_info}Engineers: {self.get_technician_count()}\n"

        return base_info
