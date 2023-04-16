# Module de dessins utilisant Turtle

from turtle import *
from math import cos, pi

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
    "fonction etoile5() spécialisée dans le dessin d’étoiles à 5 branches de taille et de couleur déterminées"
    color(couleur)
    right(angle)
    i = 0
    while i < 5:
        forward(taille)
        right(180-36)
        i = i + 1
    right((360-angle) % 360)

def etoile6(taille, couleur, angle):
    "onction etoile5() spécialisée dans le dessin d’étoiles à 6 branches de taille et de couleur déterminées"
    triangle(taille, couleur, angle)
    up()    # déplacement pour faire le second triangle équilatéral
    right(angle)
    forward(taille)
    left(120)
    forward(taille/3)
    right(60)
    forward(taille/3)
    right(60)
    left(angle)
    down()
    triangle(taille, couleur, angle+180)
    up()    # retour à la position du début du dessin de l'étoile
    right(angle)
    backward(taille)
    right(60)
    forward(taille/3)
    right(60)
    forward(taille/3)
    left(120)
    right((360-angle) % 360)

