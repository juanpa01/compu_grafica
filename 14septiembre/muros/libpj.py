import pygame

AZUL=(0,0,255)
NEGRO=(0,0,0)

class Jugador(pygame.sprite.Sprite):
    muros=None
    def __init__(self, archivo, xi, yi):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=xi
        self.rect.y=yi
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x+=self.var_x
        ls_golpes=pygame.sprite.spritecollide(self, self.muros,False)
        for bloque in ls_golpes:
            if self.var_x >0:
                self.rect.right=bloque.rect.left
            else:
                self.rect.left=bloque.rect.right

        self.rect.y+=self.var_y
        ls_golpes=pygame.sprite.spritecollide(self, self.muros,False)
        for bloque in ls_golpes:
            if self.var_y >0:
                self.rect.bottom=bloque.rect.top
            else:
                self.rect.top=bloque.rect.bottom



class Muro(pygame.sprite.Sprite):
    def __init__(self, xi, yi):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.rect.x=xi
        self.rect.y=yi
