import math
import random
from datatypes.coordinates import Coordinates
from datatypes.rectangle import Rectangle
from datatypes.rooms import Rooms

class RoomGenerator():
	def __init__(self, length, width, tile_size):
		self.length = length
		self.width = width
		self.tile_size = tile_size

	def get_room_count(self):
		return math.floor(math.sqrt((self.length - 3) * (self.width - 3) / 4))

	def get_random_point_in_circle(self, radius, center_x, center_y):
		r = radius * math.sqrt(random.random())
		theta = 2 * math.pi * random.random()

		x_coordinate = self.roundm(center_x + r * math.cos(theta), self.tile_size)
		y_coordinate = self.roundm(center_y + r * math.sin(theta), self.tile_size)
		return Coordinates(x_coordinate, y_coordinate)

	def roundm(self, n, tile_size):
		"""Rounds up coordinates so that it snaps to the grid made out of pixels"""

		return math.floor(((n + tile_size - 1) / tile_size)) * tile_size

	def get_room_size(self):
		"""Returns a random sized rectangle. 
		The maximum length and width are calculated with some random math I made up
		Room size is given in a rectangles width and length"""

		room_count = self.get_room_count()
		room_width = random.randint(3, int(self.width / (room_count - 1)) * 2)
		room_length = random.randint(3, int(self.length / (room_count - 1)) * 2)
		return Rectangle(room_width, room_length)

	def generate_room(self, game_map):
		"""Generates a room to an empty place
		Starting corner is offset by the scale of the room to be generated so that the whole room fits better to the map.
		If the initial placement is not empty, it tries to find room from the direction that is given by 
		the function get_away_direction()
		"""

		room_size = self.get_room_size()
		width = int(self.width / 2)
		length = int(self.length / 2)
		starting_corner = self.get_random_point_in_circle(self.get_radius_of_cirle(), width, length)
		starting_corner.x -= room_size.width
		starting_corner.y -= room_size.length

		direction = self.get_away_direction()

		failed_attempts = 0
		while not self.check_if_room(room_size, starting_corner, game_map):
			if failed_attempts < 20:
				failed_attempts += 1
				starting_corner.x += direction.x
				starting_corner.y += direction.y
			else:
				starting_corner = self.get_random_point_in_circle(self.get_radius_of_cirle(), width, length)
				starting_corner.x -= room_size.width
				starting_corner.y -= room_size.length
				failed_attempts = 0

		cells = self.create_room(room_size, starting_corner, game_map)
		new_room = Rooms(starting_corner, len(cells[0]), len(cells), cells)
		return new_room

	def create_room(self, room_size: Rectangle, starting_corner: Coordinates, game_map):
		cells = []
		for y_coordinate in range(starting_corner.y, starting_corner.y + room_size.length):
			row = []
			for x_coordinate in range(starting_corner.x, starting_corner.x + room_size.width):
				if y_coordinate in range(1, len(game_map)-1) \
				and x_coordinate in range(1, len(game_map[y_coordinate])-1) \
				and game_map[y_coordinate][x_coordinate] == "#":
					game_map[y_coordinate][x_coordinate] = " "
					row.append((x_coordinate,y_coordinate))
			cells.append(row)
		return cells

	def check_if_room(self, room_size: Rectangle, starting_corner: Coordinates, game_map):
		"""Checks if there is room for a room
		
		Returns false if there is no room for a room or there is room for a room, but the room would be less than 3 wide or less than 3 long.
		"""		

		for y in range(starting_corner.y-1, starting_corner.y + room_size.length+1):
			if y not in range(len(game_map)) and starting_corner.y < 3:
				return False
			for x in range(starting_corner.x-1, starting_corner.x + room_size.width+1):
				if y in range(len(game_map)) and x in range(len(game_map[0])) and game_map[y][x] != "#":
					return False
				if x not in range(len(game_map[0])) and starting_corner.x < 3:
					return False
		return True

	def get_radius_of_cirle(self):
		length = self.length
		width = self.width
		if length < width:
			smaller = length
		else:
			smaller = width
		return math.floor(smaller / 2)

	def get_away_direction(self):
		"""Returns the direction where the room should head when there is not room for it
		in its original position. The direction will be chosen randomly.
		"""

		direction_chance = random.random()

		if direction_chance > 0.75:
			direction = Coordinates(-1,-1)
		elif direction_chance > 0.50:
			direction = Coordinates(-1,1)
		elif direction_chance > 0.25:
			direction = Coordinates(1,1)
		else:
			direction = Coordinates(1,-1)

		return direction
