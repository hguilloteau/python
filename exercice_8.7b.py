# a) Créez un court programme qui  les 5 anneaux olympiques dans un rec - tangle de fond blanc(white). Un bouton « Quitter » doit permettre de fermer la fe - nêtre.
# b) Modifiez le programme ci-dessus en y ajoutant 5 boutons. Chacun de ces boutons provoquera le tracé de chacun des 5 anneaux

# Import bibliothèque graphique tkinter
from tkinter import *


def drawcircle(i):
    "Tracé d'un anneau olympique"
    can1.create_oval(coord[i][0], coord[i][1], coord[i]
                     [0]+120, coord[i][1]+120, width=4, outline=pal[i])


def circle1():
    "Tracé de l'anneau 1"
    drawcircle(0)


def circle2():
    "Tracé de l'anneau 1"
    drawcircle(1)


def circle3():
    "Tracé de l'anneau 1"
    drawcircle(2)


def circle4():
    "Tracé de l'anneau 1"
    drawcircle(3)


def circle5():
    "Tracé de l'anneau 1"
    drawcircle(4)


# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# coordonnées des anneaux
coord = [[100, 80], [220, 80], [340, 80], [150, 160], [270, 160]]
# palette de couleur des anneaux
pal = ['blue', 'black', 'red', 'yellow', 'green']
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='white', height=300, width=500)
can1.pack(side=TOP)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=RIGHT)

boucircle1 = Button(fen1, text='Anneau 1', command=circle1)
boucircle1.pack(side=LEFT)
boucircle2 = Button(fen1, text='Anneau 2', command=circle2)
boucircle2.pack(side=LEFT)
boucircle3 = Button(fen1, text='Anneau 3', command=circle3)
boucircle3.pack(side=LEFT)
boucircle4 = Button(fen1, text='Anneau 4', command=circle4)
boucircle4.pack(side=LEFT)
boucircle5 = Button(fen1, text='Anneau 5', command=circle5)
boucircle5.pack(side=LEFT)


fen1.mainloop()     # démarrage du réceptionnaire d’événements
fen1.destroy()      # destruction (fermeture) de la fenêtre
