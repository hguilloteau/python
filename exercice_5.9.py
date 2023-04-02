# Script qui recopie une chaîne (dans une nouvelle variable) en l’inversant. Ainsi par exemple, « zorglub » deviendra « bulgroz »

ch = "laval"
ch_inversee = ""
lg_ch = len(ch)

i = 0
while i < lg_ch:
    i = i+1
    ch_inversee = ch_inversee + ch[lg_ch-i]

print("chaine à l'endroit :", ch)
print("chaine à l'envers :", ch_inversee)

# Fin du script qui détermine si une chaîne de caractères donnée est un palindrome (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s ».

if ch == ch_inversee:
    print("On a trouvé un palindrome")
else:
    print("On n'a pas trouvé de palindrome")
