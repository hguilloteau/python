# Écrivez un script qui recopie un fichier texte en triplant tous les espaces entre les mots.

filename = "Monfichier.txt"
filename_espace = "Monfichier_espace.txt"
file = open(filename, 'r')
file_espace = open(filename_espace, 'w')


def triplement_espace(phrase):
    "fonction qui triple tous les espaces d'une phrase"
    phrase_new = ''
    i = 0
    while i < len(phrase):
        if phrase[i] == ' ':
            phrase_new = phrase_new + '   '
        else:
            phrase_new = phrase_new + phrase[i]
        i = i + 1
    return phrase_new


# récupération du contenu du fichier dans une liste de lignes
original = file.readlines()
# parcours de toutes les lignes
n = 0
while n < len(original):
    ligne = triplement_espace(original[n])
    file_espace.write(ligne)
    n = n + 1

file.close()
file_espace.close()
