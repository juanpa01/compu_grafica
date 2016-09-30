import pygame
from Libreria import *
y=0
#mp=[x1,y1,x2,y2]
def dibujarPatron(x,y):
    s=[[x,y],[x+30,y],[x+30,y-20],[x+50,y-20],[x+50,y-30],[x+20,y-30],[x+20,y-10],[x,y-10]]
    sta=TaL([0,400],s)
    pygame.draw.polygon(pantalla,AZUL,sta)
    pygame.display.flip()

def dibujarPatron2(x,y):
    s2=[[x,y],[x+30,y],[x+30,y-20],[x+50,y-20],[x+50,y-30],[x+20,y-30],[x+20,y-10],[x,y-10]]
    sta2=TaL([0,400],s2)
    pygame.draw.polygon(pantalla,AZUL,sta2)
    pygame.display.flip()

def dibujarPatron3(x,y):
    s3=[[x+30,y],[x+30,y-30],[x+10,y-30],[x+10,y-50],[x,y-50],[x,y-20],[x+20,y-20],[x+20,y]]
    sta3=TaL([0,400],s3)
    pygame.draw.polygon(pantalla,AZUL,sta3)
    pygame.display.flip()

def dibujarPatron4(x,y):
    s4=[[x+30,y],[x+30,y-30],[x+10,y-30],[x+10,y-50],[x,y-50],[x,y-20],[x+20,y-20],[x+20,y]]
    sta4=TaL([0,400],s4)
    pygame.draw.polygon(pantalla,AZUL,sta4)
    pygame.display.flip()
if __name__ == "__main__":
    ban=0
    l=[]
    while ban < ANCHO:
        a=dibujarPatron(ban,ALTO-10)
        ban+=40
        l.append(a)
    print l

    ban2=0
    l2=[]
    while ban2 < ANCHO:
        a=dibujarPatron2(ban2,ALTO-360)
        ban2+=40
        l2.append(a)
    print l2

    ban3=0
    l3=[]
    while ban3 < ALTO:
        c=dibujarPatron3(ANCHO-390,ban3)
        ban3+=40
        l3.append(c)
    print l3

    ban4=0
    l4=[]
    while ban4 < ALTO:
        c=dibujarPatron3(ANCHO-40,ban4)
        ban4+=40
        l4.append(c)
    print l4
    '''mt=[0+x1,0,30,10]
    mt2=[20,0,10,30]
    mt3=[20,20,30,10]
    pygame.draw.rect(pantalla, AZUL, mt)
    pygame.draw.rect(pantalla, AZUL, mt2)
    pygame.draw.rect(pantalla, AZUL, mt3)'''

    fin=False
while not fin:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            fin=True

    pygame.display.update()
