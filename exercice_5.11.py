# Soient les listes suivantes:
# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
# Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des deux listes en les alternant, de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :
# ['Janvier',31,'Février',28,'Mars',31, etc...].

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

lg_t1 = len(t1)
lg_t2 = len(t2)
new_liste = []

if lg_t1 == lg_t2:
    i=0
    while i < lg_t1:
        new_liste.append(t2[i])
        new_liste.append(t1[i])
        i = i+1
    print(new_liste)
else:
    print("Les 2 listes n'ont pas le même nombre d'éléments")