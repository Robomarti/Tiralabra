import unittest
from logic import automata

class TestCaveGenerator(unittest.TestCase):
	def setUp(self):
		self.cg = automata.CaveGenerator()
		self.cg.map = [[" ", "x", " "],  ["x", " ", "x"], [" ", "x", " "]]

	def test_wall_count(self):
		wall_count = self.cg.wall_count(1,1)
		self.assertEqual(wall_count, 4)
