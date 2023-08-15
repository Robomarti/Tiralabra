
def generate_distances(vertices: list, edges: list[tuple]):
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
				distance = vertices[i] + vertices[j]
			else:
				distance = 0
			row.append(distance)
		distances.append(row)

	return distances

edges = [(3,1), (4,2), (0,3), (3,4), (0,3)]
vertices = []
for edge in edges:
	if not edge[0] in vertices:
		vertices.append(edge[0])
	if not edge[1] in vertices:
		vertices.append(edge[1])

print(vertices)
print(generate_distances(vertices, edges))