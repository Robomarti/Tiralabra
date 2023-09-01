import unittest
from unittest.mock import MagicMock
from logic import room_generation
from datatypes.coordinates import Coordinates
from datatypes.rectangle import Rectangle
from unittest.mock import patch

class TestRoomGenerator(unittest.TestCase):
	def setUp(self):
		self.room_generator = room_generation.RoomGenerator(10,8,1)
		self.game_map = [["#", "#", "#"],  ["#", "#", "#"], ["#", "#", "#"]]
		self.starting_corner = Coordinates(0,0)
		self.room_size = Rectangle(3,3)

	@patch('logic.room_generation.random.randint')
	def test_room_count(self, mock_random):
		mock_random.return_value = 4
		room_count = self.room_generator.get_room_count()
		self.assertEqual(room_count, 4)

	@patch('logic.room_generation.random.randint')
	def test_get_room_size(self, mock_random):
		mock_random.return_value = 4
		room_size = self.room_generator.get_room_size()
		self.assertEqual(room_size, Rectangle(4,4))

	def test_create_room_tiles(self):
		self.game_map = [["#", "#", "#", "#"],  ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"]]
		room_size = Rectangle(2,2)
		starting_corner = Coordinates(1,1)
		self.room_generator.create_room_tiles(room_size,starting_corner,self.game_map)
		self.assertEqual(self.game_map, [["#", "#", "#", "#"],  ["#", " ", " ", "#"], ["#", " ", " ", "#"], ["#", "#", "#", "#"]])

	@patch('logic.room_generation.random')
	def test_get_away_direction(self, mock_random):
		away_direction = self.room_generator.get_away_direction()
		self.assertEqual(away_direction, Coordinates(-1,-1))

	def test_get_center_point(self):
		center = self.room_generator.get_center_point(self.starting_corner, self.room_size)
		self.assertEqual(center, Coordinates(1,1))

	def test_if_room_when_room(self):
		room_size = Rectangle(4,4)
		starting_corner = Coordinates(1,1)
		game_map = [["#"]*6]*6
		is_room = self.room_generator.check_if_room(room_size, starting_corner,game_map)
		self.assertEqual(is_room, True)

	def test_if_room_when_no_room(self):
		room_size = Rectangle(4,4)
		starting_corner = Coordinates(1,1)
		game_map = [["#"]*6]*6
		game_map[2] = [" "]*6
		is_room = self.room_generator.check_if_room(room_size, starting_corner,game_map)
		self.assertEqual(is_room, False)

	def test_if_room_when_start_next_to_border(self):
		room_size = Rectangle(4,4)
		starting_corner = Coordinates(0,0)
		game_map = [["#"]*6]*6
		is_room = self.room_generator.check_if_room(room_size, starting_corner,game_map)
		self.assertEqual(is_room, False)

	def test_if_room_when_area_would_be_small(self):
		room_size = Rectangle(3,3)
		starting_corner = Coordinates(1,1)
		game_map = [["#"]*4]*4
		is_room = self.room_generator.check_if_room(room_size, starting_corner,game_map)
		self.assertEqual(is_room, False)

	def test_get_random_point_in_game_map(self):
		"""Tests that a random point is inside the game_map"""
		point = self.room_generator.get_random_point_in_map()
		self.assertLess(point.x, self.room_generator.width)
		self.assertLess(point.y, self.room_generator.length)
		self.assertGreater(point.x, 0)
		self.assertGreater(point.y, 0)

	def test_move_room(self):
		self.room_generator.get_room_size = MagicMock(return_value=Rectangle(1,1))
		self.room_generator.get_random_point_in_map = MagicMock(return_value=Coordinates(1,1))
		self.room_generator.check_if_room = MagicMock(return_value=True)
		result = self.room_generator.move_room_starting_point_if_necessary(self.game_map)
		self.assertEqual(result, (Rectangle(1,1),Coordinates(1,1)))

	def test_move_room_results_in_success(self):
		game_map = [["#"]*8]*10
		result = self.room_generator.move_room_starting_point_if_necessary(game_map)
		self.assertIsNotNone(result)

	def mock_if_room(self, starting_corner: Coordinates, game_map):
		if game_map[starting_corner.y][starting_corner.x] != "#":
				return False
		return True

	def test_two_rooms_cant_be_placed_on_top_of_each_other(self):
		self.room_generator.get_room_size = MagicMock(return_value=Rectangle(1,1))
		self.room_generator.get_random_point_in_map = MagicMock(return_value=Coordinates(1,1))
		self.room_generator.get_away_direction = MagicMock(return_value=Coordinates(0,0))
		self.room_generator.check_if_room = MagicMock(return_value=self.mock_if_room(Coordinates(1,1), self.game_map))
		result = self.room_generator.move_room_starting_point_if_necessary(self.game_map)
		self.assertIsNotNone(result)

		self.game_map = [["#", "#", "#"],  ["#", " ", "#"], ["#", "#", "#"]]
		self.room_generator.check_if_room = MagicMock(return_value=self.mock_if_room(Coordinates(1,1), self.game_map))
		result = self.room_generator.move_room_starting_point_if_necessary(self.game_map)
		self.assertIsNone(result)