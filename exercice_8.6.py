# - Supprimez la ligne global x1, y1, x2, y2 dans la fonction drawline du programme original. Que se passe-t-il ? Pourquoi ?
# Ca ne trace plus la ligne, il y a des erreurs à l'appel de la fonction drawline car les variables ne sont pas définis et n'ont pas de valeur
# - Si vous placez plutôt « x1, y1, x2, y2 » entre les parenthèses, dans la ligne de définition de la fonction drawline, de manière à transmettre ces variables à la fonction en tant que paramètres, le programme fonctionne-t-il encore ? N’oubliez pas de modifier aussi la ligne du programme qui fait appel à cette fonction !
# Les variables globales ne peuvent pas être modifiées par la fonction donc elles ne changent pas, on trace toujours la même ligne
# - Si vous définissez x1, y1, x2, y2 = 10, 390, 390, 10 à la place de global x1, y1, ..., que se passe-t-il ? Pourquoi ? Quelle conclusion pouvez-vous tirer de tout cela ?
# Quelque soit les valeurs passées en arguments de la fonction, comme on redéfinit leur valeur, on trace des lignes avec les valeurs définies dans la fonction (quasiment hors cadre). Et idem point précédent, la modification de ces valeurs à la fin de la fonction ne sert à rien et n'a aucun effet

# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---


def drawline(x1, y1, x2, y2, coul):
    "Tracé d'une ligne dans le canevas can1"
    # global x1, y1, x2, y2, coul
    x1, y1, x2, y2 = 10, 390, 390, 10
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1-10


def changecolor():
    "Changement aléatoire de la couleur du tracé"
    # => génère un nombre aléatoire de 0 à 7
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green',
           'red', 'blue', 'orange', 'yellow']
    c = randrange(8)
    # ---------------------------------------------------------------------
    # Exercice 8.1 - Comment faut-il modifier le programme pour ne plus avoir que des lignes de couleur cyan, maroon et green
    # pal = ['maroon', 'cyan', 'green']
    # c = randrange(3)
    # ---------------------------------------------------------------------
    coul = pal[c]


# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# coordonnées de la ligne
x1, y1, x2, y2 = 10, 190, 190, 10
# couleur de la ligne
coul = 'dark green'
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer une ligne',
              command=lambda: drawline(x1, y1, x2, y2, coul))
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
fen1.mainloop()     # démarrage du réceptionnaire d’événements
fen1.destroy()      # destruction (fermeture) de la fenêtre
