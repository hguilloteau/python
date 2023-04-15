# Module de dessins utilisant Turtle

from turtle import *


def carre(taille, couleur, angle):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    right(angle)
    c = 0
    while c < 4:
        forward(taille)
        right(90)
        c = c + 1
    right(360-angle)    # pour revenir à l'orientation initiale


def triangle(taille, couleur, angle):
    "Fonction qui permet de dessiner un triangle équilatéral de taille et de couleur déterminées"
    color(couleur)
    right(angle)
    forward(taille)
    left(120)
    forward(taille)
    left(120)
    forward(taille)
    left(120)
    right(360-angle)    # pour revenir à l'orientation initiale
