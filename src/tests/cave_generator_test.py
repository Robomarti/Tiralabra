import unittest
from logic import cave_generator

class TestCaveGenerator(unittest.TestCase):
	def setUp(self):
		self.cg = cave_generator.CaveGenerator()
		self.cg.map = [[" ", "#", " "],  ["#", " ", "#"], [" ", "#", " "]]

	def test_wall_count(self):
		wall_count = self.cg.wall_count(1,1)
		self.assertEqual(wall_count, 4)
		self.cg.map = [["#", " ", "#"],  [" ", "#", " "], ["#", " ", "#"]]
		wall_count2 = self.cg.wall_count(1,1)
		self.assertEqual(wall_count2, 4)

	def test_create_walls(self):
		self.cg.map = [[" ", " ", " "],  [" ", " ", " "], [" ", " ", " "]]
		self.cg.create_walls()
		self.assertEqual(self.cg.map, [["#", "#", "#"],  ["#", " ", "#"], ["#", "#", "#"]])
