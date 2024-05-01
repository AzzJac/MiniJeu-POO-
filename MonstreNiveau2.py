from MonstreNiveau1 import *


class monstre2 (MonstreLvl1):
    sort = 0
    dégât = 0
    estVivant = True
    deM = de
    nom = "monstre 2"

    def __init__(self, dégatSort, dégat):
        super().__init__(10)
        self.sort = dégatSort
        self.dégât = dégat
        self.deM = de
        self.nom = "monstre 2"

    def Attaquer(self, joueur):
        super().Attaquer(joueur)
        result = super().JeterDe()
        if result == 6:
            joueur.Bouclier()
