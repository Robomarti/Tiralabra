import logic.dungeon_generation

dg = logic.dungeon_generation.DungeonGenerator()

def generate_dungeon():
	while True:
		dg.generate_blank_map()
		room_count = dg.room_generator.room_count
		for _ in range(room_count):
			dg.generate_room()
		if len(dg.rooms) > 2:
			break

	dg.start_delaunay()
	print("Map after random room placement:")
	dg.print_map(dg.map)

	dg.remove_duplicates_from_paths()
	delaunay_map = dg.connect_rooms(dg.paths)
	print("Map after Delaunay triangulation:")
	dg.print_map(delaunay_map)

	spanned_paths = dg.start_spanning()
	span_map = dg.connect_rooms(spanned_paths)
	print("Map after minimum spanning tree:")
	printable = dg.color_map(span_map)
	dg.print_map(printable)

generate_dungeon()
