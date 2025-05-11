# Place de cinema

# récolter l'âge de la personne
age = int(input("Quel est votre age ?"))

# si la personne est mineur -> 7€
if age < 18:
    prix_total = 7
# si la personne est majeur -> 12€
else:
    prix_total = 12

# souhaitez-vous du pop corn ?
pop_corn = input("Souhaitez-vous du pop corn ? (Oui, Non)")

# si oui
if pop_corn == "Oui":
    prix_total += 5

print("Vous devez payer", prix_total, "€")