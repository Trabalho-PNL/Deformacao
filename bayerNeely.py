from numpy import *
from imageio import mimsave, imsave, imread
from point import Point
from line import Line
import math

#semelhante1
pontosImagemSemelhante1  = { 
	"cabeca" :  [ Point(128, 67), Point(80, 87), Point(40, 120), Point(30, 170), Point(40, 223), Point(80, 258), Point(128,268) ],
	"maxilar": [ Point(147, 115), Point(188, 116), Point(220, 132), Point(235, 155), Point(235, 192), Point(220, 209), Point(188, 224), Point(147, 230) ],
	"boca": [ Point(195, 150), Point(193, 163), Point(192, 173), Point(193, 183), Point(195, 195) ],
	"olhoEsquerdo": [ Point(134, 134), Point(125, 147), Point(134, 160), Point(138, 147) ],
	"olhoDireito": [ Point(135, 193), Point(128, 205), Point(135, 218) ,Point(140, 205) ],
	"nariz": [ Point(171, 166), Point(172, 185) ],
	"pescoco": [ Point(261, 115), Point(287, 129), Point(287, 172), Point(287, 206), Point(260, 219) ]

}

linhasImagemSemelhante1 = []
linhasImagemSemelhante1 = linhasImagemSemelhante1 + [ Line(pontosImagemSemelhante1["cabeca"][index], pontosImagemSemelhante1["cabeca"][index + 1]) for index in range(0, len(pontosImagemSemelhante1["cabeca"])-1) ]
linhasImagemSemelhante1 = linhasImagemSemelhante1 + [ Line(pontosImagemSemelhante1["maxilar"][index], pontosImagemSemelhante1["maxilar"][index + 1]) for index in range(0, len(pontosImagemSemelhante1["maxilar"])-1)]
linhasImagemSemelhante1 = linhasImagemSemelhante1 + [ Line(pontosImagemSemelhante1["boca"][index], pontosImagemSemelhante1["boca"][index + 1]) for index in range(0, len(pontosImagemSemelhante1["boca"])-1) ]
linhasImagemSemelhante1 = linhasImagemSemelhante1 + [ Line(pontosImagemSemelhante1["olhoEsquerdo"][index], pontosImagemSemelhante1["olhoEsquerdo"][index + 1]) for index in range(0, len(pontosImagemSemelhante1["olhoEsquerdo"])-1) ]
linhasImagemSemelhante1 = linhasImagemSemelhante1 + [ Line(pontosImagemSemelhante1["olhoDireito"][index], pontosImagemSemelhante1["olhoDireito"][index + 1]) for index in range(0, len(pontosImagemSemelhante1["olhoDireito"])-1) ]
linhasImagemSemelhante1 = linhasImagemSemelhante1 + [ Line(pontosImagemSemelhante1["nariz"][index], pontosImagemSemelhante1["nariz"][index + 1]) for index in range(0, len(pontosImagemSemelhante1["nariz"])-1) ]
linhasImagemSemelhante1 = linhasImagemSemelhante1 + [ Line(pontosImagemSemelhante1["pescoco"][index], pontosImagemSemelhante1["pescoco"][index + 1]) for index in range(0, len(pontosImagemSemelhante1["pescoco"])-1) ]


#semelhante2
pontosImagemSemelhante2 = { 
	"cabeca": [ Point(107, 85), Point(63, 76), Point(14, 115), Point(5, 167), Point(14, 223), Point(63, 251), Point(107, 252) ],
	"maxilar": [ Point(132, 107), Point(183, 113), Point(218, 123) ,Point(234, 143), Point(234, 186), Point(218, 202), Point(183, 220), Point(132, 225) ],
	"boca": [ Point(198, 148), Point(197, 155), Point(197, 162), Point(197, 169), Point(198, 178) ],
	"olhoEsquerdo": [ Point(138, 123), Point(130, 136), Point(138, 146), Point(143, 136) ],
	"olhoDireito": [ Point(135, 180), Point(130, 191), Point(135, 200), Point(140, 191) ],
	"nariz": [ Point(171, 151), Point(171, 170) ],
	"pescoco": [ Point(242, 114), Point(275, 123), Point(285, 164), Point(275, 205), Point(242, 222) ]
}

linhasImagemSemelhante2 = []
linhasImagemSemelhante2 = linhasImagemSemelhante2 +  [ Line(pontosImagemSemelhante2["cabeca"][index], pontosImagemSemelhante2["cabeca"][index + 1]) for index in range(0, len(pontosImagemSemelhante2["cabeca"])-1) ]
linhasImagemSemelhante2 = linhasImagemSemelhante2 +  [ Line(pontosImagemSemelhante2["maxilar"][index], pontosImagemSemelhante2["maxilar"][index + 1]) for index in range(0, len(pontosImagemSemelhante2["maxilar"])-1) ]
linhasImagemSemelhante2 = linhasImagemSemelhante2 +  [ Line(pontosImagemSemelhante2["boca"][index], pontosImagemSemelhante2["boca"][index + 1]) for index in range(0, len(pontosImagemSemelhante2["boca"])-1) ]
linhasImagemSemelhante2 = linhasImagemSemelhante2 +  [ Line(pontosImagemSemelhante2["olhoEsquerdo"][index], pontosImagemSemelhante2["olhoEsquerdo"][index + 1]) for index in range(0, len(pontosImagemSemelhante2["olhoEsquerdo"])-1) ]
linhasImagemSemelhante2 = linhasImagemSemelhante2 +  [ Line(pontosImagemSemelhante2["olhoDireito"][index], pontosImagemSemelhante2["olhoDireito"][index + 1]) for index in range(0, len(pontosImagemSemelhante2["olhoDireito"])-1) ]
linhasImagemSemelhante2 = linhasImagemSemelhante2 +  [ Line(pontosImagemSemelhante2["nariz"][index], pontosImagemSemelhante2["nariz"][index + 1]) for index in range(0, len(pontosImagemSemelhante2["nariz"])-1) ]
linhasImagemSemelhante2 = linhasImagemSemelhante2 +  [ Line(pontosImagemSemelhante2["pescoco"][index], pontosImagemSemelhante2["pescoco"][index + 1]) for index in range(0, len(pontosImagemSemelhante2["pescoco"])-1) ]

"""Numero de imagens alem das duas originais"""
numeroImagensIntermediarias = 10 
conjuntoLinhasInterpoladas = []

for passo in range(0, numeroImagensIntermediarias+2):
	interpolacao = []

	for indiceVetor in range(0, len(linhasImagemSemelhante1)):
		linhaOriginalSemelhante1 = linhasImagemSemelhante1[indiceVetor]
		linhaOriginalSemelhante2 = linhasImagemSemelhante2[indiceVetor]

		t = float(passo)/(numeroImagensIntermediarias+1)
		pontoInicialLinhaInterpolada = linhaOriginalSemelhante1.ponto_inicial*(1-t) + linhaOriginalSemelhante2.ponto_inicial*t
		pontoFinalLinhaInterpolada = linhaOriginalSemelhante1.ponto_final*(1-t) + linhaOriginalSemelhante2.ponto_final*t


		interpolacao.append(Line(pontoInicialLinhaInterpolada, pontoFinalLinhaInterpolada))

	conjuntoLinhasInterpoladas.append(interpolacao)


def calculateU(pontoX, pontoP, pontoQ):
	return ((pontoX - pontoP).produtoEscalar(pontoQ - pontoP))/(pontoQ - pontoP).norma()**2

def calculateV(linhaPQ, pontoX):
	return (pontoX - linhaPQ.ponto_inicial).produtoEscalar(linhaPQ.perpendicular())/(linhaPQ.ponto_inicial - linhaPQ.ponto_final).norma()
def calculateXlinha(u, v, linhaPQ):
	return linhaPQ.ponto_inicial + linhaPQ.tamanhoLinha() * u + (linhaPQ.perpendicular() * v)/linhaPQ.tamanhoLinha().norma()

def gera_imagens_semelhante1():
	imagemSource = imread("semelhante1.jpg")

	alturaImagem, larguraImagem, _ = shape(imagemSource)

	imagemDeformada = imagemSource.copy()
	contador = 1

	for linhasInterpoladas in conjuntoLinhasInterpoladas:
		for linhaPixel in range(0, alturaImagem):
			print "Imagem semelhante1, interpolacao: " + str(contador) + " Linha: " + str(linhaPixel)
			for colunaPixel in range(0, larguraImagem):
				X = Point(linhaPixel, colunaPixel)
				DSUM = Point(0,0)
				weightsum = 0

				for linhaAtualInterpolada in linhasInterpoladas:
					
					indice = linhasInterpoladas.index(linhaAtualInterpolada)
					
					linhaEquivalenteEmSemelhante1 = linhasImagemSemelhante1[indice]
					
					
					U = calculateU(X, linhaAtualInterpolada.ponto_inicial, linhaAtualInterpolada.ponto_final)
					V = calculateV(linhaAtualInterpolada, X)

					
					Xi = calculateXlinha(U, V, linhaEquivalenteEmSemelhante1)
					
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


		nomeImagem = "imagens_semelhante1/deformacao_passo"+ str(contador) + ".jpg"
		imsave(nomeImagem, imagemDeformada)

		contador = contador + 1


def gera_imagens_semelhante2():
	imagemSource = imread("semelhante2.jpg")

	alturaImagem, larguraImagem, _ = shape(imagemSource)

	imagemDeformada = imagemSource.copy()
	contador = 1

	for linhasInterpoladas in conjuntoLinhasInterpoladas:
		for linhaPixel in range(0, alturaImagem):
			print "Imagem semelhante2, interpolacao: " + str(contador) + " Linha: " + str(linhaPixel)
			for colunaPixel in range(0, larguraImagem):
				X = Point(linhaPixel, colunaPixel)
				DSUM = Point(0,0)
				weightsum = 0

				for linhaAtualInterpolada in linhasInterpoladas:
					
					indice = linhasInterpoladas.index(linhaAtualInterpolada)
					
					linhaEquivalenteEmSemelhante2 = linhasImagemSemelhante2[indice]
					
					
					U = calculateU(X, linhaAtualInterpolada.ponto_inicial, linhaAtualInterpolada.ponto_final)
					V = calculateV(linhaAtualInterpolada, X)

					
					Xi = calculateXlinha(U, V, linhaEquivalenteEmSemelhante2)
					
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


		nomeImagem = "imagens_semelhante2/deformacao_passo"+ str(contador) + ".jpg"
		imsave(nomeImagem, imagemDeformada)

		contador = contador + 1

def merge_imagens():
 	listaImagensMergeadas = []

 	for passo in range(0, numeroImagensIntermediarias + 2):
 		print "Mergeando passo: " + str(passo)
 		imagemDeformada1 = imread("imagens_semelhante1/deformacao_passo" + str(passo) + ".jpg")
 		imagemDeformada2 = imread("imagens_semelhante2/deformacao_passo" + str(passo) + ".jpg")

 		imagemMergeada = imagemDeformada2.copy()
 		alturaImagem, larguraImagem, _ = shape(imagemMergeada)

 		for linhaPixel in range(0, alturaImagem):
 			for colunaPixel in range(0,larguraImagem):
 				t = passo * 1.0/(numeroImagensIntermediarias + 1)
 				imagemMergeada[linhaPixel, colunaPixel] = (1 - t) * imagemDeformada1[linhaPixel, colunaPixel] + (t) * imagemDeformada2[linhaPixel, colunaPixel]


		imsave("imagensMedias/imagemMediaPasso" + str(passo) + ".jpg", imagemMergeada)
		listaImagensMergeadas.append(imagemMergeada)

	return listaImagensMergeadas

def criaGif(nomeArquivo, imagens, duracaoFrames=0.5):
	mimsave(nomeArquivo, imagens, 'GIF', duration=duracaoFrames)


if __name__ == "__main__":
	gera_imagens_semelhante1()
	gera_imagens_semelhante2()

	listaImagens = merge_imagens()
	criaGif("transformacaoMorfologica.gif", listaImagens)







	






