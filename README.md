TOURS DE HANOI                                                                                                                                
                                                                                                                                                                    
Projet INF101 (DLST - UGA)

Fichier à exécuter : script.py 
(Aucun module supplémentaire à installer)

Version Python : 3.9.5

Toutes les parties ont été implémentées à l'exception de certains bonus (statistiques matplotlib, indices)
Cependant, afin d'implémenter notre système de boutons et d'évènements Turtle (onscreenclick()), nous avons du changer des choses (notamment des fonctions) par rapport au sujet. 
(Sont concernées les fonctions de la partie C, ainsi que le code du programme principal.)

Extensions réalisées (bonus dans le projet):
- Boutons d'interaction (Déplacements des disques d'une tour à une autre, annulation d'un coup, abandon de la partie : résolution récursive montrée, quitter le jeu)
- Sauvegarde des scores dans le fichier pickle "data" (dont le temps de partie)
- Affichage sur Turtle des classements (en fonction du nombre de disques choisi) et du nombre de coups
- (Ecran et interface adaptatifs grâce au module ctypes)

Problèmes et bugs connus :
- Il ne faut pas être trop brusque avec les boutons sinon ils n'arrivent plus à suivre (attendre la fin de l'animation turtle avant de sélectionner un nouveau déplacement et éviter les double clics) 
-> il est possible que relancer le programme soit nécessaire (Ce bug vient du fait que nous avons rajouté des fonctions permettant de "surligner" les boutons utilisés)

=> Nous vous avons mis à disposition le fichier script2.py qui ne contient pas l'animation de boutons et est donc bien plus fluide.

__________________________

Explication de la fonction récursive (partie F) :
Tout d'abord, cette dernière modifie (effet de bord) la liste de déplacement définie juste avant.

Soit n le nombre de disques.
Le cas de base de la fonction est lorsque n vaut 1 : dans ce cas on déplace simplement le disque de la tour de départ à la tour d'arrivée.
Autrement, nous voulons à chaque étape, déplacer le disque le plus grand (situé en dessous de la tourde départ) de la tour de départ à la tour d'arrivée.
Le cas général consiste donc à appliquer une première fois l'algorithme pour n-1 disques, que l'on déplacera de la tour de départ à la tour intermédiaire (celle qui n'est ni celle de départ, ni celle d'arrivée). On a donc la tour intermédiaire qui devient la tour d'arrivée et la tour d'arrivée qui devient la tour intermédiaire. Puis on déplace le n-ème disque de la tour de départ à la tour d'arrivée. Enfin, on applique une seconde fois l'algorithme sur les n-1 disques situés sur la tour intermédire, pour les déplacer sur la tour d'arrivée (la tour de départ devient dans ce cas la tour intermédiaire).

Explication des calculs de dimensions des disques ainsi que les coordonnées de Turtle :
Pour le dessin du plateau, nous nous sommes basés sur le diamètre du plus grand disque (disque n, avec n le nombre de disques) qui vaut donc : 40 + 30 * (n-1) 
Car 40 est le diamètre du disque le plus petit et il augmente de 30 pour chaque disque plus grand.
Nous avons donc pu calculer la longueur du plateau en fonction de n, qui vaut donc : 80 + 3*(diamètre du grand disque) car on a 20 d'espace entre chaque tour (en plus des disques) et 20 d'espace aux extrémités du plateau, ainsi que 3 tours, donc 3 diamètres du plus grand disque.

__________________________

Principale difficulté rencontrée : 
Les évènements de clique de Turtle nous ont beaucoup posé problème et nous ont fait perdre pas mal de temps. Nous avont testé beaucoup de choses et avons finalement été contraints de modifier complètement la partie C ainsi que le programme principal.
