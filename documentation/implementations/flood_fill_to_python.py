def flood_fill(game_map:list, starting_node: tuple):
	"""Simple flood fill algorithm using
	pseudocode from https://en.wikipedia.org/wiki/Flood_fill"""
	#1. Set Q to the empty queue or stack.
	queue_q = []
	#2. Add node to the end of Q.
	queue_q.append(starting_node)
	#3. While Q is not empty:
	while len(queue_q) > 0:
		#4.   Set n equal to the first element of Q.
		#5.   Remove first element from Q.
		node_n = queue_q.pop(0)
		#6.   If n is Inside:
		is_inside = 0
		if game_map[node_n[1]][node_n[0]] == " ":
			is_inside = 1
		elif game_map[node_n[1]][node_n[0]] == ".":
			is_inside = 2

		if is_inside == 1 or is_inside == 2: 
			#Set the n
			if is_inside == 1:
				game_map[node_n[1]][node_n[0]] = "-"
			else:
				game_map[node_n[1]][node_n[0]] = "o"

			#Add the node to the west of n to the end of Q.
			queue_q.append((node_n[0]-1, node_n[1]))
			#Add the node to the east of n to the end of Q.
			queue_q.append((node_n[0]+1, node_n[1]))
			#Add the node to the north of n to the end of Q.
			queue_q.append((node_n[0], node_n[1]-1))
			#Add the node to the south of n to the end of Q.

	#7. Continue looping until Q is exhausted.
	#8. Return.
	return game_map
