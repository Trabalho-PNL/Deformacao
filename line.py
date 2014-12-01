from point import Point

class Line():
	"""docstring for Line"""
	def __init__(self, ponto_inicial, ponto_final):
		self.ponto_inicial = ponto_inicial
		self.ponto_final = ponto_final

	def __str__(self):
		return "Ponto Inicial: " + str(self.ponto_inicial) + "\nPonto Final: " + str(self.ponto_final)
		
