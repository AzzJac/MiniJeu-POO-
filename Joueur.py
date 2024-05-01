from De import *


class joueur:
    nom = ""
    pv = 10
    deJ = de
    monstre1 = 0
    monstre2 = 0

    def __init__(self, pv):
        self.pv = pv
        self.deJ = de
        self.monstre1 = 0
        self.monstre2 = 0

    def EstVivant(self):
        if self.pv > 0:
            print("Le joueur est mort")

    def JeterDe(self):
        resultat = self.deJ.jeterDe()
        print("de Joueur = " + str(resultat))
        return resultat

    def Attaquer(self, monstre):
        monstre.RecoitDegat
        if monstre.nom == "monstre 1":
            self.monstre1 += 1
        else:
            self.monstre2 += 1

    def RecoitDegat(self, valeurDegat):
        self.pv -= valeurDegat

    def CompterScore(self):
        print("Vous été tué ...")
        print("Bravo, vous avez gagné et tué " + str(self.monstre1) + " monstres de niveau 1 et " + str(self.monstre2) + " monstres de niveau 2.")
        print("Vous avez gagné " + str(self.monstre1 + self.monstre2) + " points.")

    def Bouclier(self):
        result = self.JeterDe()
        if result <= 2:
            self.RecoitDegat(0)
        else:
            self.RecoitDegat(10)
