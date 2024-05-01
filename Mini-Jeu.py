from random import *
from Joueur import *
from MonstreNiveau1 import *
from MonstreNiveau2 import *

player = joueur(100)


def FabriqueMonstre():
    resultat = randint(1, 2)
    if resultat == 1:
        monstre = MonstreLvl1(10)
        
    else:
        monstre = monstre2(20, 10)

    print(monstre.nom)
    return monstre





def VerifierValeurDe(Monstre):
    resultat = LancerDe(Monstre)
    if resultat == True:
        player.Attaquer(Monstre)
        Monstre.RecoitDegat()
    elif resultat == False:
        Monstre.Attaquer(player)
       

def LancerDe(Monstre):
    presult = player.JeterDe()
    mresult = Monstre.JeterDe()
    if presult > mresult:
        return True
    elif presult< mresult:
        return False
    elif presult == mresult:
        LancerDe(Monstre)

def Game(pMonstre):
    
    if pMonstre is False:
        pMonstre = FabriqueMonstre()
        Game(pMonstre)
    else:
        while player.pv > 0 and pMonstre.estVivant == True:
            VerifierValeurDe(pMonstre)
            if pMonstre.estVivant == False:
                del pMonstre
                pMonstre = FabriqueMonstre()
            if player.pv <= 0:
                player.CompterScore() 
monstre = False
Game(monstre)