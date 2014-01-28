class Spiral(object):

	def start(self, x):
		if isinstance(x, int):
			return x
		else:
			raise ValueError