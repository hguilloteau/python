# programme de jeu fonctionnant de la manière suivante : une balle se déplace au hasard sur un canevas, à vitesse faible. Le joueur doit essayer de cliquer sur cette balle à l’aide de la souris. S’il y arrive, il gagne un point, mais la balle se déplace désormais un peu plus vite, et ainsi de suite. Arrêter le jeu après un certain nombre de clics et afficher le score atteint

from tkinter import *
from random import randrange
# définition des gestionnaires
# d'événements :


def move():
    "déplacement de la balle"
    global x1, y1, dx, dy, flag
    x1, y1 = x1 + dx, y1 + dy
    if x1+dim_ball > lg:
        # => génère un nombre aléatoire pour déterminer le nouveau mouvement de la balle
        dx = randrange(-16, -2, 2)
        dy = randrange(2, 16, 2)
        x1 = lg-dim_ball
        can1.itemconfig(oval1, fill='blue')
    if y1+dim_ball > ht:
        dx = randrange(-16, -2, 2)
        dy = randrange(-16, -2, 2)
        y1 = ht-dim_ball
        # y1, dx, dy = ht-dim_ball, -15, -5
        can1.itemconfig(oval1, fill='orange')
    if x1 < 0:
        dx = randrange(2, 16, 2)
        dy = randrange(-16, -2, 2)
        x1 = 0
        # x1, dx, dy = 0, 5, -15
        can1.itemconfig(oval1, fill='green')
    if y1 < 0:
        dx = randrange(2, 16, 2)
        dy = randrange(2, 16, 2)
        y1 = 0
        # y1, dx, dy = 0, 15, 5
        can1.itemconfig(oval1, fill='red')
    can1.coords(oval1, x1, y1, x1+dim_ball, y1+dim_ball)
    if flag > 0:
        # => boucler, après 50 millisecondes
        fen1.after(lag, move)


def stop_it():
    "arrêt de l'animation"
    global flag
    flag = 0


def detectionclic(event):
    "détection du clic de souris sur le canevas et vérifier si on clique sur la balle"
    global x1, y1, shoot, shoot_ko, lag
    # vérifier si le clic était sur le cercle et que la balle bouge
    if flag == 1:
        if event.x >= x1 and event.x <= x1+30:
            if event.y >= y1 and event.y <= y1+30:
                shoot = shoot + 1
                lag = lag - 10
                if lag <= 10:
                    lag = 10
            else:
                shoot_ko = shoot_ko + 1
        else:
            shoot_ko = shoot_ko + 1
        chaine.configure(
            text="Nombre de clics sur la balle : " + str(shoot))
        chaine2.configure(
            text="sur " + str(shoot + shoot_ko) + " clic(s) au total")


def start_it():
    "démarrage de l'animation"
    global flag
    # si on enlève ce test, on lance plusieurs fonctions move en parallèle ce qui provoque le déplacement plus rapide de la balle
    if flag == 0:  # pour ne lancer qu’une seule boucle
        flag = 1
        move()


# ========== Programme principal =============
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10
dx, dy = 15, 5  # déplacement rectiligne si un d nul, si 2 valeurs, déplacement oblique
flag = 0
# dimension canevas
lg = 800
ht = 600
# temps d'attente qui donne la vitesse de déplacement
lag = 200
# taille de la balle
dim_ball = 30
# nombre de clic sur la balle
shoot = 0
shoot_ko = 0
# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "enfants" :
can1 = Canvas(fen1, bg='dark grey', height=ht, width=lg)
can1.pack(side=LEFT, padx=5, pady=5)
# détection de clic dans le canvas
can1.bind("<Button-1>", detectionclic)
oval1 = can1.create_oval(x1, y1, x1+dim_ball, y1+dim_ball, width=2, fill='red')
bou1 = Button(fen1, text='Quitter', width=8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Démarrer', width=8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arrêter', width=8, command=stop_it)
bou3.pack()
chaine = Label(fen1)
chaine.configure(text="Nombre de clic sur la balle = 0")
chaine.pack()
chaine2 = Label(fen1)
chaine2.configure(text="Ratio clic réussi")
chaine2.pack()
# démarrage du réceptionnaire d'événements (boucle principale) :
fen1.mainloop()
