# Écrivez un programme qui fait apparaître une fenêtre avec un canevas. Dans ce canevas, placez un petit cercle censé représenter une balle. Sous le canevas, placez un bouton. Chaque fois que l’on clique sur le bouton, la balle doit avancer d’une petite distance vers la droite, jusqu’à ce qu’elle atteigne l’extrémité du canevas. Si l’on continue à cliquer, la balle doit alors revenir en arrière jusqu’à l’autre extrémité, et ainsi de suite.

from tkinter import *
# procédure générale de déplacement :


def avance():
    "Fonction qui permet de déplacer un cercle de gd et dh pixels"
    global x, y, dx
    # vérifier qu'avec le pas de déplacement on se sort pas du canevas
    if x+30+dx >= xmax:
        dx = dx * -1
        x = xmax - 30
    elif x+dx <= 0:
        dx = dx * -1
        x = 0
    else:
        x = x + dx
    can1.coords(cercle[0], x, y, x+30, y+30)

# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# pas de déplacement du cerdle
dx = 10
# dimension du canevas
xmax = 300
ymax = 50
# coordonnées initiales cercle 1
x = 135
y = 20
n = 0  # pour déterminer un cercle sélectionné
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=ymax, width=xmax)
cercle = [0]
# cercle 1
cercle[0] = can1.create_oval(
    x, y, x+30, y+30, width=2, fill='red')
can1.grid(row=1, column=1)
Button(fen1, text='Déplacement', command=avance).grid(
    row=2, column=1)
Button(fen1, text='Quitter', command=fen1.quit).grid(
    row=3, column=1)


# démarrage du réceptionnaire d’évènements (boucle principale) :
fen1.mainloop()
