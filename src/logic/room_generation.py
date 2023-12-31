import math
import random
from datatypes.coordinates import Coordinates
from datatypes.rectangle import Rectangle
from datatypes.rooms import Rooms

random = random.Random()

class RoomGenerator():
	def __init__(self, length, width, tile_size):
		self.length = length
		self.width = width
		self.tile_size = tile_size
		self.room_count = self.get_room_count()

	def get_room_count(self):
		"""Returns an integer using random math that I made up"""		
		minimum = max(3,math.floor(self.width * self.length / 200))
		maximum = max(4, math.floor(self.width * self.length / 100))
		return random.randint(minimum, maximum)

	def get_random_point_in_map(self):
		"""Returns a random point on the map.
		Should not return a point on the edges of the map"""
		x_coordinate = random.randint(1, self.width-2)
		y_coordinate = random.randint(1, self.length-2)
		return Coordinates(x_coordinate, y_coordinate)

	def get_room_size(self):
		"""Returns a random sized rectangle. 
		The maximum length and width are calculated with some random math I made up
		Room size is given in a rectangles width and length"""

		room_width = random.randint(3, max(3,self.width // math.sqrt(self.room_count)))
		room_length = random.randint(3, max(3, self.length // math.sqrt(self.room_count)))
		return Rectangle(room_width, room_length)

	def generate_room(self, game_map: list):
		"""Generates a room to an empty place

		Starting corner is offset by the scale of the room to be generated so that the whole room
		fits better to the map.
		
		In the while loop, if the initial placement is not empty, it tries to find room from the
		direction that is given by the function get_away_direction(). If it can not find place for
		room there, selects another starting corner and tries again."""

		success = self.move_room_starting_point_if_necessary(game_map)
		if success:
			room_size = success[0]
			starting_corner = success[1]

			cells = self.create_room_tiles(room_size, starting_corner, game_map)
			center_point = self.get_center_point(starting_corner, room_size)
			new_room = Rooms(center_point, cells, [], None)
			return new_room
		return " "

	def get_center_point(self, starting_corner: Coordinates, room_size: Rectangle):
		"""Returns a center point of a room in Coordinates form"""
		x_coordinate = starting_corner.x + math.floor(room_size.width / 2)
		y_coordinate = starting_corner.y + math.floor(room_size.length / 2)
		return Coordinates(x_coordinate, y_coordinate)

	def create_room_tiles(self, room_size: Rectangle, starting_corner: Coordinates, game_map: list):
		"""Replaces the # tiles in the map with spaces"""
		cells = []
		for y_coordinate in range(starting_corner.y, starting_corner.y + room_size.length):
			for x_coordinate in range(starting_corner.x, starting_corner.x + room_size.width):
				game_map[y_coordinate][x_coordinate] = " "
				cells.append((x_coordinate,y_coordinate))
		return cells

	def move_room_starting_point_if_necessary(self, game_map: list):
		"""Checks whether the room has an empty place to be placed in.
		If not, moves the room to a random direction. If moving fails to
		find a empty spot for the room, creates a new room and tries again"""
		room_size = self.get_room_size()
		starting_corner = self.get_random_point_in_map()
		away_direction = self.get_away_direction()

		failed_attempts = 0
		big_failures = 0
		while not self.check_if_room(room_size, starting_corner, game_map):
			failed_attempts += 1
			if failed_attempts < 20:
				starting_corner.x += away_direction.x
				starting_corner.y += away_direction.y
				if starting_corner.x + room_size.width >= len(game_map[0]) or starting_corner.y + room_size.length >= len(game_map):
					failed_attempts = 20
			elif big_failures < 10:
				big_failures += 1
				failed_attempts = 0
				room_size = self.get_room_size()
				starting_corner = self.get_random_point_in_map()
				away_direction = self.get_away_direction()
			else:
				return None

		return (room_size,starting_corner)

	def check_if_room(self, room_size: Rectangle, starting_corner: Coordinates, game_map) -> bool:
		"""Checks if there is room for a room
		
		Returns false if there is no room for a room or there is room for a room, but the room
		would be less than 3 wide or less than 3 long.

		First checks if the room corner has moved outside of the game_map.
		Then checks if the corner + width a.k.a. a part of the room is outside
		of the game_map. Then assigns the checking area and checks."""
		if starting_corner.x <= 0 or starting_corner.y <= 0:
			return False
		if starting_corner.x + room_size.width >= len(game_map[0]):
			room_size.width -= starting_corner.x + room_size.width - len(game_map[0]) + 1
		if starting_corner.y + room_size.length >= len(game_map):
			room_size.length -= starting_corner.y + room_size.length - len(game_map) + 1

		if room_size.width < 3:
			return False
		if room_size.length < 3:
			return False

		checking_area = [starting_corner.x-1, starting_corner.y-1, \
		   				starting_corner.x+room_size.width, starting_corner.y+room_size.length]

		#from upper border to lower border
		for y_coordinate in range(checking_area[1], checking_area[3]+1):
			#from left border to right border
			for x_coordinate in range(checking_area[0], checking_area[2]+1):
				if game_map[y_coordinate][x_coordinate] != "#":
					return False
		return True

	def get_away_direction(self):
		"""Returns the direction where the room should head when there is not room for it
		in its original position. The direction will be chosen randomly."""
		direction_chance = float(random.random())

		if direction_chance > 0.75:
			direction = Coordinates(-1,-1)
		elif direction_chance > 0.50:
			direction = Coordinates(-1,1)
		elif direction_chance > 0.25:
			direction = Coordinates(1,1)
		else:
			direction = Coordinates(1,-1)

		return direction
