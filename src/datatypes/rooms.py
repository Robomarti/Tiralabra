from dataclasses import dataclass
from datatypes.coordinates import Coordinates

@dataclass
class Rooms:
	"""A class for a custom datatype Rooms represents a generated room inside the dungeon"""
	starting_coordinate: Coordinates
	width: int
	length: int
	cells: list
	center_point: Coordinates
