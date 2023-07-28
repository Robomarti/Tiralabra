import random

LENGTH = 20
HEIGHT = 20

class CaveGenerator:
	def __init__(self):
		self._map = []

	def generate_map(self):
		for _ in range(HEIGHT):
			row = []
			for _ in range(LENGTH):
				if random.random() > 0.4:
					row.append("x")
				else:
					row.append(" ")
			self._map.append(row)
	
	def print_map(self):
		for row in self._map:
			print(row)