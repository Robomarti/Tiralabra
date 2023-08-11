import unittest
from logic import dungeon_generation

class TestDungeonGenerator(unittest.TestCase):
	def setUp(self):
		self.dg = dungeon_generation.DungeonGenerator()
		self.dg.map = [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]]

	def test_generate_blank_map(self):
		self.dg.map = []
		self.dg.change_width_and_length(3,3)
		self.dg.generate_blank_map()
		self.assertEqual(self.dg.map, [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]])
