import math

class Spiral(object):

	def start(self, x):
		if isinstance(x, int):
			return str(x)
		else:
			raise ValueError

	def nextSquare(self, x):
		x = math.floor(math.sqrt(x) + 1)
		return x*x

	def columnCount(self, x):
		return math.floor(math.sqrt(x)) + 1

	def rowCount(self, x):
		pass

