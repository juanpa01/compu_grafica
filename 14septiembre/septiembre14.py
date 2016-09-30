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
    sp_x = 100
    sp_y = 100
    pantalla.blit(fondo,[0,0])
    pantalla.blit(sp,[sp_x,sp_y])
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_RIGHT:
                    sp_x += 10
                if event.key  == pygame.K_LEFT:
                    sp_x -= 10
                if event.key  == pygame.K_UP:
                    sp_y -= 10
                if event.key  == pygame.K_DOWN:
                    sp_y += 10

        pantalla.blit(fondo,[0,0])
        pantalla.blit(sp,[sp_x,sp_y])
        pygame.display.flip()
