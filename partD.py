from partB import *

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