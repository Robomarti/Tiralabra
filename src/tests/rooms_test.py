import unittest
from datatypes.rooms import Rooms, find_room_by_center, find_longest_path, distance_to_root
from datatypes.coordinates import Coordinates

class TestRooms(unittest.TestCase):
	def setUp(self):
		self.room_list = [Rooms(Coordinates(1,1), [(0,0),(0,1)], [], None), 
		    Rooms(Coordinates(3,3), [(2,2),(3,2)], [], None),
		    Rooms(Coordinates(5,5), [(4,4),(6,6)], [], None),
		    Rooms(Coordinates(7,7), [(4,4),(6,6)], [], None)]

	def test_find_center_when_in(self):
		center = (3,3)
		found = find_room_by_center(center, self.room_list)
		self.assertEqual(found, Rooms(Coordinates(3,3), [(2,2),(3,2)], [], None))

	def test_find_center_when_not_in(self):
		center = (4,4)
		found = find_room_by_center(center, self.room_list)
		self.assertIsNone(found)

	def test_find_longest_path(self):
		"""Connect every room and finds the two most distant"""
		for room1 in self.room_list:
			for room2 in self.room_list:
				if room1 != room2:
					room1.connected_rooms.append(room2)

		most_distant = find_longest_path(self.room_list)
		self.assertEqual(most_distant[0].center_point, self.room_list[3].center_point)
		self.assertEqual(most_distant[1].center_point, self.room_list[0].center_point)

	def test_distance_to_root(self):
		for i in range(1,len(self.room_list)):
			self.room_list[i].parent = self.room_list[i-1]
		dist = distance_to_root(self.room_list[3], self.room_list[3].parent)
		correct_dist = (2+2) + (2+2) + (2+2)
		self.assertEqual(dist, correct_dist)