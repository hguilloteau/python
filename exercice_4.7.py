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
