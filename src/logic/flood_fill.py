def flood_fill(game_map: list, starting_node: tuple):
	"""Simple flood fill algorithm using
	pseudocode from https://en.wikipedia.org/wiki/Flood_fill
	Replaces floor cells with blue color, and path cells with yellow"""
	queue_q = []
	queue_q.append(starting_node)

	while len(queue_q) > 0:
		node_n = queue_q.pop(0)
		is_inside = 0
		if game_map[node_n[1]][node_n[0]] == " ":
			is_inside = 1
		elif game_map[node_n[1]][node_n[0]] == ".":
			is_inside = 2
		#so that we don't rewrite visited cells
		elif game_map[node_n[1]][node_n[0]] == "#":
			is_inside = 3

		if is_inside == 1 or is_inside == 2:
			if is_inside == 1:
				game_map[node_n[1]][node_n[0]] = '\u001b[0;34;44m '
			else:
				game_map[node_n[1]][node_n[0]] = '\u001b[0;37;43m.'

			queue_q.append((node_n[0]-1, node_n[1]))
			queue_q.append((node_n[0]+1, node_n[1]))
			queue_q.append((node_n[0], node_n[1]-1))
			queue_q.append((node_n[0], node_n[1]+1))
		elif is_inside == 3:
			game_map[node_n[1]][node_n[0]] = '\u001b[0;37;40m#'

	return game_map
