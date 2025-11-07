import pygame 
from pygame.locals import *
from sys import exit 

from jogo import run_game

pygame.init()
pygame.font.init()
pygame.mixer.init()

info_monitor = pygame.display.Info()
largura = info_monitor.current_w 
altura  = info_monitor.current_h 

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sopa de letrinhas')

caminho_musica = 'sons/musica.mp3' 
pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.play(-1)

def desenhar_retangulo(tela, informacao, y):
    fonte = pygame.font.Font('fonte/ArchivoBlack-Regular.ttf', 60)
    texto = '{}'.format(informacao)
    cor = (0, 0, 0)

    x_centro = (largura - 330) / 2
    y_centro = (altura -  70) / 2

    retangulo = pygame.draw.rect(tela, (3, 166, 161), (x_centro, y_centro + y, 330, 70), border_radius = 4)
        
    texto_formatado = fonte.render(texto, True, cor)

    rect_texto = texto_formatado.get_rect(center = retangulo.center)
        
    tela.blit(texto_formatado, rect_texto)

    return retangulo

def main_menu(tela):

    imagem_fundo = pygame.image.load('imagens/menu.png').convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

    informacao1 = "Iniciar"
    informacao2 = "Menu"
    informacao3 = "Sair"

    while True: 
        tela.fill((0,0,0))
        tela.blit(imagem_fundo, (0,0))

        retangulo1 = desenhar_retangulo(tela, informacao1, -90)
        retangulo2 = desenhar_retangulo(tela, informacao2, 0)
        retangulo3 = desenhar_retangulo(tela, informacao3, 90)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos

                if retangulo1.collidepoint(mouse):
                    return "JOGAR"
                if retangulo2.collidepoint(mouse):
                    pass
                if retangulo3.collidepoint(mouse):
                    return "SAIR"
                
        pygame.display.update()

estado = 'MENU'

while True:

    if estado == 'MENU':
        estado = main_menu(tela)
    elif estado == 'JOGAR':
        estado = run_game(tela)
    elif estado == "SAIR":
        break

pygame.mixer.music.stop()
pygame.quit()
exit()



    

