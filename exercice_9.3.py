# Écrivez un script qui génère automatiquement un fichier texte contenant les tables de multiplication de 2 à 30 (chacune d’entre elles incluant 20 termes seulement)

def tablemultiplication(num, maxval):
    "Fonction qui renvoie une chaine de carctère contenant la table de multiplication num jusqu'à maxval"
    chaine = ""
    i = 1
    while i <= maxval:
        chaine = chaine + str(num) + " * " + str(i) + \
            " = " + str(num*i) + " - "
        i = i + 1
    return chaine


filename = "tablemultiplication.txt"
file = open(filename, 'w')

i = 2
max = 30
while i <= max:
    file.write(tablemultiplication(i, 20) + '\n')
    i = i + 1

file.close()
