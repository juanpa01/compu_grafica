import pygame

Ancho = 600
Alto = 600

Blanco = [255, 255, 255]
Negro = [0 ,0 ,0 ]
Rojo = [255, 0, 0]

def dibujarEjes(c, p, al, an):
    pygame.draw.line(p, Rojo, (0,c[1]), (an, c[1]))
    pygame.draw.line(p, Rojo, (c[0], 0), (c[0], al))

def cartesiano (pantalla,c, p):
    px = c[0]+p[0]
    py = c[1] - p[1]
    p= (px, py)
    pygame.draw.line(pantalla,Negro, c, p)


pygame.init()
pantalla=pygame.display.set_mode((Ancho, Alto))
#pygame.draw.line(pantalla, Blanco, (200,200),(200,10), 1)
#pygame.draw.line(pantalla, Blanco, (200,200),(390,200), 1)
#pygame.draw.line(pantalla, Blanco, (210,150),(300,100), 1)
centro = (300, 300)
pantalla.fill(Blanco)
dibujarEjes(centro,pantalla,Alto, Ancho)
cartesiano(pantalla,centro, (50, -100))

pygame.display.flip()

while 1:
    tecla=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
