from lib.BaseItem import BaseItem
from lib.SaveGameFile import SaveGameFile

from os import path

# This class handles the base file as a whole including saving and loading all the bases
class BaseGameFile(SaveGameFile):
    base_size = 296

    def __init__(self, file_path):
        self.file_name="BASE.DAT"
        self.file_path=path.join(file_path, self.file_name)
        self.bases = self.__parse_bases__()

    def __parse_bases__(self):
        bases_raw=""
        bases = []

        with open(self.file_path, 'rb') as base_file:
            bases_raw =  base_file.read(-1)
            base_file.close()
        i = 0
        self.data = bytearray(bases_raw)

        while (i < 8):
            start_of_base = i * self.base_size
            i = i + 1
            xcom_base = BaseItem(i, bases_raw[start_of_base:self.base_size*i])
            bases.append(xcom_base)

        return bases

    def update_base(self, base): # don't forget that the base number != base _index_
        self.bases[base.get_base_no()-1].set_base_data(base.get_base_data())

    def save_bases(self):
        self.data = "" # if we don't do this it'll append and crash xD
        for _base in self.bases:
            if len(self.data) <1:
                self.data = _base.get_base_data()
            else:
                self.data = self.data + _base.get_base_data()
        self.save_file()

    def get_bases(self):
        return self.bases

    def print_info(self):
        i = 0
        for base in self.bases:
            print(base.get_info())
