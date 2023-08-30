import unittest
from settings.config import get_configs

class TestRooms(unittest.TestCase):
	def setUp(self):
		pass

	def test_broken_values(self):
		with open("src/settings/config.txt", "w", encoding="utf8") as text1:
			text1.write("LENGTH = asd\nWIDTH = asdda\nUSE_SPANNING = 123")

		configs = get_configs()

		width = configs[1]
		length = configs[0]
		spanning = configs[2]

		self.assertEqual(width, 30)
		self.assertEqual(length, 30)
		self.assertEqual(spanning, "True")

	def test_small_values(self):
		with open("src/settings/config.txt", "w", encoding="utf8") as text2:
			text2.write("LENGTH = 10\nWIDTH = 10\nUSE_SPANNING = False")

		configs = get_configs()

		width = configs[1]
		length = configs[0]
		spanning = configs[2]

		self.assertEqual(width, 20)
		self.assertEqual(length, 20)
		self.assertEqual(spanning, "False")