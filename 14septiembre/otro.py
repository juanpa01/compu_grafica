import pygame
import random

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
    def __init__ (self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update (self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Enemigo(pygame.sprite.Sprite):
    def __init__ (self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel= 2
        self.fuego = 0
        self.t = 40

    def update (self):
        self.rect.x -= self.vel

    def time(self):
        self.t = 1
        if self.t == 0:
            self.t = 40
            self.fuego = 1
        else:
            self.fuego = 0



class Disparo(pygame.sprite.Sprite):
    def __init__ (self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = 10
        self.dir = 0

    def update (self):
        if self.dir == 0:
            self.rect.x += self.vel
        if self.dir == 1:
            self.rect.x -= self.vel

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.mouse.set_visible(False)
    jp =  jugador('sprite/nave.png')
    todos = pygame.sprite.Group()
    todos.add(jp)

    enemigos = pygame.sprite.Group()
    for i in range(10):
        #x = random.randrange(ANCHO - 20)
        x= ANCHO
        y = random.randrange(ALTO - 20)
        e = Enemigo('sprite/naveE.png')
        e.rect.x = x
        e.rect.y = y
        e.vel= random.randrange(10)
        enemigos.add(e)
        todos.add(e)

    balas = pygame.sprite.Group()
    ebalas = pygame.sprite.Group()
    pygame.display.flip()
    reloj =  pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                b = Disparo('sprite/bala.png')
                b.rect.x = jp.rect.x + 40
                b.rect.y = jp.rect.y
                balas.add(b)
                todos.add(b)

        #eliminar bala fuera
        for b in balas:
            ls_imp = pygame.sprite.spritecollide(b,enemigos, True)
            for b_imp in ls_imp:
                balas.remove(b)
                todos.remove(b)

            if b.rect.y < 0:
                balas.remove(b)
                todos.remove(b)

        for e in enemigos:
            if e.rect.x < 0:
                y = e.rect.y
                x= ANCHO
                vel = e.vel
                enemigos.remove(e)
                todos.remove(e)
                e.rect.x = x
                e.rect.y = y
                e.vel= vel
                enemigos.add(e)
                todos.add(e)

            if e.fuego == 1:
                b = Disparo('sprite/ball.png')
                b.rect.x = e.rect.x
                b.rect.y = e.rect.y
                b.dir = 1
                ebalas.add(b)
                todos.add(b)



        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
