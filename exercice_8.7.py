# a) Créez un court programme qui dessinera les 5 anneaux olympiques dans un rec - tangle de fond blanc(white). Un bouton « Quitter » doit permettre de fermer la fe - nêtre.
# b) Modifiez le programme ci-dessus en y ajoutant 5 boutons. Chacun de ces boutons provoquera le tracé de chacun des 5 anneaux

# Import bibliothèque graphique tkinter
from tkinter import *


# def drawcircle():
#     "Tracé des 5 anneaux olympiques"
#     # global x1, y1, x2, y2, coul
#     can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
#     # modification des coordonnées pour la ligne suivante :
#     y2, y1 = y2+10, y1-10


# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
# coordonnées des anneaux
coord = [[100, 80], [220, 80], [340, 80], [150, 160], [270, 160]]
# palette de couleur des anneaux
pal = ['blue', 'black', 'red', 'yellow', 'green']
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='white', height=300, width=500)
can1.pack(side=TOP)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
# bou2 = Button(fen1, text='Tracer une ligne',
#               command=lambda: drawline(x1, y1, x2, y2, coul))
# bou2.pack()
# bou3 = Button(fen1, text='Dessiner Anneaux', command=drawRings)
# bou3.pack()

i = 0
nb = len(pal)
while i < nb:
    can1.create_oval(coord[i][0], coord[i][1], coord[i]
                     [0]+120, coord[i][1]+120, width=4, outline=pal[i])
    i = i + 1

fen1.mainloop()     # démarrage du réceptionnaire d’événements
fen1.destroy()      # destruction (fermeture) de la fenêtre
