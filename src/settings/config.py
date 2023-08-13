"""Cave generation values"""
LENGTH = 20
WIDTH = 20

with open("src/settings/config.txt", "r", encoding="utf8") as text:
	lines = text.readlines()
	LENGTH = int(lines[0].split(' ')[2])
	WIDTH = int(lines[1].split(' ')[2])
    