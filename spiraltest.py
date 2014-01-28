import unittest
from spiral import Spiral

class SpiralTests(unittest.TestCase):

	spiral = Spiral()

	def test_spiral_raises_error_if_arg_not_integer(self):
		self.assertRaises(ValueError, self.spiral.start, 'five')

	def test_spiral_returns_string(self):
		self.assertIsInstance(self.spiral.start(5), str)

	def test_spiral_returns_next_square(self):
		nextSquare = self.spiral.nextSquare(20)
		self.assertEqual(nextSquare, 25)

	def test_column_count(self):
		columnCount = self.spiral.columnCount(48)
		self.assertEqual(columnCount, 7)

	def test_row_count(self):
		rowCount = self.spiral.rowCount(24)
		self.assertEqual(rowCount, 5)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
