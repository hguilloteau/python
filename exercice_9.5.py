# Vous avez à votre disposition un fichier texte dont chaque ligne est la représentation d’une valeur numérique de type réel (mais sans exposants). Par exemple :
#   14.896
#   7894.6
#   123.278
#   etc.
# Écrivez un script qui recopie ces valeurs dans un autre fichier en les arrondissant en nombres entiers (l’arrondi doit être correct).

filename = 'nombre_reel.txt'
file = open(filename, 'r')
filename_arrondi = 'nombre_reel_arrondi.txt'
file_arrondi = open(filename_arrondi, 'w')

endfile = 0
while not endfile:
    ligne = file.readline()
    if ligne == "" or ligne == "\n":
        endfile = 1
    else:
        num = eval(ligne)
        num = round(num, 0)
        file_arrondi.write(str(num) + '\n')

file.close()
file_arrondi.close()
