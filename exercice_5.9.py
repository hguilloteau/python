# Script qui recopie une chaîne (dans une nouvelle variable) en l’inversant. Ainsi par exemple, « zorglub » deviendra « bulgroz »

ch = "il faut le mettre à l'envers"
ch_inversee = ""
lg_ch = len(ch)

i = 0
while i < lg_ch:
    i = i+1
    ch_inversee = ch_inversee + ch[lg_ch-i]

print("chaine à l'endroit :",ch)
print("chaine à l'envers :",ch_inversee)