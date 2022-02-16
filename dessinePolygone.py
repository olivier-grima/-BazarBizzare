from turtle import*
def dessinePolygone(nbCote,lCote,px,py,couleur):
    color(couleur)
    begin_fill()
    up()
    goto(px,py)
    down()

    i=0
    a=360/nbCote
    while i<nbCote:
        forward(lCote)
        left(a)
        i=i+1
    end_fill()
