from dataclasses import dataclass
from datatypes.coordinates import Coordinates

@dataclass
class Rooms:
	"""A class for a custom datatype Rooms represents a generated room inside the dungeon"""
	center_point: Coordinates
	cells: list
	connected_rooms: list

def find_room_by_cell(cell: tuple, room_list: list[Rooms]):
	for room in room_list:
		if cell in room.cells:
			return room
	return None

def remove_duplicates(room: Rooms):
	"""Removes duplicates in a room's connected_rooms list"""
	visited = []
	for point in room.connected_rooms:
		if not point in visited:
			visited.append(point)
	room.connected_rooms = visited

def is_own_room(cell: tuple, room_center: tuple, rooms: list[Rooms]):
	found = find_room_by_cell(cell, rooms)
	if found and (found.center_point.x, found.center_point.y) == room_center:
		return True
	return False