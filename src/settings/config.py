LENGTH = 20
WIDTH = 20
FLOOR_CHANCE = 0.4

with open("src/settings/config.txt", "r") as text:
	lines = text.readlines()
	LENGTH = int(lines[0].split(' ')[2])
	WIDTH = int(lines[1].split(' ')[2])
	FLOOR_CHANCE = float(lines[2].split(' ')[2])
    