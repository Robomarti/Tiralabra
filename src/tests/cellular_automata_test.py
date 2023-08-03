import unittest
from logic import dungeon_generation
from logic import cellular_automata

class TestCellularAutomata(unittest.TestCase):
	def setUp(self):
		self.cg = dungeon_generation.DungeonGenerator()
		self.cg.map = [[" ", "#", " "],  ["#", " ", "#"], [" ", "#", " "]]

	def test_wall_count(self):
		wall_count = cellular_automata.wall_count(self.cg.map,1,1)
		self.assertEqual(wall_count, 4)
		self.cg.map = [["#", " ", "#"],  [" ", "#", " "], ["#", " ", "#"]]
		wall_count2 = cellular_automata.wall_count(self.cg.map,1,1)
		self.assertEqual(wall_count2, 4)

	def test_cellular_automata_not_changing(self):
		cellular_automata.cellular_automata(self.cg.map, 3, 3)
		self.assertEqual(self.cg.map, [[" ", "#", " "],  ["#", " ", "#"], [" ", "#", " "]])
		self.cg.map = [["#", " ", "#"],  [" ", "#", " "], ["#", " ", "#"]]
		cellular_automata.cellular_automata(self.cg.map, 3, 3)
		self.assertEqual(self.cg.map, [["#", " ", "#"],  [" ", "#", " "], ["#", " ", "#"]])

	def test_cellular_automata_changing(self):
		self.cg.map = [["#", "#", "#"],  ["#", " ", "#"], [" ", "#", " "]]
		cellular_automata.cellular_automata(self.cg.map, 3, 3)
		self.assertEqual(self.cg.map, [["#", "#", "#"],  ["#", "#", "#"], [" ", "#", " "]])