import unittest
import math
from logic import delaunay_triangulation
from datatypes.rooms import Rooms
from datatypes.coordinates import Coordinates

class TestDungeonGenerator(unittest.TestCase):
	def setUp(self):
		self.rooms = [Rooms(Coordinates(2,2),[],[]),Rooms(Coordinates(4,4),[],[]),Rooms(Coordinates(6,6),[],[]),Rooms(Coordinates(8,8),[],[]),Rooms(Coordinates(50,50),[],[])]
