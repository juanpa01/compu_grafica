import lib
import pygame
import random

Ancho = 600;
Alto = 600;
centro = (300,300)

pygame.init()
pantalla = pygame.display.set_mode((Ancho, Alto))
lib.dibujarEjes(centro,pantalla,Alto,Ancho,[255, 255, 255])

punto1 = (10, 50)
punto2 = (80, 30)

lib.dibujarPuntosEje(pantalla,punto1, lib.Blanco, centro)
lib.dibujarPuntosEje(pantalla,punto2, lib.Blanco, centro)

vec = lib.vector_Respuesta(punto1,punto2)

lib.dibujarlineaEje(pantalla,centro,vec,lib.Azul)

pygame.display.flip()    #refresca la pantalla
while 1:                  #ciclo para mantener la pantalla abierta
    tecla=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           exit()
