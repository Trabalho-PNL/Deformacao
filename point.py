import math

class Point():
	"""docstring for Python"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
	 return "x = " + str(self.x) + " y = " + str(self.y) 

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
	
	def __mul__(self, other):
		return Point(other*self.x, other*self.y)

	def produtoInterno(self, other):
		return self.x * other.x + self.y * other.y

	def distancia(self, other):
		direcao = self - other
		return math.sqrt( direcao.produtoInterno(direcao) )