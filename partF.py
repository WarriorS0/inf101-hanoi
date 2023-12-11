import turtle as tl
from partB import *

###################################################################################################################
################################# Partie F : Jeu automatique, fonction récursive ##################################
###################################################################################################################

listeDep = []

def resolution(n: int, dep=0, arr=2, inter=1):
    """Modifie la liste des déplacements afin de résoudre le problème à n disques"""
    if n == 1:
        listeDep.append((dep, arr))
    else:
        resolution(n - 1, dep, inter, arr)
        listeDep.append((dep, arr))
        resolution(n - 1, inter, arr, dep)

def dessineRes(n:int, dep=listeDep):
    """Joue les dédplacements pour résoudre le problème à n disques"""
    dessinePlateau(n)
    config = init(n)
    for i in range(n):
        dessineDisque(i+1,config,n)
    for e in dep:
        tourDep, tourArr = e
        disque = config[tourDep][-1]
        effaceDisque(disque, config, n)
        config[tourDep].pop(-1)
        config[tourArr].append(disque)
        dessineDisque(disque, config, n)
    tl.done()
