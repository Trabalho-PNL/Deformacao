from numpy import *
from imageio import mimsave, imread

sharpLaplaciano = array([[0, 4, 0], [4, -20, 4], [0, 4, 0]])
laplaciano = - array([[1,1,1], [1, -8, 1], [1, 1, 1]])
gaussiano = array([ [1,2,1],[2,4,2],[1,2,1] ])
LoG = [sharpLaplaciano, gaussiano]

def binarizacao(imagem, limiar = 128):
	'''Binariza uma imagem, preferencialmente em escala de cinza, 
	usando o limiar como ponto de corte.'''
	imagem = imagem.copy()
	imagem[imagem >= limiar] = 255
	imagem[imagem < limiar] = 0
	return imagem

def escalaCinza(imagem):
	'''Retorna uma nova imagem com a escala de cinza nas 3 camadas.
	https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale'''
	imagem = imagem.copy()
	imagem[:,:,0] = 0.2126*imagem[:,:,0] + 0.7152*imagem[:,:,1] + 0.0722*imagem[:,:,2]
	imagem[:,:,1], imagem[:,:,2] = imagem[:,:,0], imagem[:,:,0]
	return imagem

def convolucao(imagem, mascaras):
	'''Retorna o resultado da convolucao da imagem com as mascaras 
	usando a Transformada de Fourrier.'''

	if type(mascaras) is not list:
		mascaras = [mascaras]

	imagem = imagem.copy()
	for mascara in mascaras:
		#Calcula a Transformada 2D de cada camada da imagem
		f_im = fft.fft2(imagem, axes = (0,1))

		#Normaliza mascara se necessario
		soma = sum(mascara)*1.0
		if soma != 0:
			mascara = mascara/soma

      	#forca a mascara a ser do tamanho da imagem
		f_mascara = fft.fft2(mascara, s=(f_im.shape[0], f_im.shape[1]) )

		for l in range(3):
			f_convolucao = f_mascara * f_im[:,:,l]
			camada = fft.ifft2(f_convolucao)
			camada[camada < 0 ] = 0
			camada[camada > 255 ] = 255
			imagem[:,:,l] = real(camada)

	return imagem

def criaGif(nomeArquivo, imagens, duracaoFrames=0.5):
	'''Binding para a funcao de save da biblioteca imageio, 
		que recebe a lista de imagens e as salva como um .GIF'''
	mimsave(nomeArquivo, imagens, 'GIF', duration=duracaoFrames)

def carregaImagem(nomeArquivo):
	''' Retorna uma matriz do numpy, carregada do arquivo de imagem especificado. '''
	return imread(nomeArquivo)

def centralizacao(img1, img2):
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
	'''Retorna uma lista de frames que sao o resultado da transformacao 
	de uma imagem na outra linearmente. Espera-se imagens de mesmo tamanho.'''

	frames = [imagemInicial] * delay
	passo = (imagemFinal - imagemInicial)/numPassos
	
	#Aparentemente nessa situacoes o python 
	#copia apenas a referencia para a lista, entao deve-se forcar uma copia
	atual = imagemInicial.copy()
	for i in range(numPassos):
		atual += passo
		frames.append( around( atual.copy() ) )

	return frames + [imagemFinal]*delay

def tratamento(imagem):
	'''Funcao utilitaria que agrega todos os tratamentos feitos na imagem para teste'''
	imagem = imagem.copy()
	imagem = escalaCinza(imagem)
	imagem = convolucao(imagem, LoG )
	imagem = binarizacao(imagem)
	return imagem

if __name__ == '__main__':
	imagemInicial, imagemFinal = carregaImagem('pessoa14.jpg'), carregaImagem('pessoa1.jpg')
	imagemInicial, imagemFinal = centralizacao(imagemInicial, imagemFinal)
	imagemInicial, imagemFinal = tratamento(imagemInicial), tratamento(imagemFinal)
	frames = deformacaoBasica(imagemInicial, imagemFinal, numPassos=10)
	criaGif('resultado.gif', frames)