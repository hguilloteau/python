# Dans un script, écrivez une fonction qui recherche le nombre de mots contenus dans une phrase donnée.

def comptemot(phrase):
    "fonction qui compte le nombre de mots d'une phrase et renvoie ce nombre"
    nbmot = 0
    if len(phrase) == 0:
        # la phrase est vide, pas de mot
        return nbmot
    else:
        # il y a au moins un mot
        nbmot = nbmot + 1
        for car in phrase:
            if car == " ":
                nbmot = nbmot + 1
    return nbmot


# Test :
if __name__ == '__main__':
    chaine = 'ihenri guilloteau '
    print('test de comptemot dans ',
          chaine, ' : ', comptemot(chaine))
