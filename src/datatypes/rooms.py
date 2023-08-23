from __future__ import annotations
from math import inf
from dataclasses import dataclass
from datatypes.coordinates import Coordinates

@dataclass
class Rooms:
	"""A class for a custom datatype Rooms represents a generated room inside the dungeon"""
	center_point: Coordinates
	cells: list
	connected_rooms: list
	parent: Rooms

def find_room_by_cell(cell: tuple, room_list: list[Rooms]):
	for room in room_list:
		if cell in room.cells:
			return room
	return None

def find_room_by_center(center: tuple, room_list: list[Rooms]):
	for room in room_list:
		if center == (room.center_point.x, room.center_point.y):
			return room
	return None

def is_own_room(cell: tuple, room_center: tuple, rooms: list[Rooms]):
	found = find_room_by_cell(cell, rooms)
	if found and (found.center_point.x, found.center_point.y) == room_center:
		return True
	return False


def find_longest_path(rooms: list[Rooms]):
	"""Finds the two most distant rooms by first finding the most distant room from the random first room
	in rooms. Then it finds the most distant room from that room.
	Source: https://saturncloud.io/blog/algorithm-for-diameter-of-a-graph-explained-for-data-scientists/#:~:text=The%20Algorithm%3A%20Breadth-First%20Search,from%20a%20given%20source%20node."""
	most_distant_from_first = find_most_distant(rooms, rooms[0])
	most_distant_from_initial = find_most_distant(rooms, most_distant_from_first)
	return (most_distant_from_first, most_distant_from_initial)

def find_most_distant(rooms: list[Rooms], root: Rooms):
	"""Using pseudocode from https://en.wikipedia.org/wiki/Breadth-first_search"""
	explored = {}
	for room in rooms:
		room.parent = None
		explored[(room.center_point.x,room.center_point.y)] = False

	queue_q = []
	explored[(root.center_point.x, root.center_point.y)] = True
	queue_q.append(root)

	while len(queue_q) > 0:
		vertex_v = queue_q.pop(0)
		for connected in vertex_v.connected_rooms:
			if not explored[(connected.center_point.x, connected.center_point.y)]:
				explored[(connected.center_point.x, connected.center_point.y)] = True
				connected.parent = vertex_v
				queue_q.append(connected)

	return find_room_by_center(longest_path(rooms), rooms)

def longest_path(rooms):
	"""Generates distances from each room to their the root room.
	Returns the coordinates of the most distant room"""
	distances = {}
	for room in rooms:
		if room.parent:
			distances[(room.center_point.x, room.center_point.y)] = distance_to_root(room, room.parent)

	return max(distances, key=distances.get)

def distance_to_root(room, parent):
	"""Recursively find the length of the path to the only node without a parent"""
	if parent.parent:
		return(get_distance_of_path(room, parent) + distance_to_root(parent, parent.parent))
	return get_distance_of_path(room, parent)

def get_distance_of_path(point1: Rooms, point2: Rooms):
	return abs(point2.center_point.x - point1.center_point.x) + abs(point2.center_point.y - point1.center_point.y)
