from turtle import*
def carte(tailleC,hauteur,largeur):
    compteur = 0
    while compteur < 45:
            forward(tailleC)
            left(2)
            compteur+= 1
    forward(largeur)
    while compteur < 90:
        forward(tailleC)
        left(2)
        compteur+= 1
    forward(hauteur)
    while compteur < 135:
        forward(tailleC)
        left(2)
        compteur+= 1
    forward(largeur)
    while compteur < 180:
        forward(tailleC)
        left(2)
        compteur+= 1
    forward(hauteur)
