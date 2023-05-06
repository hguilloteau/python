# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---


def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    # ---------------------------------------------------------------------
    # Exercice 8.5 - Reprenez le programme initial. Remplacez la méthode create_line par create_rec- tangle. Que se passe-t-il ?
    # De la même façon, essayez aussi create_arc, create_oval, et create_polygon.
    # Pour chacune de ces méthodes, notez ce qu’indiquent les coordonnées fournies en pa - ramètres.
    # (Remarque: pour le polygone, il est nécessaire de modifier légèrement le pro - gramme !)
    # ---------------------------------------------------------------------
    # can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    # Pour un rectangle x1 y1 coin supérieur gauche x2 y2 coin inférieur droit
    # can1.create_rectangle(x1, y1, x2, y2, width=2, fill=coul)
    # Pour un arc x1 y1 pas comrpis les argumesnts de coordoneés
    # can1.create_arc(x1, y1, x2, y2, width=2, fill=coul)
    # Pour un oval x1 y1 coin supérieur gauche x2 y2 coin inférieur droit ce qui définit un rectangle dans lequel s'inscrit l'ovale
    # can1.create_oval(x1, y1, x2, y2, width=2, fill=coul)
    # Pour un polygon x1 y1 premier point x2 y2 deuxième point ... et ainsi de suite
    can1.create_polygon(x1, y1, 150, 150, x2, y2, 50, 50,
                        splinesteps=5, width=2, fill=coul)

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
bou2 = Button(fen1, text='Tracer une ligne', command=drawline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
fen1.mainloop()     # démarrage du réceptionnaire d’événements
fen1.destroy()      # destruction (fermeture) de la fenêtre
