import math
import random
import settings.config
import logic.cellular_automata
from dataclasses import dataclass

length = settings.config.LENGTH
width = settings.config.WIDTH

tile_size = 1

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

	def generate_blank_map(self):
			for _ in range(self.length):
				row = []
				for _ in range(self.width):
					row.append("#")
				self.map.append(row)

	def get_room_count(self):
		return math.floor(math.sqrt((length - 3) * (width - 3) / 10))

	def get_random_point_in_circle(self, radius, center_x, center_y):
		r = radius * math.sqrt(random.random())
		theta = 2 * math.pi * random.random()

		x_coordinate = self.roundm(center_x + r * math.cos(theta), tile_size)
		y_coordinate = self.roundm(center_y + r * math.sin(theta), tile_size)
		return Coordinates(x_coordinate, y_coordinate)

	def roundm(self, n,tile_size):
		"""Rounds up coordinates so that it snaps to the grid made out of pixels"""
		return math.floor(((n + tile_size - 1) / tile_size)) * tile_size

	def get_room_size(self):
		room_count = self.get_room_count()
		width = random.randint(3, int(self.width / (room_count - 1)) * 2)
		length = random.randint(3, int(self.length / (room_count - 1)) * 2)
		return Coordinates(width, length)

	def generate_room(self):
		room_size = self.get_room_size()
		starting_corner = self.get_random_point_in_circle(self.get_radius_of_cirle(), int(self.width / 2), int(self.length / 2))

		attempts = 0
		while (not self.check_if_room(room_size, starting_corner)) and attempts < 5:
			starting_corner.x -= 1
			starting_corner.y -= 1
			attempts += 1
		if not attempts >= 5:
			self.create_room(room_size, starting_corner)
							
	def create_room(self, room_size, starting_corner):
		for y in range(starting_corner.y, starting_corner.y + room_size.y):
				for x in range(starting_corner.x, starting_corner.x + room_size.x):
					if y in range(len(self.map)-1) and x in range(len(self.map[y])-1):
						if self.map[y][x] == "#":
							self.map[y][x] = " "

	def check_if_room(self, room_size, starting_corner):
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

		for y in range(1,len(self.map)-1):
			self.map[y][0] = "#"
			self.map[y][-1] = "#"
		self.map[0] = ["#"] * len(self.map[0])
		self.map[-1] = ["#"] * len(self.map[0])

	def change_width_and_length(self, width, length):
		self.width = width
		self.length = length
