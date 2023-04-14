# Demander à l’utilisateur d’entrer trois longueurs a,b,c. À l’aide de ces trois longueurs, déterminer s’il est possible de construire un triangle. Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque. Attention : un triangle rectangle peut être isocèle.

print("Veuillez saisir les longueurs des côtés d'un triangle ?")
a, b, c = eval(input())

# est-ce un triangle ?
if a > b + c or b > a + c or c > a + b :
    print("Ce n'est pas un triangle")
else :
    particulier = 0
    if a == b and b == c :
        print("C'est un triangle équilatéral")
        particulier = 1
    elif a == b or b == c or a == c :
        print("C'est un triangle isocèle")
        particulier = 1
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b :
        print("C'est un triangle rectangle")
        particulier = 1
    if particulier == 0:
        print("C'est un triangle quelconque")