# Importez le module turtle pour pouvoir effectuer des dessins simples.
# dessiner une série de triangles équilatéraux de différentes couleurs.
# définisser d’abord une fonction triangle() capable de dessiner un triangle d’une couleur bien déterminée (ce qui signifie donc que la définition de votre fonction doit comporter un paramètre pour recevoir le nom de cette couleur).
# Utiliser ensuite cette fonction pour reproduire ce même triangle en différents endroits, en changeant de couleur à chaque fois.

from turtle import *

def triangle(couleur):
    "Fonction qui permet de dessiner un triangle équilatéral"
    color(couleur)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

liste_couleurs = ["blue", "red", "yellow", "green", "orange"]

up()
goto(-300,0)
down()

i = 0
while i < len(liste_couleurs):
    triangle(liste_couleurs[i])
    i = i + 1
    up()
    forward(120)
    down()
    
input("Taper sur entrée pour stopper")