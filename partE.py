import pickle
import turtle as tl

###################################################################################################################
############################### Partie E : Comparaison des scores et temps de jeu #################################
###################################################################################################################

def sauvScore(joueur: str, nbDisques: int, nbCoups: int, temps: float):
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

def reflexionMoy() -> dict:
    """Récupère les scores et renvoie le temps moyen de réflexion par coup et par joueur"""
    
    with open("data","rb") as data:
        scores = pickle.load(data)
    
    tempsMoy = {}
    
    for joueur in scores:
        for partie in scores[joueur]:
            tempsMoy[joueur] = round(partie[2]/partie[1])
    
    return tempsMoy
            
def afficheScores(nb:int):
    """Affiche un tableau des meilleurs scores selon un nombre de disques donné sur la fenêtre turtle (classement en fonction du nombre de coups)"""
    
def afficheChronos(nb:int):
    """Affiche un tableau des meilleurs scores selon un nombre de disques donné sur la fenêtre turtle (classement en fonction du temps de jeu)"""
    
def afficheReflexMoy(nb:int):
    """Affiche un tableau des meilleurs scores selon un nombre de disques donné sur la fenêtre turtle (classement en fonction du temps de réflexion moyen)"""
