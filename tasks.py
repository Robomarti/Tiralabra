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
    
@task(iterable=["length", "width",])
def config(ctx, length, width):
	"""Prints the given inputs and sets the corresponding config values as the inputs.
	
	It first checks which config values are given and only replaces those values."""
	old_configs = get_configs_from_text()
	if len(length) > 0:
		config_length = length[0]
	else:
		config_length = old_configs[0]
	if len(width) > 0:
		config_width = width[0]
	else:
		config_width = old_configs[1]

	print(f"new configuration: LENGTH: {config_length}, WIDTH: {config_width}")

	with open("src/settings/config.txt", "w") as text:
		text.write(f"LENGTH = {config_length} \nWIDTH = {config_width}")

def get_configs_from_text():
	"""Returns the values in the config.txt file"""
	with open("src/settings/config.txt", "r", encoding="utf8") as text:
		lines = text.readlines()
		length = int(lines[0].split(' ')[2])
		width = int(lines[1].split(' ')[2])
    
	return (length, width)