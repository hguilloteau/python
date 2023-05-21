# Écrivez un script qui recherche le nombre de caractères "e", "é", "è", "ê", "ë" contenus dans une phrase donnée.

def comptecar(chaine, caractere):
    "fonction qui cherche un caractere dans une chaine et renvoie le nombre de caracteres trouvés, renvoie -1 si pas trouvé"
    nb = 0
    for car in chaine:
        if car == caractere:
            nb = nb + 1
    return nb


def compteseriecar(chaine, caracteres):
    "fonction qui cherche une serie de caracteres dans la chaine"
    for car in caracteres:
        print('Caractère', car, ' : ', comptecar(chaine, car))


# Test :
if __name__ == '__main__':
    chaine = 'je vais à l\'école élèmentaire en vélo pour la fête'
    caracteres = 'éèêërt'
    print('test de recherche des caractères ', caracteres, ' dans ',
          chaine, ' : ')
    print(compteseriecar(chaine, caracteres))
