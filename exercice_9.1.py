# Écrivez un script qui permette de créer et de relire aisément un fichier texte. Votre programme demandera d’abord à l’utilisateur d’entrer le nom du fichier. Ensuite il lui proposera le choix, soit d’enregistrer de nouvelles lignes de texte, soit d’afficher le contenu du fichier.
# L’utilisateur devra pouvoir entrer ses lignes de texte successives en utilisant simplement la touche <Enter> pour les séparer les unes des autres. Pour terminer les entrées, il lui suffira d’entrer une ligne vide (c’est-à-dire utiliser la touche <Enter> seule). L’affichage du contenu devra montrer les lignes du fichier séparées les unes des autres de la manière la plus naturelle (les codes de fin de ligne ne doivent pas apparaître).

def sansDC(ligne):
    "Fonction qui renvoie la chaine de caractère amputé du dernier caractère"
    i = 0
    j = len(ligne)-1
    newligne = ""
    while i < j:
        newligne = newligne + ligne[i]
        i = i + 1
    return newligne


def see(file):
    "fonction qui affiche le contenu d'un fichier"
    endfile = 0
    while not endfile:
        ligne = file.readline()
        if ligne == "":
            endfile = 1
        else:
            print(sansDC(ligne))


def insert(file):
    "fonction qui insère des lignes à la fin du fichier"
    fin = 0
    while not fin:
        ligne = input("Taper le texte à ajouter :")
        if ligne != "":
            file.write(ligne + '\n')
        else:
            fin = 1


file_open = 0
# Boucle de saisie du nom du fichier à ouvrir
while not file_open:
    print("Veuillez saisir le nom du fichier à ouvrir :")
    filename = input()
    try:
        file = open(filename, 'r')
        file_open = 1
        file.close
    except:
        print("Fichier inexistant")

# Choix à faire :
# pour lire le contenu du fichier
# pour afficher le contenu

choix = 0
while not choix:
    print("Taper 1 pour voir le contenu du fichier")
    print("Taper 2 pour insérer des lignes dans le fichier")
    c = eval(input())
    if c == 1:
        file = open(filename, 'r')
        see(file)
        file.close()
        choix = 1
    elif c == 2:
        file = open(filename, 'a')
        insert(file)
        file.close()
        choix = 1
