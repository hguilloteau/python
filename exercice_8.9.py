# 8.9 Inspirez-vous du script précédent pour écrire une petite application qui fait apparaître un damier (dessin de cases noires sur fond blanc) lorsque l’on clique sur un bouton
# 8.10 À l’application de l’exercice précédent, ajoutez un bouton qui fera apparaître des pions au hasard sur le damier (chaque pression sur le bouton fera appa- raître un nouveau pion).

# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange

# Variable pour définir la taille du cases du damier et du nombre de cases
largeur = 50
nb_cases = 10
taille_canvas = largeur * nb_cases


def damier():
    "Fonction qui dessine un damier"
    i = 0  # lignes
    while i < nb_cases:
        j = 0  # colonnes
        while j < nb_cases:
            # Pour un rectangle x1 y1 coin supérieur gauche x2 y2 coin inférieur droit
            # can1.create_rectangle(x1, y1, x2, y2, width=2, fill=coul)
            if i % 2 == 0:  # en fonxtion de ligne, il ne faut pas faire les cases dans le même ordre
                if j % 2 == 0:
                    can1.create_rectangle(j*largeur, i*largeur, (j+1)*largeur,
                                          (i+1)*largeur, width=1, fill="black")
            else:
                if (j+1) % 2 == 0:
                    can1.create_rectangle(j*largeur, i*largeur, (j+1)*largeur,
                                          (i+1)*largeur, width=1, fill="black")
            j = j + 1
        i = i + 1


def pion():
    "Dessiner un pion sur le damier"
    # => génère un nombre aléatoire pour déterminer la position du pion
    l = randrange(nb_cases - 1)
    c = randrange(nb_cases - 1)
    can1.create_oval(l*largeur, c*largeur, (l+1)*largeur,
                     (c+1)*largeur, width=1, fill="red")


# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='white', height=taille_canvas, width=taille_canvas)
can1.pack(side=TOP)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=RIGHT)
boucircle1 = Button(fen1, text='Damier', command=damier)
boucircle1.pack(side=LEFT)
boucircle1 = Button(fen1, text='Ajouter pion', command=pion)
boucircle1.pack(side=LEFT)

fen1.mainloop()     # démarrage du réceptionnaire d’événements
fen1.destroy()      # destruction (fermeture) de la fenêtre
