import unittest
from logic.flood_fill import flood_fill

class TestRooms(unittest.TestCase):
	def setUp(self):
		self.game_map = [
			["#","#","#","#"],
			["#","#",".","#"],
			["#"," ",".","#"],
			["#"," "," ","#"],
			["#","#",".","#"],
			["#","#","#","#"]]

	def test_flood_fill(self):
		"""Unvisited cells stay the same"""
		filled_map = flood_fill(self.game_map, (2,2))
		correct_map = [
			["#","#",'\u001b[0;37;40m#',"#"],
			["#",'\u001b[0;37;40m#','\u001b[0;37;43m.','\u001b[0;37;40m#'],
			['\u001b[0;37;40m#','\u001b[0;34;44m ','\u001b[0;37;43m.','\u001b[0;37;40m#'],
			['\u001b[0;37;40m#','\u001b[0;34;44m ','\u001b[0;34;44m ','\u001b[0;37;40m#'],
			["#",'\u001b[0;37;40m#','\u001b[0;37;43m.','\u001b[0;37;40m#'],
			["#","#",'\u001b[0;37;40m#',"#"]]
		self.assertEqual(filled_map, correct_map)