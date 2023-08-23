import unittest
from datatypes.rooms import Rooms, find_room_by_cell, is_own_room
from datatypes.coordinates import Coordinates

class TestRooms(unittest.TestCase):
	def setUp(self):
		self.room_list = [Rooms(Coordinates(1,1), [(0,0),(0,1)], [], None), 
		    Rooms(Coordinates(3,3), [(2,2),(3,2)], [], None), Rooms(Coordinates(5,5), [(4,4),(6,6)], [], None)]
		self.room = Rooms(Coordinates(5,5), [(4,4),(6,6)], [(1,1),(3,3)], None)

	def test_find_room_by_cell_when_found(self):
		cell = (0,0)
		found = find_room_by_cell(cell, self.room_list)
		self.assertTrue(isinstance(found, Rooms))

	def test_find_room_by_cell_when_not_found(self):
		cell = (10,10)
		found = find_room_by_cell(cell, self.room_list)
		self.assertFalse(isinstance(found, Rooms))

	def test_is_own_room_when_is(self):
		cell = (0,0)
		found = is_own_room(cell, (1,1), self.room_list)
		self.assertTrue(found)

	def test_is_own_room_when_not(self):
		cell = (2,2)
		found = is_own_room(cell, (1,1), self.room_list)
		self.assertFalse(found)

	def test_is_own_room_when_not_exists(self):
		cell = (10,10)
		found = is_own_room(cell, (1,1), self.room_list)
		self.assertFalse(found)