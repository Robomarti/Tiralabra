from math import inf, sqrt

class Prim:
	def __init__(self, edges):
		vertices = []
		for edge in edges:
			if not edge[0] in vertices:
				vertices.append(edge[0])
			if not edge[1] in vertices:
				vertices.append(edge[1])

		print()
		print("vertices:", vertices)
		self.distances = self.generate_distances(vertices, edges)
		print()
		print("distances:",self.distances)
		print()

	def generate_distances(self, vertices: list[tuple], edges: list[tuple]):
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
					distance = self.get_distance(vertices[i], vertices[j])
				else:
					distance = 0
				row.append(distance)
			distances.append(row)

		return distances

	def get_distance(self, point1, point2):
		"""Distance = sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)"""
		return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

	def start(self, vertices, index=0):
		visited = [True] * len(vertices)
		distances = [0] * len(vertices)
		parents = [0] * len(vertices)

		for i in range(len(vertices)):
			visited[i] = False
			distances[i] = -inf

		distances[index] = inf
		parents[index] = -1

		for i in range(len(vertices)-1):
			max_vertex_index = self.find_max_distance(visited, distances)
			visited[max_vertex_index] = True
			for j in range(len(vertices)):
				if self.distances[j][max_vertex_index] != 0 and visited[j] == False:
					if self.distances[j][max_vertex_index] > distances[j]:
						distances[j] = self.distances[j][max_vertex_index]
						parents[j] = max_vertex_index

	def find_max_distance(self, visited, distances):
		index = -1
		maximum_weight = -inf
		for i in range(len(self.vertices)):
			if visited[i] == False and distances[i] > maximum_weight:
				maximum_weight = distances[i]
				index = i
		return index
