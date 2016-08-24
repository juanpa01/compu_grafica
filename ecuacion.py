#Vector resultante dado dos vectores
def vecRes(u, v):
    vec= (v[0] - u[0], v[1] - u[1])
    return vec

u = raw_input("Ingrese el primer punto: ").split(" ")
x1 = int(u[0])
y1 = int(u[1])
u = (x1,y1)

v = raw_input("Ingrese el segundo punto: ").split(" ")
x2 = int(v[0])
y2 = int(v[1])
v = (x2,y2)

vec = vecRes(u,v)
#Ecuacion vectorial y parametrizada de una recta dado dos puntos A y P
print "Ecuacion de la recta = "
print "(x,y) = ({0},{1})+K({2},{3})".format(u[0],u[1],vec[0],vec[1])
print "Ecuacion parametrica de X"
print "x = {0} + {1}K".format(u[0],vec[0])
print "Ecuacion parametrica de Y"
print "y = {0} + {1}K".format(u[1],vec[1])
