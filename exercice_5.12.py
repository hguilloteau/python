# Programme qui affiche « proprement » tous les éléments d’une liste. Si on l’appliquait par exemple à la liste t2
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
lg_t2 = len(t2)
i=0

while i < lg_t2:
    print(t2[i],end=" ")
    i=i+1
