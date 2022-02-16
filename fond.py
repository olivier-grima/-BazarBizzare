from turtle import*
#from dessinePolygone import*
import turtle
from math import*
import math
from dessineRect import*
from carte import*
from sapin import*
from sapinf import*
from bonhomme import*
from boule import*
from cadeau import*
from etoile import*

scene = turtle.Screen()
scene.setup(width=1.0, height=1.0)
x=-0.5*window_width()
y=-0.15*window_height()
couleurC="deep sky blue"
couleurS="medium sea green"


def fond(xCote,yCote,yCotee,x,y,couleurC,couleurS,tailleC,hauteur,largeur):
    #speed("fastest")
    tracer(0)
    dessineRect(4,xCote,yCote,x,y,couleurC)#dessine le ciel
    right(90)
    dessineRect(4,yCotee,xCote,x,y,couleurS)#dessine le sol 

    
    right(200)
    #on décine les montagnes 
    i=x
    color("gainsboro")
    begin_fill()
    forward(0.5*window_height())
    right(140)
    forward
    forward(0.5*window_height())
    up()
    forward(-0.2*window_height())
    down()
    left(135)
    forward(0.15*window_height())
    right(130)
    forward(0.164*window_height())
    left(65)
    up()
    x=x+2*0.5*window_height()*cos(math.radians(70))
    goto(x,y)
    down()
    left(70)
    forward(0.65*window_height())
    right(140)
    forward(0.65*window_height())
    up()
    forward(-0.3*window_height())
    down()
    left(135)
    forward(0.2*window_height())
    right(130)
    forward(0.51*window_height())
    left(65)
    
    x=x+2.5*0.65*window_height()*cos(math.radians(70))
    

    
#permt de compléter la chaine de montagne en répétant les 3 premières 
    while i<0.5*window_width():
        up()
        goto(x,y)
        left(70)
        down()
        forward(0.5*window_height())
        right(140)
        forward
        forward(0.5*window_height())
        up()
        forward(-0.2*window_height())
        down()
        left(135)
        forward(0.15*window_height())
        right(130)
        forward(0.164*window_height())
        left(65)
        up()
        x=x+2*0.5*window_height()*cos(math.radians(70))
        goto(x,y)
        down()
        left(70)
        forward(0.65*window_height())
        right(140)
        forward(0.65*window_height())
        left(70)
        x=x+2*0.60*window_height()*cos(math.radians(70))
        i=x
    x=-0.5*window_width()
    goto(x,y)
    end_fill()

    #on dessine la neige de la première montagne 
    color("white")
    up()
    x=x+2*0.5*window_height()*cos(math.radians(70))
    goto(x,y)
    left(70)
    forward(0.53*window_height())
    down()
    begin_fill()
    forward(0.12*window_height())
    right(140)
    forward(0.12*window_height())
    right(35)
    forward(0.03*window_height())
    right(135)
    forward(0.03*window_height())
    left(135)
    forward(0.05*window_height())
    right(140)
    forward(0.05*window_height())
    left(135)
    forward(0.03*window_height())
    right(140)
    forward(0.03*window_height())
    end_fill()
    
    #on dessine la neige de la deuxième montagne
    right(110)
    up()
    x=x+2.5*0.65*window_height()*cos(math.radians(70))
    x=x+2*0.5*window_height()*cos(math.radians(70))
    goto(x,y)
    left(70)
    forward(0.53*window_height())
    down()
    begin_fill()
    forward(0.12*window_height())
    right(140)
    forward(0.12*window_height())
    right(35)
    forward(0.03*window_height())
    right(135)
    forward(0.03*window_height())
    left(135)
    forward(0.05*window_height())
    right(140)
    forward(0.05*window_height())
    left(135)
    forward(0.03*window_height())
    right(140)
    forward(0.03*window_height())
    end_fill()

    #on dessine la neige de la troisième montagne
    right(110)
    up()
    x=x+2*0.60*window_height()*cos(math.radians(70))
    x=x+2*0.5*window_height()*cos(math.radians(70))
    goto(x,y)
    left(70)
    forward(0.53*window_height())
    down()
    begin_fill()
    forward(0.12*window_height())
    right(140)
    forward(0.12*window_height())
    right(35)
    forward(0.03*window_height())
    right(135)
    forward(0.03*window_height())
    left(135)
    forward(0.05*window_height())
    right(140)
    forward(0.05*window_height())
    left(135)
    forward(0.03*window_height())
    right(140)
    forward(0.03*window_height())
    end_fill()

    #on déssine la carte
    up()
    left(250)
    s=0
    ps=-0.47*window_width()
    while s<window_width()-150:
        sapinf(0.47,-0.47*window_width()+s,-0.15*window_height(),"dark green","green","forest green")
        s=s+0.041*window_width()
    s2=0
    while s2<window_width():
        sapinf(0.60,-0.445*window_width()+s2,-0.17*window_height(),"dark green","green","forest green")
        s2=s2+0.06*window_width()

    #on place les pions sur le fond
    sapin(0.8,-0.37*window_width(),-0.36*window_height(),"sea green")
    boule(0.84,-0.18*window_width(),-0.4*window_height(),"crimson")
    etoile(0.8,-0.065*window_width(),-0.28*window_height(),"gold")
    cadeau(0.7,0.28*window_width(),-0.4*window_height(),"royal blue")
    bonhommeNeige(0.5,0.15*window_width(),-0.4*window_height(),"white smoke")
    






    up()
    goto((0.40*window_height())/2,0.01*window_height())
    down()
    color("ivory")
    begin_fill()
    carte(tailleC,hauteur,largeur)
    end_fill()
    goto((0.96*(0.40*window_height()))/2,0.018*window_height())
    #color("white")
    pensize(5)
    pencolor("black")
    carte(tailleC,0.96*hauteur,0.92*largeur)

 
