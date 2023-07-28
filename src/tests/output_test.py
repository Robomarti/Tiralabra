import unittest

class TestOutput(unittest.TestCase):
	def setUp(self):
		self.moi = "moi"
		self.map = [[1], [2], [3]]

	def test_handle_output(self):
		self.assertEqual(self.moi, "moi")