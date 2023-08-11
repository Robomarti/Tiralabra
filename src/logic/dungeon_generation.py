import settings.config
import logic.room_generation
from math import sqrt

class DungeonGenerator:
	def __init__(self):
		self.map = []
		self.rooms = []
		self.length = settings.config.LENGTH
		self.width = settings.config.WIDTH
		self.floor_chance = settings.config.FLOOR_CHANCE
		self.tile_size = 1
		self.room_generator = logic.room_generation.RoomGenerator(self.length, self.width, self.tile_size)
		self.distances = []
		self.paths = []

	def generate_blank_map(self):
		for _ in range(self.length):
			row = []
			for _ in range(self.width):
				row.append("#")
			self.map.append(row)

	def generate_room(self):
		room = self.room_generator.generate_room(self.map)
		if room != " ":
			self.rooms.append(room)

	def generate_distances(self, rooms):
		for i in range(len(rooms)):
			distances_of_room = []
			for j in range(len(rooms)):
				distance = sqrt((rooms[i].center_point.x - rooms[j].center_point.x)**2 + (rooms[i].center_point.y - rooms[j].center_point.y)**2)
				distances_of_room.append(distance)
			self.distances.append(distances_of_room)

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

	def change_width_and_length(self, width, length):
		self.width = width
		self.length = length
