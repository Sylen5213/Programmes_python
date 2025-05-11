
# exemple: Systeme de vérification de mots de passe
password = input("entrez votre mot de passe")
password_lenght = len(password)

if password_lenght <= 8:
    print("mot de passe trop court !")
elif 8 < password_lenght <= 12:
    print("mot de passe moyen ! ")
else:
    print("mot de passe parfait !")

print(password_lenght)