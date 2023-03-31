# programme qui calcule les 50 premiers termes de la table de multiplication par 13, mais n’affiche que ceux qui sont des multiples de 7

nbre_terme = 50
nbre_a_multiplier = 13

i=0
while ( i<nbre_terme ):
    i = i+1
    if ((nbre_a_multiplier*i)%7 == 0):
        print ( nbre_a_multiplier,"*",i,"=",nbre_a_multiplier*i)