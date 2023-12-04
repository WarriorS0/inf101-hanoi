import turtle as tl
from time import *
import doctest
from pickle import *

###################################################################################################################
################################################### Partie A ######################################################
###################################################################################################################


def init(n: int) -> list:
    """Renvoie la liste initiale
    >>> init(3)
    [[3,2,1], [], []]
    """
    return [[i for i in range(n, 0, -1)], [], []]


def nbDisques(plateau: list, numtour: int) -> int:
    """(liste config, num tour) -> nb disques tour"""
    return len(plateau[numtour])


def disqueSup(plateau: list, numtour: int) -> int:
    """(liste config, num tour) -> num disque supérieur de la tour (-1 si incorrect)"""
    if nbDisques(plateau, numtour) == 0:
        return -1
    return plateau[numtour][-1]


def posDisque(plateau: list, numdisque: int) -> int:
    """(liste config, num disque) -> position disque (num tour)"""
    for i in range(len(plateau)):
        if numdisque in plateau[i]:
            return i


def verifDep1(plateau: list, nt1: int, nt2: int) -> bool:
    """(liste config, pos1, pos2) -> bool (déplacement possible ou non)"""
    if nbDisques(plateau, nt1) != 0 and (
        disqueSup(plateau, nt1) < disqueSup(plateau, nt2)
        or nbDisques(plateau, nt2) == 0
    ):
        return True
    return False


def verifVictoire(plateau: list, n: int) -> bool:
    """(liste config, nb disques) -> bool (victoire)"""
    return plateau == [[], [], [i for i in range(n, 0, -1)]]


###################################################################################################################
################################################### Partie B ######################################################
###################################################################################################################

tl.speed(0)


def dessinePlateau(n: int):
    """Dessine le plateau de jeu vide pouvant recevoir n disques"""
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


def dessineDisque(nd: int, plateau: list, n: int):
    """Trouve les coordonnées du disque nd et le dessine"""
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
    tl.color("black")
    tl.fillcolor("grey")
    tl.begin_fill()
    for i in range(2):
        tl.forward(40 + 30 * (nd - 1))
        tl.right(90)
        tl.forward(20)
        tl.right(90)
    tl.end_fill()


def effaceDisque(nd: int, plateau: list, n: int):
    """Trouve les coordonnées du disque nd et l'efface"""
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


def effaceTout(plateau: list, n: int):
    """Efface tous les disques"""
    for i in range(1, n + 1):
        effaceDisque(i, plateau, n)


###################################################################################################################
################################################### Partie C ######################################################
###################################################################################################################


def lireCoords(plateau: list) -> tuple[int, int]:
    # ATTENTION : Nous partons du principe que les 3 tours portent les numéros 0, 1 et 2 !
    verif = False
    while not verif:
        tour_dep = input("Tour de départ ? ")
        # Existence de la tour
        if tour_dep not in ["0","1","2"]:
            print("Entrée invalide ! Cette tour n'existe pas.")
        # Verif tour vide ou non
        elif len(plateau[int(tour_dep)]) == 0:
            print("Entrée invalide ! Tour vide.")

        else:
            # Vérif mvt possibles ou non
            tour_dep = int(tour_dep)
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
        tour_arr = input("Tour d'arrivée ? ")
        if tour_arr not in ["0","1","2"]:
            print("Entrée invalide ! Cette tour n'existe pas.")
        elif not (verifDep1(plateau, tour_dep, int(tour_arr))):
            print("Déplacement impossible.")
        else:
            verif = True
            tour_arr = int(tour_arr)

    return (tour_dep, tour_arr)


def jouerUnCoup(plateau: list, n: int):
    """Récupère le déplacement du joueur et déplace le disque + modifie la configuration"""
    tour_dep, tour_arr = lireCoords(plateau)
    effaceDisque(disqueSup(plateau, tour_dep), plateau, n)
    plateau[tour_arr].append(disqueSup(plateau, tour_dep))
    plateau[tour_dep].pop(-1)
    dessineDisque(disqueSup(plateau, tour_arr), plateau, n)


def boucleJeu(plateau: list, n: int) -> int:
    """Interragit avec l'utilisateur pour déplacer des disques jusqu'à la victoire"""
    global cpt
    temps1 = time()
    cpt = 0
    coups = {0: init(nb)}
    while not verifVictoire(plateau, n):
        jouerUnCoup(plateau, n)
        cpt += 1
        coups[cpt] = plateau
        if not verifVictoire(plateau, n):
            annulation = input(
                'Si vous souhaitez annuler votre dernier coup, tapez "cancel" ! '
            )
        if annulation == "cancel":
            annulerDernierCoup(coups)
            plateau = coups[cpt]
    temps2 = time()
    return "Bravo, tu as fini en " + str(cpt) + " mouvements et en " + str(int(temps2-temps1)) + " secondes !"


###################################################################################################################
################################################### Partie D ######################################################
###################################################################################################################


def dernierCoup(coups: dict) -> tuple[int, int]:
    """Renvoie le dernier coup joué"""
    av_der = coups[len(coups) - 2]
    der = coups[len(coups) - 1]
    for i in range(3):
        if len(av_der[i]) < len(der[i]):
            tour_dep = i
        elif len(av_der[i]) > len(der[i]):
            tour_arr = i
    return (tour_dep, tour_arr)


def annulerDernierCoup(coups: dict):
    """Annule le dernier coups (modifie le dictionnaire)"""
    dep, arr = dernierCoup(coups)
    global cpt
    effaceDisque(coups[cpt][arr][-1], coups[cpt], len(coups[0][0]))
    del coups[cpt]
    cpt -= 1
    print(coups[cpt][dep])
    dessineDisque(coups[cpt][dep][-1], coups[cpt], len(coups[0][0]))


###################################################################################################################
################################################### Partie E ######################################################
###################################################################################################################


def sauvScore(joueur: str, nbDisques: int, nbCoups: int, temps: int):
    if joueur in scores:
        scores[joueur].append((nbDisques, nbCoups, temps))
    else:
        scores[joueur] = [(nbDisques, nbCoups, temps)]


###################################################################################################################
############################################## Programme principal ################################################
###################################################################################################################

tl.hideturtle()
print("Bienvenue dans le jeu : Les tours de Hanoi !")
verifType = False
# Vérification du type de valeur -> erreur du int renvoie au except
# Et vérification que nb > 0

while not verifType:
    try:
        nb = int(input("Combien souhaitez-vous de disques en jeu ? "))
        if nb <= 0:
            print("Nombre impossible !")
        else:
            verifType = True
    except:
        print("Valeur impossible !")

dessinePlateau(nb)
for i in range(nb):
    dessineDisque(i + 1, init(nb), nb)
print(boucleJeu(init(nb), nb))
tl.done()

scores = {}

doctest.testmod()
