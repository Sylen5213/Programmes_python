import random
nombre = random.randint(1,20)
deviner = int(input("Je pense à un nombre entre 1 et 20, essaie de le deviner."))

while deviner != nombre:
    if deviner < nombre:
        print("Ton nombre est tros bas...")
    else:
        print("Ton nombre est trop haut...")
    deviner = int(input("Essaie à nouveau..."))
print("Félicitations, tu as réussi !")
