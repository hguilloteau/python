# programme qui convertisse en mètres par seconde et en km/h une vitesse fournie par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)

v_miles = input("Donner la vitesse en miles par heure :")

v_km = float(v_miles) * 1.609

print("Vitesse en miles par heure :", v_miles)
print("Vitesse en km par heure :", v_km)
