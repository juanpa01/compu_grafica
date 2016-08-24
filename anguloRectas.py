import math

def norma(vec):
    n = math.sqrt(vec[0]**2 + vec[1]**2)
    return n

def punto(vec1,vec2):
    res = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    return res

def angulo(vector1,vector2):
    a = math.fabs(punto(vector1,vector2))
    b = norma(vector1) * norma(vector2)
    t = math.acos(a/b)
    return math.degrees(t)

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

ang = angulo(r1,r2)

print "Recta 1"
print "{0}x + {1}y + {2}= 0".format(A1,B1,C1)
print "Recta 2"
print "{0}x + {1}y + {2}= 0".format(A2,B2,C2)
print "El angulo entre las dos rectas es : {0}".format(ang)
