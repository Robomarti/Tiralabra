import settings.config
import logic.room_generation
import logic.delaunay_triangulation
from datatypes.rooms import Rooms, find_room_by_cell, remove_duplicates, is_own_room

class DungeonGenerator:
	def __init__(self):
		self.map = []
		self.rooms = []
		self.paths = []
		self.length = settings.config.LENGTH
		self.width = settings.config.WIDTH
		tile_size = 1
		self.room_generator = logic.room_generation.RoomGenerator(self.length, self.width, tile_size)
		self.delaunay = logic.delaunay_triangulation.DelaunayTriangulation()

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
		if isinstance(room, Rooms):
			self.rooms.append(room)

	def init_can_access(self):
		for room in self.rooms:
			coordinates = (room.center_point.x,room.center_point.y)
			self.can_access[coordinates] = []

	def get_paths(self):
		"""Sets the paths to be the edges that the delaunay component has"""
		self.paths = self.delaunay.edges

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

	def connect_rooms(self, paths: list[tuple]):
		"""Adds paths between the centers of the rooms"""
		for path in paths:
			visited = []
			if path[0][0] < path[1][0]:
				x_direction = 1
			else:
				x_direction = -1

			if path[0][1] < path[1][1]:
				y_direction = 1
			else:
				y_direction = -1

			for x_coordinate in range(path[0][0],path[1][0]+x_direction,x_direction):
				if self.map[path[0][1]][x_coordinate] != " ":
					self.map[path[0][1]][x_coordinate] = "."
				else:
					if not is_own_room((x_coordinate,path[0][1]), path[0], self.rooms):
						visited.append((x_coordinate,path[0][1]))

			for y_coordinate in range(path[0][1],path[1][1]+y_direction,y_direction):
				if self.map[y_coordinate][path[1][0]] != " ":
					self.map[y_coordinate][path[1][0]] = "."
				else:
					if not is_own_room((path[1][0],y_coordinate), path[0], self.rooms):
						if (path[1][0],y_coordinate) not in visited: #in case that previous for loop added the cell to visited
							visited.append((path[1][0],y_coordinate))

			visited_founds = []
			for cell in visited:
				self_room = find_room_by_cell(path[0], self.rooms)
				found = find_room_by_cell(cell, self.rooms)
				if found and found not in visited_founds:
					visited_founds.append(found)
					coordinates = (found.center_point.x, found.center_point.y)
					self_room.connected_rooms.append(coordinates)
					remove_duplicates(self_room)

	def change_width_and_length(self, width, length):
		self.width = width
		self.length = length
