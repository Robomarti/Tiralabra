import unittest
from logic import delaunay_triangulation
from datatypes.rooms import Rooms

class TestDungeonGenerator(unittest.TestCase):
	def setUp(self):
		self.dt = delaunay_triangulation.DelaunayTriangulation()
		self.rooms = [Rooms((1,1),(2,2),[],[],0),Rooms((3,3),(4,4),[],[],0),Rooms((5,5),(6,6),[],[],0),Rooms((7,7),(8,8),[],[],0)]
		self.dt.add_rooms(self.rooms)

