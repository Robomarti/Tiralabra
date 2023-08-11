from dataclasses import dataclass
from datatypes.coordinates import Coordinates

@dataclass
class Rooms:
	"""A class for a custom datatype Rooms represents a generated room inside the dungeon"""
	starting_coordinate: Coordinates
	center_point: Coordinates
	cells: list
	connected_rooms: list
	delaunay_value: int
