
print("Bonjour vous êtes sur la caisse automatique de Media-Markt® pou achetez un ordinateur au prix de 2590")

# avoir la valeur du porte monnaie de quelqu'un

wallet = 3000
print("vous avez actuellement " + str(wallet))

# avoir le nom du produit
produit1 = "Ordinateur"

# avoir la valeur du produit
prix_total = 2590

name = (input("Voulez vous MacOS comme système d'exploitation ? (Oui, Non)"))

if name == "Oui":
    prix_total += 200

    print("vous devez payer " + str(prix_total) + "€")

    print("produit acheté ! ")

    wallet = wallet - prix_total

    print("il ne vous reste plus que " + str(wallet) + " €")

elif name == "Non":
    name = (input("Que voulez vous alors ? (Windows, Linux)"))

if name == "Windows":
    prix_total += 150

    print("Vous devez payer " + str(prix_total) + "€")

    print("produit acheté ! ")

    wallet = wallet - prix_total

    print("il ne vous reste plus que " + str(wallet) + " €")

elif name == "Linux":

    print("Vous devez payer " + str(prix_total) + "€")

    print("produit acheté ! ")

    wallet = wallet - prix_total

    print("il ne vous reste plus que " + str(wallet) + " €")