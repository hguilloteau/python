# Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d’une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments.
# Par exemple, l’exécution de l’instruction:
# print(volBoite(5.2, 7.7, 3.3)) doit donner le résultat: 132.132.
# 7.14
# Modifiez la fonction volBoite(x1,x2,x3) que vous avez définie dans un exercice précédent, de manière à ce qu’elle puisse être appelée avec trois, deux, un seul, ou même au- cun argument. Utilisez pour ceux ci des valeurs par défaut égales à 10.


def volBoite(x1=10, x2=10, x3=10):
    "renvoie le volume d’une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments"
    return x1 * x2 * x3


print("Le volume d'un parallépipède de 5.2, 7.7, 3.3 de côté est :",
      volBoite(5.2, 7.7, 3.3))

print("Test appel sans arguments :", volBoite())

print("Test avec 1 argument 5.2 :", volBoite(5.2))

print("Test avec 2 arguemnts 5.2 et 3:", volBoite(5.2,3))