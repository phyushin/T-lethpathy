from os import path
from pathlib import Path as plib

class SaveGameFile():
    encoding='utf-8'

    def __init__ (self, file_name, file_path):
        self.file_name=file_name
        self.file_path=path.join(file_path, file_name)
        self.data = {}

    def check_file_exists(file_path):
        p = plib(file_path)
        ret_val = False
        if  p.is_dir():
            ret_val = True

        return ret_val

    def load_file(self):
        if not self.check_file_exists:
            print(f"Could not parse file at {self.file_path}")
            return

        data_raw=""

        with open(self.file_path, 'rb') as raw_file:
            data_raw =  raw_file.read(-1)
            raw_file.close()
            self.data = bytearray(data_raw)

    def save_file(self):
        with open(self.file_path, 'wb') as out_file:
            for byte in bytes(self.data):
                out_file.write(byte.to_bytes(1,byteorder='little'))
            out_file.close()

    def get_info(self):
        return f"Name:\n{self.file_name}\nFull path:\n{self.file_path}\nData:\n{self.data}"

