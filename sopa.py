import pygame 
from pygame.locals import *

class Sopa(pygame.sprite.Sprite):
    def __init__(self, largura):

        super().__init__()

        imagem = pygame.image.load('imagens/panela.png').convert_alpha()
        self.image = pygame.transform.smoothscale(imagem, (233, 175))
        self.rect = self.image.get_rect()

        self.rect.centerx = largura / 2
        y = 600
        self.rect.y = y

    def update(self):
        if pygame.key.get_pressed()[K_a]:
            self.rect.x = self.rect.x - 1
        if pygame.key.get_pressed()[K_d]:
            self.rect.x = self.rect.x + 1
