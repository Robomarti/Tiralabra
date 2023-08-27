import unittest
from math import sqrt
from logic import minimum_spanning_tree

class TestRoomGenerator(unittest.TestCase):
	def setUp(self):
		pass

	def test_distance(self):
		distance = minimum_spanning_tree.get_distance((4,5), (8,8))
		self.assertEqual(distance, 5)