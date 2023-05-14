# Améliorez le programme 8.17 pour que la balle décrive cette fois une trajectoire circulaire ou elliptique dans le canevas (lorsque l’on clique continuellement). Note : pour arriver au résultat escompté, vous devrez nécessairement définir une variable qui représentera l’angle décrit, et utiliser les fonctions sinus et cosinus pour positionner la balle en fonction de cet angle.
# Modifiez le programme ci-dessus de telle manière que la balle, en se déplaçant, laisse derrière elle une trace de la trajectoire décrite.

from tkinter import *
from math import sin, cos
# procédure générale de déplacement :


def avance():
    "Fonction qui permet de déplacer un cercle sur une ellipse"
    global x, y, angle
    xold = x
    yold = y
    angle = angle + delta_angle
    # calcul de la nouvelle position du cercle sur l'ellipse pour un angle de x radian
    x = x0 + b * cos(angle)
    y = y0 + a * sin(angle)
    can1.coords(cercle[0], x, y, x+20, y+20)
    # il faut ajouter 10 pour le suivi de la trajectoire parte bien du centre du cercle qui fait 20 de diamètre
    can1.create_line(x+10, y+10, xold+10, yold+10, width=1, fill='black')


# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# angle de déplacement
delta_angle = 0.1
angle = 0
# dimension ellipse
a = 80
b = 120
# dimension du canevas
xmax = 300
ymax = 300
# coordonnées centre de l'ellipse
x0 = 150
y0 = 150
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=ymax, width=xmax)
# position initale du cercle
x = x0 + b
y = y0
# cercle 1
cercle = [0]
cercle[0] = can1.create_oval(
    x, y, x+20, y+20, width=1, fill='red')
can1.grid(row=1, column=1)
Button(fen1, text='Déplacement', command=avance).grid(
    row=2, column=1)
Button(fen1, text='Quitter', command=fen1.quit).grid(
    row=3, column=1)


# démarrage du réceptionnaire d’évènements (boucle principale) :
fen1.mainloop()
