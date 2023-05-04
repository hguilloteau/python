# Ajoutez une fonction drawline2 qui tracera deux lignes rouges en croix au centre du canevas : l’une horizontale et l’autre verticale. Ajoutez également un bouton portant l’indication « viseur ». Un clic sur ce bouton devra provoquer l’affichage de la croix.

# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---


def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2-5, y1-5


def drawline2():
    "Tracé de 2 lignes rouges formant une croix au centre du canevas can1"
    can1.create_line(0, 250, 500, 250, width=2, fill='red')
    can1.create_line(250, 0, 250, 500, width=2, fill='red')


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
x1, y1, x2, y2 = 0, 500, 500, 500
# couleur de la ligne
coul = 'dark green'
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=500, width=500)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer une ligne', command=drawline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
bou3 = Button(fen1, text='Viseur', command=drawline2)
bou3.pack()
fen1.mainloop()     # démarrage du réceptionnaire d’événements
fen1.destroy()      # destruction (fermeture) de la fenêtre
