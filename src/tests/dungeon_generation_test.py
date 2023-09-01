import unittest
from logic import dungeon_generation
from datatypes.coordinates import Coordinates
from datatypes.rooms import Rooms

class TestDungeonGenerator(unittest.TestCase):
	def setUp(self):
		self.dg = dungeon_generation.DungeonGenerator()
		self.dg.map = [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]]
		self.dg.width = 3
		self.dg.length = 3
		self.paths = [((0,0),(1,0)),((0,2),(2,2))]

	def test_generate_blank_map(self):
		self.dg.map = []
		
		self.dg.generate_blank_map()
		self.assertEqual(self.dg.map, [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]])

	def test_remove_duplicates_from_paths(self):
		self.dg.paths = [((1,1),(2,2)), ((2,2), (1,1)), ((1,1), (3,3))]
		self.dg.remove_duplicates_from_paths()
		self.assertEqual(self.dg.paths, [((1,1),(2,2)), ((1,1), (3,3))])

	def test_connect_rooms(self):
		result = self.dg.connect_rooms(self.paths)
		self.assertEqual(result[0], [".", ".", "#"])
		self.assertEqual(result[2], [".", ".", "."])

		self.dg.map = [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]]
		self.paths = [((0,0),(0,2))]
		result = self.dg.connect_rooms(self.paths)
		self.assertEqual(result[0], [".", "#", "#"])
		self.assertEqual(result[1], [".", "#", "#"])
		self.assertEqual(result[2], [".", "#", "#"])

	def test_start_delaunay_good_input(self):
		rooms = []
		for coord in [Coordinates(2,3),Coordinates(7,2),Coordinates(5,5),Coordinates(7,6),Coordinates(3,7),Coordinates(11,2),Coordinates(11,5),Coordinates(9,8),Coordinates(4,1),
				 Coordinates(1,6),Coordinates(6,8),Coordinates(11,7)]:
			rooms.append(Rooms(coord,[],[],None))
		self.dg.rooms = rooms
		success = self.dg.start_delaunay()
		self.assertTrue(success)

	def test_start_delaunay_bad_input(self):
		rooms = []
		for coord in [Coordinates(8,1), Coordinates(10,1), Coordinates(4,1)]:
			rooms.append(Rooms(coord,[],[],None))
		self.dg.rooms = rooms
		success = self.dg.start_delaunay()
		self.assertFalse(success)

	def test_create_room_connections(self):
		rooms = []
		for coord in [Coordinates(2,3),Coordinates(7,2),Coordinates(5,5),Coordinates(7,6),Coordinates(3,7),Coordinates(11,2),Coordinates(11,5),Coordinates(9,8),Coordinates(4,1),
				 Coordinates(1,6),Coordinates(6,8),Coordinates(11,7)]:
			rooms.append(Rooms(coord,[],[],None))
		self.dg.rooms = rooms
		success = self.dg.start_delaunay()
		self.assertTrue(success)
		self.dg.create_room_connections(self.dg.paths)
		for room in self.dg.rooms:
			path_exists = False
			for connected in room.connected_rooms:
				for path in self.dg.paths:
					if path[0] == (room.center_point.x, room.center_point.y) and path[1] == (connected.center_point.x, connected.center_point.y):
						path_exists = True
					if path[1] == (room.center_point.x, room.center_point.y) and path[0] == (connected.center_point.x, connected.center_point.y):
						path_exists = True

			self.assertTrue(path_exists)
		