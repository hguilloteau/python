# programme qui affiche la suite de symboles suivante :
#        *
#        **
#        ***
#        ****
#        *****
#        ******
#        *******

i = 0
iteration = 7

while ( i <= iteration):
    i = i + 1
    j=0
    while ( j < i):
        print( "*", end=" ")
        j = j +1
    print ("")