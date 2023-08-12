import settings.config
import logic.room_generation
import logic.delaunay_triangulation
from math import sqrt
from colorama import Fore
from datatypes.coordinates import Coordinates
from datatypes.rooms import Rooms

class DungeonGenerator:
	def __init__(self):
		self.map = []
		self.rooms = []
		self.length = settings.config.LENGTH
		self.width = settings.config.WIDTH
		self.floor_chance = settings.config.FLOOR_CHANCE
		self.tile_size = 1
		self.room_generator = logic.room_generation.RoomGenerator(self.length, self.width, self.tile_size)
		self.delaunay = logic.delaunay_triangulation.DelaunayTriangulation()
		self.paths = []
		self.canAccess = {}

	def generate_blank_map(self):
		"""Initializes the map.
		Initially the map only needs to be length * width many cells of #"""
		for _ in range(self.length):
			row = []
			for _ in range(self.width):
				row.append("#")
			self.map.append(row)

	def generate_room(self):
		"""Generates a new room and if it succeeded, adds it to the rooms list"""
		room = self.room_generator.generate_room(self.map)
		if type(room) == Rooms:
			self.rooms.append(room)

	def get_edges(self):
		"""Sets the paths to be the edges that the delaunay component has"""
		self.paths = self.delaunay.edges
		for path in self.paths:
			self.canAccess[path[0]] = [path[1]]

	def print_map(self):
		"""Prints every row of the map instead of the whole map at once, so that it is more readable"""

		print()
		for row in self.map:
			print(" ".join(row))
		print()

	def print_rooms(self):
		"""Prints every room of the map instead of all rooms at once, so that it is more readable"""
		print()
		for room in self.rooms:
			print(room)
		print()
		
	def print_paths(self):
		"""Prints every room of the map instead of all rooms at once, so that it is more readable"""
		print()
		for path in self.paths:
			print(path)
		print()

	def connect_rooms(self):
		"""Adds paths between the centers of the rooms"""
		for path in self.paths:
			if path[0][0] < path[1][0]:
				x_direction = 1
			else:
				x_direction = -1

			#because y-direction is downwards, this has to be reversed
			if path[0][1] < path[1][1]:
				y_direction = 1
			else:
				y_direction = -1

			for x_coordinate in range(path[0][0],path[1][0]+x_direction,x_direction):
				if self.map[path[0][1]][x_coordinate] != " ":
					self.map[path[0][1]][x_coordinate] = "."

			for y_coordinate in range(path[0][1],path[1][1]+x_direction,y_direction):
				if self.map[y_coordinate][path[1][0]] != " ":
					self.map[y_coordinate][path[1][0]] = "."
			

	def change_width_and_length(self, width, length):
		self.width = width
		self.length = length
