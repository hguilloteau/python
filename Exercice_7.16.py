# Définissez une fonction changeCar(ch,ca1,ca2,debut,fin) qui remplace tous les caractères ca1 par des caractères ca2 dans la chaîne de caractères ch, à partir de l’indice de- but et jusqu’à l’indice fin, ces deux derniers arguments pouvant être omis (et dans ce cas la chaîne est traitée d’une extrémité à l’autre). Exemples de la fonctionnalité atten- due :
# >>> phrase = 'Ceci est une toute petite phrase.'
# >>> print(changeCar(phrase, ' ', '*')) Ceci*est*une*toute*petite*phrase.
# >>> print(changeCar(phrase, ' ', '*', 8, 12)) Ceci est*une*toute petite phrase.
# >>> print(changeCar(phrase, ' ', '*', 12)) Ceci est une*toute*petite*phrase.
# >>> print(changeCar(phrase, ' ', '*', fin = 12)) Ceci*est*une*toute petite phrase.

def changeCar(ch, ca1, ca2, debut=-1, fin=-1):
    "emplace tous les caractères ca1 par des caractères ca2 dans la chaîne de caractères ch, à partir de l’indice de- but et jusqu’à l’indice fin, ces deux derniers arguments pouvant être omis (et dans ce cas la chaîne est traitée d’une extrémité à l’autre)"

    if fin == -1:
        fin = len(ch)

    if debut == -1:
        debut = 0

    i = 0
    lg = len(ch)
    ch_new = ""

    while i < lg:
        if i >= debut and i <= fin:
            if ch[i] == ca1:
                ch_new = ch_new + ca2
            else:
                ch_new = ch_new + ch[i]
        else:
            ch_new = ch_new + ch[i]
        i = i + 1
    
    return ch_new


phrase = 'Ceci est une toute petite phrase.'
print(changeCar(phrase, ' ', '*'))
print(changeCar(phrase, ' ', '*', 8, 12))
print(changeCar(phrase, ' ', '*', 12))
print(changeCar(phrase, ' ', '*', fin=12))
