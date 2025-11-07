import pygame 
from pygame.locals import *
import random

lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                'Á', 'Ã', 'Â', 'É', 'Ê', 'Í', 'Ô', 'Õ', 'Ú', 'Ç' ]

class Letra(pygame.sprite.Sprite):
    def __init__(self, x, altura_tela):

        super().__init__()
        
        self.largura_letra = 80
        self.altura_letra = 100
        self.simbolo = random.choice(lista_letras)
        self.altura_tela = altura_tela
        self.x = x
        self.y = 300
    
    def desenhar_letra(self, tela):
        fonte = pygame.font.Font('fonte/ArchivoBlack-Regular.ttf', 70)
        texto = '{}'.format(self.simbolo)
        cor = (0, 0, 0)
        
        retangulo = pygame.draw.rect(tela, (3, 166, 161), (self.x, self.y, self.largura_letra, self.altura_letra), border_radius = 4)
        
        texto_formatado = fonte.render(texto, True, cor)

        rect_texto = texto_formatado.get_rect(center = retangulo.center)
        
        tela.blit(texto_formatado, rect_texto)
    
    def descida(self, altura):
        if self.y >= altura:
            self.y = 0
        self.y = self.y + 0.9

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura_letra, self.altura_letra)

    def reset_letra(self, x):
        self.x = x
        self.y = 0
        self.simbolo = random.choice(lista_letras)

    def get_simbolo(self):
        return self.simbolo
    
    def get_y(self):
        return self.y

