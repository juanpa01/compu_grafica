import pygame
import li


Ancho = 600
Alto = 6000
centro = (300,300)
pygame.init()  #inicia
pantalla=pygame.display.set_mode((Ancho, Alto))    #define tamano de la pamtalla

pantalla.fill(li.Blanco)
li.dibujarEjes(centro, pantalla, Alto, Ancho, li.Rojo)

p1 = (50, 50)
p2 = (75, 75)
p3 = (175, 75)
p4 = (125, 50)

puntos = (p1, p2, p3, p4)
s = (2,2)
puntosT = li.traslacion(centro,puntos)

li.dibujapoligono(pantalla, li.Azul, puntosT, 1)

puntosE = li.escalar(puntos, s)
puntosET = li.traslacion(centro, puntosE)

li.dibujapoligono(pantalla, li.Azul, puntosET, 1)
li.dibujapoligono(pantalla, li.Azul, li.traslacion(centro,li.escalar(puntos, (3,3))), 1)
li.dibujapoligono(pantalla, li.Azul, li.traslacion(centro,li.escalar(puntos, (0.5,0.5))), 1)


pygame.display.flip()    #refresca la pantalla
while 1:                  #ciclo para mantener la pantalla abierta
    tecla=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
