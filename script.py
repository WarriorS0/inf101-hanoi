import turtle as tl
from time import *
import doctest
import pickle
import ctypes
from partA import *
from partB import *
from partC import *
from partD import *
from partE import *
from partF import *

# Paramètres fenêtre turtle

user32 = ctypes.windll.user32 
tl.setup(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
tl.title("Les tours de Hanoï")
tl.bgcolor("lightgrey")

###################################################################################################################
############################################## Programme principal ################################################
###################################################################################################################

tl.hideturtle()
print("Bienvenue dans le jeu : Les tours de Hanoi !")
verifType = False

nb = int(tl.numinput("Les tours de Hanoï","Combien souhaitez-vous de disques en jeu ? ", minval = 1))

dessinePlateau(nb)
for i in range(nb):
    dessineDisque(i + 1, init(nb), nb)
coups, temps, victoire = boucleJeu(init(nb), nb)

if victoire:
    joueur = tl.textinput("Partie gagnée en "+str(coups)+" coups et en "+str(temps)+" secondes !","Quel est votre nom ? ")
    sauvScore(joueur, nb, coups, temps)

tl.bye()

with open("data", "rb") as data:
    print(pickle.load(data))


doctest.testmod()

"""
resolution(9) 
dessineRes(9)
"""
