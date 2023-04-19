# Définissez une fonction eleMax(liste,debut,fin) qui renvoie l’élément ayant la plus grande valeur dans la liste transmise. Les deux arguments debut et fin indiqueront les indices entre lesquels doit s’exercer la recherche, et chacun d’eux pourra être omis (comme dans l’exercice précédent). Exemples de la fonctionnalité attendue :
# >> > serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
# >> > print(eleMax(serie))
# 9
# >> > print(eleMax(serie, 2, 5))
# 7
# >> > print(eleMax(serie, 2))
# 8
# >> > print(eleMax(serie, fin=3, debut=1))
# 6

def eleMax(liste, debut=-1, fin=-1):
    "Renvoie l’élément ayant la plus grande valeur dans la liste transmise. Les deux arguments debut et fin indiqueront les indices entre lesquels doit s’exercer la recherche, et chacun d’eux pourra être omis"

    if fin == -1:
        fin = len(liste)

    if debut == -1:
        debut = 0

    max = liste[debut]

    while debut + 1 < fin:
        if liste[debut+1] > max:
            max = liste[debut+1]
        debut = debut + 1

    return max


serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]

print(eleMax(serie))
print(eleMax(serie, 2, 5))
print(eleMax(serie, 2))
print(eleMax(serie, fin=3, debut=1))
