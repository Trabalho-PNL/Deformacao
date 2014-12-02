from point import Point

class Line():
	"""docstring for Line"""
	def __init__(self, ponto_inicial, ponto_final):
		self.ponto_inicial = ponto_inicial
		self.ponto_final = ponto_final
		
	def __str__(self):
		return "Ponto Inicial: " + str(self.ponto_inicial) + "\nPonto Final: " + str(self.ponto_final)

	def distanciaPonto(self, ponto):
		''' Calcula a distancia do segmento de reta a um dado ponto. Baseado em :
		https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment'''
		
		vetorDirecao = self.ponto_final - self.ponto_inicial
		norma = vetorDirecao.produtoInterno(vetorDirecao)

		if norma == 0.0:
			return ponto.distancia(self.ponto_inicial) # reta degenerada em um ponto

		t = (ponto - self.ponto_inicial).produtoInterno(vetorDirecao) / norma
		
		if t < 0.0:
			return ponto.distancia(self.ponto_inicial)
		elif t > 1.0:
			return ponto.distancia(self.ponto_final)
		else :
			projecao = self.ponto_inicial + vetorDirecao * t
			return ponto.distancia(projecao)

if __name__ == "__main__":
	l1 = Line(Point(0.0, 0.0), Point(0.0, 2.0))
	l2 = Line(Point(0.0, 2.0), Point(0.0, 5.0))
	p  = Point(2.0, 2.0)
	print( l1.distanciaPonto(p) )
	print( l2.distanciaPonto(p) )