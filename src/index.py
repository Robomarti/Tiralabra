import logic.dungeon_generation
from settings.config import get_configs

dg = logic.dungeon_generation.DungeonGenerator()
use_spanning = get_configs()[2]

def generate_dungeon():
	while True:
		dg.generate_blank_map()
		room_count = dg.room_generator.room_count
		for _ in range(room_count):
			dg.generate_room()

		if len(dg.rooms) > 2:
			break

	print("Map after random room placement:")
	dg.print_map(dg.map)

	dg.start_delaunay()
	dg.remove_duplicates_from_paths()
	delaunay_map = dg.connect_rooms(dg.paths)
	print("Map after Delaunay triangulation:")
	dg.print_map(delaunay_map)

	if use_spanning == "True":
		spanned_paths = dg.start_spanning()
		dg.create_room_connections(spanned_paths)
		span_map = dg.connect_rooms(spanned_paths)
		print("Map after minimum spanning tree and flood fill:")
		printable = dg.color_map(span_map)
		dg.print_map(printable)
	else:
		dg.create_room_connections(dg.paths)
		print("Map after flood fill:")
		printable = dg.color_map(delaunay_map)
		dg.print_map(printable)

generate_dungeon()
