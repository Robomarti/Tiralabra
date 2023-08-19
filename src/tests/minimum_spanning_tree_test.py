import unittest
from math import sqrt
from logic import minimum_spanning_tree

class TestRoomGenerator(unittest.TestCase):
	def setUp(self):
		pass

	def test_generate_distances(self):
		vertices = [(1,1), (2,2), (3,3)]
		edges = [((1,1),(2,2)), ((1,1),(3,3))]
		distances = minimum_spanning_tree.generate_distances(vertices, edges)[0]
		self.assertEqual(distances[(1,1)], sqrt(2))

	def test_distance(self):
		distance = minimum_spanning_tree.get_distance((4,5), (8,8))
		self.assertEqual(distance, 5)