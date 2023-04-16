# Définissez une fonction inverse(ch) qui permette d’inverser les l’ordre des caractères d’une chaîne quelconque. La chaîne inversée sera renvoyée au programme appelant.

def inverse(ch):
    "Permet d’inverser les l’ordre des caractères d’une chaîne quelconque. La chaîne inversée sera renvoyée au programme appelan"
    lg = len(ch)
    gl = ""
    i = 0
    while i < lg:
        gl = gl + ch[lg-1-i]
        i = i + 1
    return gl


ch = "teste ma chaine pour voir"
print(ch, "<-->", inverse(ch))
