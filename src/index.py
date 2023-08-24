import logic.dungeon_generation

dg = logic.dungeon_generation.DungeonGenerator()

def generate_dungeon():
	dg.generate_blank_map()
	room_count = dg.room_generator.room_count
	for _ in range(room_count):
		dg.generate_room()
	print("Map after random room placement:")
	dg.print_map(dg.map)

	if dg.start_delaunay():
		dg.remove_duplicates_from_paths()
		delaunay_map = dg.connect_rooms(dg.paths)
		print("Map after Delaunay triangulation:")
		dg.print_map(delaunay_map)

		dg.start_spanning()
		span_map = dg.connect_rooms(dg.prim)
		print("Map after minimum spanning tree:")
		printable = dg.color_map(span_map)
		dg.print_map(printable)

generate_dungeon()
