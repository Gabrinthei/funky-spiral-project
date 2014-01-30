import math

class Spiral(object):

	def start(self, x):
		if isinstance(x, int):
			if x == 0:
				return self.arrayToString([[0]])
			if x == 1:
				return self.arrayToString([[0,1]])
			if x == 2:
				return self.arrayToString([[0,1],['f',2]])
			if x == 3:
				return self.arrayToString([[0,1],[3,2]])
			flag = True
			
			return str(x)
		else:
			raise ValueError

	def arrayToString(self, array):
		arrayString = ''
		for row in array:
			for col in row:
				arrayString += str(col)
			arrayString += '\n'
		return arrayString

	def initializeArray(self, x):
		array = [['f' for i in range(self.columnCount(x))] for j in range(self.rowCount(x))]
		zeroRow, zeroCol = self.zeroStart(x)
		array[zeroRow][zeroCol] = 0
		array[zeroRow][zeroCol+1] = 1
		array[zeroRow+1][zeroCol+1] = 2
		array[zeroRow+1][zeroCol] = 3
		return array

	def nextSquare(self, x):
		x = math.floor(math.sqrt(x) + 1)
		return int(x*x)

	def columnCount(self, x):
		return int(math.floor(math.sqrt(x)) + 1)

	def rowCount(self, x):
		return int(x // math.sqrt(self.nextSquare(x)) + 1)

	def zeroStart(self, x):
		return int(float(self.rowCount(x)) / 2 + .5) -1 , int(float(self.columnCount(x)) / 2 + .5) -1

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

	def traversalLogic(self, corner, array):
		if self.isSquare(corner):
			if corner % 2 == 0:
				return 'up'
			else:
				return 'down'
		
		if math.floor(math.sqrt(corner)) % 2 == 0:
			return 'right'
		
		return 'left'
