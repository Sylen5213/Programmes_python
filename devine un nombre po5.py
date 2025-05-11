import random

nbr_secret = random.randint(1, 100)
INVITE = "propose un nombre. "

def jouer_tour():
    while True:
        nbr_joueur = input(INVITE)
        if nbr_secret == int(nbr_joueur):
            print("Correct !")
            break
        elif nbr_secret > int(nbr_joueur):
            print("Trop petit !")
        else:
            print("Trop grand !")

jouer_tour()
exit()
