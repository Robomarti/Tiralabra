from datatypes.coordinates import Coordinates
from datatypes.triangle import Triangle

def delaunay_triangulation(point_list: list[Coordinates], width, length) -> list[Triangle]:
	"""Construct paths between all the centers of the rooms that pass the Delaunay rule.
	For more documanetation about this functions see documentation/bowyerwatson_to_python.py
	or https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm#Pseudocode"""
	triangulation = []
	super_triangle_1 = Triangle(Coordinates(-1,-1), Coordinates(-1,length+1), Coordinates(width+1, length+1))
	super_triangle_2 = Triangle(Coordinates(-1,-1), Coordinates(width+1,-1), Coordinates(width+1, length+1))
	triangulation.append(super_triangle_1)
	triangulation.append(super_triangle_2)

	for point in point_list:
		bad_triangles = []

		for triangle in triangulation:
			if triangle.point_inside_circumcircle(point):
				bad_triangles.append(triangle)

		polygon = []
		for triangle in bad_triangles:
			for edge in triangle.edges:
				if edge_not_in_other_bad_triangles(triangle, edge, bad_triangles):
					polygon.append(edge)

		for i in range(len(bad_triangles)-1,-1,-1):
			triangulation.remove(bad_triangles[i])

		for edge in polygon:
			new_triangle = Triangle(edge[0], edge[1], point)
			triangulation.append(new_triangle)

	for i in range(len(triangulation)-1,-1,-1):
		if triangulation[i].contains_vertex_from_super_triangle(super_triangle_1):
			triangulation.remove(triangulation[i])
		elif triangulation[i].contains_vertex_from_super_triangle(super_triangle_2):
			triangulation.remove(triangulation[i])

	return triangulation

def edge_not_in_other_bad_triangles(own_triangle, edge, bad_triangles: list[Triangle]):
	edge2 = (edge[1], edge[0])
	for triangle in bad_triangles:
		if triangle != own_triangle:
			if edge in triangle.edges or edge2 in triangle.edges:
				return False
	return True
