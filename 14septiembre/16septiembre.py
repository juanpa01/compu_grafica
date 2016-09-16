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
AZUL=(0,0,255)

class jugador(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x = 0
        self.var_y = 0
        self.vida = 20
        self.sonido = pygame.mixer.Sound("disparo.wav")

    def golpe (self):
        self.vida -= 5
        self.sonido.play()

    def update (self):
        self.rect.x += self.var_x
        self.rect.y += self.var_y

class Enemigo(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.golpe = False

    def update (self):
        if self.golpe :
            self.sonido.play()
            self.golpe = False


class Premio(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.punto = 0

    def puntos (self):
        self.punto += 1


    def update (self):
        pass

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    gano = pygame.image.load("win.png")
    pantalla.blit(gano,[-300,-300])

    todos = pygame.sprite.Group()
    jp = jugador(100,100)
    todos.add(jp)

    enemigos = pygame.sprite.Group()
    for i in range (30):
        x = random.randrange(ANCHO)
        y = random.randrange(ALTO)
        e = Enemigo(x,y)
        todos.add(e)
        enemigos.add(e)

    premios = pygame.sprite.Group()
    for i in range(10):
        x = random.randrange(ANCHO)
        y = random.randrange(ALTO)
        p = Premio(x,y)
        todos.add(p)
        premios.add(p)

    sonido = pygame.mixer.Sound("disparo.wav")
    reloj = pygame.time.Clock()
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():    #seccion de capturas de evento
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x = 5
                    jp.var_y = 0
                if event.key == pygame.K_LEFT:
                    jp.var_x = -5
                    jp.var_y = 0
                if event.key == pygame.K_UP:
                    jp.var_x = 0
                    jp.var_y = -5
                if event.key == pygame.K_DOWN:
                    jp.var_x = 0
                    jp.var_y = 5
                if event.key == pygame.K_s:
                    jp.var_x = 0
                    jp.var_y = 0
                    sonido.play()


        #logica de juego
        if jp.rect.x > ANCHO:
        #    jp.rect.x = 0
             jp.var_x = 0
             jp.rect.x = ANCHO - jp.rect.width


        l_col = pygame.sprite.spritecollide(jp,enemigos,True)
        for en in l_col:
            #en.golpe = True
            jp.golpe()

        if jp.vida == 0:
            fin = True

        p_col = pygame.sprite.spritecollide(jp,premios,True)
        for en in p_col:
            p.puntos()
            if p.punto == 3:
                print "gano"
                pantalla.blit(gano,[100,100])
                pygame.display.flip()

        pantalla.fill(BLANCO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
