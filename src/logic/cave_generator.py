# pylint: disable-all

import random
import settings.config
import logic.perlin_noise
import logic.cellular_automata

class CaveGenerator:
	def __init__(self):
		self.map = []
		self.length = settings.config.LENGTH
		self.width = settings.config.WIDTH
		self.floor_chance = settings.config.FLOOR_CHANCE
		self.perlin_floor_chance = settings.config.PERLIN_FLOOR_CHANCE

	def generate_map(self):
		"""Generates the initial map randomly.
		A cell will be a wall with a (1-floor_chance)*100 % chance
		"""

		for _ in range(self.length):
			row = []
			for _ in range(self.width):
				if random.random() < self.floor_chance:
					row.append(" ")
				else:
					row.append("#")
			self.map.append(row)

	def generate_noise_map(self):
		for y in range(self.length):
			row = []
			for x in range(self.width):
				randomness = random.random() * random.randint(1,20)
				xy = logic.perlin_noise.perlin_noise(x/randomness,y/randomness)
				if xy < self.floor_chance:
					row.append(" ")
				else:
					row.append("#")
			self.map.append(row)

	def generate_blank_map(self):
		for _ in range(self.length):
			row = []
			for _ in range(self.width):
				row.append("#")
			self.map.append(row)

	def print_map(self):
		"""Prints every row of the map instead of the whole map at once, so that it is more readable"""

		print()
		for row in self.map:
			print(" ".join(row))
		print()

	def smoothen(self):
		logic.cellular_automata.cellular_automata(self.map, self.length, self.width)

	def create_walls(self):
		"""Creates a border of walls around the map
		This should always be called after the generate_map() function
		"""

		for y in range(1,len(self.map)-1):
			self.map[y][0] = "#"
			self.map[y][-1] = "#"
		self.map[0] = ["#"] * len(self.map[0])
		self.map[-1] = ["#"] * len(self.map[0])

	def change_width_and_length(self, width, length):
		self.width = width
		self.length = length
