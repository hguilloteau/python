# Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d’une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments.
# Par exemple, l’exécution de l’instruction:
# print(volBoite(5.2, 7.7, 3.3)) doit donner le résultat: 132.132.

def volBoite(x1, x2, x3):
    "renvoie le volume d’une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments"
    return x1 * x2 * x3

print("Le volume d'un parallépipède de 5.2, 7.7, 3.3 de côté est :",
      volBoite(5.2, 7.7, 3.3))
