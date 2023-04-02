# Une légende de l’Inde ancienne raconte que le jeu d’échecs a été inventé par un vieux sage, que son roi voulut remercier en lui affirmant qu’il lui accorderait n’importe quel cadeau en récompense. Le vieux sage demanda qu’on lui fournisse simplement un peu de riz pour ses vieux jours, et plus précisément un nombre de grains de riz suffisant pour que l’on puisse en déposer 1 seul sur la première case du jeu qu’il venait d’inven- ter, deux sur la suivante, quatre sur la troisième, et ainsi de suite jusqu’à la 64e case.
# Programme Python qui affiche le nombre de grains à déposer sur chacune des 64 cases du jeu. Calculez ce nombre de deux manières :
# • le nombre exact de grains (nombre entier) ;

nbre_de_cases = 64
nbre_riz = 1

i = 0
while i < nbre_de_cases:
    i = i+1
    print("case n°",i," :",nbre_riz,"grains de riz")
    nbre_riz = nbre_riz * 2

# • le nombre de grains en notation scientifique (nombre réel).
nbre_riz = 1.0

i = 0
while i < nbre_de_cases:
    i = i+1
    print("case n°",i," :",nbre_riz,"grains de riz")
    nbre_riz = nbre_riz * 2