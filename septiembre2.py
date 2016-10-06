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
                #archivo modificada para probar versionamiento
                """
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont == 2:
                   cont = 0
                if cont == 0:
                    punto1 = pygame.mouse.get_pos()
                if cont == 1:
                    lib.dibujarEjes(centro,pantalla,Alto,Ancho,lib.Negro)
                    punto2 = pygame.mouse.get_pos()

                    pt1 = lib.transformadaPunto(punto1, centro)
                    pt2 = lib.transformadaPunto(punto2, centro)
                    pygame.draw.line(pantalla,lib.Rojo, pt1, pt2)

                    vec2 = lib.vector_Respuesta(punto1, punto2)
                    lib.dibujarlineaEje(pantalla,centro,vec2,lib.Negro)
                    pygame.display.flip()
                cont += 1
"""
