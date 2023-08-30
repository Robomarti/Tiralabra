import unittest
from math import sqrt
from logic import minimum_spanning_tree

class TestRoomGenerator(unittest.TestCase):
	def test_distance(self):
		distance = minimum_spanning_tree.get_distance((4,5), (8,8))
		self.assertEqual(distance, 5)
	
	def test_prims_algorithm(self):
		"""Calculated by hand"""
		paths = [((20,20),(20,25)),((20,20),(25,20)),((20,25),(25,20)),((25,20),(28,23)),((28,23),(28,27)),((20,20),(25,31)),((25,31),(28,27))]
		prim_paths = minimum_spanning_tree.prim(paths)
		should_be_paths = [((20,20),(20,25)),((20,20),(25,20)),((25,20),(28,23)),((28,23),(28,27)),((25,31),(28,27))]
		self.assertEqual(prim_paths, should_be_paths)