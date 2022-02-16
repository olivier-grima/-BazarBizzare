from turtle import*
from dessinePolygone import*
from dessineRect import*

def sapin(p,x,y,couleur):       #sapin(1,0,0,"sea green")
    hideturtle()                #cacher le pointeur
    tracer(0)                   #dessiner instantanément
    pensize(0)
    #variables
    a=window_height()           #nombre de pixel sur la hauteur de l'écran
    lCote=a*0.15*p              #longueur d'un cote du triangle du sapin en fonction du nombre de pixels de l'ecran
    largBande=a*0.02*p          #largeur du tronc en fonction des pixels de la hauteur de l'ecran
    longBande=a*0.05*p          #longueur du tronc en fonction des pixels de la hauteur de l'ecran

    #dessiner le tronc
    dessineRect(4,largBande,longBande,x+(lCote/2)-(largBande/2),y-longBande,"brown")

    #dessiner le sapin
    up()                        #lever turtle
    goto(x,y)                   #aller en (x,y)
    down()                      #poser turtle
    begin_fill()                #commencer de tout colorier
    dessinePolygone(3,lCote,x,y,couleur)                #faire un triangle
    dessinePolygone(3,lCote,x,y+(lCote/4),couleur)      #faire une deuxième triangle
    dessinePolygone(3,lCote,x,y+(lCote/2),couleur)      #faire un troisième triangle
    end_fill()                  #finir de tout colorier
    
    update()
