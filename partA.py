###################################################################################################################
##################################### Partie A : Plateau de jeu et listes #########################################
###################################################################################################################

def init(n: int) -> list:
    """Renvoie la liste initiale
    >>> init(3)
    [[3, 2, 1], [], []]
    """

    return [[i for i in range(n, 0, -1)], [], []]


def nbDisques(plateau: list, numtour: int) -> int:
    """(liste config, num tour) -> nb disques tour
    >>> nbDisques(init(3), 0)
    3
    """

    return len(plateau[numtour])


def disqueSup(plateau: list, numtour: int) -> int:
    """(liste config, num tour) -> num disque supérieur de la tour (-1 si incorrect)
    >>> disqueSup(init(3), 0)
    1
    """

    if nbDisques(plateau, numtour) == 0:
        return -1
    return plateau[numtour][-1]


def posDisque(plateau: list, numdisque: int) -> int:
    """(liste config, num disque) -> position disque (num tour)
    >>> posDisque(init(3), 2)
    0
    """

    for i in range(len(plateau)):
        if numdisque in plateau[i]:
            return i


def verifDep1(plateau: list, nt1: int, nt2: int) -> bool:
    """(liste config, pos1, pos2) -> bool (déplacement possible ou non)
    >>> verifDep1(init(3), 0, 2)
    True
    >>> verifDep1([[3], [2, 1], []], 0, 1)
    False
    """

    if nbDisques(plateau, nt1) != 0 and (
        disqueSup(plateau, nt1) < disqueSup(plateau, nt2)
        or nbDisques(plateau, nt2) == 0
    ):
        return True
    return False


def verifVictoire(plateau: list, n: int) -> bool:
    """(liste config, nb disques) -> bool (victoire)
    >>> verifVictoire([[], [], [3, 2, 1]], 3)
    True
    """

    return plateau == [[], [], [i for i in range(n, 0, -1)]]
