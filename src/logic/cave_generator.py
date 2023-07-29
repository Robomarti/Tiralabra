import random
import settings.config

length = settings.config.LENGTH
width = settings.config.WIDTH
floor_chance = settings.config.FLOOR_CHANCE

class CaveGenerator:
	def __init__(self):
		self.map = []

	def generate_map(self):
		"""Generates the initial map randomly.
		A cell will be a wall with a (1-floor_chance)*100 % chance
		"""

		for _ in range(length):
			row = []
			for _ in range(width):
				if random.random() > floor_chance:
					row.append("#")
				else:
					row.append(" ")
			self.map.append(row)

	def print_map(self):
		"""Prints every row of the map instead of the whole map at once, so that it is more readable"""

		print()
		for row in self.map:
			print(" ".join(row))
		print()

	def wall_count(self, x, y):
		"""Calculates every neighbour of the given cell in a 3x3 area.
		Returns the number of neighbours.

		Arguments:
			x: the x coordinate of the cell
			y: the y coordinate of the cell
		"""

		wallcount = 0
		for i in (-1,0,1):
			for j in (-1,0,1):
				if self.map[i+y][j+x] == "#" and not (i == 0 and j == 0):
					wallcount += 1

		return wallcount

	def cellular_automata(self):
		"""Modifies the map by making every cell more like its neighbours using cellular automata."""		

		for y in range(1,length-1):
			for x in range(1,width-1):
				wallcount = self.wall_count(x, y)
				if wallcount > 5:
					self.map[y][x] = "#"
				elif self.map[y][x] == "#" and wallcount > 3:
					self.map[y][x] = "#"
				else:
					self.map[y][x] = " "

	def create_walls(self):
		"""Creates a border of walls around the map
		This should always be called after the generate_map() function
		"""

		for y in range(1,len(self.map)-1):
			self.map[y][0] = "#"
			self.map[y][-1] = "#"
		self.map[0] = ["#"] * len(self.map[0])
		self.map[-1] = ["#"] * len(self.map[0])
