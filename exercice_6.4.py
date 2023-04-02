#  Programme qui permette d’encoder des valeurs dans une liste. Ce pro- gramme devrait fonctionner en boucle, l’utilisateur étant invité à entrer sans cesse de nouvelles valeurs, jusqu’à ce qu’il décide de terminer en frappant <Enter> en guise d’en- trée. Le programme se terminerait alors par l’affichage de la liste. Exemple de fonc- tionnement :
# Veuillez entrer une valeur: 25
# Veuillez entrer une valeur: 18
# Veuillez entrer une valeur: 6284
# Veuillez entrer une valeur:
#     [25, 18, 6284]

liste = []

print("Pour stopper, appuyer sur Entrée sans saisir de valeur")

arret = 0
while arret == 0:
    valeur_saisie = input("Veuiller saisir une valeur :")
    if len(valeur_saisie) > 0:
        liste.append(valeur_saisie)
    else:
        arret = 1

print(liste)