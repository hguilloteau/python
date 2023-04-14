# Demander à l’utilisateur qu’il entre un nombre. Afficher ensuite : soit la racine carrée de ce nombre, soit un message indiquant que la racine carrée de ce nombre ne peut être calculée.

from math import sqrt

print("Veuillez saisir un nombre ?")
nombre = float(input())

print("La racine carré de",nombre,"est",sqrt(nombre))
print(type(nombre))