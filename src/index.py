import logic.dungeon_generation

dg = logic.dungeon_generation.DungeonGenerator()

def generate_dungeon():
	dg.generate_blank_map()
	room_count = dg.room_generator.room_count
	for _ in range(room_count):
		dg.generate_room()
	dg.print_map(dg.map)

	dg.start_delaunay()
	dg.remove_duplicates_from_paths()
	delaunay_map = dg.connect_rooms(dg.paths)
	dg.print_map(delaunay_map)

	dg.start_spanning()
	span_map = dg.connect_rooms(dg.prim)
	dg.print_map(span_map)

generate_dungeon()
