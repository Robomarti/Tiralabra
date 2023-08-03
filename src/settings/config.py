"""Cave generation values"""
LENGTH = 20
WIDTH = 20
FLOOR_CHANCE = 0.4

"""Perlin noise values"""
PERLIN_FLOOR_CHANCE = 0.4
INTERPOLATE_STATE = "DEFAULT"
CLAMPING = False

with open("src/settings/config.txt", "r", encoding="utf8") as text:
	lines = text.readlines()
	LENGTH = int(lines[0].split(' ')[2])
	WIDTH = int(lines[1].split(' ')[2])
	FLOOR_CHANCE = float(lines[2].split(' ')[2])
    