from lib.SaveGameFile import SaveGameFile
from os import path

class BaseGameFile(SaveGameFile):
    base_size = 0x128

    def __init__(self, file_path):
        self.file_name="BASE.DAT"
        self.data = self.parse_bases(file_path)

    def parse_bases(self, file_path):
        file_path = path.join(file_path, f"{self.file_name}")
        bases_raw=""
        bases = []

        with open(file_path, 'rb') as base_file:
            bases_raw =  base_file.read()
            base_file.close()
        i = 0
        while (i < 8):
            start_of_base = i * self.base_size
            print(f"start of base:{start_of_base}")
            bases.append(bases_raw[start_of_base:self.base_size])
            i = i + 1

        return bases

    def print_info(self):
        i = 0
        for base in self.data:
            i = i+1
            print(f"Base {i}:\n{base}")
