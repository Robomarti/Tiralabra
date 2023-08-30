import unittest
from logic import delaunay_triangulation
from datatypes.rooms import Rooms
from datatypes.coordinates import Coordinates
from datatypes.triangle import Triangle

class TestDelaunayTriangulation(unittest.TestCase):
	def setUp(self):
		self.rooms = [Rooms(Coordinates(8,11), [], [], None),
		Rooms(Coordinates(10,7), [], [], None),
		Rooms(Coordinates(4,15), [], [], None),
		Rooms(Coordinates(16,7), [], [], None)]
		self.coordinates = [Coordinates(8,11), Coordinates(10,7), Coordinates(4,15), Coordinates(16,7)]

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

	def test_delaunay(self):
		"""Tests delaunay with a set of rooms that did not result in a correct
		triangulation before, due to a circumcircle not fitting on the the checking area."""
		triangulation = delaunay_triangulation.delaunay_triangulation(self.coordinates, 20, 20)
		t1 = [Coordinates(10,7),Coordinates(8,11),Coordinates(4,15)]
		t2 = [Coordinates(8,11),Coordinates(10,7),Coordinates(16,7)]
		t3 = [Coordinates(8,11),Coordinates(4,15),Coordinates(16,7)]

		for i in range(len(triangulation)):
			triangulation[i] = triangulation[i].corners

		self.assertEqual(triangulation, [t1,t2,t3])

	def test_with_degenerate_points(self):
		"""The Bowyer-Wattson algorithm does not work with degenerate point set"""
		coordinates = [Coordinates(8,1), Coordinates(10,1), Coordinates(4,1)]
		triangulation = delaunay_triangulation.delaunay_triangulation(coordinates, 20, 20)
		self.assertEqual(triangulation, [])
