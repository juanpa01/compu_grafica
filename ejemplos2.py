l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[9,8,7],[6,5,4],[3,2,1]]
l3 = [[0,0,0],[0,0,0],[0,0,0]]

for fila in range(len(l1)):
    for columna in range(len(l1)):
        l3[fila][columna] = l1[fila][columna] + l2[fila][columna]

for pos in l3:
    print pos
