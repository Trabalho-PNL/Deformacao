from point import Point
from line import Line
import math
from classBayerNeely import BayerNeely

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


numeroImagensIntermediarias = 4
conjuntoLinhasInterpoladas = []

for passo in range(0, numeroImagensIntermediarias+2):
	interpolacao = []

	for indiceVetor in range(0, len(linhasImagemSemelhante1)):
		linhaOriginalSemelhante1 = linhasImagemSemelhante1[indiceVetor]
		linhaOriginalSemelhante2 = linhasImagemSemelhante2[indiceVetor]

		pontoInicialLinhaInterpolada = linhaOriginalSemelhante1.ponto_inicial + (linhaOriginalSemelhante2.ponto_inicial - linhaOriginalSemelhante1.ponto_inicial) * passo  / numeroImagensIntermediarias
		pontoFinalLinhaInterpolada = linhaOriginalSemelhante1.ponto_final + (linhaOriginalSemelhante2.ponto_final - linhaOriginalSemelhante1.ponto_final) * passo / numeroImagensIntermediarias

		interpolacao.append(Line(pontoInicialLinhaInterpolada, pontoFinalLinhaInterpolada))

	conjuntoLinhasInterpoladas.append(interpolacao)



if __name__ == "__main__":

	contador = 1
	threadsSemelhante1 = []
	threadsSemelhante2 = []
	
	for linhasInterpoladas in conjuntoLinhasInterpoladas:

		deformacao1 =  BayerNeely("semelhante1", linhasImagemSemelhante1, linhasInterpoladas, contador)
		deformacao2 = BayerNeely("semelhante2", linhasImagemSemelhante2, linhasInterpoladas, contador)

		threadsSemelhante1.append(deformacao1)
		threadsSemelhante2.append(deformacao2)

		contador = contador + 1

	[thread.start() for thread in threadsSemelhante1]
	[thread.join() for thread in threadsSemelhante1]

	[thread.start() for thread in threadsSemelhante2]
	[thread.join() for thread in threadsSemelhante2]