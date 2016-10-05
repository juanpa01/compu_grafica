import os,sys
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
AZUL=(0,0,255)

class Cuadro:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.click = False
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill(TURQUEZA)

    def update (self, surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image, self.rect)

def Juego (cuadro):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cuadro.rect.collidepoint(event.pos):
                cuadro.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            cuadro.click = False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()


def main(pantalla, cuadro):
    #captura de teclas
    Juego(cuadro)
    pantalla.fill(0)
    cuadro.update(pantalla)

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pantalla = pygame.display.set_mode((1000,600))
    reloj = pygame.time.Clock()
    cuadro = Cuadro((0,0,150,150))
    cuadro.rect.center = pantalla.get_rect().center

    while 1:
        main(pantalla,cuadro)
        pygame.display.update()
        reloj.tick(60)
