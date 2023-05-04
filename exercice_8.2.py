# Comment modifier le programme pour que toutes les lignes tracées soient horizon - tales et parallèles ?

# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---


def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2-3, y1-3


def changecolor():
    "Changement aléatoire de la couleur du tracé"
    # => génère un nombre aléatoire de 0 à 7
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green',
           'red', 'blue', 'orange', 'yellow']
    c = randrange(8)
    coul = pal[c]


# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# coordonnées de la ligne
# x1, y1, x2, y2 = 10, 190, 190, 10
# Modification des points d'init pour faire des lignes horizontales
x1, y1, x2, y2 = 10, 190, 190, 190
# couleur de la ligne
coul = 'dark green'
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer une ligne', command=drawline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
fen1.mainloop()     # démarrage du réceptionnaire d’événements
fen1.destroy()      # destruction (fermeture) de la fenêtre
