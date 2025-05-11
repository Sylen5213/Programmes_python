alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

chaîneACrypter = input("S'il te plaît, entre un message a crypter :")

chaîneACrypter = chaîneACrypter.upper()

quantitéDécalage = int(input("S'il te plaît, entre un nombre entier positif ou négatif de 1 à 25 en guise de clé."))
chaîneCryptée = ""
for caractèreActuel in chaîneACrypter:
    position = alphabet.find(caractèreActuel)
    nouvellePosition = position + quantitéDécalage
    chaîneCryptée = chaîneCryptée + alphabet[nouvellePosition]
    print("ton message crypté ou décrypté est ", chaîneCryptée) 
