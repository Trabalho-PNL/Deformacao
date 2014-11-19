from numpy import *
from imageio import mimsave, imread

def criaGif(nomeArquivo, imagens, duracaoFrames=0.5):
	'''Binding para a funcao de save da biblioteca imageio, 
		que recebe a lista de imagens e as salva como um .GIF'''
	mimsave(nomeArquivo, imagens, 'GIF', duration=duracaoFrames)

def carregaImagem(nomeArquivo):
	''' Retorna uma matriz do numpy, carregada do arquivo de imagem especificado. '''
	return imread(nomeArquivo)

def tratamento(img1, img2):
	'''Iguala as dimensoes de cada imagem, arredondando para cima, 
		centralizando-se e completando com preto.'''
	x1,y1,_ = shape(img1)
	x2,y2,_ = shape(img2)
	
	#Rever se eh melhor arrendondar para cima
	xF = max(x1,x2)
	yF = max(y1,y2)

	dx1 = xF - x1
	dy1 = yF - y1
	dx2 = xF - x2
	dy2 = yF - y2

	#pad eh uma funcao do numpy que faz o preenchimento que seria necessario nesse passo. Vide documentacao
	img1 = pad(img1, ( ( (dx1+1)//2, (dx1)//2 ), ( (dy1+1)//2, (dy1)//2 ), (0,0) ), mode='constant' )
	img2 = pad(img2, ( ( (dx2+1)//2, (dx2)//2 ), ( (dy2+1)//2, (dy2)//2 ), (0,0) ), mode='constant' )
	return img1, img2

def deformacaoBasica(imagemInicial, imagemFinal, numPassos, delay=3):
	'''Retorna uma lista de frames que sao o resultado da transformacao de uma imagem na outra linearmente'''
	imagemInicial, imagemFinal = tratamento(imagemInicial, imagemFinal)

	frames = [imagemInicial] * delay
	passo = (imagemFinal - imagemInicial)/numPassos
	
	#Aparentemente nessa situacoes o python 
	#copia apenas a referencia para a lista, entao deve-se forcar uma copia
	atual = imagemInicial.copy()
	for i in range(numPassos):
		atual += passo
		frames.append( around( atual.copy() ) )

	return frames + [imagemFinal]*delay

if __name__ == '__main__':
	imagemInicial, imagemFinal = carregaImagem('aecio.jpg'), carregaImagem('dilma.jpg')
	frames = deformacaoBasica(imagemInicial, imagemFinal, numPassos=10)
	criaGif('resultado.gif', frames)