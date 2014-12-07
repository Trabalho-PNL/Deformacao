from numpy import *
from imageio import mimsave, imsave, imread
from point import Point
from line import Line
import math
from threading import Thread

class BayerNeely(Thread):

	def __init__(self, nomeImagem, linhasImagemASerDeformada, linhasInterpoladas, passo):
		super(BayerNeely, self).__init__()
		self.daemon = True
		self.cancelled = False

		self.nomeImagem = nomeImagem
		self.linhasImagemASerDeformada = linhasImagemASerDeformada
		self.linhasInterpoladas = linhasInterpoladas
		self.passo = passo



	def calculateU(self, pontoX, pontoP, pontoQ):
		return ((pontoX - pontoP).produtoEscalar(pontoQ - pontoP))/(pontoQ - pontoP).norma()**2

	def calculateV(self, linhaPQ, pontoX):
		return (pontoX - linhaPQ.ponto_inicial).produtoEscalar(linhaPQ.perpendicular())/(linhaPQ.ponto_inicial - linhaPQ.ponto_final).norma()
	
	def calculateXlinha(self, u, v, linhaPQ):
		return linhaPQ.ponto_inicial + linhaPQ.tamanhoLinha() * u + (linhaPQ.perpendicular() * v)/linhaPQ.tamanhoLinha().norma()

	def gera_imagens_deformadas(self):
		imagemSource = imread(self.nomeImagem + ".jpg")


		alturaImagem, larguraImagem, _ = shape(imagemSource)

		imagemDeformada = imagemSource.copy()


		for linhaPixel in range(0, alturaImagem):
			print "Imagem: "+ self.nomeImagem + ", interpolacao: " + str(self.passo) + " Linha: " + str(linhaPixel)
			for colunaPixel in range(0, larguraImagem):
				X = Point(linhaPixel, colunaPixel)
				DSUM = Point(0,0)
				weightsum = 0

				for linhaAtualInterpolada in self.linhasInterpoladas:
					
					indice = self.linhasInterpoladas.index(linhaAtualInterpolada)
					
					linhaEquivalenteEmSemelhante1 = self.linhasImagemASerDeformada[indice]
					
					
					U = self.calculateU(X, linhaAtualInterpolada.ponto_inicial, linhaAtualInterpolada.ponto_final)
					V = self.calculateV(linhaAtualInterpolada, X)

					
					Xi = self.calculateXlinha(U, V, linhaEquivalenteEmSemelhante1)
					
					Di = Xi - X
					
					if U > 0 and U <  1:
						dist = abs(V)
					elif U < 0:
						dist = X.distancia(linhaAtualInterpolada.ponto_inicial)
					else:
						dist = X.distancia(linhaAtualInterpolada.ponto_final)

					weight = ( 1 / (0.001 + dist) )**2

					DSUM = DSUM + (Di * weight)

					weightsum = weightsum + weight

				Xlinha = X + DSUM/weightsum
				
				# para evitar inconsistencias e pegar valores inexistentes
				if Xlinha.x >= 288:
					Xlinha.x = 287
				elif Xlinha.x < 0:
					Xlinha.x = 0

				if Xlinha.y >= 384:
					Xlinha.y = 383
				elif Xlinha.y < 0:
					Xlinha.y = 0
				
				imagemDeformada[X.x, X.y] = imagemSource[int(math.trunc(Xlinha.x)), int(math.trunc(Xlinha.y))]


		nomeImagem = "imagens_" + self.nomeImagem + "/deformacao_passo"+ str(self.passo) + ".jpg"
		imsave(nomeImagem, imagemDeformada)

		self.cancelled = True

	def run(self):
		self.gera_imagens_deformadas()