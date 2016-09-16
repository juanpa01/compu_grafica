import pygame


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

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fondo = pygame.image.load("fondo.jpg")
    sp = pygame.image.load("pig1.png")
    ball = pygame.image.load("ball.png")
    sp_x = 1000
    sp_y = 400
    ball_x = 600
    ball_y = 400
    pantalla.blit(fondo,[0,0])
    pantalla.blit(sp,[sp_x,sp_y])
    pantalla.blit(ball,[ball_x,ball_y])
    pygame.display.flip()
    reloj = pygame.time.Clock()
    fin=False
    posx = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pantalla.blit(fondo,[0,0])
        if sp_x >= 660:
            sp_x -= 2
            pantalla.blit(sp,[sp_x,sp_y])
            pantalla.blit(ball,[ball_x,ball_y])
        """else:
            ball_x -= 2
            pantalla.blit(ball,[ball_x,ball_y])
"""
        if ball_x == 0:
            posx = True

        if posx == True:
            ball_x += 2
        if ball_x == 600:
            posx = False
        if posx == False:
            ball_x -= 2
        pantalla.blit(fondo,[0,0])
        pantalla.blit(sp,[sp_x,sp_y])
        pantalla.blit(ball,[ball_x,ball_y])
        pygame.display.flip()
        reloj.tick(60)
