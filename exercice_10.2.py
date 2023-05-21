# Découpez une grande chaîne en fragments de 5 caractères chacun. Rassemblez ces morceaux dans l’ordre inverse. La chaîne doit pouvoir contenir des caractères accen- tués.

chaine = "Découpez une grande chaîne en fragments de 5 caractères chacun. Rassemblez ces morceaux dans l’ordre inverse. La chaîne doit pouvoir contenir des caractères accentués"

chaine_inverse5 = ""

i = 0
findechaine = 0
while not findechaine:
    bloc = chaine[i*5:(i+1)*5]
    if bloc == '':
        findechaine = 1
    else:
        chaine_inverse5 = bloc + chaine_inverse5
    i = i + 1

print(chaine)
print(chaine_inverse5)
