#programme qui affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
nbre_terme = 20
nbre_a_multiplier = 7

i=0
while ( i<nbre_terme ):
    i = i+1
    print ( nbre_a_multiplier,"*",i,"=",nbre_a_multiplier*i,end =" ")
    if ((nbre_a_multiplier*i)%3 == 0):
        print( "*")
    else:
        print ("")

# solution de l'exercice dans le livre
# affichage des 20 premiers termes de la table par 7,
# avec signalement des multiples de 3 :
i = 1 # compteur : prendra successivement les valeurs de 1 à 20
while i < 21:
    # calcul du terme à afficher :
    t=i* 7
    # affichage sans saut à la ligne (utilisation de la virgule) :
    print(t, end =' ')
    # ce terme est-il un multiple de 3 ? (utilisation de l'opérateur modulo) :
    if t % 3 == 0:
        print("*", end =' ') # affichage d'une astérisque dans ce cas
    i = i + 1 # incrémentation du compteur dans tous les cas