def wall_count(game_map, x, y):
	"""Calculates every neighbour of the given cell in a 3x3 area.
	Returns the number of neighbours.

	Arguments:
		x: the x coordinate of the cell
		y: the y coordinate of the cell
	"""

	wallcount = 0
	for i in (-1,0,1):
		for j in (-1,0,1):
			if game_map[i+y][j+x] == "#" and not (i == 0 and j == 0):
				wallcount += 1

	return wallcount

def cellular_automata(game_map, length, width):
	"""Modifies the map by making every cell more like its neighbours using cellular automata."""		

	for y in range(1,length-1):
		for x in range(1,width-1):
			wallcount = wall_count(game_map, x, y)
			if wallcount > 5:
				game_map[y][x] = "#"
			elif game_map[y][x] == "#" and wallcount > 3:
				game_map[y][x] = "#"
			else:
				game_map[y][x] = " "
