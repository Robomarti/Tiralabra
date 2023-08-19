import math
from datatypes.coordinates import Coordinates

class Triangle:
	def __init__(self, corner1: Coordinates, corner2: Coordinates, corner3: Coordinates):
		self.corner1 = corner1
		self.corner2 = corner2
		self.corner3 = corner3
		self.corners = [corner1, corner2, corner3]

		self.edges = [(corner1,corner2),(corner2,corner3),(corner3,corner1)]
		self.circumcenter = circumcenter_of_triangle(corner1, corner2, corner3)
		self.radius = get_distance(self.corner1, self.circumcenter)

	def point_inside_circumcircle(self, point: Coordinates):
		return get_distance(point, self.circumcenter) < self.radius

	def contains_vertex_from_super_triangle(self, super_triangle):
		for corner in self.corners:
			if corner in super_triangle.corners:
				return True
		return False

def get_distance(point1: Coordinates, point2: Coordinates):
	"""By Pythagoras a^2 + b^2 = c^2"""
	return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)

def circumcenter_of_triangle(point1: Coordinates, point2: Coordinates, point3: Coordinates):
	"""Using distance formula?

	I copied this function from https://stackoverflow.com/q/58116412/16279075 that I reformed and 
	cleaned a little."""
	ad = point1.x **2 + point1.y **2
	bd = point2.x **2 + point2.y **2
	cd = point3.x **2 + point3.y **2
	distance = 2 * (point1.x * (point2.y - point3.y) + point2.x * (point3.y - point1.y) + point3.x * (point1.y - point2.y))
	if distance == 0:
		distance = 0.1
	x_coordinate = 1 / distance * (ad * (point2.y - point3.y) + bd * (point3.y - point1.y) + cd * (point1.y - point2.y))
	y_coordinate = 1 / distance * (ad * (point3.x - point2.x) + bd * (point1.x - point3.x) + cd * (point2.x - point1.x))
	return Coordinates(x_coordinate, y_coordinate)
