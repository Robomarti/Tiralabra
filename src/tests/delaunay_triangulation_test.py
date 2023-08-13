import unittest
import math
from logic import delaunay_triangulation
from datatypes.rooms import Rooms
from datatypes.coordinates import Coordinates

class TestDungeonGenerator(unittest.TestCase):
	def setUp(self):
		self.dt = delaunay_triangulation.DelaunayTriangulation()
		self.rooms = [Rooms(Coordinates(2,2),[],[]),Rooms(Coordinates(4,4),[],[]),Rooms(Coordinates(6,6),[],[]),Rooms(Coordinates(8,8),[],[]),Rooms(Coordinates(50,50),[],[])]
		self.dt.add_rooms(self.rooms)

	def test_distance_of_two_points(self):
		room1 = Rooms(Coordinates(3,2), [], [])
		room2 = Rooms(Coordinates(7,8), [], [])
		result = self.dt.distance_of_two_points(room1, room2)
		self.assertEqual(result, 2*math.sqrt(13))
		room1 = Rooms(Coordinates(3,2), [], [])
		room2 = Rooms(Coordinates(7,10), [], [])
		result = self.dt.distance_of_two_points(room1, room2)
		self.assertEqual(result, 4*math.sqrt(5))

	def test_generate_distances(self):
		self.dt.generate_distances(self.rooms)
		self.dt.connect_points()
		paths = self.dt.get_paths()
		self.assertEqual(paths[0], ((2,2),(4,4)))