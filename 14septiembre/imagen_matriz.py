import pygame


ANCHO=1024
ALTO=384
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



def Cargar_fondo(archivo, ancho_corte, alto_corte):
    imagen = pygame.image.load(archivo).convert_alpha()
    img_ancho , img_alto = imagen.get_size()
    print img_ancho,' ',img_alto
    matriz_fondo = []
    for fila in range(0, img_ancho/ancho_corte):
        linea = []
        matriz_fondo.append(linea)
        for columna in range(0, img_alto/alto_corte):
            cuadro = (fila*ancho_corte, columna*alto_corte, ancho_corte, alto_corte)
            linea.append(imagen.subsurface(cuadro))
    return matriz_fondo




if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    #Fondo = pygame.image.load('sprite/terrenogen.png').convert_alpha()
    Fondo = Cargar_fondo('sprite/animales.png',32,32)
    cont = 0
    reloj = pygame.time.Clock()
    pantalla.fill((0,0,0))
    pos_y = 0
    pos_x = 0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        #pantalla.fill((0,0,0))
        if event.type == pygame.KEYDOWN:
            pantalla.fill((0,0,0))
            if event.key  == pygame.K_RIGHT:
                pos_x += 0.10
                if cont <= 2:
                    pantalla.blit(Fondo[3+cont][6], [pos_x, pos_y])
                    cont += 1
                else:
                    cont = 0
                    pantalla.blit(Fondo[3+cont][6], [pos_x, pos_y])
            if event.key  == pygame.K_LEFT:
                pos_x -= 0.10
                if cont <= 2:
                    pantalla.blit(Fondo[3+cont][5], [pos_x, pos_y])
                    cont += 1
                else:
                    cont = 0
                    pantalla.blit(Fondo[3+cont][5], [pos_x, pos_y])
            if event.key  == pygame.K_UP:
                pos_y -= 0.10
                if cont <= 2:
                    pantalla.blit(Fondo[3+cont][7], [pos_x, pos_y])
                    cont += 1
                else:
                    cont = 0
                    pantalla.blit(Fondo[3+cont][7], [pos_x, pos_y])
            if event.key  == pygame.K_DOWN:
                pos_y += 0.10
                if cont <= 2:
                    pantalla.blit(Fondo[3+cont][4], [pos_x, pos_y])
                    cont += 1
                else:
                    cont = 0
                    pantalla.blit(Fondo[3+cont][4], [pos_x, pos_y])

        '''
        pantalla.fill((0,0,0))
        if cont <= 2:
            pos_y += var_y
            pantalla.blit(Fondo[3+cont][4], [0, pos_y])
            cont += 1
        else:
            cont = 0
            pos_y += var_y
            pantalla.blit(Fondo[3+cont][4],[0, pos_y])
        '''
        pygame.display.flip()
        #reloj.tick(10)
