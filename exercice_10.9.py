# Écrivez une fonction est UnChiffre() qui renvoie «vrai», si l’argument transmis est un chiffre, et « faux » sinon. Tester ainsi tous les caractères d’une chaîne en parcourant celle-ci à l’aide d’une boucle for.

chiffre = '1234567890'


def UnChiffre(arg):
    "Fonction renvoie «vrai», si l’argument transmis est un chiffre, et « faux » sinon"
    if arg in '1234567890':
        return True
    else:
        return False


# Test :
if __name__ == '__main__':
    test = 'hfqse73B98Fkljnfspçà789'
    for car in test:
        print('test si', car, 'est un chiffre :', UnChiffre(car))
