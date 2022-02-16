from turtle import*
from math import*
from dessinePolygone import*
from dessineRect import*

def bonhommeNeige(p,x,y,couleur): #bonhommeNeige(1,0,0,"light gray")
    hideturtle()                #cacher le pointeur
    tracer(0)                   #dessiner instantanément
    pensize(5)
    #variables
    a=window_height()           #nombre de pixel sur la hauteur de l'écran
    r1=a*0.085*p                #rayon du premier cercle
    r2=r1/(1.5)                 #rayron du deuxième cercle


    #dessiner bras gauche
    left(150)                   #donner une inclinaisaon de 150° sur la gauche au bras
    dessineRect(4,r1,(r2/8),-((3*r2)/4)+x,2*r2+y,"sienna")
    setheading(0)               #remettre le pointeur horizontal et dirigé vers la droite
    
    #dessiner bras droit
    left(30)                    #donner une inclinaison de 30° au bras droit
    dessineRect(4,r1,(r2/8),((3*r2)/4)+x,2*r2+y,"sienna")
    setheading(0)               #remettre le pointeur horizontal et dirigé vers la droite

    #dessiner le premier cercle (celui du bas)
    up()                        #lever turtle
    goto(x,y)                   #placer turtle sur les coordonnées (x,y)
    down()                      #poser turtle
    color(couleur)              #utiliser la couleur "light gray" pour les cercles
    begin_fill()                #démarer de tout colorier
    circle(r1)                  #tracer un cercle de rayon r1

    #dessiner le deuxième cercle
    up()                        #lever turtle
    goto(x,(2*r1)-(r2/4)+y)       #pour tracer le deuxième cercle il faut etre au dessus du premier cercle (2*r1) mais il faut que les ceux cercles se chevauche de 1/4 du diamètre du deuxième cercle
    down()                      #poser turtle
    color(couleur)
    circle(r2)                  #tracer un cercle de rayon r2
    end_fill()                  #fin de colorier les deux cercles en "light gray"

    #dessiner l'oeil gauche
    up()                        #lever turtle
    goto(x-(r2/3),(2*r1)+((14*r2)/15)+y)
    down()                      #poser turtle
    color("black")              #utiliser la couleur "noire"
    begin_fill()                #commencer à colorier en noir
    circle(2)                   #tracer un cercle de rayon 2

    #dessiner l'oeil droit
    up()                        #lever turtle
    goto(x+(r2/3),(2*r1)+((14*r2)/15)+y)
    down()                      #poser turtle
    circle(2)                   #tracer un cercle de rayon 2
    end_fill()                  #finir de tout colorier en noir

    #dessiner bonnet
    color("red")
    begin_fill()
    dessinePolygone(3,r1,-(r1/2)+x,(2*r1)+(1.5*r2)+(r2/8)+y,"red")
    end_fill()

    dessineRect(4,r1,(r2/8),-(r1/2)+x,(2*r1)+(1.5*r2)+y,"alice blue")
    
    up()
    goto(x,(2*r1)+(1.5*r2)+(r2/8)+(0.8*r1)+y)
    down()
    color("alice blue")
    begin_fill()
    circle(12)
    end_fill()
    update()
