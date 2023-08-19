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

	# 1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
	# 2. Grow the tree by one edge: Of the edges that connect the tree to vertices not yet in the tree, find the maximum-weight edge, and transfer it to the tree.
	# 3. Repeat step 2 (until all vertices are in the tree).
	#In more detail, it may be implemented following the pseudocode below.

	# 1. Associate with each vertex v of the graph a number C[v] (the greatest cost of a connection to v) and an edge E[v] (the edge providing that greatest connection).
	#To initialize these values, set all values of C[v] to -∞ (or to any number smaller than the minimum edge weight) and set each E[v] to a special flag value indicating
	# that there is no edge connecting v to earlier vertices.

	distances_edges = generate_distances(vertices, paths)
	distances_c = distances_edges[0]
	edges_e = distances_edges[1]

	# 2. Initialize an empty forest F and a set Q of vertices that have not yet been included in F (initially, all vertices).

	forest_f = set()
	set_q = set(vertices)
	# 3. Repeat the following steps until Q is empty:
	while len(set_q) > 0:
		# Find and remove a vertex v from Q having the maximum possible value of C[v]
		vertex_v = ()
		maximum_value = -inf
		for vertex in set_q:
			if distances_c[vertex] > maximum_value:
				vertex_v = vertex
				maximum_value = distances_c[vertex]

		set_q.remove(vertex_v)

		# Add v to F
		forest_f.add(vertex_v)

		# Loop over the edges vw connecting v to other vertices w.
		for edge_wv in paths:
			if edge_wv[0] == vertex_v:
				edge_w = edge_wv[1]
				#For each such edge, if w still belongs to Q and vw has greater weight than C[w], perform the following steps:
				if edge_w in set_q and get_distance(edge_wv[0], edge_w) > distances_c[edge_w]:
					# Set C[w] to the cost of edge vw
					distances_c[edge_w] = get_distance(edge_wv[0], edge_w)
					# Set E[w] to point to edge vw.
					edges_e[edge_w] = edge_wv

			elif edge_wv[1] == vertex_v:
				edge_w = edge_wv[0]
				#For each such edge, if w still belongs to Q and vw has greater weight than C[w], perform the following steps:
				if edge_w in set_q and get_distance(edge_wv[1], edge_w) > distances_c[edge_w]:
					# Set C[w] to the cost of edge vw
					distances_c[edge_w] = get_distance(edge_wv[1], edge_w)
					# Set E[w] to point to edge vw.
					edges_e[edge_w] = edge_wv

	# 4. Return F, which specifically includes the corresponding edges in E
	return edges_e

def generate_distances(vertices: list[tuple], edges: list[tuple]):
	"""Takes a list of all the vertices and all the edges, and
	constructs a dictionary of connections between vertices, which it
	uses to calculate lengths of all edges"""

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
		distances_c[vertices[i]] = -inf
		new_edges_e[vertices[i]] = (-1,-1)
		for j in range(len(vertices)):
			if vertices[j] in connections[vertices[i]]:
				distance = get_distance(vertices[i], vertices[j])
			else:
				distance = -1
			if distance > distances_c[vertices[i]]:
				distances_c[vertices[i]] = distance
				new_edges_e[vertices[i]] = (vertices[i], vertices[j])

	return (distances_c, new_edges_e)

def get_distance(point1, point2):
	"""Distance = sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2), a.k.a. the
	pythagorean theorem"""
	return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
