from turtle import*

def etoile(p,x,y,couleur):  #etoile(1,0,0,"gold")
    hideturtle()            #cacher le pointeur
    tracer(0)               #dessiner instantanément
    pensize(0)

    #variables
    a=window_height()       #nombre de pixel sur la hauteur de l'écran
    lCote=a*0.25*p          #longueur d'un cote de l'etoile en fonction du nombre de pixels de l'ecran

    #dessiner etoile
    up()                    #lever turtle
    goto(x,y)               #placer turtle sur les coordonnées (x,y)
    down()                  #poser turtle
    color(couleur)          #utiliser la couleur "gold" pour l'étoile
    begin_fill()            #commencer ce que l'on veut colorier
    right(36)               #tourner à droite de 36°
    i=0
    while i<5:              #il y a 5 cote qui forme une étoile
        forward(lCote)      #se déplacer de la longueur lCote
        left(144)           #tourner à gauche de 144°
        i=i+1
    end_fill()              #finir de tout colorier en "gold"
    left(36)                #tourner à gauche de 36° afin de retrouver turtle dans son orientation de base(horizontalement et dirigé vers la droite)
    update()
