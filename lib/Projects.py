from lib.SaveGameFile import SaveGameFile
import path from os

class Projects(SaveGameFile):
    name="PROJECT.DAT"
    data= {}

    def __init__(self, file_path):
        super().__init__(self.name, file_path)
