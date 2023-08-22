from copy import deepcopy
from math import inf
import settings.config
import logic.room_generation
import logic.delaunay_triangulation
import logic.minimum_spanning_tree
from datatypes.rooms import Rooms
from datatypes.coordinates import Coordinates

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
			print("room count was", len(points),"while used count was", {used_count}, ". This means that delaunay triangulation was not succesfull in connecting every room.",
	 		"Most likely this is because less than three rooms were generated.")

	def remove_duplicates_from_paths(self):
		new_paths = []
		for path in self.paths:
			if not (path in new_paths or (path[1], path[0]) in new_paths):
				new_paths.append(path)

		self.paths = new_paths

	def start_spanning(self):
		prim = logic.minimum_spanning_tree.prim(self.paths)

		new_paths = []
		for path in prim:
			if not (path in new_paths or (path[1], path[0]) in new_paths):
				new_paths.append(path)

		self.prim = new_paths

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

			new_map[path[0][1]][path[0][0]] = "x"
			new_map[path[1][1]][path[1][0]] = "x"

		return new_map

	def sort_rooms(self):
		smallest = Rooms(Coordinates(inf,inf),[])
		largest = Rooms(Coordinates(-1,-1),[])
		for room in self.rooms:
			if room.center_point.y < smallest.center_point.y:
				smallest = room
			elif room.center_point.y == smallest.center_point.y and room.center_point.x < smallest.center_point.x:
				smallest = room
			if room.center_point.y > largest.center_point.y:
				largest = room
			elif room.center_point.y == largest.center_point.y and room.center_point.x > largest.center_point.x:
				largest = room

		return (smallest.center_point, largest.center_point)

	def print_map(self, map_to_print):
		"""Prints every row of the map instead of the whole map at once, so that it is more readable"""

		print()
		for row in map_to_print:
			print(" ".join(row))
		print()
