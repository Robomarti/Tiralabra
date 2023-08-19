from math import inf, sqrt

def reverse_prim(paths: list):
	vertices = []
	for path in paths:
		point1 = path[0]
		point2 = path[1]
		if point1 not in vertices:
			vertices.append(point1)
		if point2 not in vertices:
			vertices.append(point2)

	weighted_distances = generate_distances(vertices, paths)
	print(weighted_distances)


def generate_distances(vertices: list[tuple], edges: list[tuple]):
	"""Takes a list of all the vertices and all the edges, and
	constructs a dictionary of connections between vertices, which it
	uses to calculate lengths of all edges"""

	connections = {}
	for edge in edges:
		if edge[0] not in connections:
			connections[edge[0]] = []
		connections[edge[0]].append(edge[1])

		if edge[1] not in connections:
			connections[edge[1]] = []
		connections[edge[1]].append(edge[0])
			
	distances = []
	for i in range(len(vertices)):
		row = []
		for j in range(len(vertices)):
			if vertices[j] in connections[vertices[i]]:
				distance = get_distance(vertices[i], vertices[j])
			else:
				distance = 0
			row.append(distance)
		distances.append(row)

	return distances

def get_distance(point1, point2):
	"""Distance = sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2), a.k.a. the
	pythagorean theorem"""
	return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

