from numpy import *
from imageio import mimsave, imsave, imread
from point import Point
from line import Line

#semelhante1
pontosImagemOrigem  = { 
	"cabeca" :  [ Point(128, 67), Point(80, 87), Point(40, 120), Point(30, 170), Point(40, 223), Point(80, 258), Point(128,268) ],
	"maxilar": [ Point(147, 115), Point(188, 116), Point(220, 132), Point(235, 155), Point(235, 192), Point(220, 209), Point(188, 224), Point(147, 230) ],
	"boca": [ Point(195, 150), Point(193, 163), Point(192, 173), Point(193, 183), Point(195, 195) ],
	"olhoEsquerdo": [ Point(134, 134), Point(125, 147), Point(134, 160), Point(138, 147) ],
	"olhoDireito": [ Point(135, 193), Point(128, 205), Point(135, 218) ,Point(140, 205) ],
	"nariz": [ Point(171, 166), Point(172, 185) ],
	"pescoco": [ Point(261, 115), Point(287, 129), Point(287, 172), Point(287, 206), Point(260, 219) ]

}

linhasImagemOrigem = {
	"cabeca": [ Line(pontosImagemOrigem["cabeca"][index], pontosImagemOrigem["cabeca"][index + 1]) for index in range(0, len(pontosImagemOrigem["cabeca"])-1) ],
	"maxilar": [Line(pontosImagemOrigem["maxilar"][index], pontosImagemOrigem["maxilar"][index + 1]) for index in range(0, len(pontosImagemOrigem["maxilar"])-1)],
	"boca": [ Line(pontosImagemOrigem["boca"][index], pontosImagemOrigem["boca"][index + 1]) for index in range(0, len(pontosImagemOrigem["boca"])-1) ],
	"olhoEsquerdo": [ Line(pontosImagemOrigem["olhoEsquerdo"][index], pontosImagemOrigem["olhoEsquerdo"][index + 1]) for index in range(0, len(pontosImagemOrigem["olhoEsquerdo"])-1) ],
	"olhoDireito": [ Line(pontosImagemOrigem["olhoDireito"][index], pontosImagemOrigem["olhoDireito"][index + 1]) for index in range(0, len(pontosImagemOrigem["olhoDireito"])-1) ],
	"nariz": [ Line(pontosImagemOrigem["nariz"][index], pontosImagemOrigem["nariz"][index + 1]) for index in range(0, len(pontosImagemOrigem["nariz"])-1) ],
	"pescoco": [ Line(pontosImagemOrigem["pescoco"][index], pontosImagemOrigem["pescoco"][index + 1]) for index in range(0, len(pontosImagemOrigem["pescoco"])-1) ]
}

#semelhante2
pontosImagemDestino = { 
	"cabeca": [ Point(107, 85), Point(63, 76), Point(14, 115), Point(5, 167), Point(14, 223), Point(63, 251), Point(107, 252) ],
	"maxilar": [ Point(132, 107), Point(183, 113), Point(218, 123) ,Point(234, 143), Point(234, 186), Point(218, 202), Point(183, 220), Point(132, 225) ],
	"boca": [ Point(198, 148), Point(197, 155), Point(197, 162), Point(197, 169), Point(198, 178) ],
	"olhoEsquerdo": [ Point(138, 123), Point(130, 136), Point(138, 146), Point(143, 136) ],
	"olhoDireito": [ Point(135, 180), Point(130, 191), Point(135, 200), Point(140, 191) ],
	"nariz": [ Point(171, 151), Point(171, 170) ],
	"pescoco": [ Point(242, 114), Point(275, 123), Point(285, 164), Point(275, 205), Point(242, 222) ]
}

linhasImagemDestino = {
	"cabeca": [ Line(pontosImagemDestino["cabeca"][index], pontosImagemDestino["cabeca"][index + 1]) for index in range(0, len(pontosImagemDestino["cabeca"])-1) ],
	"maxilar": [Line(pontosImagemDestino["maxilar"][index], pontosImagemDestino["maxilar"][index + 1]) for index in range(0, len(pontosImagemDestino["maxilar"])-1)],
	"boca": [ Line(pontosImagemDestino["boca"][index], pontosImagemDestino["boca"][index + 1]) for index in range(0, len(pontosImagemDestino["boca"])-1) ],
	"olhoEsquerdo": [ Line(pontosImagemDestino["olhoEsquerdo"][index], pontosImagemDestino["olhoEsquerdo"][index + 1]) for index in range(0, len(pontosImagemDestino["olhoEsquerdo"])-1) ],
	"olhoDireito": [ Line(pontosImagemDestino["olhoDireito"][index], pontosImagemDestino["olhoDireito"][index + 1]) for index in range(0, len(pontosImagemDestino["olhoDireito"])-1) ],
	"nariz": [ Line(pontosImagemDestino["nariz"][index], pontosImagemDestino["nariz"][index + 1]) for index in range(0, len(pontosImagemDestino["nariz"])-1) ],
	"pescoco": [ Line(pontosImagemDestino["pescoco"][index], pontosImagemDestino["pescoco"][index + 1]) for index in range(0, len(pontosImagemDestino["pescoco"])-1) ]
}

def marcaPontosNaImagem(imagem, jsonPontosMarcados):

	canaisImagem = shape(imagem)[2]

	for key in jsonPontosMarcados:
		for pontoInteresse in jsonPontosMarcados[key]:
			for canal in range(canaisImagem):
				imagem[pontoInteresse.x, pontoInteresse.y, canal] = 255

	return imagem

def calculateU(pontoX, pontoP, pontoQ):
	return ((pontoX - pontoP).produtoEscalar(pontoQ - pontoP))/(pontoQ - pontoP).norma()**2

def calculateV(linhaPQ, pontoX):
	return (pontoX - linhaPQ.ponto_inicial).produtoEscalar(linhaPQ.perpendicular())/(linhaPQ.ponto_inicial - linhaPQ.ponto_final).norma()
def calculateXlinha(u, v, linhaPQ):
	return linhaPQ.ponto_inicial + linhaPQ.tamanhoLinha() * u + (linhaPQ.perpendicular() * v)/linhaPQ.tamanhoLinha().norma()

if __name__ == "__main__":

	X = Point(4.0,3.0)
	P = Point(2.0,1.0)
	Q = Point(2.0,4.0)
	Plinha = Point(5.0, 1.0)
	Qlinha = Point(5.0, 4.0)

	U = calculateU(X, P, Q)
	V = calculateV(Line(P, Q), X)
	Xlinha = calculateXlinha(U, V, Line(Plinha, Qlinha))

	print(U)
	print(V)
	print Xlinha

	imagemOriginal, imagemDestino = imread("semelhante1.jpg"), imread("semelhante2.jpg")

	imagemOriginalComPontosMarcados =  marcaPontosNaImagem(imagemOriginal.copy(), pontosImagemOrigem)
	imagemDestinoComPontosMarcados = marcaPontosNaImagem(imagemDestino.copy(), pontosImagemDestino)

	imsave("pontosImagemOriginal.jpg", imagemOriginalComPontosMarcados)
	imsave("pontosImagemDestino.jpg", imagemDestinoComPontosMarcados)