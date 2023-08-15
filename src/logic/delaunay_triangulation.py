from datatypes.coordinates import Coordinates
from datatypes.triangle import Triangle

"""Shameless copy of https://stackoverflow.com/q/58116412/16279075 that I reformed and 
cleaned a little.

In addition to that, I fixed the bug that https://stackoverflow.com/users/11306106/giveme30dollars 
asked about their code in their original post"""

def delaunay_triangulation(points, width, length) -> list[Triangle]:
	triangulation = []
	st_point1 = Coordinates(int(width / 2), -length*2)
	st_point2 = Coordinates(3*width, length*2)
	st_point3 = Coordinates(-2*width, length*2)
	super_triangle = Triangle(st_point1,st_point2,st_point3)
	triangulation.append(super_triangle)

	for point in points:
		bad_triangles = []
		for triangle in triangulation:
			if triangle.is_point_in_circumcircle(point):
				bad_triangles.append(triangle)

		polygon = []
		for triangle in bad_triangles:
			for triangle_edge in triangle.edges:
				shared = False
				for other in bad_triangles:
					if triangle == other:
						continue
					for other_edge in other.edges:
						if edge_is_equal(triangle_edge, other_edge):
							shared = True
				if shared is False:
					polygon.append(triangle_edge)

		for i in range(len(bad_triangles)-1,-1,-1):
			triangle = triangulation[i]
			triangulation.remove(triangle)

		for edge in polygon:
			new_triangle = Triangle(edge[0],edge[1],point)
			triangulation.append(new_triangle)

	for i in range(len(triangulation)-1, -1, -1):
		triangle = triangulation[i]
		if triangle.has_vertex(st_point1):
			triangulation.remove(triangle)
		elif triangle.has_vertex(st_point2):
			triangulation.remove(triangle)
		elif triangle.has_vertex(st_point3):
			triangulation.remove(triangle)

	return triangulation

def edge_is_equal(edge1: list[Coordinates], edge2: list[Coordinates]):
	if (edge1[0] == edge2[0] and edge1[1] == edge2[1]) or (edge1[0] == edge2[1] and edge1[1] == edge2[0]):
		return True
	return False
