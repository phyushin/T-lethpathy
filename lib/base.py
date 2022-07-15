from lib.BaseItem import BaseItem
from lib.SaveGameFile import SaveGameFile

from os import path

class BaseGameFile(SaveGameFile):
    base_size = 0x128

    def __init__(self, file_path):
        self.file_name="BASE.DAT"
        self.bases = self.__parse_bases__(file_path)

    def __parse_bases__(self, file_path):
        file_path = path.join(file_path, f"{self.file_name}")
        bases_raw=""
        bases = []

        with open(file_path, 'rb') as base_file:
            bases_raw =  base_file.read(-1)
            base_file.close()
        i = 0

        while (i < 8):
            start_of_base = i * self.base_size
            i = i + 1
            xcom_base = BaseItem(i, bases_raw[start_of_base:self.base_size*i])
            bases.append(xcom_base)

        return bases

    def get_bases(self):
        return self.bases

    def print_info(self):
        i = 0
        for base in self.bases:
            print(base.get_info())
