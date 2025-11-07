import pygame 
from pygame.locals import *

class Coracao(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        imagem = pygame.image.load('imagens/coraçãoColorido.png').convert_alpha()
        self.image = pygame.transform.smoothscale(imagem, (200, 200))
        self.rect = self.image.get_rect()

class ConfiguracaoIcon(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        imagem = pygame.image.load('imagens/configuraçãoIcon.png').convert_alpha()
        self.image = pygame.transform.smoothscale(imagem, (200, 200))
        self.rect = self.image.get_rect()

class MenuIcon(pygame.sprite.Sprite):
    def __init__(self, altura, largura):

        super().__init__()

        imagem = pygame.image.load('imagens/menuIcon.png').convert_alpha()
        self.image = pygame.transform.smoothscale(imagem, (200, 200))
        self.rect = self.image.get_rect()

        self.rect.x = largura - self.image.get_width()
        self.rect.y = self.image.get_height()
