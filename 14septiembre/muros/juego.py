import pygame
from libpj import *

ANCHO=600
ALTO=400

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    jp=Jugador('imagenes/enem2a.png',100,100)
    todos=pygame.sprite.Group()
    todos.add(jp)

    ls_muros=pygame.sprite.Group()
    for i in range(0,ANCHO,40):
        muro=Muro(i,0)
        ls_muros.add(muro)
        todos.add(muro)
        muro=Muro(i,ALTO-40)
        ls_muros.add(muro)
        todos.add(muro)

    for i in range(0,ALTO, 40):
        muro=Muro(0,i)
        ls_muros.add(muro)
        todos.add(muro)
        muro=Muro(ANCHO-40,i)
        ls_muros.add(muro)
        todos.add(muro)

    jp.muros=ls_muros
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x=-5
                    jp.var_y=0
                if event.key == pygame.K_RIGHT:
                    jp.var_x=5
                    jp.var_y=0
                if event.key == pygame.K_UP:
                    jp.var_x=0
                    jp.var_y=-5
                if event.key == pygame.K_DOWN:
                    jp.var_x=0
                    jp.var_y=5
                if event.key == pygame.K_SPACE:
                    jp.var_x=0
                    jp.var_y=0

        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
