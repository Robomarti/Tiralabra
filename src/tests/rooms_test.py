import unittest
from datatypes.rooms import Rooms, find_room_by_center
from datatypes.coordinates import Coordinates

class TestRooms(unittest.TestCase):
	def setUp(self):
		self.room_list = [Rooms(Coordinates(1,1), [(0,0),(0,1)], [], None), 
		    Rooms(Coordinates(3,3), [(2,2),(3,2)], [], None), Rooms(Coordinates(5,5), [(4,4),(6,6)], [], None)]
		self.room = Rooms(Coordinates(5,5), [(4,4),(6,6)], [(1,1),(3,3)], None)

	def test_find_center_when_in(self):
		center = (3,3)
		found = find_room_by_center(center, self.room_list)
		self.assertEqual(found, Rooms(Coordinates(3,3), [(2,2),(3,2)], [], None))

	def test_find_center_when_not_in(self):
		center = (4,4)
		found = find_room_by_center(center, self.room_list)
		self.assertIsNone(found)
