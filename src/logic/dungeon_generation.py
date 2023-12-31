from copy import deepcopy
from settings.config import get_configs
import logic.room_generation
import logic.delaunay_triangulation
import logic.minimum_spanning_tree
from logic.flood_fill import flood_fill
from datatypes.rooms import Rooms, find_longest_path, find_room_by_center

class DungeonGenerator:
	def __init__(self):
		self.map = []
		self.rooms = []
		self.paths = []
		configs = get_configs()
		self.length = configs[0]
		self.width = configs[1]
		tile_size = 1
		self.room_generator = logic.room_generation.RoomGenerator(self.length, self.width, tile_size)

	def generate_blank_map(self):
		"""Creates a blank map.
		A blank map is a matrix which has width * length of #"""
		new_map = []
		for _ in range(self.length):
			row = []
			for _ in range(self.width):
				row.append("#")
			new_map.append(row)

		self.map = new_map

	def generate_room(self):
		"""Generates a new room and if it succeeded, adds it to the rooms list"""
		room = self.room_generator.generate_room(self.map)
		if isinstance(room, Rooms):
			self.rooms.append(room)

	def start_delaunay(self):
		"""Sets the paths to be the edges that the delaunay component has"""
		points = []
		for room in self.rooms:
			points.append(room.center_point)

		delaunay = logic.delaunay_triangulation.delaunay_triangulation(points, self.width, self.length)

		points_used = []
		for triangle in delaunay:
			for edge in triangle.edges:
				self.paths.append(((edge[0].x,edge[0].y), (edge[1].x,edge[1].y)))
				if edge[0] not in points_used:
					points_used.append(edge[0])
				if edge[1] not in points_used:
					points_used.append(edge[1])

		if len(points_used) != len(points):
			print()
			print("used in delaunay:", points)
			print()
			print("room count was", len(points),"while used count was", len(points_used))
			print(". This means that delaunay triangulation was not",
	  			"succesful in connecting every room. Please try again")
			return False

		return True

	def remove_duplicates_from_paths(self):
		"""Remove duplicate paths from self.paths"""
		new_paths = []
		for path in self.paths:
			if not (path in new_paths or (path[1], path[0]) in new_paths):
				new_paths.append(path)

		self.paths = new_paths

	def start_spanning(self):
		"""Discards paths that are not in the minimum spanning tree of the paths.
		
		start_delaunay() needs to be called before this, since my implementation of Prim's algorithm uses
		the paths that the Delaunay triangulation creates."""
		new_paths = []
		spanning_tree = logic.minimum_spanning_tree.prim(self.paths)

		for path in spanning_tree:
			if not (path in new_paths or (path[1], path[0]) in new_paths):
				new_paths.append(path)

		return new_paths

	def connect_rooms(self, paths):
		"""Adds paths between the centers of the rooms.
		Returns a copy of the map so that each phase of the algorithm can
		be printed. For example when we add paths according to deulaunay, we
		later remove the paths but the map would still show the deleted paths"""
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
		"""Saves the connections between rooms.
		These are used later when finding a parent for each room"""
		for room in self.rooms:
			room.connected_rooms = []

		for path in paths:
			for room in self.rooms:
				if path[0] == (room.center_point.x,room.center_point.y) and path[1] not in room.connected_rooms:
					room.connected_rooms.append(find_room_by_center(path[1], self.rooms))
				if path[1] == (room.center_point.x,room.center_point.y) and path[0] not in room.connected_rooms:
					room.connected_rooms.append(find_room_by_center(path[0], self.rooms))

	def color_map(self, map_to_color):
		"""Returns the map which was given as a argument.
		Each cell of the map is replaced with a different colored cell."""
		starting_node = self.rooms[0].center_point
		colored_map = flood_fill(map_to_color,(starting_node.x,starting_node.y))

		start_end = find_longest_path(self.rooms)
		print("Starting room is", start_end[0].center_point,
			"(green) and ending room is", start_end[1].center_point, "(red)")
		#Green square with white x for starting room and red square with white x for ending room
		colored_map[start_end[0].center_point.y][start_end[0].center_point.x] = '\u001b[0;37;42mx'
		colored_map[start_end[1].center_point.y][start_end[1].center_point.x] = '\u001b[0;37;41mx'

		return colored_map

	def print_map(self, map_to_print):
		"""Prints every row of the map instead of the whole map at once, so that it is more readable"""

		print()
		for row in map_to_print:
			print(" ".join(row))
		print()
