import pygame 
from pygame.locals import *

class Sopa:
    def __init__(self, largura):
        self.altura_sopa = 120
        self.largura_sopa = 170
        self.x = largura/ 2 - self.largura_sopa
        self.y = 600

    def desenhar_sopa(self, tela):
        pygame.draw.rect(tela, (255, 255, 0), (self.x, self.y, self.largura_sopa, self.altura_sopa))

    def movimentacao_sopa(self):
        if pygame.key.get_pressed()[K_a]:
            self.x = self.x - 0.4
        if pygame.key.get_pressed()[K_d]:
            self.x = self.x + 0.4
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura_sopa, self.altura_sopa)
    
