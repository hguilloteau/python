# un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères.
# Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »

ch = "chaine à transformer"
lg_ch = len(ch)
car_ajoute = "*"
ch_transforme = ch[0]

i = 1
while i < lg_ch: # une chaine de N caractères a un index de 0 à N-1
    ch_transforme = ch_transforme + car_ajoute + ch[i]
    i = i+1

print(ch,"\n",ch_transforme)