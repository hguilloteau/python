# Programme qui recherche le plus grand élément présent dans une liste donnée. Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
# le plus grand élément de cette liste a la valeur 75

t1 = [32, 5, 12, 8, 3, 75, 2, 15]
lg_t1 = len(t1)

# initialisation de la plus grande valeur avec la première valeur de la liste
valeur_max = t1[0]

i = 1
while i < lg_t1:
    if t1[i] > valeur_max:
        valeur_max = t1[i]
    i = i+1

print("La plus grande valeur de la liste est :", valeur_max)