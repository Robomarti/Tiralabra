from copy import deepcopy
import settings.config
import logic.room_generation
import logic.delaunay_triangulation
import logic.minimum_spanning_tree
from datatypes.rooms import Rooms, find_longest_path, find_room_by_center
from logic.flood_fill import flood_fill

class DungeonGenerator:
	def __init__(self):
		self.map = []
		self.rooms = []
		self.paths = []
		self.length = settings.config.LENGTH
		self.width = settings.config.WIDTH
		tile_size = 1
		self.room_generator = logic.room_generation.RoomGenerator(self.length, self.width, tile_size)
		self.prim = []

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

	def start_delaunay(self):
		"""Sets the paths to be the edges that the delaunay component has"""
		points = []
		points_used = {}
		for room in self.rooms:
			points.append(room.center_point)
			points_used[(room.center_point.x, room.center_point.y)] = False

		delaunay = logic.delaunay_triangulation.delaunay_triangulation(points, self.width, self.length)

		for triangle in delaunay:
			for edge in triangle.edges:
				self.paths.append(((edge[0].x,edge[0].y), (edge[1].x,edge[1].y)))
				points_used[(edge[0].x, edge[0].y)] = True
				points_used[(edge[1].x, edge[1].y)] = True

		used_count = 0
		for key in points_used:
			if points_used[key]:
				used_count += 1

		if used_count != len(points):
			print("used in delaunay:", points_used)
			print()
			print("room count was", len(points),"while used count was", used_count, ". This means that delaunay triangulation was not succesfull in connecting every room.",
	 		"Most likely this is because less than three rooms were generated. Please try again")
			return False

		return True

	def remove_duplicates_from_paths(self):
		new_paths = []
		for path in self.paths:
			if not (path in new_paths or (path[1], path[0]) in new_paths):
				new_paths.append(path)

		self.paths = new_paths

	def start_spanning(self):
		if len(self.paths) > 0:
			prim = logic.minimum_spanning_tree.prim(self.paths)

			new_paths = []
			for path in prim:
				if not (path in new_paths or (path[1], path[0]) in new_paths):
					new_paths.append(path)

			self.prim = new_paths
			self.create_room_connections(self.prim)

	def connect_rooms(self, paths):
		"""Adds paths between the centers of the rooms"""
		new_map = deepcopy(self.map)
		for path in paths:	
			if path[0][0] < path[1][0]:
				x_direction = 1
			else:
				x_direction = -1

			if path[0][1] < path[1][1]:
				y_direction = 1
			else:
				y_direction = -1

			for x_coordinate in range(path[0][0],path[1][0]+x_direction,x_direction):
				if new_map[path[0][1]][x_coordinate] == "#":
					new_map[path[0][1]][x_coordinate] = "."

			for y_coordinate in range(path[0][1],path[1][1]+y_direction,y_direction):
				if new_map[y_coordinate][path[1][0]] == "#":
					new_map[y_coordinate][path[1][0]] = "."

		return new_map

	def create_room_connections(self, paths):
		for room in self.rooms:
			room.connected_rooms = []

		for path in paths:
			for room in self.rooms:
				if path[0] == (room.center_point.x,room.center_point.y) and path[1] not in room.connected_rooms:
					room.connected_rooms.append(find_room_by_center(path[1], self.rooms))
				if path[1] == (room.center_point.x,room.center_point.y) and path[0] not in room.connected_rooms:
					room.connected_rooms.append(find_room_by_center(path[0], self.rooms))

	def color_map(self, map_to_color):
		"""Green square with white x for starting room and red square with white x for ending room"""
		starting_node = self.rooms[0].center_point
		colored_map = flood_fill(map_to_color,(starting_node.x,starting_node.y))

		start_end = find_longest_path(self.rooms)
		print("Starting room is", start_end[0].center_point, "and ending room is", start_end[1].center_point)
		map_to_color[start_end[0].center_point.y][start_end[0].center_point.x] = '\u001b[0;37;42mx'
		map_to_color[start_end[1].center_point.y][start_end[1].center_point.x] = '\u001b[0;37;41mx'
		return colored_map					

	def print_map(self, map_to_print):
		"""Prints every row of the map instead of the whole map at once, so that it is more readable"""

		print()
		for row in map_to_print:
			print(" ".join(row))
		print()
