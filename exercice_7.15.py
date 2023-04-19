# Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d’une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments.
# Par exemple, l’exécution de l’instruction:
# print(volBoite(5.2, 7.7, 3.3)) doit donner le résultat: 132.132.
# 7.14
# Modifiez la fonction volBoite(x1,x2,x3) que vous avez définie dans un exercice précédent, de manière à ce qu’elle puisse être appelée avec trois, deux, un seul, ou même au- cun argument. Utilisez pour ceux ci des valeurs par défaut égales à 10.
# 7.15
# Modifiez la fonction volBoite(x1,x2,x3) ci-dessus de manière à ce qu’elle puisse être appelée avec un, deux, ou trois arguments. Si un seul est utilisé, la boîte est considérée comme cubique (l’argument étant l’arête de ce cube). Si deux sont utilisés, la boîte est considérée comme un prisme à base carrée (auquel cas le premier argument est le côté du carré, et le second la hauteur du prisme). Si trois arguments sont utilisés, la boîte est considérée comme un parallélépipède

def volBoite(x1="none", x2="none", x3="none"):
    "renvoie le volume d’une boîte parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments. Si un seul argument est donné, on considère un cube ; si 2 arguments, on considère un prisme à base carré"
    if x1 == "none":
        return -1
    elif x2 == "none":
        return x1**3
    elif x3 == "none":
        return x1**2 * x2
    else:
        return x1 * x2 * x3


print("Test appel sans arguments :", volBoite())

print("Test avec 1 argument 5.2 :", volBoite(5.2))

print("Test avec 2 arguemnts 5.2 et 3:", volBoite(5.2, 3))

print("Le volume d'un parallépipède de 5.2, 7.7, 3.3 de côté est :",
      volBoite(5.2, 3, 7.4))
