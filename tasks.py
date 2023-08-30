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

@task
def lint(ctx):
    ctx.run("pylint src")
    
@task(iterable=["width","length", "spanning"])
def config(ctx, length, width, spanning):
	"""Prints the given inputs and sets the corresponding config values as the inputs.
	
	It first checks which config values are given and only replaces those values."""
	old_configs = get_configs_from_text()
	if len(width) > 0:
		try:
			int(width)
			config_width = width[0]
		except:
			config_width = old_configs[1]
			print("The width was not given in an integer form")
	else:
		config_width = old_configs[1]

	if len(length) > 0:
		try:
			int(length)
			config_length = length[0]
		except:
			config_length = old_configs[0]
			print("The length was not given in an integer form")
	else:
		config_length = old_configs[0]

	if len(spanning) > 0:
		if spanning[0] in ["True", "False"]:
			config_spanning = spanning[0]
		else:
			config_spanning = old_configs[2]

	print(f"new configuration: WIDTH: {config_width}, LENGTH: {config_length}, USE_SPANNING: {config_spanning}")

	with open("src/settings/config.txt", "w") as text:
		text.write(f"LENGTH = {config_length} \nWIDTH = {config_width}\nUSE_SPANNING = {config_spanning}")

def get_configs_from_text():
	"""Returns the values in the config.txt file"""
	length = src.settings.config.LENGTH
	width = src.settings.config.WIDTH
	use_spanning = src.settings.config.USE_SPANNING
    
	return (length, width, use_spanning)