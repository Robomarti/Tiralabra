import unittest
from math import sqrt
from logic import minimum_spanning_tree

class TestRoomGenerator(unittest.TestCase):
	def test_distance(self):
		distance = minimum_spanning_tree.get_distance((4,5), (8,8))
		self.assertEqual(sqrt(distance), 5)
	
	def test_prims_algorithm(self):
		"""Calculated by hand"""
		paths = [((20,20),(20,25)),((20,20),(25,20)),((20,25),(25,20)),((25,20),(28,23)),((28,23),(28,27)),((20,20),(25,31)),((25,31),(28,27))]
		prim_paths = minimum_spanning_tree.prim(paths)
		should_be_paths = [((20,20),(20,25)),((20,20),(25,20)),((25,20),(28,23)),((28,23),(28,27)),((25,31),(28,27))]
		self.assertEqual(prim_paths, should_be_paths)

	def test_prims_algorithm_2(self):
		"""Calculated by hand"""
		paths = [((1,1),(4,5)),((1,1),(1,6)),((1,1),(6,1)),((1,6),(4,5)),((1,6),(3,10)),((4,5),(3,10)),((4,5),(6,1)),((4,5),(7,4)),((7,4),(11,5)),((6,1),(11,1)),((6,1),(7,4)),
		   ((6,1),(11,5)),((11,1),(11,5)),((11,1),(14,6)),((14,6),(11,5)),((14,6),(11,10)),((7,4),(8,8)),((1,1),(4,5)),((8,8),(3,10)),((8,8),(11,10)),((3,10),(11,10))]
		prim_paths = minimum_spanning_tree.prim(paths)
		should_be_paths = [((1,1),(4,5)),((1,6),(4,5)),((4,5),(7,4)),((6,1),(7,4)),((7,4),(11,5)),((14,6),(11,5)),((11,1),(11,5)),((7,4),(8,8)),((8,8),(11,10)),((1,6),(3,10))]
		self.assertEqual(prim_paths, should_be_paths)

	def test_all_vertices_in_result(self):
		"""Calculated by hand"""
		paths = [((3,5),(8,4)),((3,5),(7,5)),((7,5),(9,9)),((8,4),(11,19)),((11,19),(25,6)),((11,19),(12,22)),((9,9),(10,10))]
		vertices = [(3,5),(8,4),(7,5),(9,9),(11,19),(25,6),(12,22),(10,10)]
		prim_paths = minimum_spanning_tree.prim(paths)
		vertices_after_prim = []
		for path in prim_paths:
			if path[0] not in vertices_after_prim:
				vertices_after_prim.append(path[0])
			if path[1] not in vertices_after_prim:
				vertices_after_prim.append(path[1])
			
		self.assertEqual(vertices.sort(), vertices_after_prim.sort())
