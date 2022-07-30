from lib.SaveGameFile import SaveGameFile


class Research(SaveGameFile):
    name = "RESEARCH.DAT"
    data = {}

    def __init__(self, file_path):
        super().__init__(self.name, file_path)

    def print_info(self):
        print(f"{self.data}")


