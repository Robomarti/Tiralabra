import logic.dungeon_generation

dg = logic.dungeon_generation.DungeonGenerator()

def generate_dungeon():
	dg.generate_blank_map()
	room_count = dg.room_generator.get_room_count()
	for _ in range(room_count):
		dg.generate_room()
	dg.print_map()
	dg.print_rooms()

generate_dungeon()
