# Définissez une fonction indexMax(liste) qui renvoie l’index de l’élément ayant la valeur la plus élevée dans la liste transmise en argument. Exemple d’utilisation: serie = [5, 8, 2, 1, 9, 3, 6, 7]
# print(indexMax(serie))
# 4

def indexMax(liste):
    "renvoie l’index de l’élément ayant la valeur la plus élevée dans la liste transmise en argument"
    max = liste[0]
    index = 0
    nb = len(liste)
    i = 1
    while i < nb:
        if liste[i] > max:
            max = liste[i]
            index = i
        i = i + 1
    return index


serie = [5, 8, 2, 1, 9, 3, 6, 7]
print("L'index de l'élément le plus grand de cette liste",
      serie, "est :", indexMax(serie))
