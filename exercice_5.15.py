# Programme qui analyse un par un tous les éléments d’une liste de mots (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']) pour générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères, l’autre les mots comportant 6 caractères ou davantag

t = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
lg_t = len(t)
t_courtes = []
t_longues = []

i = 0
while i < lg_t:
    if len(t[i]) > 6:
        t_longues.append(t[i])
    else:
        t_courtes.append(t[i])
    i = i+1

print("Liste mots courts",end=" ")
print(t_courtes)
print("Liste mots longs",end=" ")
print(t_longues)