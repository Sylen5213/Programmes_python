
def main():
    # recolter une première note
    note1 = int(input("entrer une première note"))
    # récolter un deuxième note
    note2 = int(input("entrer une deuxième note"))
    # récolter une dernière note
    note3 = int(input("entrer une troisième note"))
    note4 = int(input("entrer une quatrième note"))
    note5 = int(input("entrer une cinquième note"))
    # calculer la moyenne
    result = (note1 + note2 + note3 + note4 + note5) / 5
    # afficher le résultat
    print("la moyenne est " + str(result))

if __name__ == '__main__':
    main()
