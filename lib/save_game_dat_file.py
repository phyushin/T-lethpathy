#XCOM Savegame file
import binascii
from lib.xcom_enums import SaveGameConstants as SGConsts

class SaveGameDatFile:
	def __init__(self, path, game, verbose):
		self.path = path
		self.game = game
		self.verbose = verbose

	def load_file(self, path, verbose):
		if verbose:
			message = "Loading Game Slot: {}".format(self.path)
		else:
			message = "Loading Selected Game Slot"
		print(path)
		with open(path,"rb") as f:
			buffer = f.read()
		
		print(message)
		#print(buffer)
		return buffer

	def add_cash(self):
		path = "{0}\\Game_{1}\\LIGLOB.DAT".format(self.path, self.game)
		print("Patching Money")
		buffer = self.load_file(path, self.verbose)
		self.patch_file(buffer, 0, SGConsts.Max_Cash)

    #def patch_file(self, buffer, offset, value):
    #	return foo

	def read_data(self, buffer):
		if len(buffer) < 1 :
			print("error reading data")
		else:
			print("go do")