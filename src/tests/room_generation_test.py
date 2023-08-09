import unittest
from logic import room_generation
from datatypes.coordinates import Coordinates
from datatypes.rectangle import Rectangle
from unittest.mock import patch
from random import Random

class TestRoomGenerator(unittest.TestCase):
	def setUp(self):
		self.room_generator = room_generation.RoomGenerator(3,3,1)
		self.map = [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]]
		self.room_size = Rectangle(3,3)
		self.starting_corner = Coordinates(0,0)
		self.random = Random(1)

	def test_room_count(self):
		self.room_generator.length = 5
		self.room_generator.width = 6
		room_count = self.room_generator.get_room_count()
		self.assertEqual(room_count, 1)

	def test_create_room_tiles(self):
		self.map = [["#", "#", "#", "#"],  ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"]]
		room_size = Rectangle(2,2)
		starting_corner = Coordinates(1,1)
		self.room_generator.create_room_tiles(room_size,starting_corner,self.map)
		self.assertEqual(self.map, [["#", "#", "#", "#"],  ["#", " ", " ", "#"], ["#", " ", " ", "#"], ["#", "#", "#", "#"]])

	@patch('logic.room_generation.random')
	def test_get_random_point_in_circle(self, random):
		random.randint._mock_side_effect = self.random.randint
		random_point = self.room_generator.get_random_point_in_circle(10,10)
		self.assertEqual(random_point, Coordinates(10,10))