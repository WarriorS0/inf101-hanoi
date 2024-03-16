import turtle as tl
from time import *
import doctest
import pickle
import ctypes

# Paramètres fenêtre turtle

user32 = ctypes.windll.user32 
tl.setup(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)) # On récupère les dimensions de l'écrans et on adapte la fenêtre turtle
tl.title("Les tours de Hanoï")
tl.bgcolor("lightgrey")

tl.hideturtle()
souris = tl.Turtle() # Objet Turtle() permettant de créer les boutons pour la souris

# La tortue tl est gardée pour le dessin du plateau et des disques à chaque étape

###################################################################################################################
########################################### Panneau de commande Turtle ############################################
###################################################################################################################

def rectangle(L:int, l:int):
    """ Dessine un rectangle avec l'objet souris de la classe Turtle() """
    
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
souris.write("Contrôles",align="center", font=("Arial",10,"bold"))
souris.goto(souris.xcor(),souris.ycor()-35)
souris.write("~~~~~~~~~~~~~~",align="center", font=("Arial",10,"bold"))
boutons = ["Tour 0","Tour 1","Tour 2","Annuler","Abandonner","Quitter"]
for i in range(len(boutons)):
    souris.goto(cos_defaut[0]+20,cos_defaut[1]-(i+2)*50)
    rectangle(110, 30)
    souris.goto(souris.xcor()+55, souris.ycor()-24)
    souris.write(boutons[i],align="center", font=("Arial",10, "normal"))


screensizeX, screensizeY = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
souris.goto(0, screensizeY/2-180)
souris.write("Les Tours de Hanoï",align="center", font=("Arial",50,"bold"))

def quitter(joueur = ""):
    """ Quitte le programme en affichant un message de remerciement"""
    
    tl.clear()
    souris.clear()
    compteur.clear()
    tl.up()
    tl.goto(0,0)
    tl.write("Merci d'avoir joué "+str(joueur), align="center", font=("Arial",40,"bold"))
    sleep(2)
    tl.bye()

abandon = False

def boutons(x:int, y:int):
    """Fonction trigger par clique, exécute des évènements relatifs aux boutons"""
    
    global abandon
    if -(screensizeX/2)+120 <= x <= (screensizeX/2)+230:
        if (screensizeY/2)-450 >= y >= (screensizeY/2)-480: #Quitter
            quitter()
        elif (screensizeY/2)-400 >= y >= (screensizeY/2)-430 and not abandon: #Abandonner
            abandon = True
            resolution(nb)
            dessineRes(nb)
            quitter()
        elif (screensizeY/2)-350 >= y >= (screensizeY/2)-380 and not abandon: #Annuler
            with open("coups","rb") as coupsF:
                coups = pickle.load(coupsF)
            annulerDernierCoup(coups)
            

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

###################################################################################################################
####################################### Partie B : Graphisme avec Turtle ##########################################
###################################################################################################################

tl.speed(0)

def dessinePlateau(n: int):
    """Dessine le plateau de jeu vide pouvant recevoir n disques"""

    tl.color("black")
    diametre_grandDisque = 40 + 30 * (n - 1)
    tl.up()
    tl.goto(-(diametre_grandDisque*1.5 + 40), -(20*(n+2))/2) #Permet dde centrer le plateau de jeu dans la fenêtre
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
    diametre_grandDisque = 40 + 30 * (n - 1)
    cos_defaut = (-(diametre_grandDisque*1.5 + 40), -(20*(n+2))/2)
    tl.goto(cos_defaut)
    tour_disque = posDisque(plateau, nd)
    ind_disque = None
    for i in range(len(plateau[tour_disque])):
        if plateau[tour_disque][i] == nd:
            ind_disque = i
    tour_disque += 1
    tl.goto(cos_defaut[0] + 20 * tour_disque + (40 + 30 * (n - 1)) * (tour_disque - 1) + 15 * (n - nd), cos_defaut[1] + 20 * (ind_disque + 1))
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
    diametre_grandDisque = 40 + 30 * (n - 1)
    cos_defaut = (-(diametre_grandDisque*1.5 + 40), -(20*(n+2))/2)
    tl.goto(cos_defaut)
    tour_disque = posDisque(plateau, nd)
    ind_disque = None
    for i in range(len(plateau[tour_disque])):
        if plateau[tour_disque][i] == nd:
            ind_disque = i
    tour_disque += 1
    tl.goto(cos_defaut[0] + 20 * tour_disque + (40 + 30 * (n - 1)) * (tour_disque - 1) + 15 * (n - nd), cos_defaut[1] + 20 * (ind_disque + 1))
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

###################################################################################################################
################################### Partie C : Interactions avec le joueur ########################################
###################################################################################################################


def lireCoords(plateau: list, dep:int, arr:int) -> tuple[int, int]:
    """Reçoit 2 tours puis renvoie le déplacement si il est possible, une erreur sinon"""
        
    # ATTENTION : Nous partons du principe que les 3 tours portent les numéros 0, 1 et 2 !
    
    if dep == arr or dep not in[0,1,2] or arr not in [0,1,2] or len(plateau[dep]) == 0 or (len(plateau[arr]) != 0 and disqueSup(plateau,dep) > disqueSup(plateau, arr)):
        user32.MessageBoxW(None, 'Déplacement impossible, recommencez !', 'Tours de Hanoï', 1)
        return -1,-1
    return dep, arr

clics = []

def jouerClic(x:int,y:int):
    """Trigger par clique, récupère les coordonnées d'un clique, en déduit un bouton renvoyant à une tour et engageg un déplacement si il est possible"""
    
    if abandon:
        return
    global clics
    if -(screensizeX/2)+120 <= x <= (screensizeX/2)+230:
        if (screensizeY/2)-300 >= y >= (screensizeY/2)-330: #Tour 2
            clics.append(2)
        elif (screensizeY/2)-250 >= y >= (screensizeY/2)-280: #Tour 1
            clics.append(1)
        elif (screensizeY/2)-200 >= y >= (screensizeY/2)-230: #Tour 0
            clics.append(0)
    
    if len(clics) == 2:
        with open("coups","rb") as coupsF:
            coups = pickle.load(coupsF)
        with open("cpt","rb") as cptFile:
            cpt = pickle.load(cptFile)
        
        dep, arr = lireCoords(coups[cpt], clics[0], clics[1])
        if dep == arr == -1:
            clics = []
        else:
            deplacement(coups[cpt], len(coups[0][0]), dep, arr)
            clics = []
    
def deplacement(plateau:list, n:int, tour_dep:int, tour_arr:int):
    """ Effectue le déplacement, s'occupe d'enregistrer les données en cas de victoire et actualise un compteur de coups"""
    
    effaceDisque(disqueSup(plateau, tour_dep), plateau, n)
    plateau[tour_arr].append(disqueSup(plateau, tour_dep))
    plateau[tour_dep].pop(-1)
    dessineDisque(disqueSup(plateau, tour_arr), plateau, n)
    
    with open("cpt","rb") as cptFile:
        cpt = pickle.load(cptFile)
    cpt += 1
    with open("cpt","wb") as cptFile:
        pickle.dump(cpt, cptFile)
    
    compteur.clear()    
    compteur.write("Nombre de coups : "+str(cpt), align="center",font=("Arial",12,"bold"))
        
    with open("coups","rb") as coupsF:
        coups = pickle.load(coupsF)    
    coups[cpt] = plateau
    with open("coups","wb") as coupsF:
        pickle.dump(coups, coupsF)

    if verifVictoire(plateau, n):
        temps2 = time()
        
        temps = round(temps2-temps1,1)
        joueur = tl.textinput("Partie gagnée en "+str(cpt)+" coup(s) et en "+str(temps)+" secondes !","Quel est votre nom ? ")
        while joueur is None or joueur == "":
            joueur = tl.textinput("Partie gagnée en "+str(cpt)+" coup(s) et en "+str(temps)+" secondes !","Veuillez entrer un nom valide !")
        sauvScore(joueur, n, cpt, temps)
        
        quitter(joueur)
        

###################################################################################################################
####################################### Partie D : Annulation de coups ############################################
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
    
    with open("cpt","rb") as cptFile:
        cpt = pickle.load(cptFile)
    
    if cpt == 0:
        user32.MessageBoxW(None, 'Aucun coup à annuler !', 'Tours de Hanoï', 1)
    else:
        arr, dep = dernierCoup(coups)
        effaceDisque(coups[cpt][arr][-1], coups[cpt], len(coups[0][0]))
        del coups[cpt]
        cpt -= 1
        compteur.clear()    
        compteur.write("Nombre de coups : "+str(cpt), align="center",font=("Arial",12,"bold"))
        with open("cpt","wb") as cptFile:
            pickle.dump(cpt, cptFile)
        with open("coups","wb") as coupsF:
            pickle.dump(coups, coupsF)
        print(coups[cpt][dep])
        dessineDisque(coups[cpt][dep][-1], coups[cpt], len(coups[0][0]))


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

def afficheScores(nb:int):
    """Affiche un tableau des meilleurs scores selon un nombre de disques donné sur la fenêtre turtle (classement en fonction du nombre de coups)"""
    
    meilleurs = []
    with open("data","rb") as data:
        scores = pickle.load(data)
    for i in range(3):
        meilleur=(None,None)
        for joueur in scores:
            for partie in scores[joueur]:
                if (joueur, partie[1]) not in meilleurs and partie[0] == nb:
                    if meilleur == (None, None) or (meilleur != (None, None) and partie[1] < meilleur[1]):
                        meilleur = (joueur, partie[1])
        meilleurs.append(meilleur)
        
    cos_classement = (-(screensizeX/2)+100, (screensizeY/2)-550)
    souris.goto(cos_classement)
    rectangle(300, 300)
    souris.goto(souris.xcor()+150, souris.ycor()-35)
    souris.write("Top 3 coups avec "+str(nb)+" disques",align="center", font=("Arial",10,"bold"))
    souris.goto(souris.xcor()-130, souris.ycor())
    for i in range(3):
        souris.goto(souris.xcor(), souris.ycor()-20)
        if meilleurs[i] == (None,None):
            ch = ""
        else:
            ch = meilleurs[i][0]+" : "+str(meilleurs[i][1])+" coups"
        souris.write(str(i+1) + ". " + ch, align="left", font=("Arial",10,"normal"))
    
    
def afficheChronos(nb:int):
    """Affiche un tableau des meilleurs scores selon un nombre de disques donné sur la fenêtre turtle (classement en fonction du temps de jeu)"""
    
    meilleurs = []
    with open("data","rb") as data:
        scores = pickle.load(data)
    for i in range(3):
        meilleur=(None,None)
        for joueur in scores:
            for partie in scores[joueur]:
                if (joueur, partie[2]) not in meilleurs and partie[0] == nb:
                    if meilleur == (None, None) or (meilleur != (None, None) and partie[2] < meilleur[1]):
                        meilleur = (joueur, partie[2])
        meilleurs.append(meilleur)
        
    souris.goto(souris.xcor()+130, souris.ycor()-15)
    souris.write("___________________",align="center", font=("Arial",10,"bold"))
    souris.goto(souris.xcor(), souris.ycor()-20)
    souris.write("Top 3 chronos avec "+str(nb)+" disques",align="center", font=("Arial",10,"bold"))
    souris.goto(souris.xcor()-130, souris.ycor())
    for i in range(3):
        souris.goto(souris.xcor(), souris.ycor()-20)
        if meilleurs[i] == (None,None):
            ch = ""
        else:
            ch = meilleurs[i][0]+" : "+str(meilleurs[i][1])+" secondes"
        souris.write(str(i+1) + ". " + ch, align="left", font=("Arial",10,"normal"))
    
def afficheReflexMoy(nb:int):
    """Affiche un tableau des meilleurs scores selon un nombre de disques donné sur la fenêtre turtle (classement en fonction du temps de réflexion moyen)"""
    
    meilleurs = []
    with open("data","rb") as data:
        scores = pickle.load(data)
    for i in range(3):
        meilleur=(None,None)
        for joueur in scores:
            for partie in scores[joueur]:
                if (joueur, partie[2]/partie[1]) not in meilleurs and partie[0] == nb:
                    if meilleur == (None, None) or (meilleur != (None, None) and partie[2]/partie[1] < meilleur[1]):
                        meilleur = (joueur, partie[2]/partie[1])
        meilleurs.append(meilleur)
        
    souris.goto(souris.xcor()+130, souris.ycor()-15)
    souris.write("___________________",align="center", font=("Arial",10,"bold"))
    souris.goto(souris.xcor(), souris.ycor()-20)
    souris.write("Top 3 tps de réflex. moy. avec "+str(nb)+" disques",align="center", font=("Arial",10,"bold"))
    souris.goto(souris.xcor()-130, souris.ycor())
    for i in range(3):
        souris.goto(souris.xcor(), souris.ycor()-20)
        if meilleurs[i] == (None,None):
            ch = ""
        else:
            ch = meilleurs[i][0]+" : "+str(round(meilleurs[i][1],1))+" secondes/coup"
        souris.write(str(i+1) + ". " + ch, align="left", font=("Arial",10,"normal"))


###################################################################################################################
################################# Partie F : Jeu automatique, fonction récursive ##################################
###################################################################################################################

listeDep = []

def resolution(n: int, dep=0, arr=2, inter=1):
    """Modifie la liste des déplacements afin de résoudre le problème à n disques"""
    
    if n == 1: # Cas de base
        listeDep.append((dep, arr))
    else: # Cas général
        resolution(n - 1, dep, inter, arr)
        listeDep.append((dep, arr))
        resolution(n - 1, inter, arr, dep)

def dessineRes(n:int, dep=listeDep):
    """Joue les dédplacements pour résoudre le problème à n disques"""
    
    tl.clear()
    dessinePlateau(n)
    config = init(n)
    for i in range(n):
        dessineDisque(i+1,config,n)
    compt = 0
    compteur.clear()    
    compteur.write("Nombre de coups (solution) : "+str(compt), align="center",font=("Arial",12,"bold"))
    for e in dep:
        tourDep, tourArr = e
        disque = config[tourDep][-1]
        effaceDisque(disque, config, n)
        config[tourDep].pop(-1)
        config[tourArr].append(disque)
        dessineDisque(disque, config, n)
        compt += 1
        compteur.clear()    
        compteur.write("Nombre de coups (solution) : "+str(compt), align="center",font=("Arial",12,"bold"))
    tl.done()

###################################################################################################################
############################################## Programme principal ################################################
###################################################################################################################

nb = int(tl.numinput("Les tours de Hanoï","Combien souhaitez-vous de disques en jeu ? ", minval = 1))

compteur = tl.Turtle() # Tortue qui s'occupe d'afficher le compteur de coups
compteur.hideturtle()
compteur.up()
compteur.speed(0)

afficheScores(nb)
afficheChronos(nb)
afficheReflexMoy(nb)

plateau = init(nb)
dessinePlateau(nb)
for i in range(nb):
    dessineDisque(i + 1, init(nb), nb)
    
compteur.goto(screensizeX/2-170, screensizeY/2-50)
compteur.write("Nombre de coups : 0", align="center",font=("Arial",12,"bold"))

global temps1
temps1 = time() # Enregistre le temps depuis Epoch, est réutilisée par la fonction deplacement() pour en déduire le temps de partie
    
with open("cpt","wb") as cptFile:
    pickle.dump(0, cptFile)
cpt = 0
    
coups = {0: init(nb)}
with open("coups","wb") as coupsF:
    pickle.dump(coups, coupsF)


tl.onscreenclick(jouerClic,1) # Clique qui appelle jouerClic avec les coordonnées de la souris au moment du clique
tl.onscreenclick(boutons,1,True) # Même chose mais appelle boutons

tl.mainloop() # Permet la détection d'un évènement -> ici onscreenclick()
doctest.testmod()

