# Écrivez une fonction compteCar() qui compte le nombre d’occurrences d’un caractère donné dans une chaîne. Ainsi :
# print(compteCar("ananas au jus","a"))
# devra afficher : 4
# print(compteCar("Gédéon est déjà là","é")) devra afficher : 3.


def compteCar(chaine, caractere):
    "fonction qui cherche un caractere dans une chaine et renvoie le nombre de caracteres trouvés, renvoie -1 si pas trouvé"
    lg_ch = len(chaine)
    i = 0
    nb = 0
    while i < lg_ch:  # une chaine de N caractères a un index de 0 à N-1
        if chaine[i] == caractere:
            nb = nb + 1
        i = i+1
    return nb


# Test :
if __name__ == '__main__':
    car = 'i'
    chaine = 'ihenri guilloteau'
    print('test de comptecar ', car, ' dans ',
          chaine, ' : ', compteCar(chaine, car))
