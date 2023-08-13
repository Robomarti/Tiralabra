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

	def get_room_count(self):
		"""Returns an integer using random math that I made up"""		

		return math.floor(math.sqrt((self.length - 3) * (self.width - 3) / 4))

	def get_radius_of_cirle(self):
		"""Return the radius of a circle drawn inside of the game map"""
		length = self.length
		width = self.width
		if length < width:
			smaller = length
		else:
			smaller = width
		return math.floor(smaller / 2)

	def get_random_point_in_circle(self, center_x, center_y):
		"""Returns a random point in a circle"""

		radius = self.get_radius_of_cirle()
		r = radius * math.sqrt(random.random())
		theta = 2 * math.pi * random.random()

		x_coordinate = self.roundm(center_x + r * math.cos(theta), self.tile_size)
		y_coordinate = self.roundm(center_y + r * math.sin(theta), self.tile_size)
		return Coordinates(x_coordinate, y_coordinate)

	def roundm(self, n, tile_size):
		"""Rounds up coordinates so that it snaps to the dungeon map grid made out of pixels"""

		return math.floor(((n + tile_size - 1) / tile_size)) * tile_size

	def get_room_size(self):
		"""Returns a random sized rectangle. 
		The maximum length and width are calculated with some random math I made up
		Room size is given in a rectangles width and length"""

		room_count = self.get_room_count()
		room_width = random.randint(3, int(self.width / (room_count - 1)) * 2)
		room_length = random.randint(3, int(self.length / (room_count - 1)) * 2)
		return Rectangle(room_width, room_length)

	def generate_room(self, game_map: list):
		"""Generates a room to an empty place

		Starting corner is offset by the scale of the room to be generated so that the whole room fits better to the map.
		
		In the while loop, if the initial placement is not empty, it tries to find room from the direction that is given by 
		the function get_away_direction(). If it can not find place for room there, selects another starting corner and
		tries again.
		"""

		moved = self.move_room_starting_point_if_necessary(game_map)
		if moved:
			room_size = moved[0]
			starting_corner = moved[1]

			cells = self.create_room_tiles(room_size, starting_corner, game_map)
			center_point = self.get_center_point(starting_corner, room_size)
			new_room = Rooms(center_point, cells, [])
			return new_room
		return " "

	def get_center_point(self, starting_corner: Coordinates, room_size: Rectangle):
		"""Returns a center point of a room in Coordinates form"""
		return Coordinates(starting_corner.x + math.floor(room_size.width / 2), starting_corner.y + math.floor(room_size.length / 2))

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
		If not, moves the room to a random direction"""
		room_size = self.get_room_size()
		width = int(self.width / 2)
		length = int(self.length / 2)
		starting_corner = self.get_starting_corner(room_size, width, length)
		while starting_corner.x <= 0 or starting_corner.y <= 0:
			starting_corner = self.get_starting_corner(room_size, width, length)
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
				starting_corner = self.get_starting_corner(room_size, width, length)
				while starting_corner.x <= 0 or starting_corner.y <= 0:
					starting_corner = self.get_starting_corner(room_size, width, length)
				away_direction = self.get_away_direction()
			else:
				return None

		return (room_size,starting_corner)

	def get_starting_corner(self, room_size: Rectangle, width, length):
		starting_corner = self.get_random_point_in_circle(width, length)
		starting_corner.x -= room_size.width
		starting_corner.y -= room_size.length
		return starting_corner

	def check_if_room(self, room_size: Rectangle, starting_corner: Coordinates, game_map):
		"""Checks if there is room for a room
		
		Returns false if there is no room for a room or there is room for a room, but the room would be less than 3 wide or less than 3 long.
		"""

		if starting_corner.x <= 0 or starting_corner.y <= 0:
			return False
		if starting_corner.x + room_size.width >= len(game_map[0])-1 or starting_corner.y + room_size.length >= len(game_map)-1:
			return False

		checking_area = [starting_corner.x-1,starting_corner.y-1,starting_corner.x+room_size.width+1,starting_corner.y+room_size.length+1]

		#first check if the room is next to the border of the map
		if starting_corner.x == 1: #left border
			checking_area[0] += 1
		if starting_corner.y == 1: #upper border
			checking_area[1] += 1
		if starting_corner.x + room_size.width >= len(game_map[0])-2: #right border
			checking_area[2] = len(game_map[0])-2
		if starting_corner.y + room_size.length >= len(game_map)-2: #lower border
			checking_area[3] = len(game_map)-2

		if checking_area[0] + checking_area[2] < 3:
			return False
		if checking_area[1] + checking_area[3] < 3:
			return False

		for y in range(checking_area[1], checking_area[3]): #from upper border to lower border

			for x in range(checking_area[0], checking_area[2]): #from left border to right border

				if game_map[y][x] != "#":
					return False
		return True

	def get_away_direction(self):
		"""Returns the direction where the room should head when there is not room for it
		in its original position. The direction will be chosen randomly.
		"""

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
