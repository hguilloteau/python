# Programme qui convertit un nombre entier de secondes fourni au départ en un nombre d’années, de mois, de jours, de minutes et de secondes (utilisez l’opérateur modulo : %)
nbre_secondes_par_heure = 60 * 60
nbre_secondes_par_jour = nbre_secondes_par_heure * 24
nbre_secondes_par_mois = nbre_secondes_par_jour * 30
nbre_secondes_par_annee = nbre_secondes_par_jour * 365

nbre_secondes_initial = 12345678912
nbre_secondes = nbre_secondes_initial


annee = nbre_secondes // nbre_secondes_par_annee
nbre_secondes = nbre_secondes % nbre_secondes_par_annee

mois = nbre_secondes // nbre_secondes_par_mois
nbre_secondes = nbre_secondes % nbre_secondes_par_mois

jour = nbre_secondes // nbre_secondes_par_jour
nbre_secondes = nbre_secondes % nbre_secondes_par_jour

heure = nbre_secondes // nbre_secondes_par_heure
nbre_secondes = nbre_secondes % nbre_secondes_par_heure

minute = nbre_secondes // 60
nbre_secondes = nbre_secondes % 60



print("dans " , nbre_secondes_initial , " secondes")
print("il y a :")
print(" - ", annee , " année(s)")
print(" - " , mois , "mois") 
print(" - " , jour , "jour(s)") 
print(" - " , heure , "heure(s)")
print(" - " , minute , "minute(s)")
print("et il reste " , nbre_secondes , " seconde(s)")