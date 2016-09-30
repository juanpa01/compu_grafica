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

class jugador(pygame.sprite.Sprite):
    def __int__ (self, archivo):
        pygame.sprite.Sprite.__int__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    jp =  jugador('nave.png')
    todos = pygame.sprite.Group()
    todos.add(jp)


    pygame.display.flip()
    reloj =  pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pantalla.fill(NEGRO)
        todos.draw(pantalla)
        pygame.display.flip()
