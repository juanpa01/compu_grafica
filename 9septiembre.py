import math
import lib
import pygame


Ancho = 600
Alto = 6000
centro = (300,300)
pygame.init()  #inicia
pantalla=pygame.display.set_mode((Ancho, Alto))    #define tamano de la pamtalla
lib.dibujarEjes(centro, pantalla,Alto, Ancho, lib.Blanco)

puntos = [(100,50), (150,50), (125,100)]
""""
puntos = [(80,80), (80,160), (160,160), (160,80)]
puntosT = lib.traslacionPuntos(centro,puntos)
lib.dibujapoligono(pantalla, lib.Blanco, puntosT, 1)
print puntosT

puntosR = lib.rotacionPuntos(puntos, 90)
puntosRT = lib.traslacionPuntos(centro, puntosR)
print puntosRT
lib.dibujapoligono(pantalla, lib.Blanco, puntosRT, 1)
"""

pygame.display.flip()
fin = False
cont = 0
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

        puntosR = lib.rotacionPuntos(puntos , 45)
        puntos = puntosR
        puntosRT = lib.traslacionPuntos(centro, puntosR)
        lib.dibujapoligono(pantalla, lib.Blanco, puntosRT, 0)
        pygame.display.flip()
        """cont += 15
        if cont > 360:
            cont = 0
"""
