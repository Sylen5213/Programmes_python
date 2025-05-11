import random
choixSortie = "Rien"
while choixSortie != "QUITTER":
    print("Tu te trouves dans une pièce sombre d'un mystérieux château.")

    print("Tu dois choisir entre quatre portes")

    choixjoueur = input("Choisis 1, 2, 3 ou 4...")

    if choixjoueur == "1":
        print("Tu vois un couloir, Tu as le choix entre :")
        print("1)Continuer.")
        print("2)Rebrousser chemin.")
        choixcouloir = input("Coisis entre : 1 et 2")

    if choixjoueur == "2":
        print("La porte s'ouvre et un ogre affamé te donne un coup de massue et te dévore.")
        print("GAME OVER, TU AS PERDU !")
    
    elif choixjoueur == "3":
        print("Il y a un dragon affamé derrière la porte.")
        print("tu peux soit...")
        print("1) Essayer de voler l'or du dragon.")
        print("2) Essaye de t'enfuir avec une des griffes du dragon qui vaut beaucoup d'argent.")
        print("3) Essaye de rester et de faire ami-ami avec le dragon.")
        print("4) Essaye de tuer le dragon avec une épée qui se trouve dans le trésor")
        choixdragon = input("Entre 1, 2, 3 ou 4")
        if choixdragon == "1":
            print("Le dragon se réveille et te manges.")
            print("GAME OVER, TU AS PERDU !")
        elif choixdragon == "2":
            print("Tu trouves à terre une des griffes du dragon et t'enfuis avec. Tu la revends et tu es riche !")
            print("BRAVO, TU AS GAGNÉ !")
        elif choixdragon == "3":
            print("Tu réussis a être ami avec le dragon mais il te grille sans le faire exprès.")
            print("GAME OVER, TU AS PERDU !")
        else:
            print("Tu réussi à tuer le dragon et empoche son trésor.")
            print("BRAVO, TU AS GAGNÉ !")
    else:
        print("Tu entres dans une pièce où se trouve un sphinx.")
        print("Il te demandes de trouver le nombre auquel il pense, entre 1 et 10.")
        nombre = int(input("Quel chiffre coisis-tu ?"))
        if nombre == random.randint(1,10):
            print("Le sphinx, déçu émet un sifflement. Tu as deviné juste.")
            print("Il doit te laisser partir.")
            print("BRAVO, TU AS GAGNÉ !")
        else:
            print("Le sphinx te dit que tu n'as pas trouvé le bon nombre.")
            print("Tu as le choix entre...")
            print("1) discuter avec le sphinx pour qu'il te laisse partir.")
            print("2)De te faire prisonnier.")
            choixsphinx = input("choisis entre 1 ou 2")
            if choixsphinx == "1":
                print("le sphinx te mange car il ne veut pas discuter.")
                print("GAME OVER! TU AS PERDU!")
    choixSortie = input("Appuie sur la touche Entrée pour rejouer ou tape QUITTER pour arrêter.")
