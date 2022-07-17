from lib.SaveGameFile import SaveGameFile
from os import path

class LiGlob(SaveGameFile):

    def __init__ (self, file_path):
        self.max_money = int(((2**32)/2)-1) # 32-bit signed int
        self.file_name = "LIGLOB.DAT"
        self.file_path = path.join(file_path, self.file_name)

    def set_money(self, money):
        if (money > self.max_money):
            money = self.max_money

        self.data[0:4] = money.to_bytes(4, 'little')
        self.save_file()

    def set_max_money(self):
        self.set_money(self.max_money)

    def get_money(self):
        return int.from_bytes(self.data[0:4], 'little')
