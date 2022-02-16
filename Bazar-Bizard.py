#Binôme : GRIMA-GOSSELIN


#on importe les modules
import random
import time
from random import randrange
from fond import*
from dessineCarte import*
from turtle import*
from dessineRect import*

o=["Sapin","Boule","Etoile","Bonhomme de Neige","Cadeau"]    #défini la liste des objets 
c=["sea green","crimson","gold","white smoke","royal blue"]           #défini la liste des couleurs 

tailleC=1





def pionListe (o,c):    #on définit la liste des pions à l'aide des listes o et c
    pion0=[o.index("Sapin"),c.index("sea green")]
    pion1=[o.index("Boule"),c.index("crimson")]
    pion2=[o.index("Etoile"),c.index("gold")]
    pion3=[o.index("Bonhomme de Neige"),c.index("white smoke")]
    pion4=[o.index("Cadeau"),c.index("royal blue")]
    listePion=[pion0,pion1,pion2,pion3,pion4]
    return (listePion)

#Fonction qui tire une carte aléatoirement

def cartealeatoire(o,c):
    obj1=random.choice(o)        #tire de manière aléatoire l'objet 1 de la carte 
    col1=random.choice(c)        #tire de manière aléatoire la couleur 1 de la carte
    perso1=[o.index(obj1),c.index(col1)]        #on créer le perso 1 de la carte

    obj2=random.choice(o)       #tire de manière aléatoire l'objet 2 de la carte dans la liste o
    col2=random.choice(c)        #tire de manière aléatoire la couleur 2 de la carte dans la liste c
    while o.index(obj1)==o.index(obj2) or (o.index(obj2)==c.index(col2) and o.index(obj1)==c.index(col1)) or c.index(col1)==c.index(col2) or c.index(col1)==o.index(obj2) or o.index(obj1)==c.index(col2):
        obj2=random.choice(o)        #tire de manière aléatoire l'objet 2 de la carte dans la liste o
        col2=random.choice(c)        #tire de manière aléatoire la couleur 2 de la carte dans la liste c
    perso2=[o.index(obj2),c.index(col2)]
    
    carte=[perso1,perso2]       #on créer la carte avec les deux perso que l'on vient de créer
    return(carte)               

def bonneRep(carte,o,c):  #fonction qui calcule le pion à sélectionner pour gagner
    listePion=pionListe(o,c)
    cartealeatoire(o,c)
    if carte[0]in listePion:    #si le perso1 correspond à un des pions on assigne à la variable rep ce pion
        pion=carte[0][0]
        rep=[o[pion],c[pion]]
        return (rep)            #renvoie la valeur de rep
    elif carte[1] in listePion: #si le perso2 correspond à un des pions on assigne à la variable rep ce pion
        pion=carte[1][0]
        rep=[o[pion],c[pion]]
        return(rep)
    elif carte[0] not in listePion and carte[1] not in listePion: #on cherche le pion manquan celui qui ne possède ni les couleurs ni les formes présentent sur la carte
        total=carte[0][0]+carte[0][1]+carte[1][0]+carte[1][1]   

        if total==10:
            rep=[o[0],c[0]]
        elif total==9:
            rep=[o[1],c[1]]
        elif total==8:
            rep=[o[2],c[2]]
        elif total==7:
            rep=[o[3],c[3]]
        elif total==6:
            rep=[o[4],c[4]]
        return rep

def choixPion(choix,o,c):   #assigne le numéro du pion choisi par le joueur à sa vrai valeur
    listePion=pionListe(o,c)
    if choix==0:
        choix=[o[0],c[0]]
    elif choix==1:
        choix=[o[1],c[1]]
    elif choix==2:
        choix=[o[2],c[2]]
    elif choix==3:
        choix=[o[3],c[3]]
    elif choix==4:
        choix=[o[4],c[4]]
    return choix
    
    


#Début du programme :

fond(window_width(),0.65*window_height(),0.35*window_height(),x,y,couleurC,couleurS,1,0.40*window_height(),0.18*window_height())
update()

jouer=textinput("JEU","Voulez vous jouer (o/n) ? ")
score=0

while jouer=="o":

#on dessine à nouveau la carte pour effacer la précédente
    up()
    goto((0.40*window_height())/2,0.01*window_height())
    down()
    color("ivory")
    begin_fill()
    carte(tailleC,hauteur,largeur)
    end_fill()
    goto((0.96*(0.40*window_height()))/2,0.018*window_height())
    pensize(5)
    pencolor("black")
    carte(tailleC,0.96*hauteur,0.92*largeur)

    Carte=cartealeatoire(o,c)       #on tire la carte
    dessineCarte(Carte,o,c)         #on affiche les pions tirés 
    up()
    t1=time.time()      #récupérer la temps actuel au moment où on découvre la carte
    choix = numinput("Votre Choix","Quel pion choisissez vous ? (les pions sont numérotés de 0 à 4)",0,0,4)
    t2=time.time()      #récupérer le temps actuel au moment où l'on a entrée la réponse
    
    choix=choixPion(choix,o,c)
    
    t=t2-t1             #t est la variable qui correspond au temps mis à choisir un pion
    
    if choix==bonneRep(Carte,o,c):      #nombre de pionts donnés en focnction du temps de réponse
       
        if t<5:
            score=score+1
           
        elif t>=5 and t<10:
            score=score+(3/4)
            
        elif t>=10 and t<15:
            score=score+(1/2)
            
        elif t>=15 and t<20:
            score=score+(1/4)
            
        elif t>=20:
            score=score
           
    else:
        score=score     #Si la réponse n'est pas la bonne on ne gagne pas de point

    
    goto(0.4*window_width(),-0.4*window_height())
    color("white")
    write("Score :",font=("Arial",20,"normal"))         #affichage du texte score
    dessineRect(4,0.2*window_width(),0.1*window_height(),0.434*window_width(),-0.4*window_height(),"medium sea green")  #permet de cacher le précedents score pour ne pas qu'il se suporpose avec le suivant 
    up()
    color("white")
    goto(0.445*window_width(),-0.4*window_height())
    write(score,align="left",font=("Arial",20,"normal"))    #affiche le score du joueur

    jouer=textinput("JEU","Voulez vous jouer (o/n) ? ") #relance la boucle si le jour entre "o"
    update()


#on dessine denouveau une carte pour cacher les pions et afficher le texte de fin       
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
up()

#on affiche le texte de fin
goto(-0.3*hauteur,0.85*largeur)
write("Fin de la partie",font=("Arial",30,"normal"))
goto(-0.38*hauteur,0.6*largeur)
write("Votre score est de :",font=("Arial",30,"normal"))
goto(0,0.35*largeur)
write(score,align="center",font=("Arial",30,"normal"))
update()


