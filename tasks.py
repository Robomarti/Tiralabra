from invoke import task
import src.settings.config

@task
def start(ctx):
    ctx.run("python src/index.py")

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(test)
def coverage_report(ctx):
    ctx.run("coverage html -i")

#@task
#def format(ctx):
#    ctx.run("autopep8 --in-place --recursive src")

@task
def lint(ctx):
    ctx.run("pylint src")
    
@task(iterable=["length", "width", "floor"])
def config(ctx, length, width, floor):
	"""Prints the given inputs and sets the corresponding config values as the inputs.
	
	It first checks which config values are given and only replaces those values.
	"""

	print(length, width, floor)
	old_configs = get_configs_from_text()
	if len(length) > 0:
		config_length = length[0]
	else:
		config_length = old_configs[0]
	if len(width) > 0:
		config_width = width[0]
	else:
		config_width = old_configs[1]
	if len(floor) > 0:
		config_floor = floor[0]
	else:
		config_floor = old_configs[2]

	with open("src/settings/config.txt", "w") as text:
		text.write(f"LENGTH = {config_length} \nWIDTH = {config_width} \nFLOOR_CHANCE = {config_floor} \n")

def get_configs_from_text():
	"""Returns the values in the config.txt file"""
	with open("src/settings/config.txt", "r", encoding="utf8") as text:
		lines = text.readlines()
		length = int(lines[0].split(' ')[2])
		width = int(lines[1].split(' ')[2])
		floor_chance = float(lines[2].split(' ')[2])
    
	return (length, width, floor_chance)