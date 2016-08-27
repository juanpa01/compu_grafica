import pygame

Ancho = 600
Alto = 600

Blanco = [255, 255, 255]
Negro = [0 ,0 ,0 ]
Rojo = [255, 0, 0]
Verde = [0, 255, 0]
Azul = [0, 0, 255]

def dibujarEjes(c, p, al, an):
    pygame.draw.line(p, Rojo, (0,c[1]), (an, c[1]))
    pygame.draw.line(p, Rojo, (c[0], 0), (c[0], al))

def cartesiano (pantalla,c, p, color):
    px = c[0]+p[0]
    py = c[1]-p[1]
    punto= (px, py)
    pygame.draw.line(pantalla,color, c, punto)

def cartesiano2 (c, p, color):
    px = c[0]+p[0]
    py = c[1]-p[1]
    punto= (px, py)
    pygame.draw.line(pantalla,color, c, punto)

pygame.init()
pantalla=pygame.display.set_mode((Ancho, Alto))


centro = (300, 300)
pantalla.fill(Blanco)
dibujarEjes(centro,pantalla,Alto, Ancho)

vec1 = raw_input("ingrese corrdenadas del primer vector -->").split(" ")
x1 = int(vec1[0])
y1 = int(vec1[1])

vec2 = raw_input("ingrese corrdenadas del segundo vector -->").split(" ")
x2 = int(vec2[0])
y2 = int(vec2[1])

cartesiano(pantalla,centro, (x1, y1), Rojo)
cartesiano(pantalla,centro, (x2, y2), Verde)

x3 = x1 + x2
y3 = y1 + y2

cartesiano(pantalla,centro, (x3, y3), Azul)

pygame.display.flip()

while 1:
    tecla=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
