import random
#import time

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.etat = "bonne sante"
        self.jours_sans_manger = 0
        self.jours_sans_dormir = 0
        self.jours_malade = 0
        self.inventaire = []

    def dormir(self):
        self.jours_sans_dormir = 0
        if self.etat == "malade":
            self.jours_malade += 1
            if self.jours_malade == 3:
                self.etat = "bonne sante"
                self.jours_malade = 0
        return f"{self.nom} a dormi"

    def chercher_nourriture(self):
        trouve = random.choices(
            ["Fruits", "Poisson", "Champignons", "Rien", "Rien"],
            [1, 1, 1, 2, 2]
        )[0]
        if trouve != "Rien":
            self.inventaire.append(trouve)
        return f"{self.nom} a recuperer {trouve}."

    def manger(self):
        if not self.inventaire:
            return f"{self.nom} n'a rien a manger"
        print(f"Inventaire de {self.nom}: {', '.join(self.inventaire)}")
        choix = input("quel aliment vous voulez manger? ")
        while choix not in self.inventaire:
            print("Choix non valide")
            choix = input("quel aliment vous voulez manger? ")
        self.inventaire.remove(choix)
        if choix == "Champignons":
            self.etat = "malade"
        self.jours_sans_manger = 0
        return f"{self.nom} a manger {choix}."

    def passer_jour(self):
        self.jours_sans_manger += 1
        self.jours_sans_dormir += 1
        if self.etat == "malade" and self.jours_malade == 2:
            self.etat = "mort"
        if self.jours_sans_manger == 2 or self.jours_sans_dormir == 2:
            self.etat = "mort"
        return self.etat
    
    
def jeu_survie():
    nathan = Personnage("Nathan")
    drake = Personnage("Drake")
    actions = {
        "dormir": Personnage.dormir,
        "chercher": Personnage.chercher_nourriture,
        "manger": Personnage.manger
        }
        
    with open("survie.txt", "w") as f:
        for jour in range(1,8):
            f.write(f"Jour {jour}\n")
            for i in range(1,4): 
                for personnage in [nathan, drake]:
                    if personnage.etat != "mort":
                        print(f"Actions disponibles pour {personnage.nom}: dormir, chercher, manger")
                        choix = input(f"Quelle action {personnage.nom} doit effectuer? ")
                        while choix not in actions:
                            print("Action non valide")
                            choix = input(f"Quelle action {personnage.nom} doit effectuer? ")
                        resultat = actions[choix](personnage)
                        f.write(resultat + "\n")
            nathan.passer_jour()
            drake.passer_jour()
            if nathan.etat == "mort" and drake.etat == "mort":
                f.write("les deux personnage sont mort\n")
                break
        if nathan.etat != "mort":
            f.write(f"{nathan.nom} a survécu les 7 jour\n")
        if drake.etat != "mort":
            f.write(f"{drake.nom} a survécu les 7 jour\n")

if __name__ == "__main__":
    jeu_survie()
                
                    
