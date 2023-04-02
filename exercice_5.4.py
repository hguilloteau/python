# Programme qui calcule les intérêts accumulés chaque année pendant 20 ans, par capitalisation d’une somme de 100 euros placée en banque au taux fixe de 4,3 %

montant_initial = 100
duree = 20 # en années
taux = 4.3

# montant_final = (montant_initial * (1+taux/100)) ** duree

annee = 1
montant_final = montant_initial
while annee <= duree:
    #print("passage n°",annee)
    montant_final = montant_final + montant_final * taux / 100 
    annee = annee + 1
    
print(montant_initial,"déposé pendant",duree,"ans au taux de",taux ,"% donnera",montant_final)