# Considérons que vous avez à votre disposition un fichier texte contenant des phrases de différentes longueurs. Écrivez un script qui recherche et affiche la phrase la plus longue.

filename = "Monfichier.txt"
file = open(filename, 'r')

endfile = 0
lgmax = 0
lignelapluslongue = ""
while not endfile:
    ligne = file.readline()
    if ligne == "":
        endfile = 1
    else:
        if len(ligne) > lgmax:
            lignelapluslongue = ligne
            lgmax = len(ligne)

print("La ligne la plus longue est : ", lignelapluslongue)
