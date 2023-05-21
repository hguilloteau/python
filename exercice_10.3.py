# Tâchez d’écrire une petite fonction trouve() qui fera exactement le contraire de ce que fait l’opérateur d’indexage (c’est-à-dire les crochets [ ]). Au lieu de partir d’un index donné pour retrouver le caractère correspondant, cette fonction devra retrouver l’in- dex correspondant à un caractère donné.
# En d’autres termes, il s’agit d’écrire une fonction qui attend deux arguments : le nom de la chaîne à traiter et le caractère à trouver. La fonction doit fournir en retour l’in- dex du premier caractère de ce type dans la chaîne. Ainsi par exemple, l’instruction : print(trouve("Juliette & Roméo", "&"))
# devra afficher : 9
# Attention : il faut penser à tous les cas possibles. Il faut notamment veiller à ce que la fonction renvoie une valeur particulière (par exemple la valeur -1) si le caractère re- cherché n’existe pas dans la chaîne traitée. Les caractères accentués doivent être ac- ceptés.

# 10.4 Améliorezlafonctiondel’exerciceprécédentenluiajoutantuntroisièmeparamètre: l’index à partir duquel la recherche doit s’effectuer dans la chaîne. Ainsi par exemple, l’instruction :
# print(trouve ("César & Cléopâtre", "r", 5))
# devra afficher : 15 (et non 4 !).

def trouve(chaine, caractere, debut=0):
    "fonction qui cherche un caractere dans une chaine et renvoie la position du caractere, renvoie -1 si pas trouvé"
    lg_ch = len(chaine)
    i = debut
    while i < lg_ch:  # une chaine de N caractères a un index de 0 à N-1
        if chaine[i] == caractere:
            return i
        i = i+1
    return -1


# Test :
if __name__ == '__main__':
    car = 'i'
    chaine = 'ihenri'
    print('test de recherche du ', car, ' dans ',
          chaine, ' : ', trouve(chaine, car, 1))
