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

	#Algoritmi aloittaa puun muodostamisen tilanteesta, jossa puussa on vain yksi solmu
	tree = []
	tree.append(vertices[0])
	vertices.remove(vertices[0])
	new_paths = []

	while len(vertices) > 0:
		minimum_weight = inf
		chosen_path = ()
		vertex_to_add = ()

		#Tämän jälkeen se etsii joka vaiheessa kevyimmän kaaren, 
		for i in range(len(paths)):
			#jonka toinen päätesolmu kuuluu puuhun ja toinen päätesolmu on vielä puun ulkopuolella
			if paths[i][0] in tree and paths[i][1] not in tree:
				length_of_edge = get_distance(paths[i][0],paths[i][1])
				if length_of_edge < minimum_weight:
					minimum_weight = length_of_edge
					chosen_path = paths[i]
					vertex_to_add = paths[i][1]

			elif paths[i][1] in tree and paths[i][0] not in tree:
				length_of_edge = get_distance(paths[i][0],paths[i][1])
				if length_of_edge < minimum_weight:
					minimum_weight = length_of_edge
					chosen_path = paths[i]
					vertex_to_add = paths[i][0]

		# ja lisää puuhun tämän kaaren
		vertices.remove(vertex_to_add)
		tree.append(vertex_to_add)
		new_paths.append(chosen_path)

	#Kun kaikki solmut on lisätty puuhun, pienin virittävä puu on valmis.
	return new_paths

def get_distance(point1: tuple, point2: tuple):
	"""Distance = sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2), a.k.a. the
	pythagorean theorem"""
	return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
