# Soit la liste suivante:
# ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
# Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant.

liste = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']

n = len(liste)
i = 0

while i < n:
    print(liste[i],len(liste[i]))
    i = i +1