import logic.cave_generator
import logic.dungeon_generation

cg = logic.cave_generator.CaveGenerator()
dg = logic.dungeon_generation.DungeonGenerator()

def generate_with_noise():
	cg.generate_noise_map()
	cg.create_walls()
	cg.print_map()
	cg.smoothen()
	cg.smoothen()
	cg.smoothen()
	cg.smoothen()
	cg.print_map()

def generate_normally():
	cg.generate_map()
	cg.create_walls()
	cg.print_map()
	cg.smoothen()
	cg.smoothen()
	cg.smoothen()
	cg.smoothen()
	cg.print_map()

def generate_dungeon():
	dg.generate_blank_map()
	room_count = dg.get_room_count()
	for _ in range(room_count):
		print(dg.get_room_size())
		dg.generate_room()
	dg.print_map()

generate_dungeon()
