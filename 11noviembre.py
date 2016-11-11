import random
import pygame
import os, sys

ANCHO = 800
ALTO = 600
CENTRO = (300,300)
BLANCO = (255,255,255)
NEGRO = (0,0,0)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivo, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

if __name__ == '__main__':

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    #fondo de pantalla
    fondo = pygame.image.load("fondo.jpg")
    dim_fondo =  fondo.get_rect()
    marco = fondo.subsurface(0,800, ANCHO, ALTO)
    #mira
    mira = pygame.image.load("aaaa.png").convert_alpha()
    dim_mira =  mira.get_rect()
    pygame.mouse.set_visible(False)

    #disparo
    disparo = pygame.mixer.Sound('disparo.wav')

    e = Enemigo("juan1.png", 900, 300)
    todos = pygame.sprite.Group()
    todos.add(e)

    var_x = 0
    pos_x = 0
    reloj = pygame.time.Clock()

    while 1:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print "oprimio"
                disparo.play()
                for e in todos:
                    if e.rect.collidepoint(pygame.mouse.get_pos()):
                        print "impacto"
        #restriccion de dimension de la pantalla para deslizarse en la imagen
        if pos[0] >= ANCHO - 100:
            pos_x += 5
            for e in todos:
                e.rect.x -= 5

        if pos[0] <= 100:
            pos_x -= 5
            for e in todos:
                e.rect.x += 5
        if pos_x >= 0 and pos_x < (dim_fondo.width - ANCHO):
            ventana = fondo.subsurface(pos_x, 800, ANCHO, ALTO)

        pantalla.blit(ventana, (0,0))
        pantalla.blit(mira, (pos[0]-100,pos[1]-100))
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
