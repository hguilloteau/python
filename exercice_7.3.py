# Définissez une fonction surfCercle(R). Cette fonction doit renvoyer la surface (l’aire) d’un cercle dont on lui a fourni le rayon R en argument. Par exemple, l’exécution de l’instruction :
# print(surfCercle(2.5)) doitdonnerlerésultat:19.63495...

from math import pi


def surfCercle(R):
    "Renvoie la surface (l’aire) d’un cercle dont on lui a fourni le rayon R en argument"
    return pi * R * R

print("La surface d'un cercle de 2.5 de rayon est :",surfCercle(2.5))