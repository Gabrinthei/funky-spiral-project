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
		self.assertEqual(row, 3)
		self.assertEqual(col, 3)

	def test_if_square(self):
		self.assertTrue(self.spiral.isSquare(144))
		self.assertFalse(self.spiral.isSquare(13))

	def test_go_right(self):
		testArray = self.spiral.goRight(0, 0, 6, 7, [['f', 'f', 'f', 'f'], [5,0,1,'f'], [4,3,2,'f']])
		self.assertEqual(testArray, [[6,7,'f','f'], [5,0,1,'f'], [4,3,2,'f']])

	def test_go_left(self):
		testArray = self.spiral.goLeft(3, 4, 12, 13, [['f', 'f', 'f', 'f','f'], ['f',5,0,1,'f'], ['f',4,3,2,'f'], ['f','f', 'f', 'f', 'f']])
		self.assertEqual(testArray, [['f','f', 'f', 'f', 'f'], ['f',5,0,1,'f'], ['f',4,3,2,'f'], ['f','f','f',13,12]])

	def test_go_up(self):
		testArray = self.spiral.goUp(2, 0, 4, 5, [['f', 'f', 'f'], ['f',0,1], ['f',3,2]])
		self.assertEqual(testArray, [['f','f','f'], [5,0,1], [4,3,2]])

	def test_go_down(self):
		testArray = self.spiral.goDown(0, 3, 9, 11, [[6,7,8,'f'], [5,0,1,'f'], [4,3,2,'f'], ['f','f','f','f']])
		self.assertEqual(testArray, [[6,7,8,9], [5,0,1,10], [4,3,2,11], ['f','f','f','f']])

	def test_traversal_logic(self):
		testArray = [[6,7,8,9], [5,0,1,10], [4,3,2,11], ['f','f','f','f']]
		self.assertEqual(self.spiral.traversalLogic(4, testArray), 'up')
		self.assertEqual(self.spiral.traversalLogic(6, testArray), 'right')
		self.assertEqual(self.spiral.traversalLogic(9, testArray), 'down')
		self.assertEqual(self.spiral.traversalLogic(12, testArray), 'left')

	def test_initialize_array(self):
		self.assertEqual(self.spiral.initializeArray(4), [['f',0,1],['f',3,2]])

def main():
	unittest.main()

if __name__ == '__main__':
	main()
