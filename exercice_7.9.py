#  fonction compteCar(ca,ch) qui renvoie le nombre de fois que l’on ren- contre le caractère ca dans la chaîne de caractères ch. Par exemple, l’exécution de l’instruction :
# print(compteCar(’e’, ’Cette phrase est un exemple’)) doit donner le résultat: 7

def compteCar(ca, ch):
    "Renvoie le nombre de fois que l’on rencontre le caractère ca dans la chaîne de caractères ch"
    lg = len(ch)
    i = 0
    n = 0
    while i < lg:
        if ch[i] == ca:
            n = n + 1
        i = i + 1
    return n


ph = "Cette phrase est un exemple"
ca = 'e'
print("Le nombre de", ca, "dans cette phrase -", ph, "- est :", compteCar(ca, ph))
