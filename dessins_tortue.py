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
    right((360-angle) % 360)    # pour revenir à l'orientation initiale


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
    right((360-angle) % 360)    # pour revenir à l'orientation initiale


def etoile5(taille, couleur, angle):
    "fonction etoile5() spécialisée dans le dessin d’étoiles à 5 branches"
    color(couleur)
    right(angle)
    i = 0
    while i < 5:
        forward(taille)
        right(180-36)
        i = i + 1
    right((360-angle) % 360)
