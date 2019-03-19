from lib.SaveGameDatFile import SaveGameDatFile
from lib.XcomEnums import Save_Game_Constants as Consts

class BaseDatFile(SaveGameDatFile):
	buffer = ""
	
	def __init__(self, path, game_slot, verbose):
		self.path = "{0}//GAME_{1}//BASE.DAT".format(path, game_slot)
		buffer = super().load_file(self.path, verbose)
		#base_slice = slice(1,len(buffer),Consts.Base_Length)
		#bases = {}
		#bases[]
