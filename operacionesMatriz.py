#mostrar la matriz opuesta

import random

m = [[2,0],[3,-6]]

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
    tam = len(m)
    l = [0]*tam
    for i in range(len(m)):
        for j in range(len(m)):
            l[j] += m[i][j]
    return l
#suma todsa las columnas de una matriz
def suma_columnas(m):
    tam = len(m)
    l = [0]*tam
    for i in range(len(m)):
        for j in range(len(m)):
            l[j] += m[j][i]
    return l

ma = []
mb = []


ma = matrizRandom(3,3)
mb = matrizRandom(3,3)

fil = suma_filas(ma)
col = suma_columnas(ma)
for fila in ma:
    print fila
print
print fil
print
print col
