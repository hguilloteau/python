# Programme de test du module desssins_tortue.py pour l'étoile 6 côtés et les autres

from dessins_tortue import *

serie = 3
i = 0

up()
goto(-200, 0)
down()

#triangle(40,"red", 0)
#etoile6(40,"blue",30)

while i < serie:
    right(30*i)
    etoile6(30+i*10, "red", 0)
    up()
    forward(40+i*10)
    down()
    carre(30+i*10, "blue", 0)
    up()
    forward(40+i*10)
    down()
    etoile5(30+i*10, "orange", 0)
    up()
    forward(40+i*10)
    down()
    i = i + 1

input("Taper sur entrée pour stopper")
