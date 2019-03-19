import unittest
import lib.save_game_dat_file as datFile

class TestSaveGameDatFile(unittest.TestCase):

	def test_load_file(self):
		test = datFile("../XCOM", 10, True)
		result = test.load_file("../XCOM/GAME_10/LIGLOB.DAT", True)
		self.assertNotEqual(len(result),0)

if __name__ =='__main__':
	unittest.main()