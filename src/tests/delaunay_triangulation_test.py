import unittest
from logic import delaunay_triangulation
from datatypes.rooms import Rooms
from datatypes.coordinates import Coordinates
from datatypes.triangle import Triangle

class TestDungeonGenerator(unittest.TestCase):
	def setUp(self):
		pass

	def test_edge_not_in_when_not_in(self):
		own_triangle = Triangle(Coordinates(1,1),Coordinates(2,2),Coordinates(3,3))
		edge = (Coordinates(1,1),Coordinates(2,2))
		bad_triangles = [own_triangle, Triangle(Coordinates(2,2), Coordinates(3,3), Coordinates(4,4))]
		not_in = delaunay_triangulation.edge_not_in_other_bad_triangles(own_triangle, edge, bad_triangles)
		self.assertEqual(not_in, True)

	def test_edge_not_in_when_in(self):
		own_triangle = Triangle(Coordinates(1,1),Coordinates(2,2),Coordinates(3,3))
		edge = (Coordinates(1,1),Coordinates(2,2))
		bad_triangles = [own_triangle, Triangle(Coordinates(1,1), Coordinates(2,2), Coordinates(4,4))]
		not_in = delaunay_triangulation.edge_not_in_other_bad_triangles(own_triangle, edge, bad_triangles)
		self.assertEqual(not_in, False)