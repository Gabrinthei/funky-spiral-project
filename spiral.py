class Spiral(object):

	def start(self, x):
		if isinstance(x, int):
			return str(x)
		else:
			raise ValueError