from turtle import*
from dessineRect import*

def boule(p,x,y,couleur):   #boule(1,0,0,"crimson")
    hideturtle()            #cacher le pointeur
    tracer(0)               #dessiner instantanément
    pensize(0)
    #variables
    a=window_height()       #nombre de pixel sur la hauteur de l'écran
    r=a*0.09*p              #rayon de la boule
    longAttache=a*0.02*p    #longueur de l'attache en fonction du nb de pixels de la hauteur de l'ecran
    largAttache=a*0.02*p    #largeur de l'attache en fonction du nb de pixels de la hauteur de l'ecran
    largBoucle=a*0.0125*p   #largeur de la boucle en fonction du nb de pixels de la hauteur de l'ecran
    
    #dessiner boule
    up()                    #lever turtle
    goto(x,y)               #aller sur (x,y)
    down()                  #poser turtle
    color(couleur)          #utiliser la couleur "crimson"
    begin_fill()            #commencer de tout colorier
    circle(r)               #dessiner un cercle de rayon r
    end_fill()              #finir de tout colorier

    #dessiner attache
    up()                    #lever turtle             
    goto(x-(largAttache/2),y+(2*r))
    down()                  #poser turtle
    color("goldenrod")      #utiliser la couleur "goldenrod
    forward(longAttache)    #faire un rectangle pour la boucle de l'accroche
    left(90)
    forward(largAttache)
    left(90)
    forward(longAttache)
    left(90)
    forward(largAttache)
    left(90)

    dessineRect(4,longAttache,largBoucle,x-(largAttache/2),y+(2*r),"goldenrod")
