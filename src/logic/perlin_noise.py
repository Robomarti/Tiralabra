# pylint: disable-all

import math
import settings.config
from dataclasses import dataclass

interpolate_state = settings.config.INTERPOLATE_STATE
clamping = settings.config.CLAMPING

@dataclass
class Vector2:
	"""A class for a custom datatype, Vector2 represents a 2-dimensional vector"""
	x: float
	y: float

def interpolate(a0: float, a1: float, weight: float):
	"""Linearly interpolate between a0 and a1
	Weight should be in range [0.0, 1.0]
	Use cubic interpolation [[Smoothstep]] instead, for a smooth appearance
	Use [[Smootherstep]] for an even smoother result with a second derivative equal to zero on boundaries
	"""
	if clamping:
		if weight < 0:
			return a0
		elif weight > 1:
			return a1

	if interpolate_state == "SMOOTHSTEP":
		result = (a1-a0) * (3.0 - weight * 2.0) * weight * weight + a0
	elif interpolate_state == "SMOOTHERSTEP":
		result = (a1-a0) * ((weight * (weight * 6.0 - 15.0) + 10.0) * weight * weight * weight) + a0
	else:
		result =  (a1-a0) * weight + a0

	return result

# Create pseudorandom direction vector
def pseudoRandomGradient(ix: int, iy: int):
	weight = 8*4 # if sizeof(unsigned) == 4
	rotation_width = int(weight / 2)
	a = ix
	b = iy
	a *= 3284157443
	b ^= a << rotation_width | a >> weight - rotation_width
	b *= 1911520717
	a ^= b << rotation_width | b >> weight - rotation_width
	a *= 2048419325
	random = a * (3.14159265 / 2147483648) # ~(~0u >> 1) which is just ~(~0 >> 1) in python does not work in python. In python it is 0
	vector_x = math.cos(random)
	vector_y = math.sin(random)
	return Vector2(vector_x, vector_y)

# Computes the dot product of the distance and gradient vectors.
def dotGridGradient(ix: int, iy: int, x: float, y: float):
	# Get gradient from integer coordinates
	gradient = pseudoRandomGradient(ix, iy)

	# Compute the distance vector
	dx = x - ix
	dy = y - iy

	# Compute the dot-product
	return dx * gradient.x + dy * gradient.y

#Compute Perlin noise at coordinates x, y
def perlin_noise(x: float, y: float):
	#Determine grid cell coordinates
	x0 = math.floor(x)
	x1 = x0 + 1
	y0 = math.floor(y)
	y1 = y0 +1
	
	#Determine interpolation weights. Could also use higher order polynomial/s-curve here
	sx = x - x0
	sy = y - y0
	
	# Interpolate between grid point gradients
	n0 = dotGridGradient(x0, y0, x, y)
	n1 = dotGridGradient(x1, y0, x, y)
	ix0 = interpolate(n0, n1, sx)
	
	n0 = dotGridGradient(x0, y1, x, y)
	n1 = dotGridGradient(x1, y1, x, y)
	ix1 = interpolate(n0, n1, sx)
	
	value = interpolate(ix0, ix1, sy)
	return value * 0.5 + 0.5 # Will return in range -1 to 1. To make it in range 0 to 1, multiply by 0.5 and add 0.5
	 