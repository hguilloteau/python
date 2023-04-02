# programmequianalyseunparuntouslesélémentsd’unelistedenombres (par exemple celle de l’exercice précédent) pour générer deux nouvelles listes. L’une contiendra seulement les nombres pairs de la liste initiale, et l’autre les nombres im- pairs. Par exemple, si la liste initiale est celle de l’exercice précédent, le programme de- vra construire une liste pairs qui contiendra [32, 12, 8, 2], et une liste impairs qui contiendra [5, 3, 75, 15]. Astuce : pensez à utiliser l’opérateur modulo (%) déjà cité précédemment

t1 = [32, 5, 12, 8, 3, 75, 2, 15]
lg_t1 = len(t1)
t_pair = []
t_impair = []

i=0
while i < lg_t1:
    if t1[i]%2 == 0:
        t_pair.append(t1[i])
    else:
        t_impair.append(t1[i])
    i = i+1

print("Les valeurs paires",end=" ")
print(t_pair)
print("Les valeurs impaires",end=" ")
print(t_impair)