# Script qui détermine si une chaîne contient ou non le caractère « e »

ch = "y a-t-il un e dans cette chaine"
lg_ch = len(ch)
car_cherche = "e"

i = 0
while i < lg_ch: # une chaine de N caractères a un index de 0 à N-1
    if ch[i] == car_cherche:
        print("il y a un e dans cette chaine à la position",i)
    i = i+1