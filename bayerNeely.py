from numpy import *
from imageio import mimsave, imsave, imread

#semelhante1
pontosImagemOrigem  = { 
	"cabeca" :  [ [128, 67], [80, 87], [40, 120], [30, 170], [40, 223], [80, 258], [128,268] ],
	"maxilar": [ [147, 115], [188, 116], [220, 132], [235, 155], [235, 192], [220, 209], [188, 224], [147, 230] ],
	"boca": [ [195, 150], [193, 163], [192, 173], [193, 183], [195, 195] ],
	"olhoEsquerdo": [ [134, 134], [125, 147], [134, 160], [138, 147] ],
	"olhoDireito": [ [135, 193], [128, 205], [135, 218] ,[140, 205] ],
	"nariz": [ [171, 166], [172, 185] ],
	"pescoco": [ [261, 115], [287, 129], [287, 172], [287, 206], [260, 219] ]

}

#semelhante2
pontosImagemDestino = { 
	"cabeca": [ [107, 85], [63, 76], [14, 115], [5, 167], [14, 223], [63, 251], [107, 252] ],
	"maxilar": [ [132, 107], [183, 113], [218, 123] ,[234, 143], [234, 186], [218, 202], [183, 220], [132, 225] ],
	"boca": [ [198, 148], [197, 155], [197, 162], [197, 169], [198, 178] ],
	"olhoEsquerdo": [ [138, 123], [130, 136], [138, 146], [143, 136] ],
	"olhoDireito": [ [135, 180], [130, 191], [135, 200], [140, 191] ],
	"nariz": [ [171, 151], [171, 170] ],
	"pescoco": [ [242, 114], [275, 123], [285, 164], [275, 205], [242, 222] ]
}

def marcaPontosNaImagem(imagem, jsonPontosMarcados):

	canaisImagem = shape(imagem)[2]

	for key in jsonPontosMarcados:
		for pontoInteresse in jsonPontosMarcados[key]:
			for canal in range(canaisImagem):
				imagem[pontoInteresse[0], pontoInteresse[1], canal] = 255

	return imagem


if __name__ == "__main__":

	imagemOriginal, imagemDestino = imread("semelhante1.jpg"), imread("semelhante2.jpg")

	imagemOriginalComPontosMarcados =  marcaPontosNaImagem(imagemOriginal.copy(), pontosImagemOrigem)
	imagemDestinoComPontosMarcados = marcaPontosNaImagem(imagemDestino.copy(), pontosImagemDestino)

	imsave("pontosImagemOriginal.jpg", imagemOriginalComPontosMarcados)
	imsave("pontosImagemDestino.jpg", imagemDestinoComPontosMarcados)