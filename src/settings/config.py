with open("src/settings/config.txt", "r", encoding="utf8") as text:
	lines = text.readlines()
	try:
		LENGTH = int(lines[0].split(' ')[2])
	except:
		LENGTH = 30

	try:
		WIDTH = int(lines[1].split(' ')[2])
	except:
		WIDTH = 30

	if WIDTH < 20:
		WIDTH = 20

	USE_SPANNING = lines[2].split(' ')[2]
	if USE_SPANNING not in ["True", "False"]:
		USE_SPANNING = "True"
    