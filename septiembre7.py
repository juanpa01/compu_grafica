import pygame
import lib


Ancho = 600
Alto = 6000
centro = (300,300)
pygame.init()  #inicia
pantalla=pygame.display.set_mode((Ancho, Alto))    #define tamano de la pamtalla

pantalla.fill(lib.Blanco)
lib.dibujar_ejes(centro, pantalla, Alto, Ancho, lib.Rojo)

p1 = (50, 50)
p2 = (75, 75)
p3 = (175, 75)
p4 = (125, 50)

puntos = (p1, p2, p3, p4)
s = (2,2)
puntosT = lib.traslacion_puntos(centro,puntos)

lib.dibujar_poligono(pantalla, lib.Azul, puntosT, 1)

puntosE = lib.escalar_puntos(puntos, s)
puntosET = lib.traslacion_puntos(centro, puntosE)

lib.dibujar_poligono(pantalla, lib.Azul, puntosET, 1)
lib.dibujar_poligono(pantalla, lib.Azul, lib.traslacion_puntos(centro, lib.escalar_puntos(puntos, (3,3))), 1)
lib.dibujar_poligono(pantalla, lib.Azul, lib.traslacion_puntos(centro,lib.escalar_puntos(puntos, (0.5,0.5))), 1)


pygame.display.flip()    #refresca la pantalla
while 1:                  #ciclo para mantener la pantalla abierta
    tecla=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
