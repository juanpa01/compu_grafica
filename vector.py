#encuentra los paramteros para la ecuacion general de la recta Ax + By + c = 0
def parametros(u,v):
    a = v[1]
    b = -v[0]
    c = u[1]*v[0] - u[0]*v[1]
    return a,b,c

a = raw_input("ingrese el primer punto A  ").split(" ")
x0 = int(a[0])
y0 = int(a[1])
a = (x0,y0)

v = raw_input("ingrese el vector V  ").split(" ")
Vx = int(v[0])
Vy = int(v[1])
v = (Vx,Vy)

p = parametros(a,v)

print "Ecuacion continua de la recta"
print "(x - {0})/{1} = (y - {2})/{3}".format(a[0],v[0],a[1],v[1])
print "Ecuacion general de la recta"
print "{0}x + {1}y + {2} = 0".format(p[0],p[1], p[2])
