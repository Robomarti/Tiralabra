import unittest
from dataclasses import dataclass
from logic import dungeon_generation

@dataclass
class Coordinates:
	"""A class for a custom datatype, Coordinates represents a 2-dimensional Coordinates"""
	x: float
	y: float


class TestDungeonGenerator(unittest.TestCase):
	def setUp(self):
		self.dg = dungeon_generation.DungeonGenerator()
		self.dg.map = [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]]
		self.room_size = Coordinates(2,2)
		self.starting_corner = Coordinates(1,1)

	def test_create_walls(self):
		self.dg.map = [[" ", " ", " "],  [" ", " ", " "], [" ", " ", " "]]
		self.dg.create_walls()
		self.assertEqual(self.dg.map, [["#", "#", "#"],  ["#", " ", "#"], ["#", "#", "#"]])

	def test_generate_blank_map(self):
		self.dg.map = []
		self.dg.change_width_and_length(3,3)
		self.dg.generate_blank_map()
		self.assertEqual(self.dg.map, [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]])

	def test_room_count(self):
		self.dg.length = 5
		self.dg.width = 6
		room_count = self.dg.get_room_count()
		self.assertEqual(room_count, 1)

	def test_create_room_does_not_replace_outer_rim(self):
		self.dg.create_room(self.room_size, self.starting_corner)
		self.assertEqual(self.dg.map, [["#", "#", "#"],  ["#", " ", "#"], ["#", "#", "#"]])

	def test_if_room_when_there_is_room(self):
		is_room = self.dg.check_if_room(self.room_size, self.starting_corner)
		self.assertEqual(is_room, True)
		print(is_room)

	def test_if_room_when_there_is_not_room(self):
		self.dg.map = [["#", "#", "#"],  ["#", " ", " "], ["#", "#", "#"]]
		is_room = self.dg.check_if_room(self.room_size, self.starting_corner)
		self.assertEqual(is_room, False)
