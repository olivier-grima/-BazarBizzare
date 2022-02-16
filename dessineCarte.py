from turtle import*
from sapin import*
from boule import*
from cadeau import*
from etoile import*
from bonhomme import*
hauteur=0.40*window_height()
largeur=0.18*window_height()

def dessineCarte(carte,o,c):
    if carte[0][0]==0:
        sapin(0.8,-0.45*hauteur,0.37*largeur,c[carte[0][1]])
    elif carte[0][0]==1:
        boule(0.84,-0.3*hauteur,0.25*largeur,c[carte[0][1]])
    elif carte[0][0]==2:
        etoile(0.75,-0.533*hauteur,0.85*largeur,c[carte[0][1]])
    elif carte[0][0]==3:
        bonhommeNeige(0.5,-0.3*hauteur,0.2*largeur,c[carte[0][1]])
    elif carte[0][0]==4:
        cadeau(0.7,-0.475*hauteur,0.3*largeur,c[carte[0][1]])


    if carte[1][0]==0:
        sapin(0.8,0.15*hauteur,0.37*largeur,c[carte[1][1]])
    if carte[1][0]==1:
        boule(0.84,0.3*hauteur,0.25*largeur,c[carte[1][1]])
    if carte[1][0]==2:
        etoile(0.75,0.067*hauteur,0.85*largeur,c[carte[1][1]])
    if carte[1][0]==3:
        bonhommeNeige(0.5,0.3*hauteur,0.2*largeur,c[carte[1][1]])
    if carte[1][0]==4:
        cadeau(0.7,0.126*hauteur,0.3*largeur,c[carte[1][1]])
    
