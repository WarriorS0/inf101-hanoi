import turtle as tl
from partA import *

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
        pos = tl.pos()
        tl.up()
        tl.goto(pos[0]-3, pos[1]-18)
        tl.down()
        tl.write("Tour "+str(i), font=("Arial",10,"bold"), align="center")
        tl.up()
        tl.goto(pos)
        tl.down()
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
    tl.color("lightgrey")
    tl.fillcolor("lightgrey")
    tl.begin_fill()
    #Efface le disque supérieur
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
    tl.forward((40 + 30 * (nd - 1)) / 2 - 2)


def effaceTout(plateau: list, n: int):
    """Efface tous les disques"""

    for i in range(1, n + 1):
        effaceDisque(i, plateau, n)