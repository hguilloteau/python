# Script qui compte le nombre d’occurrences du caractère « e » dans une chaîne

ch = "combien y a-t-il de e dans cette chaine"
lg_ch = len(ch)
car_cherche = "e"
nbre_car_cherche = 0

i = 0
while i < lg_ch: # une chaine de N caractères a un index de 0 à N-1
    if ch[i] == car_cherche:
        nbre_car_cherche = nbre_car_cherche + 1
    i = i+1

print("il y a",nbre_car_cherche,"e dans cette chaine de",lg_ch,"caractères")