import unittest
from logic import cave_generator
from logic import cellular_automata

class TestCaveGenerator(unittest.TestCase):
	def setUp(self):
		self.cg = cave_generator.CaveGenerator()
		self.cg.map = [[" ", "#", " "],  ["#", " ", "#"], [" ", "#", " "]]

	def test_create_walls(self):
		self.cg.map = [[" ", " ", " "],  [" ", " ", " "], [" ", " ", " "]]
		self.cg.create_walls()
		self.assertEqual(self.cg.map, [["#", "#", "#"],  ["#", " ", "#"], ["#", "#", "#"]])

	def test_generate_blank_map(self):
		self.cg.map = []
		self.cg.change_width_and_length(3,3)
		self.cg.generate_blank_map()
		self.assertEqual(self.cg.map, [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]])