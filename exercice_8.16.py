# Écrivez un petit programme qui fait apparaître une fenêtre avec deux champs:l’un indique une température en degrés Celsius, et l’autre la même température exprimée en degrés Fahrenheit. Chaque fois que l’on change une quelconque des deux températures, l’autre est corrigée en conséquence. Pour convertir les degrés Fahrenheit en Celsius et
# vice-versa, on utilise la formule T F =T C ×1,80+32 . Revoyez aussi le petit programme concernant la calculatrice simplifiée (page 94).

# Exercice utilisant la bibliothèque graphique tkinter et le module math
from tkinter import *
from math import *
# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :


# def evaluer(event):
#     chaine1.configure(text="Résultat = " + str(eval(entree.get())))

def evaluercelsius(event):
    "Analyse la sasie de la température en Celsius et convertit en Fahrenheit"
    resultat = eval(celsius.get()) * 1.8 + 32
    fahreneit.insert(0, str(round(resultat, 2)))


def evaluerfahreneit(event):
    "Analyse la sasie de la température en Fahrenheit et convertit en Celsius"
    resultat = (eval(fahreneit.get()) - 32) / 1.8
    celsius.insert(0, str(round(resultat, 2)))


# ----- Programme principal : -----
fen1 = Tk()

chaine1 = Label(fen1)
chaine1.configure(text="Température en degré celsius")
chaine1.grid(row=1, column=1, sticky=E)
celsius = Entry(fen1)
celsius.bind("<Return>", evaluercelsius)
celsius.grid(row=1, column=2)
chaine2 = Label(fen1)
chaine2.configure(text="Température en degré fahreneit")
chaine2.grid(row=2, column=1, sticky=E)
fahreneit = Entry(fen1)
fahreneit.bind("<Return>", evaluerfahreneit)
fahreneit.grid(row=2, column=2)

fen1.mainloop()
