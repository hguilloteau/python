# Programme qui demande à l’utilisateur d’entrer des notes d’élèves. La boucle se terminera seulement si l’utilisateur entre une valeur négative. Avec les notes ainsi entrées, construire progressivement une liste. Après chaque entrée d’une nouvelle note (et donc à chaque itération de la boucle), afficher le nombre de notes entrées, la note la plus élevée, la note la plus basse, la moyenne de toutes les notes.

nb = 0
moy = 0

arret = 0
premiere_note = 1

while not arret:
    note = float(input("Vauillez entrer une note - tapez une note négative pour arrêter : "))
    if note < 0:
        arret = 1
    else:
        # initialisation du min et du max lors de la première note saisie
        if premiere_note:
            max = note
            min = note
            premiere_note = 0
        
        if note < min:
            min = note

        if note > max:
            max = note
        
        moy = ((moy*nb)+note)/(nb+1)

        nb = nb + 1

        print("Note max :", max)
        print("Note min :", min)
        print("Note moyenne :", moy)
        print("Nombre de notes", nb)