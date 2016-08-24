def paralelas (vec1, vec2):
    k1 = vec1[1]/vec2[1]
    tol = k1*0.005
    arriba = k1 + tol
    abajo = k1 - tol
    k2 = vec1[0]/vec2[0]
    if k2 >= abajo and k2 <= arriba:
        return True
    return False

def perpendicular (vec1, vec2):
    return vec1[1]*vec2[1] + vec1[0]*vec2[0]


print "Ingrese los datos de la primera recta Ax+By+c=0"
a = raw_input("Ingrese A--->")
b = raw_input("Ingrese B--->")
c = raw_input("Ingrese C--->")

A1 = int(a)
B1 = int(b)
C1 = int(c)
r1 = (-A1,B1)

print "Ingrese los datos de la segunda recta Ax+By+c=0"
a = raw_input("Ingrese A--->")
b = raw_input("Ingrese B--->")
c = raw_input("Ingrese C--->")

A2 = int(a)
B2 = int(b)
C2 = int(c)
r2 = (-A2,B2)

bol = paralelas(r1,r2)

num = perpendicular(r1,r2)

if bol:
    print "las rectas son paralelas"
else:
    print "Las rectas no son paralelas"

if num == 0:
    print "las rectas son perpendicular"
else:
    print "Las rectas no son perpendicular"
