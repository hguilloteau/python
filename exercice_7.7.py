# Programme de test du module desssins_tortue.py pour l'étoile 5 côtés

from dessins_tortue import *

nbre_etoiles = 3
i = 0

up()
goto(-300,0)
down()

while i < nbre_etoiles:
    etoile5(20+i*10, "blue", 30+i*10)
    up()
    forward(30+i*10)
    down()
    i = i + 1

input("Taper sur entrée pour stopper")
