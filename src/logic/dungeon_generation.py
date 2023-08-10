import settings.config
import logic.room_generation

class DungeonGenerator:
	def __init__(self):
		self.map = []
		self.rooms = []
		self.length = settings.config.LENGTH
		self.width = settings.config.WIDTH
		self.floor_chance = settings.config.FLOOR_CHANCE
		self.tile_size = 1
		self.room_generator = logic.room_generation.RoomGenerator(self.length, self.width, self.tile_size)

	def generate_blank_map(self):
		for _ in range(self.length):
			row = []
			for _ in range(self.width):
				row.append("#")
			self.map.append(row)

	def generate_room(self):
		self.rooms.append(self.room_generator.generate_room(self.map))

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
