import pygame
import random

ANCHO=1252
ALTO=682
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AQUA=(0,255,255)
CHOCOLATE=(210,105,30)
ROSADO=(255,192,203)
AMARILLO=(255,255,0)
TURQUEZA=(64,224,208)
NARANJA=(255,69,0)
VERDE=(0,128,0)

class jugador(pygame.sprite.Sprite):
    def __init__ (self, archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update (self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
