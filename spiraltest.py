import unittest
from spiral import Spiral

class SpiralTests(unittest.TestCase):

	spiral = Spiral()

	def test_spiral_raises_error_if_arg_not_integer(self):
		self.assertRaises(ValueError, self.spiral.start, 'five')

def main():
	unittest.main()

if __name__ == '__main__':
	main()
