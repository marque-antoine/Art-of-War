import random
# Pioche


#CrÃ©e une pioche
def creer_pioche():
    return []

#true si vide, false sinon
#pioche -> bool
def piocheVide(pioche):
    return len(pioche) == 0

#Renvoie la taille de la pioche en paramètre(nbcartes)
#pioche -> int 
def getTaillePioche(pioche):
    return len(pioche)
   

#Pioche une carte
def piocher(Joueur): 
    return 0
   
#Melange la pioche
#pioche -> pioche
def melanger_pioche(pioche):
	random.shuffle(pioche)
    return 0
   
