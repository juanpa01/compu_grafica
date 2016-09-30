import pygame
import lib
#ejercicio: mostrar la posicion cartesiana del raton

Ancho = 600;
Alto = 600;
centro = (300,300)

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((Ancho, Alto))
    pantalla.fill(lib.Blanco)
    lib.dibujarEjes(centro,pantalla,Alto,Ancho,lib.Negro)
    puntos =  [[100, 100],[100, 50],[50,100]]
    lib.dibujapoligono(pantalla,lib.Negro,puntos,1)

    vec1 = lib.vector_Respuesta(puntos[0],puntos[1])
    vec2 = lib.vector_Respuesta(puntos[1],puntos[2])
    vec3 = lib.vector_Respuesta(puntos[0],puntos[2])

    angulo1 = lib.angulo(vec1,vec2 )
    angulo2 = lib.angulo(vec2,vec3 )
    angulo3 = lib.angulo(vec1,vec3 )
    print angulo1
    print angulo2
    print angulo3
    pygame.display.flip()

    fin = False
    punto1 = (0,0)
    punto2 = (0,0)
    cont = 0

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

