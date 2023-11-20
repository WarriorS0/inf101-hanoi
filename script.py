import turtle as tl
from time import *
import doctest

###################################################################################################################
################################################### Partie A ######################################################
###################################################################################################################


def init(n):
    """(nb disques) -> liste initiale"""
    return [[i for i in range(n, 0, -1)], [], []]


def nbDisques(plateau, numtour):
    """(liste config, num tour) -> nb disques tour"""
    return len(plateau[numtour])


def disqueSup(plateau, numtour):
    """(liste config, num tour) -> num disque supérieur de la tour (-1 si incorrect)"""
    if nbDisques(plateau, numtour) == 0:
        return -1
    return plateau[numtour][-1]


def posDisque(plateau, numdisque):
    """(liste config, num disque) -> position disque (num tour)"""
    for i in range(len(plateau)):
        if numdisque in plateau[i]:
            return i


def verifDep1(plateau, nt1, nt2):
    """(liste config, pos1, pos2) -> bool (déplacement possible ou non)"""
    if nbDisques(plateau, nt1) != 0 and (
        disqueSup(plateau, nt1) < disqueSup(plateau, nt2)
        or nbDisques(plateau, nt2) == 0
    ):
        return True
    return False


def verifVictoire(plateau, n):
    """(liste config, nb disques) -> bool (victoire)"""
    return plateau == [[], [], [i for i in range(n, 0, -1)]]


###################################################################################################################
################################################### Partie B ######################################################
###################################################################################################################

tl.speed(0)


def dessinePlateau(n):
    """(nb disques) ->"""
    """ Dessine le plateau de jeu vide pouvant recevoir n disques """
    tl.color("black")
    diametre_grandDisque = 40 + 30 * (n - 1)
    tl.up()
    tl.goto(-300, -200)
    tl.down()
    # Base du plateau
    for i in range(2):
        tl.forward(80 + diametre_grandDisque * 3)
        tl.right(90)
        tl.forward(20)
        tl.right(90)
    # Tours
    for i in range(3):
        tl.forward(20 + diametre_grandDisque / 2 - 3)
        tl.left(90)
        tl.forward(20 * (n + 1))
        tl.right(90)
        tl.forward(6)
        tl.right(90)
        tl.forward(20 * (n + 1))
        tl.left(90)
        tl.forward(diametre_grandDisque / 2 - 3)


def dessineDisque(nd, plateau, n):
    """(num Disque, liste config, nb disques) ->"""
    """ Trouve les coordonnées du disque nd et le dessine """
    tl.up()
    cos_defaut = (-300, -200)
    tl.goto(cos_defaut)
    tour_disque = posDisque(plateau, nd)
    ind_disque = None
    for i in range(len(plateau[tour_disque])):
        if plateau[tour_disque][i] == nd:
            ind_disque = i
    tour_disque += 1
    tl.goto(
        cos_defaut[0]
        + 20 * tour_disque
        + (40 + 30 * (n - 1)) * (tour_disque - 1)
        + 15 * (n - nd),
        cos_defaut[1] + 20 * (ind_disque+1),
    )
    tl.down()
    tl.color("black")
    tl.fillcolor("grey")
    tl.begin_fill()
    for i in range(2):
        tl.forward(40 + 30 * (nd - 1))
        tl.right(90)
        tl.forward(20)
        tl.right(90)
    tl.end_fill()


def effaceDisque(nd, plateau, n):
    """(num Disque, liste config, nb disques) ->"""
    """ Trouve les coordonnées du disque nd et l'efface """
    tl.up()
    cos_defaut = (-300, -200)
    tl.goto(cos_defaut)
    tour_disque = posDisque(plateau, nd)
    ind_disque = None
    for i in range(len(plateau[tour_disque])):
        if plateau[tour_disque][i] == nd:
            ind_disque = i
    tour_disque += 1
    tl.goto(
        cos_defaut[0]
        + 20 * tour_disque
        + (40 + 30 * (n - 1)) * (tour_disque - 1)
        + 15 * (n - nd),
        cos_defaut[1] + 20 * (ind_disque + 1),
    )
    tl.down()
    tl.color("white")
    tl.fillcolor("white")
    tl.begin_fill()
    for i in range(2):
        tl.forward(40 + 30 * (nd - 1))
        tl.right(90)
        tl.forward(20)
        tl.right(90)
    tl.end_fill()
    tl.up()
    tl.goto(tl.pos()[0], tl.pos()[1] - 20)
    tl.color("black")
    tl.down()
    tl.forward((40 + 30 * (nd - 1)) / 2 - 3)
    tl.left(90)
    tl.forward(20)
    tl.backward(20)
    tl.right(90)
    tl.forward(6)
    tl.left(90)
    tl.forward(20)
    tl.backward(20)
    tl.right(90)
    tl.forward((40 + 30 * (nd - 1)) / 2 - 3)


def effaceTout(plateau, n):
    """(liste config, nb disques) ->"""
    """ Efface tous les disques """
    for i in range(1, n + 1):
        effaceDisque(i, plateau, n)


###################################################################################################################
################################################### Partie C ######################################################
###################################################################################################################


def lireCoords(plateau):
    """(liste config) -> (num tour départ, num tour arrivée)"""

    # ATTENTION : Nous partons du principe que les 3 tours portent les numéros 0, 1 et 2 !
    verif = False
    while not verif:
        tour_dep = int(input("Tour de départ ? "))
        # Existence de la tour
        if not (0 <= tour_dep <= 2):
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
        tour_arr = int(input("Tour d'arrivée ? "))
        if not (0 <= tour_arr <= 2):
            print("Entrée invalide ! Cette tour n'existe pas.")
        elif not (verifDep1(plateau, tour_dep, tour_arr)):
            print("Déplacement impossible.")
        else:
            verif = True

    return (tour_dep, tour_arr)


def jouerUnCoup(plateau, n):
    """(liste config, nb disques) ->"""
    """ Récupère le déplacement du joueur et déplace le disque + modifie la configuration """
    tour_dep, tour_arr = lireCoords(plateau)
    effaceDisque(disqueSup(plateau, tour_dep), plateau, n)
    plateau[tour_arr].append(disqueSup(plateau, tour_dep))
    plateau[tour_dep].pop(-1)
    dessineDisque(disqueSup(plateau, tour_arr), plateau, n)


def boucleJeu(plateau, n):
    """(liste config, nb disques) -> cpt coups"""
    """ Interragit avec l'utilisateur pour déplacer des disques jusqu'à la victoire """
    cpt = 0
    while not verifVictoire(plateau, n):
        jouerUnCoup(plateau, n)
        print(plateau)
        cpt += 1
    return "Bravo, tu as fini en " + str(cpt) + " mouvements !"

###################################################################################################################
################################################### Partie D ######################################################
###################################################################################################################

def dernierCoup(coups):
    """ (dict coups) -> (tour_dep, tour_arr) """
    """ Renvoie le dernier coup joué """
    av_der = coups[len(coups)-2]
    der = coups[len(coups)-1]
    for i in range(3):
        if len(av_der[i]) < len(der[i]):
            tour_dep = i
        elif len(av_der[i]) > len(der[i]):
            tour_arr = i
    return (tour_dep,tour_arr)

def annulerDernierCoup(coups):
    """ (dict coups) -> """
    """ Annule le dernier coups (modifie le dictionnaire) """

###################################################################################################################
############################################## Programme principal ################################################
###################################################################################################################

print("Bienvenue dans le jeu : Les tours de Hanoi !")
nb = int(input("Combien souhaitez-vous de disques en jeu ? "))
while nb <= 0:
    print("Pas possible bro :3")
    nb = int(input("Combien souhaitez-vous de disques en jeu ? "))
dessinePlateau(nb)
for i in range(nb):
    dessineDisque(i + 1, init(nb), nb)
print(boucleJeu(init(nb), nb))
tl.done()
