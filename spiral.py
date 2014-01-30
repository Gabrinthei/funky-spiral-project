import math

class Spiral(object):

	def start(self, x):
		if isinstance(x, int):
			return str(x)
		else:
			raise ValueError

	def nextSquare(self, x):
		x = math.floor(math.sqrt(x) + 1)
		return int(x*x)

	def columnCount(self, x):
		return math.floor(math.sqrt(x)) + 1

	def rowCount(self, x):
		return x // math.sqrt(self.nextSquare(x)) + 1

	def zeroStart(self, x):
		return int(float(self.rowCount(x)) / 2 + .5) , int(float(self.columnCount(x)) / 2 + .5)

	def isSquare(self, x):
		return (math.floor(math.sqrt(x)) * math.floor(math.sqrt(x)) == x)

	def goRight(self, row, col, value, final, array):
		for i in range(self.nextSquare(value) - value + 1):
			if value + i <= final:
				array[row][col + i] = value + i
		return array

	def goLeft(self, row, col, value, final, array):
		for i in range(self.nextSquare(value) - value + 1):
			if value + i <= final:
				array[row][col - i] = value + i
		return array

	def goUp(self, row, col, value, final, array):
		for i in range(int(math.sqrt(value)) + 1):
			if value + i <= final:
				array[row-i][col] = value + i
		return array

	def goDown(self, row, col, value, final, array):
		for i in range(int(math.sqrt(value)) + 1):
			if value + i <= final:
				array[row+i][col] = value + i
		return array