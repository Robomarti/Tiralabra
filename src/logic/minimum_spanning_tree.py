from math import inf, sqrt

def prim(paths: list):
	vertices = []
	for path in paths:
		point1 = path[0]
		point2 = path[1]
		if point1 not in vertices:
			vertices.append(point1)
		if point2 not in vertices:
			vertices.append(point2)

	distances_edges = generate_distances(vertices, paths)
	distances_c = distances_edges[0]
	edges_e = distances_edges[1]

	set_q = set(vertices)

	while len(set_q) > 0:
		vertex_v = ()
		minimum_value = inf
		for vertex in set_q:
			if distances_c[vertex] < minimum_value:
				vertex_v = vertex
				minimum_value = distances_c[vertex]

		set_q.remove(vertex_v)

		for edge_wv in paths:
			if edge_wv[0] == vertex_v:
				edge_w = edge_wv[1]
				if edge_w in set_q and get_distance(edge_wv[0], edge_w) < distances_c[edge_w]:
					distances_c[edge_w] = get_distance(edge_wv[0], edge_w)
					edges_e[edge_w] = edge_wv

			elif edge_wv[1] == vertex_v:
				edge_w = edge_wv[0]
				if edge_w in set_q and get_distance(edge_wv[1], edge_w) < distances_c[edge_w]:
					distances_c[edge_w] = get_distance(edge_wv[1], edge_w)
					edges_e[edge_w] = edge_wv

	return edges_e

def generate_distances(vertices: list[tuple], edges: list[tuple]):
	"""Takes a list of all the vertices and all the edges, and
	constructs a dictionary of connections between vertices, which it
	uses to calculate smallest edges between points"""

	connections = {}
	for edge in edges:
		if edge[0] not in connections:
			connections[edge[0]] = [edge[0]] 
		connections[edge[0]].append(edge[1])

		if edge[1] not in connections:
			connections[edge[1]] = [edge[1]]
		connections[edge[1]].append(edge[0])

	distances_c = {}
	new_edges_e = {}

	for i in range(len(vertices)):
		distances_c[vertices[i]] = inf
		new_edges_e[vertices[i]] = (-1,-1)
		for j in range(len(vertices)):
			if i == j:
				continue
			if vertices[j] in connections[vertices[i]]:
				distance = get_distance(vertices[i], vertices[j])
			else:
				distance = inf

			if distance < distances_c[vertices[i]]:
				distances_c[vertices[i]] = distance
				new_edges_e[vertices[i]] = (vertices[i], vertices[j])

	return (distances_c, new_edges_e)

def get_distance(point1: tuple, point2: tuple):
	"""Distance = sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2), a.k.a. the
	pythagorean theorem"""
	return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
