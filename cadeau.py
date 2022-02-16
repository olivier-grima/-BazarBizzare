from turtle import*
from dessinePolygone import*
from dessineRect import*

def cadeau(p,x,y,couleur):          #cadeau(1,0,0,"royal blue")
    hideturtle()                    #cacher le pointeur
    tracer(0)                       #dessiner instantanément
    pensize(0)
    
    #variables
    a=window_height()               #nombre de pixel sur la hauteur de l'écran
    lCote=a*0.2*p                   #longueur cote en fonction du nb de pixels de la hauteur de l'ecran
    lBande=lCote/4                  #définir la largeur de la bande sur le cadeau en foncton de lCote

    #dessiner la carré qi forme le cadeau
    up()                            #lever turtle
    goto(x,y)                       #se déplacer sur les coordonnées (x,y)
    down()                          #poser turtle
    color(couleur)                 #utiliser la couleur du cadeau "royal blue"
    begin_fill()                    #commencer de tout colorier
    dessinePolygone(4,lCote,x,y,couleur)   #utiliser la fonction dessinePolygone pour tracer un carré
    end_fill()                      #finir de tout colorier en "royal blue"

    #dessiner la bande horizontale
    dessineRect(4,lCote+0.1*lCote,lBande,x-0.05*lCote,y+lCote-lBande,couleur)
    setheading(0)
    dessineRect(4,lCote+0.1*lCote,0.025*lCote,x-0.05*lCote,lCote-lBande-0.025*lCote+y,"medium blue")
    
    #dessiner la bande verticale
    dessineRect(4,lBande,lCote,x+(lCote/2)-(lBande/2),y,"midnight blue")
    setheading(0)

    
    
    update()
