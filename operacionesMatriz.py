#mostrar la matriz opuesta

import random

m = [[2,0],[3,-6]]

def matrizOpuesta(m):
    for fila in range(len(m)):
        for col in range(len(m)):
             m[fila][col] = m[fila][col] * -1
    return m


ma = []
mb = []
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

ma = matrizRandom(3,3)
mb = matrizRandom(3,3)

def transpuesta(m):
    mr= [[0,0,0,],[0,0,0,],[0,0,0]]

    for i in range(len(m)):
        for j in range(len(m)):
            mr[j][i] = m[i][j]

    return mr
