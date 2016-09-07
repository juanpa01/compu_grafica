#Este archivo almacenara las funciones utlizadas en los demas archivos
#que tengo desordenados, por hacer archivos a la ligera
#3234979023
#funciones de vectores
import pygame
import math
#retorna la norma de un vector
def norma(vec):
    n = math.sqrt(vec[0]**2 + vec[1]**2)
    return n
#retorna el producto punto de un vector
def producto_punto(vec1,vec2):
    res = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    return res
#retorna el angulo (gradientes) de dos vectores
def angulo(vector1,vector2):
     a = math.fabs(producto_punto(vector1,vector2))
    b = norma(vector1) * norma(vector2)
    t = math.acos(a/b)
    return math.degrees(t)
#retorna la distancia entre dos puntos
def distancia(p1,p2):
    a = p2[0]-p1[0]
    b = p2[1]-p1[1]
    dis = math.sqrt(a**2 + b**2)
    return dis
#Vector resultante dado dos puntos
def vector_Respuesta(u, v):
    vec= (v[0] - u[0], v[1] - u[1])
    return vec
#define si dos rectas son paralelas entre ellas
def paralelas (vec1, vec2):
    k1 = vec1[1]/vec2[1]
    tol = k1*0.005
    arriba = k1 + tol
    abajo = k1 - tol
    k2 = vec1[0]/vec2[0]
    if k2 >= abajo and k2 <= arriba:
        return True
    return False
#define si dos rectas son perpendicular entre ellas
def perpendicular (vec1, vec2):
    return vec1[1]*vec2[1] + vec1[0]*vec2[0]


#funciones acerca de grficos
#recordar que cada archivo que se use graficos
#en dicho archivo debe ir las siguentes lineas comentadas
#
#pygame.init()  #inicia
#pantalla=pygame.display.set_mode((Ancho, Alto))    #define tamano de la pamtalla

#pygame.display.flip()    #refresca la pantalla
#while 1:                  #ciclo para mantener la pantalla abierta
#    tecla=pygame.key.get_pressed()
#    for event in pygame.event.get():
#        if event.type==pygame.QUIT:
#            exit()

Blanco = [255, 255, 255]
Negro = [0 ,0 ,0 ]
Rojo = [255, 0, 0]
Verde = [0, 255, 0]
Azul = [0, 0, 255]

#dibuja los ejes en pantalla
def dibujarEjes(centro, pantalla, alto, ancho, color):
    pygame.draw.line(pantalla, color, (0,centro[1]), (ancho, centro[1]))
    pygame.draw.line(pantalla, color, (centro[0], 0), (centro[0], alto))

#dibuja linea desde la parte superior izquierda de la pantalla
def dibujarlinea(pantalla, punto, color):
    pygame.draw.line(pantalla,color, punto)
#dibuja una linea en un plano cartesiano dibujado anteriormente
def dibujarlineaEje (pantalla,centro, punto, color):
    px = centro[0]+punto[0]
    py = centro[1]-punto[1]
    punto2= (px, py)
    pygame.draw.line(pantalla,color, centro, punto2)

#dibuja puntos desde la parte superior izquierda de la pantalla
def dibujarPuntos(pantalla,punto, color):
    pantalla.set_at(punto,color)
#dibuja puntos con un centro establecido en pantalla
def dibujarPuntosEje(pantalla,punto, color, centro):
    px = centro[0]+punto[0]
    py = centro[1]-punto[1]
    punto2= (px, py)
    pantalla.set_at(punto2,color)

#dibuja circulos desde la parte superior izqueirda de la pamntalla
def dibujarcirculo(pantalla,color, punto, radio, ancho):
    pygame.draw.circle(pantalla,color,punto,radio,ancho)

def dibujarcirculoEje(pantalla,color, punto, radio, ancho, centro):
    px = centro[0]+punto[0]
    py = centro[1]-punto[1]
    punto2= (px, py)
    pygame.draw.circle(pantalla,color,punto2,radio,ancho)
    
#transformada de un punto
def transformadaPunto(punto, centro):
    px = centro[0]+punto[0]
    py = centro[1]-punto[1]
    return (px,py)

#dibuja un triangulo
def dibujapoligono(pantalla, color, vertices, ancho):
    pygame.draw.polygon(pantalla, color, vertices, ancho)

#Funciones de matrices
#cada numero de la matriz se multiplica por -1
def matrizOpuesta(m):
    for fila in range(len(m)):
        for col in range(len(m)):
             m[fila][col] = m[fila][col] * -1
    return m


#Genera una matriz random mxn
def matrizRandom(tamf, tamc):
    """
    f=[0]*3
    m=[0]*3
    for i in range(len(f)):
        m[i] = f
    for fila in m:
        print fila
    """
    m= [[0,0,0,],[0,0,0,],[0,0,0]]
    for i in range(tamf):
        for j in range(tamc):
            valor = random.randrange(7)
            m[i][j] = valor

    return m
#retorna una matriz transpuesta, es decir cambia filas por columnas
def transpuesta(m):
    mr= [[0,0,0,],
         [0,0,0,],
         [0,0,0]]

    for i in range(len(m)):
        for j in range(len(m)):
            mr[j][i] = m[i][j]
    return mr
#suma todas las filas de una matriz|
def suma_filas(m):
    tam = len(m[0])
    l = [0]*tam
    for i in range(len(m)):
        for j in range(len(m[0])):
            l[j] += m[i][j]
    return l
#suma todsa las columnas de una matriz
def suma_columnas(m):
    tam = len(m)
    l = [0]*tam
    for i in range(len(m[0])):
        for j in range(len(m)):
            l[j] += m[j][i]
    return l

