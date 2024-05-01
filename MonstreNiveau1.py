from De import *


class MonstreLvl1:
    nom = "monstre 1"
    dégât = 0
    estVivant = True
    deM = de

    def __init__(self, degat):
        self.dégât = degat
        self.estVivant = True
        self.deM = de
        self.nom = "monstre 1"

    def JeterDe(self):
        resultat = self.deM.jeterDe()
        print("de Monstre = " + str(resultat))
        return resultat

    def Attaquer(self, joueur):
        joueur.Bouclier()

    def RecoitDegat(self):
        print("Le monstre a été vaincu ")
        self.estVivant = False
