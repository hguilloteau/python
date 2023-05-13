# En vous inspirant du programme qui détecte les clics de souris dans un canevas, modifiez le programme ci-dessus pour y réduire le nombre de boutons : pour déplacer un astre, il suffira de le choisir avec un bouton, et ensuite de cliquer sur le canevas pour que cet astre se positionne à l’endroit où l’on a cliqué.
# --> consigne pas respecté : le programme gère des clics sur le canvas pour gérer la sélection du cercle à déplacer : si on clique sur un cercle, les 4 boutons de déplacements déplacent ce dernier

from tkinter import *
from math import sqrt
# procédure générale de déplacement :


def avance(gd, hb):
    "Fonction qui permet de déplacer un cercle de gd et dh pixels"
    global x, y
    x[n], y[n] = x[n] + gd, y[n] + hb
    can1.coords(cercle[n], x[n], y[n], x[n]+30, y[n]+30)
    distance()


def distance():
    "Fonction qui met à jour un label avec la distance entre les 2 cercles"
    global x, y
    dist = sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)
    chaine.configure(text="Distance entre les 2 cercles : " + str(round(dist)))


def detectionclic(event):
    "Fonction qui détecte un clic et voit si c'est dans un cercle"
    global x, y, n
    # vérifier si le clic était sur le cercle 0
    if event.x >= x[0] and event.x <= x[0]+30:
        if event.y >= y[0] and event.y <= y[0]+30:
            n = 0
    elif event.x >= x[1] and event.x <= x[1]+30:
        if event.y >= y[1] and event.y <= y[1]+30:
            n = 1

# gestionnaires d'événements :


def depl_gauche():
    avance(-10, 0)


def depl_droite():
    avance(10, 0)


def depl_haut():
    avance(0, -10)


def depl_bas():
    avance(0, 10)


# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# coordonnées initialesn cercle 1 et 2
x = [100, 470]
y = [130, 130]
n = 0  # pour déterminer un cercle sélectionné
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
chaine = Label(fen1)
chaine.configure(text="Distance entre les 2 cercles")
chaine.grid(row=1, column=1, columnspan=3)

can1 = Canvas(fen1, bg='dark grey', height=300, width=600)
# détection de clic dans le canvas
can1.bind("<Button-1>", detectionclic)
cercle = [0]*2
# cercle 1
cercle[0] = can1.create_oval(
    x[0], y[0], x[0]+30, y[0]+30, width=2, fill='red')
# cercle 2
cercle[1] = can1.create_oval(
    x[1], y[1], x[1]+30, y[1]+30, width=2, fill='blue')
can1.grid(row=2, column=1, columnspan=3)
Button(fen1, text='Gauche', command=depl_gauche).grid(
    row=3, rowspan=2, column=1, sticky=E)
Button(fen1, text='Haut', command=depl_haut).grid(row=3, column=2)
Button(fen1, text='Bas', command=depl_bas).grid(row=4, column=2)
Button(fen1, text='Droite', command=depl_droite).grid(
    row=3, rowspan=2, column=3, sticky=W)
Button(fen1, text='Quitter', command=fen1.quit).grid(
    row=5, column=1, columnspan=4)
# Button(fen1, text='Gauche', command=depl_gauche1).grid()
# Button(fen1, text='Droite', command=depl_droite1).grid()
# Button(fen1, text='Haut', command=depl_haut1).grid()
# Button(fen1, text='Bas', command=depl_bas1).grid()

# démarrage du réceptionnaire d’évènements (boucle principale) :
fen1.mainloop()
