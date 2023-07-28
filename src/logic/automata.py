import random

LENGTH = 20
WIDTH = 20

class CaveGenerator:
	def __init__(self):
		self.map = []

	def generate_map(self):
		for y in range(LENGTH):
			row = []
			for x in range(WIDTH):
				if x == 0 or x == WIDTH-1:
					row.append("x")
				elif y == 0 or y == LENGTH-1:
					row.append("x")
				elif random.random() > 0.4:
					row.append("x")
				else:
					row.append(" ")
			self.map.append(row)
	
	def print_map(self):
		for row in self.map:
			print(row)

	def wall_count(self, x, y):
		wallcount = 0
		for i in (-1,0,1):
			for j in (-1,0,1):
				if self.map[i+y][j+x] == "x" and not (i == 0 and j == 0):
					wallcount += 1

		return wallcount
	
	def cellular_automata(self):
		for y in range(1,LENGTH-1):
			for x in range(1,WIDTH-1):
				wallcount = self.wall_count(x, y)
				if wallcount > 4:
					self.map[y][x] = "x"
				elif self.map[y][x] == "x" and wallcount > 3:
					self.map[y][x] = "x"
				else:
					self.map[y][x] = " "