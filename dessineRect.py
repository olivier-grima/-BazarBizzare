from turtle import*
def dessineRect(nbCote,xCote,yCote,px,py,couleur):
    color(couleur)
    begin_fill()
    up()
    goto(px,py)
    down()

    i=0
    a=360/nbCote
    while i<nbCote:
        forward(xCote)
        left(a)
        forward(yCote)
        left(a)
        i=i+2
    end_fill()
