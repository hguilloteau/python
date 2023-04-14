# 6.13 ConvertirunenotescolaireNquelconque,entréeparl’utilisateursousformedepoints
# (par exemple 27 sur 85), en une note standardisée suivant le code ci-dessous:
#     Note                Appréciation
#     N >= 80 % A
#     80 % > N >= 60 % B
#     60 % > N >= 50 % C
#     50 % > N >= 40 % D
#     N < 40 % E

print("Combien de points avez vous obtenus ?")
points = float(input())

print("Sur combien de points étaient l'exercice ?")
points_max = float(input())

pourcentage = points / points_max

if pourcentage >= 0.8:
    print("Vous avez eu un A")
elif pourcentage >= 0.6:
    print("Vous avez eu un B")
elif pourcentage >= 0.5:
    print("Vous avez eu un C")
elif pourcentage >= 0.4:
    print("Vous avez eu un D")
else:
    print("Vous avez eu un E")
