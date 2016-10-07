import pygame
import random
import os,sys

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

class Icono(pygame.sprite.Sprite):
    id = -1
    def __init__ (self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False

    def update (self, surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image, self.rect)

def Crea_icono(archivo, pos):
    objeto = Icono(archivo)
    objeto.rect.y = pos[1]
    objeto.rect.x = pos[0]
    todos.add(objeto)
    iconos.add(objeto)
    return objeto

def Crea_icono_movibles(archivo):
    objeto = Icono(archivo)
    objeto.rect.center = pantalla.get_rect().center
    todos.add(objeto)
    #iconos.add(objeto)
    move_iconos.add(objeto)
    return objeto


if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pantalla = pygame.display.set_mode((600,600))
    reloj = pygame.time.Clock()

    todos = pygame.sprite.Group()
    iconos = pygame.sprite.Group()
    move_iconos = pygame.sprite.Group()

    icono1 = Crea_icono("ball.png", (0,500))
    n = 1
    icono1.id = n
    icono2 = Crea_icono("bala.png", (100,500))
    n += 1
    icono2.id = n

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            for i in iconos:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if i.rect.collidepoint(event.pos):
                        if i.id == 1:
                            icono3 = Crea_icono_movibles("ball.png")
                            n += 1
                            icono3.id = n
                        if i.id == 2:
                            icono4 = Crea_icono_movibles("bala.png")
                            n += 1
                            icono4.id = n
                        print "icono"+str(i.id)

                for ic in move_iconos:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if ic.rect.collidepoint(event.pos):
                            ic.click = True
                            print "icono"+str(ic.id)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        ic.click = False

        pantalla.fill(0)
        todos.draw(pantalla)
        move_iconos.update(pantalla)
        pygame.display.update()
        reloj.tick(60)
