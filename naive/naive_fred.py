from numpy import *
from imageio import imread, imsave, mimsave
from point import Point
from line import Line
import sys

#Imagem 1
pontosImagem1  = { 
    "cabeca" :  [ Point(128, 67), Point(80, 87), Point(40, 120), Point(30, 170), Point(40, 223), Point(80, 258), Point(128,268) ],
    "maxilar": [ Point(147, 115), Point(188, 116), Point(220, 132), Point(235, 155), Point(235, 192), Point(220, 209), Point(188, 224), Point(147, 230) ],
    "boca": [ Point(195, 150), Point(193, 163), Point(192, 173), Point(193, 183), Point(195, 195) ],
    "olhoEsquerdo": [ Point(134, 134), Point(125, 147), Point(134, 160), Point(138, 147) ],
    "olhoDireito": [ Point(135, 193), Point(128, 205), Point(135, 218) ,Point(140, 205) ],
    "nariz": [ Point(171, 166), Point(172, 185) ],
    "pescoco": [ Point(261, 115), Point(287, 129), Point(287, 172), Point(287, 206), Point(260, 219) ]

}

linhasImagem1 = []
linhasImagem1 = linhasImagem1 + [ Line(pontosImagem1["cabeca"][index], pontosImagem1["cabeca"][index + 1]) for index in range(0, len(pontosImagem1["cabeca"])-1) ]
linhasImagem1 = linhasImagem1 + [ Line(pontosImagem1["maxilar"][index], pontosImagem1["maxilar"][index + 1]) for index in range(0, len(pontosImagem1["maxilar"])-1)]
linhasImagem1 = linhasImagem1 + [ Line(pontosImagem1["boca"][index], pontosImagem1["boca"][index + 1]) for index in range(0, len(pontosImagem1["boca"])-1) ]
linhasImagem1 = linhasImagem1 + [ Line(pontosImagem1["olhoEsquerdo"][index], pontosImagem1["olhoEsquerdo"][index + 1]) for index in range(0, len(pontosImagem1["olhoEsquerdo"])-1) ]
linhasImagem1 = linhasImagem1 + [ Line(pontosImagem1["olhoDireito"][index], pontosImagem1["olhoDireito"][index + 1]) for index in range(0, len(pontosImagem1["olhoDireito"])-1) ]
linhasImagem1 = linhasImagem1 + [ Line(pontosImagem1["nariz"][index], pontosImagem1["nariz"][index + 1]) for index in range(0, len(pontosImagem1["nariz"])-1) ]
linhasImagem1 = linhasImagem1 + [ Line(pontosImagem1["pescoco"][index], pontosImagem1["pescoco"][index + 1]) for index in range(0, len(pontosImagem1["pescoco"])-1) ]


#Imagem 2
pontosImagem2 = { 
    "cabeca": [ Point(107, 85), Point(63, 76), Point(14, 115), Point(5, 167), Point(14, 223), Point(63, 251), Point(107, 252) ],
    "maxilar": [ Point(132, 107), Point(183, 113), Point(218, 123) ,Point(234, 143), Point(234, 186), Point(218, 202), Point(183, 220), Point(132, 225) ],
    "boca": [ Point(198, 148), Point(197, 155), Point(197, 162), Point(197, 169), Point(198, 178) ],
    "olhoEsquerdo": [ Point(138, 123), Point(130, 136), Point(138, 146), Point(143, 136) ],
    "olhoDireito": [ Point(135, 180), Point(130, 191), Point(135, 200), Point(140, 191) ],
    "nariz": [ Point(171, 151), Point(171, 170) ],
    "pescoco": [ Point(242, 114), Point(275, 123), Point(285, 164), Point(275, 205), Point(242, 222) ]
}

linhasImagem2 = []
linhasImagem2 = linhasImagem2 +  [ Line(pontosImagem2["cabeca"][index], pontosImagem2["cabeca"][index + 1]) for index in range(0, len(pontosImagem2["cabeca"])-1) ]
linhasImagem2 = linhasImagem2 +  [ Line(pontosImagem2["maxilar"][index], pontosImagem2["maxilar"][index + 1]) for index in range(0, len(pontosImagem2["maxilar"])-1) ]
linhasImagem2 = linhasImagem2 +  [ Line(pontosImagem2["boca"][index], pontosImagem2["boca"][index + 1]) for index in range(0, len(pontosImagem2["boca"])-1) ]
linhasImagem2 = linhasImagem2 +  [ Line(pontosImagem2["olhoEsquerdo"][index], pontosImagem2["olhoEsquerdo"][index + 1]) for index in range(0, len(pontosImagem2["olhoEsquerdo"])-1) ]
linhasImagem2 = linhasImagem2 +  [ Line(pontosImagem2["olhoDireito"][index], pontosImagem2["olhoDireito"][index + 1]) for index in range(0, len(pontosImagem2["olhoDireito"])-1) ]
linhasImagem2 = linhasImagem2 +  [ Line(pontosImagem2["nariz"][index], pontosImagem2["nariz"][index + 1]) for index in range(0, len(pontosImagem2["nariz"])-1) ]
linhasImagem2 = linhasImagem2 +  [ Line(pontosImagem2["pescoco"][index], pontosImagem2["pescoco"][index + 1]) for index in range(0, len(pontosImagem2["pescoco"])-1) ]


def calculateU(pontoX, pontoP, pontoQ):
    return ((pontoX - pontoP).produtoEscalar(pontoQ - pontoP))/(pontoQ - pontoP).norma()**2

def calculateV(linhaPQ, pontoX):
    return (pontoX - linhaPQ.ponto_inicial).produtoEscalar(linhaPQ.perpendicular())/(linhaPQ.ponto_inicial - linhaPQ.ponto_final).norma()

def pixel(U,V,linha):
    pontoNaLinha =  linha.ponto_inicial*(1-U) + linha.ponto_final*U
    pontoPerpendicular = linha.perpendicular()
    X = pontoNaLinha + ((pontoPerpendicular/pontoPerpendicular.norma())*V)


    X.x,restoXx = divmod(X.x,1)
    X.y,restoXy = divmod(X.y,1)

    if restoXx > 0.5:
        X.x += 1

    if restoXy > 0.5:
        X.y += 1
    X.x, X.y = X.y, X.x
    return X

numeroImagensIntermediarias = int(sys.argv[3])
conjuntoLinhasInterpoladas = []

for passo in range(0, numeroImagensIntermediarias+2):
    interpolacao = []

    for indiceVetor in range(0, len(linhasImagem1)):
        linhaOriginal1 = linhasImagem1[indiceVetor]
        linhaOriginal2 = linhasImagem2[indiceVetor]

        pontoInicialLinhaInterpolada = linhaOriginal1.ponto_inicial + (linhaOriginal2.ponto_inicial - linhaOriginal1.ponto_inicial) * passo  / numeroImagensIntermediarias
        pontoFinalLinhaInterpolada = linhaOriginal1.ponto_final + (linhaOriginal2.ponto_final - linhaOriginal1.ponto_final) * passo / numeroImagensIntermediarias

        interpolacao.append(Line(pontoInicialLinhaInterpolada, pontoFinalLinhaInterpolada))

    conjuntoLinhasInterpoladas.append(interpolacao)

imagemSrc = imread(sys.argv[1])
imagemDest = imread(sys.argv[2])
alturaImagem, larguraImagem, _ = shape(imagemSrc)
imagensIntermediarias = {}
imagensIntermediarias[0] = imagemSrc
imagensIntermediarias[numeroImagensIntermediarias+1] = imagemDest
for passo, linhasInterpoladas in enumerate(conjuntoLinhasInterpoladas):

    if passo == 0 or passo == numeroImagensIntermediarias + 1:
        continue

    imagemDeformada = imagemSrc.copy()

    #Linhas da imagem
    for i in range(alturaImagem):
        print "Calculando linha",i,"no passo",passo
        #Colunas da imagem
        for j in range(larguraImagem):
            X = Point(i,j)
            distFinal = float("inf")
            for numLinha,linhaDeInteresse in enumerate(linhasInterpoladas):
                U = calculateU(X, linhaDeInteresse.ponto_inicial, linhaDeInteresse.ponto_final)
                V = calculateV(linhaDeInteresse, X)

                if U > 0 and U <  1:
                    dist = abs(V)
                elif U < 0:
                    dist = X.distancia(linhaDeInteresse.ponto_inicial)
                else:
                    dist = X.distancia(linhaDeInteresse.ponto_final)

                if dist < distFinal:
                    Ufinal = U
                    Vfinal = V
                    distFinal = dist
                    numLinhaFinal = numLinha

            Xlinha = pixel(Ufinal,Vfinal,conjuntoLinhasInterpoladas[0][numLinhaFinal])
            X2linha = pixel(Ufinal,Vfinal,conjuntoLinhasInterpoladas[numeroImagensIntermediarias+1][numLinhaFinal])
            if Xlinha.x >= larguraImagem: 
                Xlinha.x = larguraImagem-1
            if Xlinha.y >= alturaImagem: 
                Xlinha.y = alturaImagem-1
            if X2linha.x >= larguraImagem: 
                X2linha.x = larguraImagem-1
            if X2linha.y >= alturaImagem: 
                X2linha.y = alturaImagem-1
            t = float(passo)/numeroImagensIntermediarias
            imagemDeformada[i,j] = [(1-t)*imagemSrc[Xlinha.y,Xlinha.x,k] + t*imagemDest[X2linha.y,X2linha.x,k] for k in range(3)]
    # imagensIntermediarias[passo] = imagemDeformada

    nomeImagem = "imagem" + str(passo)  + ".jpg"
    imsave(nomeImagem,imagemDeformada)
