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
		self.assertIsInstance(nextSquare, int)

	def test_column_count(self):
		columnCount = self.spiral.columnCount(48)
		self.assertEqual(columnCount, 7)

	def test_row_count(self):
		rowCount = self.spiral.rowCount(24)
		self.assertEqual(rowCount, 5)

	def test_zero_location(self):
		row, col = self.spiral.zeroStart(43)
		self.assertEqual(row, 4)
		self.assertEqual(col, 4)

	def test_if_square(self):
		self.assertTrue(self.spiral.isSquare(144))
		self.assertFalse(self.spiral.isSquare(13))

	def test_go_right(self):
		testArray = self.spiral.goRight(1, 1, [['f', 'f', 'f', 'f'], [5,0,1,'f'], [4,3,2,'f']])
		self.assertEqual(testArray, [[6,7,8,9], [5,0,1,'f'], [4,3,2,'f']])


def main():
	unittest.main()

if __name__ == '__main__':
	main()
