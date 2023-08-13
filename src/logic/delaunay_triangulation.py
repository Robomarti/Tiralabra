from math import sqrt, inf
from datatypes.rooms import Rooms

class DelaunayTriangulation:
	def __init__(self):
		self.edges = {}
		self.rooms = []
		self.paths = []

	def add_rooms(self, rooms: list):
		self.rooms = rooms

	def generate_distances(self, rooms: list[Rooms]):
		"""Calculates distances between all center points of rooms,
		and saves the two smallest distances for each room.
		Delaunay triangulation needs 3 points where there is not any other points
		inside a circle made through them. Realistically it is the same as just finding
		two closest points for a point, since then there can not be any point inside the
		circle they create together, because that point would be closer than the other points"""

		for i in range(len(rooms)):
			distances = [(inf,()), (inf,())]
			for j in range(len(rooms)):
				if i != j:
					distance_of_points = self.distance_of_two_points_without_sqrt(rooms[i], rooms[j])
					if distance_of_points < distances[0][0]:
						j_coordinates = (rooms[j].center_point.x, rooms[j].center_point.y)
						distances[0] = (distance_of_points, j_coordinates)
					elif distance_of_points < distances[1][0]:
						j_coordinates = (rooms[j].center_point.x, rooms[j].center_point.y)
						distances[1] = (distance_of_points, j_coordinates)

			coordinates = (rooms[i].center_point.x, rooms[i].center_point.y)

			if (distances[0][1],coordinates) not in self.edges:
				self.edges[(coordinates,distances[0][1])] = 0
			if (distances[1][1],coordinates) not in self.edges:
				self.edges[(coordinates,distances[1][1])] = 0
			if (distances[1][1],distances[0][1]) not in self.edges:
				self.edges[(distances[0][1],distances[1][1])] = 0

	def distance_of_two_points(self, point1: Rooms, point2: Rooms):
		return sqrt((point2.center_point.x - point1.center_point.x)**2 + (point2.center_point.y - point1.center_point.y)**2)

	def distance_of_two_points_without_sqrt(self, point1: Rooms, point2: Rooms):
		"""Returns the distance without squaring it so that the computer does not have to deal with small decimal comparisons"""
		return (point2.center_point.x - point1.center_point.x)**2 + (point2.center_point.y - point1.center_point.y)**2

	def connect_points(self):
		"""Creates triangles from each point and its 2 nearest points"""
		for key in self.edges:
			self.paths.append(key)

	def get_paths(self):
		return self.paths
