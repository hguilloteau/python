# Modifiez le script ci-dessus de manière à faire apparaître un petit cercle rouge à l’endroit où l’utilisateur a effectué son clic(vous devrez d’abord remplacer le widget Frame par un widget Canvas).
# Détection et positionnement d'un clic de souris dans une fenêtre :
from tkinter import *


def pointeur(event):
    chaine.configure(text="Clic détecté en X =" + str(event.x) +
                     ", Y =" + str(event.y))
    cadre.create_oval(event.x-5, event.y-5, event.x+5,
                      event.y+5, width=1, outline="black")


fen = Tk()
cadre = Canvas(fen, width=400, height=400, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()
