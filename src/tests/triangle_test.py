import unittest
from datatypes.triangle import Triangle, circumcenter_of_triangle, get_distance
from datatypes.coordinates import Coordinates

class TestTriangles(unittest.TestCase):

	def test_distance(self):
		point1 = Coordinates(4,5) # 8-4 = 4, 8-5 = 3, 4^2 = 16, 3^2 = 9, 16+9 = 25, sqrt(25) = 5
		point2 = Coordinates(8,8)
		c = 5
		pythagoras = get_distance(point1, point2)
		self.assertEqual(pythagoras, c)