# Demander à l’utilisateur son nom et son sexe (MouF). En fonction de ces données, afficher « Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne

nom = input("Veuillez saisir votre nom ? ")

saisie_ok = 1
while saisie_ok:
    sexe = input("Veuillez saisir votre sexe : M ou F ? ")
    if sexe == "M" or sexe == "F":
        saisie_ok = 0

if sexe == "M":
    print("Cher Monsieur", nom)
else:
    print("Cher Mademoiselle", nom)
