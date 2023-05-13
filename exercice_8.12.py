# programme qui fait apparaître une fenêtre avec un canevas. Dans ce canevas on verra deux cercles (de tailles et de couleurs différentes), qui sont censés représenter deux astres. Des boutons doivent permettre de les déplacer à volonté tous les deux dans toutes les directions. Sous le canevas, le programme doit afficher en permanence :
# a) la distance séparant les deux astres;
# b) la force gravitationnelle qu’ils exercent l’un sur l’autre (penser à afficher en haut de fenêtre les masses choisies pour chacun d’eux, ainsi que l’échelle des distances). Dans cet exercice, vous utiliserez évi- demment la loi de la gravitation universelle de Newton (cf. exercice 6.16, page 59, et un manuel de Physique générale).

from tkinter import *
from math import sqrt
# procédure générale de déplacement :


def avance(gd, hb, n):
    "Fonction qui permet de déplacer un cercle de gd et dh pixels"
    global x, y
    x[n], y[n] = x[n] + gd, y[n] + hb
    can1.coords(cercle[n], x[n], y[n], x[n]+30, y[n]+30)
    distance()


def distance():
    "Fonction qui met à jour un label avec la distance entre les 2 cercles"
    global x, y
    dist = sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)
    chaine.configure(text="Distance : " + str(dist))


# gestionnaires d'événements :


def depl_gauche():
    avance(-10, 0, 0)


def depl_droite():
    avance(10, 0, 0)


def depl_haut():
    avance(0, -10, 0)


def depl_bas():
    avance(0, 10, 0)


def depl_gauche1():
    avance(-10, 0, 1)


def depl_droite1():
    avance(10, 0, 1)


def depl_haut1():
    avance(0, -10, 1)


def depl_bas1():
    avance(0, 10, 1)


# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# coordonnées initialesn cercle 1 et 2
x = [100, 400]
y = [10, 10]
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=300, width=600)
cercle = [0]*2
# cercle 1
cercle[0] = can1.create_oval(
    x[0], y[0], x[0]+30, y[0]+30, width=2, fill='red')
# cercle 2
cercle[1] = can1.create_oval(
    x[1], y[1], x[1]+30, y[1]+30, width=2, fill='blue')
can1.pack(side=LEFT)
Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
Button(fen1, text='Gauche', command=depl_gauche).pack()
Button(fen1, text='Droite', command=depl_droite).pack()
Button(fen1, text='Haut', command=depl_haut).pack()
Button(fen1, text='Bas', command=depl_bas).pack()
Button(fen1, text='Gauche', command=depl_gauche1).pack()
Button(fen1, text='Droite', command=depl_droite1).pack()
Button(fen1, text='Haut', command=depl_haut1).pack()
Button(fen1, text='Bas', command=depl_bas1).pack()
chaine = Label(fen1)
chaine.configure(text="Distance entre les 2 cercles")
chaine.pack(side=TOP)
# démarrage du réceptionnaire d’évènements (boucle principale) :
fen1.mainloop()
