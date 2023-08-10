import unittest
from logic import room_generation
from datatypes.coordinates import Coordinates
from datatypes.rectangle import Rectangle
from unittest.mock import patch
import random

class TestRoomGenerator(unittest.TestCase):
	def setUp(self):
		self.room_generator = room_generation.RoomGenerator(3,3,1)
		self.map = [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]]
		self.room_size = Rectangle(3,3)
		self.starting_corner = Coordinates(0,0)
		self.room_generator.length = 10
		self.room_generator.width = 8

	def test_room_count(self):
		room_count = self.room_generator.get_room_count()
		self.assertEqual(room_count, 2)

	@patch('logic.room_generation.random.randint')
	def test_get_room_size(self, mock_random):
		mock_random.return_value = 4
		room_size = self.room_generator.get_room_size()
		self.assertEqual(room_size, Rectangle(4,4))

	def test_create_room_tiles(self):
		self.map = [["#", "#", "#", "#"],  ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"]]
		room_size = Rectangle(2,2)
		starting_corner = Coordinates(1,1)
		self.room_generator.create_room_tiles(room_size,starting_corner,self.map)
		self.assertEqual(self.map, [["#", "#", "#", "#"],  ["#", " ", " ", "#"], ["#", " ", " ", "#"], ["#", "#", "#", "#"]])

	@patch('logic.room_generation.random')
	def test_get_random_point_in_circle(self, mock_random):
		random_point = self.room_generator.get_random_point_in_circle(10,10)
		self.assertEqual(random_point, Coordinates(12,13))

	def test_radius_of_circle(self):
		radius = self.room_generator.get_radius_of_cirle()
		self.assertEqual(radius, 4)
		self.room_generator.length = 8
		self.room_generator.width = 10
		radius = self.room_generator.get_radius_of_cirle()
		self.assertEqual(radius, 4)

	@patch('logic.room_generation.random')
	def test_get_starting_corner(self, mock_random):
		room_size = Rectangle(2,2)
		starting_corner = self.room_generator.get_starting_corner(room_size, 8, 10)
		self.assertEqual(starting_corner, Coordinates(8,11))
		room_size = Rectangle(1,1)
		starting_corner = self.room_generator.get_starting_corner(room_size, 8, 10)
		self.assertEqual(starting_corner, Coordinates(9,12))

	@patch('logic.room_generation.random')
	def test_get_away_direction(self, mock_random):
		away_direction = self.room_generator.get_away_direction()
		self.assertEqual(away_direction, Coordinates(-1,-1))