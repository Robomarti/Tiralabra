import math
import random
from dataclasses import dataclass
import settings.config
import logic.cellular_automata

@dataclass
class Coordinates:
	"""A class for a custom datatype, Coordinates represents a 2-dimensional Coordinates"""
	x: float
	y: float

@dataclass
class Rooms:
	"""A class for a custom datatype, Coordinates represents a 2-dimensional Coordinates"""
	x: float
	y: float
	width: int
	length: int

class DungeonGenerator:
	def __init__(self):
		self.map = []
		self.rooms = []
		self.length = settings.config.LENGTH
		self.width = settings.config.WIDTH
		self.floor_chance = settings.config.FLOOR_CHANCE
		self.tile_size = 1

	def generate_blank_map(self):
		for _ in range(self.length):
			row = []
			for _ in range(self.width):
				row.append("#")
			self.map.append(row)

	def get_room_count(self):
		return math.floor(math.sqrt((self.length - 3) * (self.width - 3) / 4))

	def get_random_point_in_circle(self, radius, center_x, center_y):
		r = radius * math.sqrt(random.random())
		theta = 2 * math.pi * random.random()

		x_coordinate = self.roundm(center_x + r * math.cos(theta), self.tile_size)
		y_coordinate = self.roundm(center_y + r * math.sin(theta), self.tile_size)
		return Coordinates(x_coordinate, y_coordinate)

	def roundm(self, n, tile_size):
		"""Rounds up coordinates so that it snaps to the grid made out of pixels"""

		return math.floor(((n + tile_size - 1) / tile_size)) * tile_size

	def get_room_size(self):
		"""Room size is given in Coordinates, only because I like typing .x better
		compared to tuples where I have to type [0]
		I could have made another datatype called Vector2 but it seems pointless
		"""

		room_count = self.get_room_count()
		room_width = random.randint(3, int(self.width / (room_count - 1)) * 2)
		room_length = random.randint(3, int(self.length / (room_count - 1)) * 2)
		return Coordinates(room_width, room_length)

	def generate_room(self):
		"""Generates a room to an empty place
		If the initial placement is not empty, it tries to find room from the direction that is given by 
		the function get_away_direction()
		"""

		room_size = self.get_room_size()
		width = int(self.width / 2)
		length = int(self.length / 2)
		starting_corner = self.get_random_point_in_circle(self.get_radius_of_cirle(), width, length)

		direction = self.get_away_direction(starting_corner)

		while not self.check_if_room(room_size, starting_corner):
			starting_corner.x -= direction.x
			starting_corner.y -= direction.y
		self.create_room(room_size, starting_corner)

	def create_room(self, room_size: Coordinates, starting_corner: Coordinates):
		for y_coordinate in range(starting_corner.y, starting_corner.y + room_size.y):
			for x_coordinate in range(starting_corner.x, starting_corner.x + room_size.x):
				if y_coordinate in range(1, len(self.map)-1) \
				and x_coordinate in range(1, len(self.map[y_coordinate])-1) \
				and self.map[y_coordinate][x_coordinate] == "#":
					self.map[y_coordinate][x_coordinate] = " "

	def check_if_room(self, room_size: Coordinates, starting_corner: Coordinates):
		for y in range(starting_corner.y-1, starting_corner.y + room_size.y+1):
			for x in range(starting_corner.x-1, starting_corner.x + room_size.x+1):
				if y in range(len(self.map)) and x in range(len(self.map[y])) and self.map[y][x] != "#":
					return False
		return True

	def get_radius_of_cirle(self):
		length = self.length
		width = self.width
		if length < width:
			smaller = length
		else:
			smaller = width
		return math.floor(smaller / 2)

	def get_away_direction(self, starting_corner):
		"""Returns the direction where the room should head when there is not room for it
		in its original position. The direction will be chosen randomly.
		"""	

		direction_chance = random.random()

		if direction_chance > 0.75:
			direction = Coordinates(-1,-1)
		elif direction_chance > 0.50:
			direction = Coordinates(-1,1)
		elif direction_chance > 0.25:
			direction = Coordinates(1,1)
		else:
			direction = Coordinates(1,-1)

		return direction

	def print_map(self):
		"""Prints every row of the map instead of the whole map at once, so that it is more readable"""

		print()
		for row in self.map:
			print(" ".join(row))
		print()

	def smoothen(self):
		logic.cellular_automata.cellular_automata(self.map, self.length, self.width)

	def create_walls(self):
		"""Creates a border of walls around the map
		This should always be called after the generate_map() function
		"""

		for y_coordinate in range(1,len(self.map)-1):
			self.map[y_coordinate][0] = "#"
			self.map[y_coordinate][-1] = "#"
		self.map[0] = ["#"] * len(self.map[0])
		self.map[-1] = ["#"] * len(self.map[0])

	def change_width_and_length(self, width, length):
		self.width = width
		self.length = length
