#!/usr/bin/python

import math

class Spiral(object):
	#Classic naming strategy. The start method is the main method to piece it all together.
	def start(self, x):
		if isinstance(x, int):
			if x == 0:
				return self.arrayToString([[0]]), [[0]]
			if x == 1:
				return self.arrayToString([[0,1]]), [[0,1]]
			if x == 2:
				return self.arrayToString([[0,1],['f',2]]), [[0,1],['f',2]]
			if x == 3:
				return self.arrayToString([[0,1],[3,2]]), [[0,1],[3,2]]
			flag = True
			corner = 4
			spiralArray, zeroRow, zeroCol = self.initializeArray(x)
			currentRow = zeroRow + 1
			currentCol = zeroCol - 1
			
			while flag:
				direction = self.traversalLogic(corner, spiralArray)
				if direction == 'up':
					spiralArray, flag, currentRow, currentCol, corner = self.goUp(currentRow, currentCol, corner, x, spiralArray)
				elif direction == 'down':
					spiralArray, flag, currentRow, currentCol, corner = self.goDown(currentRow, currentCol, corner, x, spiralArray)
				elif direction == 'left':
					spiralArray, flag, currentRow, currentCol, corner = self.goLeft(currentRow, currentCol, corner, x, spiralArray)
				elif direction == 'right':
					spiralArray, flag, currentRow, currentCol, corner = self.goRight(currentRow, currentCol, corner, x, spiralArray)

			return self.arrayToString(spiralArray), spiralArray
		else:
			raise ValueError

	#A handy method to turn an array into a string
	def arrayToString(self, array):
		arrayString = ''
		for row in array:
			for col in row:
				if col == 'f':
					arrayString += ' '
				else:
					arrayString += str(col)
			if row != array[len(array) - 1]:
				arrayString += '\n'
		return arrayString

	#These names speak for themselves, but this handy method prints out the spiral array
	#in a nice way
	def printNiceArray(self, array):
		biggest = 0
		for row in array:
			for col in row:
				if len(str(col)) > biggest:
					biggest = len(str(col))
		for row in array:
			for col in row:
				if col != 'f':
					print ('%*s' % (biggest, str(col))),
				else:
					print ('%*s' % (biggest, ' ')),
			if row != array[len(array) - 1]:
				print

	#Initializes the array
	def initializeArray(self, x):
		array = [['f' for i in range(self.columnCount(x))] for j in range(self.rowCount(x))]
		zeroRow, zeroCol = self.zeroStart(x)
		array[zeroRow][zeroCol] = 0
		array[zeroRow][zeroCol+1] = 1
		array[zeroRow+1][zeroCol+1] = 2
		array[zeroRow+1][zeroCol] = 3
		return array, zeroRow, zeroCol

	#This method finds the next comming square root
	def nextSquare(self, x):
		x = math.floor(math.sqrt(x) + 1)
		return int(x*x)

	#Counts the number of columns required for the array
	def columnCount(self, x):
		return int(math.floor(math.sqrt(x)) + 1)

	#Counts the number of rows required for the array
	def rowCount(self, x):
		return int(x // math.sqrt(self.nextSquare(x)) + 1)

	#Finds the x,y location for the starting zero
	def zeroStart(self, x):
		return int(float(self.rowCount(x)) / 2 + .5) -1 , int(float(self.columnCount(x)) / 2 + .5) -1

	#Determines if the value is a perfect square
	def isSquare(self, x):
		return (math.floor(math.sqrt(x)) * math.floor(math.sqrt(x)) == x)

	#Traverses/populates the array to the right
	def goRight(self, row, col, value, final, array):
		flag = True
		for i in range(self.nextSquare(value) - value + 1):
			if value + i <= final:
				array[row][col + i] = value + i
			else:
				flag = False
		return array, flag, row, col + (self.nextSquare(value) - value), self.nextSquare(value)

	#Traverses/populates the array to the left
	def goLeft(self, row, col, value, final, array):
		flag = True
		for i in range(self.nextSquare(value) - value + 1):
			if value + i <= final:
				array[row][col - i] = value + i
			else:
				flag = False
		return array, flag, row, col - (self.nextSquare(value) - value), self.nextSquare(value)

	#Traverses/populates the array upwards
	def goUp(self, row, col, value, final, array):
		flag = True
		for i in range(int(math.sqrt(value)) + 1):
			if value + i <= final:
				array[row-i][col] = value + i
			else:
				flag = False
		return array, flag, row - int(math.sqrt(value)), col, value + int(math.sqrt(value))

	#Traverses/populates the array downwards
	def goDown(self, row, col, value, final, array):
		flag = True
		for i in range(int(math.sqrt(value)) + 1):
			if value + i <= final:
				array[row+i][col] = value + i
			else:
				flag = False
		return array, flag, row + int(math.sqrt(value)), col, value + int(math.sqrt(value))

	#Determines which way the numbers should be populated next
	def traversalLogic(self, corner, array):
		if self.isSquare(corner):
			if corner % 2 == 0:
				return 'up'
			else:
				return 'down'
		
		if math.floor(math.sqrt(corner)) % 2 == 0:
			return 'right'
		
		return 'left'


def main():
	try:
		import os
		os.system('python spiraltest.py')
	except IOError:
		print 'Could not find spiraltest.py'

	while True:
		try:
			value = int(raw_input("Please input integer value: "))
			if value >= 0:
				break
		except:
			pass
		print '\nIncorrect input, please try again with an integer value'
	spiral = Spiral()
	spiral.printNiceArray(spiral.start(int(value))[1])


if __name__ == '__main__':
	main()