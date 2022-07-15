from lib.SaveGameFile import SaveGameFile

class BaseItem(SaveGameFile):
    encoding='utf-8'

    def __init__(self, base_no, data):
        self.base_number = base_no
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
        print(count)
        count = str(count % 255)
        print(count)
        count = count.encode(encoding=self.encoding)

        if is_scientist:
            self.base_data[291:292] = count
        else:
            self.base_data[291:292] = count

    def name(self):
        return bytes(self.base_data[0:12])

    def set_name(self, name):
        filler = "\x00"
        name = f"{name}{filler*12}" # don't ask xD
        trunc_name = name[0:12] #base names can be 12 chars max so truncate.
        self.base_data[0:12] = trunc_name.encode(encoding=self.encoding)

    def get_scientist_count(self):
        return self.__get_staff__(True)

    def get_technician_count(self):
        return self.__get_staff__(False)


    def set_scientist_count(self, count):
        self.__set_staff__(True, count)

    def set_technician_count(self, count):
        self.__set_staff__(False, count)

    def get_info(self):
        base_data = f"Base No:{self.base_number}\nName: {self.name().decode(encoding=self.encoding)}\n"
        base_data = f"{base_data}Scientists: {self.get_scientist_count()}\n"
        base_data = f"{base_data}Engineers: {self.get_technician_count()}\n"

        return base_data
