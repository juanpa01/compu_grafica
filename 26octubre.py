import pygame
ALTO=600
ANCHO=800

BLANCO=(255,255,255)
NEGRO=(0,0,0)
VERDE=(0,255,0)
ROJO=(255,0,0)

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.rect = self.image.get_rect()
        self.image.fill(VERDE)
        self.var_x = 0
        self.id = 0
        self.enviado = 0
        self.choque = 0

    def update(self):
        self.rect.x += self.var_x

class Torre(pygame.sprite.Sprite):
    def __init__(self, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.rect = self.image.get_rect()
        self.image.fill(BLANCO)
        self.rect.x = px
        self.rect.y = py
        self.r =  Radar(100,px, py, 70, 70)

class Radar(pygame.sprite.Sprite):
    def __init__(self, radio, xo, yo, xd,yd  ):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([radio,radio])
        self.rect = self.image.get_rect()
        self.image.fill(NEGRO)
        self.cx = radio/2
        self.cy = radio/2
        nx = self.cx - (xd/2)
        ny = self.cy - (yd/2)
        self.rect.x = xo - nx
        self.rect.y = yo - ny
        print self.rect.x
        print self.rect.y



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])

    todos=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    radar=pygame.sprite.Group()
    for i in range(10):
        ene = Enemigo()
        ene.id = i
        ene.rect.x = 10
        ene.rect.y = 270
        enemigos.add(ene)
        todos.add(ene)

    t= Torre(200,200)
    todos.add(t)




    reloj=pygame.time.Clock()
    tiempo = 30
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        tiempo -= 1

        if tiempo == 0:
            for ene in enemigos:
                if ene.enviado == 0:
                    ene.enviado = 1
                    ene.var_x = 2
                    print "enviado"
                    break
            tiempo = 30

        colision = pygame.sprite.spritecollide(t.r, enemigos, False)
        for c in colision:
            print "enemigo  " + str(c.id)
            print "disparo"
            print "tam "+str(len(colision))

        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
