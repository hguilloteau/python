# Écrivez un script qui compare les contenus de deux fichiers et signale la première dif- férence rencontrée.

filename = 'Monfichier.txt'
file = open(filename, 'r')
filenamediff = 'Monfichierdiff.txt'
filediff = open(filenamediff, 'r')

# récupération du contenu des 2 fichiers dans des listes de lignes
contenu = file.readlines()
contenudiff = filediff.readlines()

# comparaison ligne à ligne puis caractère par caractère des 2 listes pour détecter une différence
nbline = len(contenu)
nblinediff = len(contenudiff)
i = 0
lignediff = -1
difference_trouve = 0
while i < nbline and not difference_trouve:
    if contenu[i] != contenudiff[i]:
        lignediff = i
        lgligne = len(contenu[i])
        j = 0
        # recherche de la diff dans la ligne au niveau du caractère
        while j < lgligne and not difference_trouve:
            if contenu[i][j] != contenudiff[i][j]:
                caracterediff = j
                difference_trouve = 1
            j = j + 1
    i = i + 1

if lignediff == -1:
    print('Pas de différence entre les 2 fichiers')
else:
    print('Différence entre les 2 fichiers : ligne ' +
          str(lignediff+1) + ' caractère : ' + str(caracterediff+1))


# Correction de l'exercice
# # Comparaison de deux fichiers, caractère par caractère :
# fich1 = input("Nom du premier fichier : ")
# fich2 = input("Nom du second fichier : ")
# fi1 = open(fich1, 'r')
# fi2 = open(fich2, 'r')
# c, f = 0, 0
# while 1:
#     # compteur de caractères et "drapeau"
#     c = c +1
#     car1 = fi1.read(1)
#     car2 = fi2.read(1)
#     if car1 =="" or car2 =="":
#             break
#     if car1 != car2 :
#         f =1 break

# fi1.close()
# fi2.close()
# # différence trouvée
# print("Ces 2 fichiers", end=' ')
# if f ==1:
#     print("diffèrent à partir du caractère n°", c)
# else:
#     print("sont identiques.")
