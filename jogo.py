import pygame 
from pygame.locals import *
from sys import exit 
import random

from letra import Letra
from sopa import Sopa
from IconsJogo import MenuIcon

def leitura_palavras(arquivo):
    with open (arquivo, "r", encoding="utf-8") as file:
        linhas = file.readlines()

    for i in range(len(linhas)):
        linhas[i] = linhas[i].strip()

    palavra = random.choice(linhas)

    return palavra

def desenhar_palavra(tela, palavra_caracteres, largura):
    fonte = pygame.font.Font('fonte/ArchivoBlack-Regular.ttf', 45)
    texto = "".join(palavra_caracteres)
    cor = ((0, 0, 0))
    texto_formatado = fonte.render(texto, True, cor)
    
    retangulo_texto = texto_formatado.get_rect()
    retangulo_texto.center = (largura // 2, 35)
    tela.blit(texto_formatado, retangulo_texto)
    
def run_game(tela):

    screem_size = pygame.display.get_window_size()
    largura = screem_size[0]
    altura = screem_size[1]

    sopa = Sopa(largura)
    letra1 = Letra(300, altura)
    letras_capturas = [] 

    imagem_fundo = pygame.image.load('imagens/fundo.png').convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

    palavra_atual = leitura_palavras("palavras.txt")
    palavra_caracteres = list(palavra_atual.upper())
    print(palavra_caracteres)

    while True: 
        tela.fill((0,0,0))
        tela.blit(imagem_fundo, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    exit()

        letra1.desenhar_letra(tela)
        letra1.descida(altura)
        sopa.update()
        tela.blit(sopa.image, sopa.rect)
        desenhar_palavra(tela, palavra_caracteres, largura)
    
        if sopa.rect.colliderect(letra1.get_rect()):
            letras_capturas.append(letra1.get_simbolo())
            print('Letra caputrada: {}'.format(letras_capturas))

            if letras_capturas[-1].upper() in palavra_caracteres:

                posicao_letra_capturada = palavra_caracteres.index(letras_capturas[-1].upper())
                palavra_caracteres.pop(posicao_letra_capturada)
                print(palavra_caracteres)
           
            letra1.reset_letra(300)
        
        elif letra1.get_y() >= 700:
            letra1.reset_letra(300)
    
        if len(palavra_caracteres) == 0:
            palavra_atual = leitura_palavras("palavras.txt")
            palavra_caracteres = list(palavra_atual.upper())
            print(palavra_caracteres)
            letras_capturas.clear()

        pygame.display.update()