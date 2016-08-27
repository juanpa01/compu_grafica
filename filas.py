
def nuevaFila(num):
    l=[]
    con=0
    while con<num:
        v = raw_input("numero  ")
        l.append(int(v))
        con += 1
    return l

m = []
m2 =[]
m3=[]
columnas= 3
numfilas=3
con=0

while con < numfilas:
    f = nuevaFila(columnas)
    m.append(f)
    con += 1

con=0
while con < numfilas:
    f = nuevaFila(columnas)
    m2.append(f)
    con += 1

con=0
while con < numfilas:
    lon=3
    m3.append([10]*lon)
    con += 1

print

for fila in m3:
    print fila

print

for fila in range(len(m)):
    for columna in range(len(m)):
        m3[fila][columna] = m[fila][columna] + m2[fila][columna]

for fila in m:
    print fila

print

for fila in m2:
    print fila

print

for fila in m3:
    print fila

###################################################

l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[9,8,7],[6,5,4],[3,2,1]]
l3 = [[0,0,0],[0,0,0],[0,0,0]]

for fila in range(len(l1)):
    for columna in range(len(l1)):
        l3[fila][columna] = l1[fila][columna] + l2[fila][columna]

for pos in l3:
    print pos
