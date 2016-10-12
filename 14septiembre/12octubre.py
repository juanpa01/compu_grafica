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
    Fondo = Cargar_fondo('sprite/terrenogen.png',32,32)
    pantalla.blit(Fondo[7][0], (0,0))
    pygame.display.flip()


    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
