from datatypes.coordinates import Coordinates
from datatypes.triangle import Triangle

def delaunay_triangulation(point_list, width, length) -> list[Triangle]:
	#// pointList is a set of coordinates defining the points to be triangulated
	point_list = point_list
	#triangulation := empty triangle mesh data structure
	triangulation = []


    #add super-triangle to triangulation // must be large enough to completely contain all the points in pointList ## I added 2 super triangles so that they form a rectangle
	super_triangle_1 = Triangle(Coordinates(-1,-1), Coordinates(-1,length+1), Coordinates(width+1, length+1))
	super_triangle_2 = Triangle(Coordinates(-1,-1), Coordinates(width+1,-1), Coordinates(width+1, length+1))
	triangulation.append(super_triangle_1)
	triangulation.append(super_triangle_2)


    #for each point in pointList do // add all the points one at a time to the triangulation
	for point in point_list:
        #badTriangles := empty set
		bad_triangles = []
        #for each triangle in triangulation do // first find all the triangles that are no longer valid due to the insertion
		for triangle in triangulation:
            #if point is inside circumcircle of triangle
			if triangle.point_inside_circumcircle(point):
                #add triangle to badTriangles
				bad_triangles.append(triangle)


        #polygon := empty set
		polygon = []


        #for each triangle in badTriangles do // find the boundary of the polygonal hole
		for triangle in bad_triangles:
            #for each edge in triangle do
			for edge in triangle.edges::
                #if edge is not shared by any other triangles in badTriangles
				if edge_not_in_other_bad_triangles(edge, bad_triangles): 
                    #add edge to polygon
					polygon.append(edge)


        #for each triangle in badTriangles do // remove them from the data structure
		for i in range(len(bad_triangles)-1,-1,-1):
            #remove triangle from triangulation
			remove_triangle_from_triangulation(bad_triangles[i], triangulation)


        #for each edge in polygon do // re-triangulate the polygonal hole
		for edge in polygon:
            #newTri := form a triangle from edge to point
			new_triangle = Triangle(edge[0], edge[1], point)
            #add newTri to triangulation
			triangulation.append(new_triangle)
    

	#for each triangle in triangulation // done inserting points, now clean up
	for i in range(len(triangulation)-1,-1,-1):
			#if triangle contains a vertex from original super-triangles
			if triangulation[i].contains_vertex_from_super_triangle(super_triangle_1):
				#remove triangle from triangulation
				triangulation.remove(triangulation[i])
			#if triangle contains a vertex from original super-triangles
			elif triangulation[i].contains_vertex_from_super_triangle(super_triangle_2):
				#remove triangle from triangulation
				triangulation.remove(triangulation[i])


	return triangulation


def edge_not_in_other_bad_triangles(edge, bad_triangles: list[Triangle]):
	edge2 = (edge[1], edge[0])
	for triangle in bad_triangles:
		if edge in triangle.edges or edge2 in triangle.edges:
			return False
	return True


def remove_triangle_from_triangulation(triangle, triangulation):
	triangulation.remove(triangle)


# Triangle class


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
		self.radius = distance(self.corner1, self.circumcenter)


	def point_inside_circumcircle(self, point: Coordinates):
		return distance(point, self.circumcenter) < self.radius


	def contains_vertex_from_super_triangle(self, super_triangle):
		for corner in self.corners:
			if corner in super_triangle.corners:
				return True
		return False


def distance(point1: Coordinates, point2: Coordinates):
	"""By Pythagoras a^2 + b^2 = c^2"""
	return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)


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
