# Écrivez une fonction estUneMaj() qui renvoie « vrai » si l’argument transmis est une majuscule. Tâchez de tenir compte des majuscules accentuées !

chiffre = '1234567890'


def estUneMaj(arg):
    "Fonction renvoie «vrai», si l’argument transmis est une majuscule, et « faux » sinon"
    if arg in 'ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÉÈÊËÇÎÏÙÜÛÔÖ':
        return True
    else:
        return False


# Test :
if __name__ == '__main__':
    test = 'hfQse73B98FkljnfÉpçà7Ç9'
    for car in test:
        print('test si', car, 'est un chiffre :', estUneMaj(car))
