### sections imports
import pickle as saumure
import os.path

### sections constantes
Nomfic_SAUVE = "carnet_pickle"
QUIT_CONFIRMER = "Voulez-vous vraiment quitter ? (O/N) "
INSTRUCTIONS = """
*********************************************
        Application Carnet d'Adresses
*********************************************
A pour Ajouter une personne;
L pour la Liste des fiches du carnet;
S pour Supprimer une fiche;
I pour revoir ces Instructions;
Q pour Quitter.
"""

# section classes
class CarnetAdr(object):
    def __init__(self):
        self.gens = []

    def ajouter_fiche(self, fiche_nouvo):
        self.gens.append(fiche_nouvo)

    def supprimer_fiche(self, index):
        if 0 <= index < len(self.gens):
            fiche = self.gens.pop(index)
            return fiche
        else:
            return None

    def sauver(self):
        with open(Nomfic_SAUVE, 'wb') as ficow:
            saumure.dump(self, ficow)

class FicheAdr(object):
    def __init__(self, prenom=None, nomfami=None, datenaiss=None, courriel=None):
        self.prenom = prenom
        self.nomfami = nomfami
        self.datenaiss = datenaiss
        self.courriel = courriel

    def __repr__(self):
        patron = "FicheAdr(prenom = '%s', nomfami = '%s', datenaiss = '%s', courriel = '%s')"
        return patron % (self.prenom, self.nomfami, self.datenaiss, self.courriel)

class Kontroleur(object):
    def __init__(self):
        self.carnet_adr = self.charger()
        if self.carnet_adr is None:
            self.carnet_adr = CarnetAdr()

    def charger(self):
        if os.path.exists(Nomfic_SAUVE):
            with open(Nomfic_SAUVE, 'rb') as ficor:
                return saumure.load(ficor)
        else:
            return None

    def gerer_menu(self):
        print(INSTRUCTIONS)
        while True:
            cmd = input("(a)jout, (l)iste, (s)upprimer, (i)nstr., (q)uitter : ")
            if cmd.lower() == "a":
                self.ajouter_fiche()
            elif cmd.lower() == "q":
                if confirmer_quitter():
                    print("Sauvegarde…")
                    self.carnet_adr.sauver()
                    print("Fin de l'application.")
                    break
            elif cmd.lower() == "i":
                print(INSTRUCTIONS)
            elif cmd.lower() == "l":
                self.lister_fiches()
            elif cmd.lower() == "s":
                self.supprimer_fiche()
            else:
                print(f"*** Touche de commande inconnue ({cmd}) !")

    def ajouter_fiche(self):
        print("Ajout d'une nouvelle fiche :")
        prenom = input("Prénom : ")
        nomfami = input("Nom de famille : ")
        datenaiss = input("Date de naissance (JJ/MM/AAAA) : ")
        courriel = input("Courriel : ")
        fiche = FicheAdr(prenom, nomfami, datenaiss, courriel)
        self.carnet_adr.ajouter_fiche(fiche)
        print("Fiche ajoutée.")

    def lister_fiches(self):
        print("Liste des fiches du carnet :")
        if not self.carnet_adr.gens:
            print("Aucune fiche enregistrée.")
        else:
            for idx, fiche in enumerate(self.carnet_adr.gens):
                print(f"{idx}. {fiche}")

    def supprimer_fiche(self):
        if not self.carnet_adr.gens:
            print("Aucune fiche à supprimer.")
            return

        self.lister_fiches()
        try:
            index = int(input("Entrez le numéro de la fiche à supprimer : "))
            fiche_supprimee = self.carnet_adr.supprimer_fiche(index)
            if fiche_supprimee:
                print(f"Fiche supprimée : {fiche_supprimee}")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un chiffre.")

### Sections fonctions
def confirmer_quitter():
    confi = input(QUIT_CONFIRMER)
    return confi.lower() != "n"

# Section principale main
if __name__ == "__main__":
    controleur = Kontroleur()
    controleur.gerer_menu()
