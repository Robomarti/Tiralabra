from datatypes.coordinates import Coordinates
from datatypes.triangle import Triangle

def delaunay_triangulation(point_list: list[Coordinates], width, length) -> list[Triangle]:
	point_list = point_list
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
				if edge_not_in_other_bad_triangles(edge, bad_triangles):
					polygon.append(edge)
        #for each triangle in badTriangles do // remove them from the data structure
		for i in range(len(bad_triangles)-1,-1,-1):
            #remove triangle from triangulation
			triangulation.remove(bad_triangles[i])
        #for each edge in polygon do // re-triangulate the polygonal hole
		for edge in polygon:
            #newTri := form a triangle from edge to point
			new_triangle = Triangle(edge[0], edge[1], point)
            #add newTri to triangulation
			triangulation.append(new_triangle)

	for triangle in triangulation:
        #if triangle contains a vertex from original super-triangle
		if triangle.contains_vertex_from_super_triangle(super_triangle_1):
            #remove triangle from triangulation
			triangulation.remove(triangle)
	return triangulation

def edge_not_in_other_bad_triangles(edge, bad_triangles: list[Triangle]):
	edge2 = (edge[1], edge[0])
	for triangle in bad_triangles:
		if edge in triangle.edges or edge2 in triangle.edges:
			return False
	return True
