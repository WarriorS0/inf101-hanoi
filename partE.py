import pickle
import turtle as tl

def sauvScore(joueur: str, nbDisques: int, nbCoups: int, temps: int):
    """Stocke les données d'une partie dans le dictionnaire scores (stocké en binaire dans le fichier data)"""

    with open("data", "rb") as data:
        scores = pickle.load(data)

    if joueur in scores:
        scores[joueur].append((nbDisques, nbCoups, temps))
    else:
        scores[joueur] = [(nbDisques, nbCoups, temps)]

    with open("data", "wb") as data:
        pickle.dump(scores, data)

def resetData():
    """ Reset les données du fichier data (dictionnaire vide)"""
    with open("data","wb") as data:
        pickle.dump({}, data)

def afficherTemps():
    """Affiche le temps écoulé en temps réel (depuis le lancement du programme)"""
    tl.up()