from lib.SaveGameFile import SaveGameFile

# This class will handle per base manipulation
class BaseItem(SaveGameFile):

    def __init__(self, base_no, data):
        self.base_no = base_no
        self.base_index = base_no -1
        self.base_data = bytearray(data)
        self.technician_count = 0
        self.scientist_count = 0

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

    def get_base_no(self):
        return self.base_no

    def get_scientist_count(self):
        return self.__get_staff__(True)

    def get_technician_count(self):
        return self.__get_staff__(False)

    def set_scientist_count(self, count):
        self.__set_staff__(True, count)

    def set_technician_count(self, count):
        self.__set_staff__(False, count)

    def get_base_data(self):
        return self.base_data

    def set_base_data(self, base_data):
        self.base_data = base_data

    def get_info(self):
        base_info = f"Base No:{self.get_base_no()}\nName: {self.get_name().decode(encoding=self.encoding)}\n"
        base_info = f"{base_info}Scientists: {self.get_scientist_count()}\n"
        base_info = f"{base_info}Engineers: {self.get_technician_count()}\n"

        return base_info
