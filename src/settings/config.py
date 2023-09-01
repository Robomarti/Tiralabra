def get_configs():
	with open("src/settings/config.txt", "r", encoding="utf8") as text:
		lines = text.readlines()
		try:
			if lines[0].split(' ')[0] != "LENGTH":
				length = 30
			else:
				length = int(lines[0].split(' ')[2])
		except:
			length = 30

		try:
			if lines[1].split(' ')[0] != "WIDTH":
				width = 30
			else:
				width = int(lines[1].split(' ')[2])
		except:
			width = 30

		length = max(length, 20)

		width = max(width, 20)

		try:
			if lines[2].split(' ')[0] != "USE_SPANNING":
				spanning = "True"
			else:
				spanning = lines[2].split(' ')[2]
				if spanning not in ["True", "False"]:
					spanning = "True"
		except:
			spanning = "True"

	return (length, width, spanning)
		