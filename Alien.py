aliens = 2
motdepasse = "ALIENS"
print("Vite ! Des aliens attaquent notre planète !")
print("Tu dois activer le réseau de défense mondiale !")
print("J'espère que tu connais le mot de passe ...")
print()
print("-----------------------------------------------------------------------")
print("             BIENVENUE DANS LE RESEAU DE DEFENSE MONDIALE              ")
print("-----------------------------------------------------------------------")
print()
deviner = input("ENTRE LE MOT DE PASSE :  ").upper()
while deviner != motdepasse:
    print()
    print("MOT DE PASSE INCORRECT")
    print()
    aliens = aliens ** 2
    print("Il y a ", aliens, "aliens sur terre réessaie")
    if aliens > 8000000000:
        break
    print()
    print("Indice sur le mot de passe : Les créatures qui nous attaquent")
    print()
    deviner = input("vite entre le mot de passe : ").upper()
if aliens > 8000000000:
    print("Game Over il y a plus d'aliens que d'humains")
else:
    print("Hourra tu as réussi")
