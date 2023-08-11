from datatypes.rooms import Rooms
from datatypes.coordinates import Coordinates
from math import sqrt

class DelaunayTriangulation:
	def __init__(self):
		self.points = []
		self.edges = []

	def add_rooms(self, rooms: list):
		points = []
		for room in rooms:
			points.append(room.center_point)
		self.points = points

	def put_points_in_increasing_order(self):
		self.points.sort(key=self.__sort_by_coordinates)

	def __sort_by_coordinates(self, center_point: Coordinates):
		return (center_point.x, center_point.y)

	def get_points(self):
		return self.points

	def start_halve_points(self):
		return self.halve_points(self.points)

	def halve_points(self, point_set):
		if len(point_set) > 3:
			middle = int(len(point_set) / 2)
			first_half = self.halve_points(point_set[:middle])
			second_half = self.halve_points(point_set[middle:])
			return first_half + second_half
		else:
			if len(point_set) == 3:
				self.make_triangles(point_set)
			else:
				self.make_edge(point_set)
			return point_set

	def find_circle_with_three_points(self, point_set):
		x1 = point_set[0].x
		y1 = point_set[0].y
		x2 = point_set[1].x
		y2 = point_set[1].y
		x3 = point_set[2].x
		y3 = point_set[2].y
		
		x12 = x1 - x2
		x13 = x1 - x3
		y12 = y1 - y2
		y13 = y1 - y3
		
		x21 = x2 - x1
		x31 = x3 - x1
		y21 = y2 - y1
		y31 = y3 - y1

		sx13 = x1**2 - x3**2
		sy13 = y1**2 - y3**2
		sx21 = x2**2 - x1**2
		sy21 = y2**2 - y1**2

		f = (((sx13) * (x12) + (sy13) * (x12) + (sx21) * (x13) + (sy21) * (x13)) // (2 * ((y31) * (x12) - (y21) * (x13))))
		g = (((sx13) * (y12) + (sy13) * (y12) + (sx21) * (y13) + (sy21) * (y13)) // (2 * ((x31) * (y12) - (x21) * (y13))))
		c = (-x1**2 - y1**2 - 2 * g * x1 - 2 * f * y1)
		# equation of circle is x^2 + y^2 + 2*g*x + 2*f*y + c = 0
		# where centre is (h = -g, k = -f) and
		# radius^2 = h^2 + k^2 - c
		h = -g
		k = -f
		centre = Coordinates(h,k)
		radius = sqrt(h * h + k * k - c)
		print("Centre = ", centre)
		print("Radius = ", radius)
		return (centre, radius)

	def check_if_point_not_in_circle(self, point: Coordinates, centre: Coordinates, radius):
		distance = sqrt((point.x-centre.x)**2 + (point.y - centre.y)**2)
		if distance > radius:
			return True
		return False

	def make_triangles(self,point_set):
		self.edges.append((point_set[0],point_set[1]))
		self.edges.append((point_set[0],point_set[2]))
		self.edges.append((point_set[1],point_set[0]))
		self.edges.append((point_set[1],point_set[2]))
		self.edges.append((point_set[2],point_set[0]))
		self.edges.append((point_set[2],point_set[1]))

	def make_edge(self, point_set):
		self.edges.append((point_set[0],point_set[1]))
		self.edges.append((point_set[1],point_set[0]))

	def print_edges(self):
		for edge in self.edges:
			print(edge)
