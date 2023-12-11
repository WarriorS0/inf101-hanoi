import turtle as tl
from time import *
import sys
sys.path.append("../")
from script import boutons
from partA import *
from partB import *
from partD import *
import pickle

###################################################################################################################
################################### Partie C : Interactions avec le joueur ########################################
###################################################################################################################

def lireCoords(plateau: list) -> tuple[int, int]:
    """Demande des coordonnées de déplacement et vérifie si le mouvement est possible avant de le renvoyer"""

    # ATTENTION : Nous partons du principe que les 3 tours portent les numéros 0, 1 et 2 !

    verif = False
    while not verif:
        tour_dep = int(tl.numinput("Tour de départ"," Veuillez rentrer la tour de départ ? "))
        # Existence de la tour
        if tour_dep not in [0, 1, 2]:
            print("Entrée invalide ! Cette tour n'existe pas.")
        # Verif tour vide ou non
        elif len(plateau[tour_dep]) == 0:
            print("Entrée invalide ! Tour vide.")

        else:
            # Vérif mvt possibles ou non
            if (
                verifDep1(plateau, tour_dep, 0)
                or verifDep1(plateau, tour_dep, 1)
                or verifDep1(plateau, tour_dep, 2)
            ):
                verif = True
            else:
                print("Aucun mouvement possible. Veuillez choisir une autre tour.")

    verif = False
    while not verif:
        tour_arr = int(tl.numinput("Tour d'arrivée"," Veuillez rentrer la tour d'arrivée ?"))
        if tour_arr not in [0, 1, 2]:
            print("Entrée invalide ! Cette tour n'existe pas.")
        elif not (verifDep1(plateau, tour_dep, tour_arr)):
            print("Déplacement impossible.")
        else:
            verif = True

    return (tour_dep, tour_arr)


def jouerUnCoup(plateau: list, n: int):
    """Récupère le déplacement du joueur et déplace le disque + modifie la configuration"""

    tour_dep, tour_arr = lireCoords(plateau)
    effaceDisque(disqueSup(plateau, tour_dep), plateau, n)
    plateau[tour_arr].append(disqueSup(plateau, tour_dep))
    plateau[tour_dep].pop(-1)
    dessineDisque(disqueSup(plateau, tour_arr), plateau, n)


def boucleJeu(plateau: list, n: int) -> tuple[int, float, bool]:
    """Interragit avec l'utilisateur pour déplacer des disques jusqu'à la victoire"""
    
    temps1 = time()
    
    with open("cpt","wb") as cptFile:
        pickle.dump(0, cptFile)
    cpt = 0
    
    coups = {0: init(n)}
    while not verifVictoire(plateau, n):
        jouerUnCoup(plateau, n)
        cpt += 1
        with open("cpt","wb") as cptFile:
            pickle.dump(cpt, cptFile)
            
        coups[cpt] = plateau
            
    temps2 = time()
    print(
        "Bravo, tu as fini en "
        + str(cpt)
        + " mouvements et en "
        + str(round(temps2 - temps1,1))
        + " secondes !"
    )
    return cpt, round(temps2 - temps1,1), True
