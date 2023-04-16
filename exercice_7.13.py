# Définissez une fonction compteMots(ph) qui renvoie le nombre de mots contenus dans la phrase ph. On considère comme mots les ensembles de caractères inclus entre des espaces.

def compteMots(ph):
    "Renvoie le nombre de mots contenus dans la phrase ph. On considère comme mots les ensembles de caractères inclus entre des espaces"
    mot = 0
    lg = len(ph)
    espace = True
    i = 0
    while i < lg:
        if ph[i] == " " and espace == False:
            mot = mot + 1
            espace = True
        elif ph[i] == " " and espace == True:
            # enchainement de plusieurs espaces
            espace = True
        elif ph[i] != " " and i + 1 == lg:
            mot = mot + 1
        else:
            espace = False
        i = i + 1
    return mot


ph = "il y a huit mots dans cette phrase"
print("il y a : ", compteMots(ph), "mots dans cette phrase :", ph)
