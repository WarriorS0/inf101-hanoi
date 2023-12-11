import turtle as tl
from time import *
import doctest
import pickle
import ctypes
import sys
sys.path.append("./Parties/")
from partA import *
from partB import *
from partC import *
from partD import *
from partE import *
from partF import *

# Paramètres fenêtre turtle

user32 = ctypes.windll.user32 
tl.setup(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)) #On récupère les dimensions de l'écrans et on adapte la fenêtre turtle
tl.title("Les tours de Hanoï")
tl.bgcolor("lightgrey")

tl.hideturtle()
souris = tl.Turtle() #Instance de l'objet Turtle permettant de créer les boutons pour la souris

#L'instance créée par défaut est gardée pour le dessin du plateau et des disques à chaque étape

###################################################################################################################
########################################### Panneau de commande Turtle ############################################
###################################################################################################################

def rectangle(L, l):
    souris.down()
    for i in range(2):
        souris.forward(L)
        souris.right(90)
        souris.forward(l)
        souris.right(90)
    souris.up()

souris.hideturtle()
souris.speed(0)
souris.up()
cos_defaut = (-(user32.GetSystemMetrics(0)/2)+100, (user32.GetSystemMetrics(1)/2)-100)
souris.goto(cos_defaut)
rectangle(150,400)
souris.goto(cos_defaut[0]+75, cos_defaut[1]-30)
souris.write("Les tours de Hanoï",align="center", font=("Arial",10,"bold"))
souris.goto(souris.xcor(),souris.ycor()-35)
souris.write("~~~~~~~~~~~~~~",align="center", font=("Arial",10,"bold"))
boutons = ["Tour 0","Tour 1","Tour 2","Annuler","Abandonner","Quitter"]
for i in range(len(boutons)):
    souris.goto(cos_defaut[0]+20,cos_defaut[1]-(i+2)*50)
    print(i,"=",souris.pos())
    rectangle(110, 30)
    souris.goto(souris.xcor()+55, souris.ycor()-24)
    souris.write(boutons[i],align="center", font=("Arial",10, "normal"))
    
# Coordonnées boutons (coin supérieur gauche)
#0 = (-840.00,340.00)
#1 = (-840.00,290.00)
#2 = (-840.00,240.00)
#3 = (-840.00,190.00)
#4 = (-840.00,140.00)
#5 = (-840.00,90.00)

def boutons(x,y):
    if -840 <= x <= -730:
        if 90 >= y >= 60: #Quitter
            tl.clear()
            souris.clear()
            tl.up()
            tl.goto(0,0)
            tl.write("Merci d'avoir joué", align="center", font=("Arial",40,"bold"))
            sleep(2)
            tl.bye()


###################################################################################################################
############################################## Programme principal ################################################
###################################################################################################################

print("Bienvenue dans le jeu : Les tours de Hanoi !")

nb = int(tl.numinput("Les tours de Hanoï","Combien souhaitez-vous de disques en jeu ? ", minval = 1))
#tl.setup((80+(40 + 30 * (nb - 1))*3)*2,(20 + 20 * (nb + 1))*2)

dessinePlateau(nb)
for i in range(nb):
    dessineDisque(i + 1, init(nb), nb)

    
tl.onscreenclick(boutons)

coups, temps, victoire = boucleJeu(init(nb), nb)

if victoire:
    joueur = tl.textinput("Partie gagnée en "+str(coups)+" coup(s) et en "+str(temps)+" secondes !","Quel est votre nom ? ")
    sauvScore(joueur, nb, coups, temps)

sleep(3)
tl.bye()


with open("data", "rb") as data:
    print(pickle.load(data))


doctest.testmod()
tl.mainloop()

"""
resolution(9) 
dessineRes(9)
"""
