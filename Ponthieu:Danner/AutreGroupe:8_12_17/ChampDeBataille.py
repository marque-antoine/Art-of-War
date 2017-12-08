
# ChampDeBataille


#Crée le cdb du joueur en paramètre,
#les positions du champ de bataille de définissent de la façon suivante:
#  | 1       |  2       |   3
#F | carte   | carte    | carte
#A | carte   | carte    | carte
# exemple: la position "F1" est la position au front à gauche
#Joueur-> ChampDeBataille
def creer_ChampDeBataille(Joueur): 
    return 0

#affiche le cdb de la manière suivante
#  | 1       |  2       |   3
#F | carte   | carte    | carte
#A | carte   | carte    | carte
# Les mots cartes doivent etre remplaces par le nom de la carte presente 
#dans la case sinon pas de carte mettre : VIDE
#ChampDeBataille -> x
def afficherCDB (cdb) :
    return 0

#Recupere les cartes du champ de bataille passe en parametre
#ChampDeBataille -> x
def getCartes(ChampDeBataille): 
    return 0

#Si le champ de bataille passe en parametre est vide, renvoie true, false le cas échéant
#ChampDeBataille -> bool
def cdbVide(ChampDeBataille): 
    return 0


#Reinitialie les points de vie des unites
#Remet les cartes en position defensive
def reinitilisationCDB(ChampDeBataille): 
    return 0

#Renvoie true si la position passee en parametre est occupee, false le cas echeant
#ChampDeBataille x position -> bool
def positionOccupee(ChampDeBataille,position): 
    return 0

#Affichage des cartes du champ de bataille a la portee de la carte en parametre  
#carte x ChampDeBataille -> x
def getAportee(carte,ChampDeBataille): 
    return 0

#Place la carte en parametre sur la position, et met la carte qui était à cette position à la fin de la réserve
def remplacerCarte(carte,position,ChampDeBataille): 
    return 0


#Passe une carte du champ de bataille au cimetiere
def cdb_vers_cimetiere(ChampDeBataille,carte): 
    return 0
    
#Avance la carte a l'arriere du champ de bataille dans le cas ou celle devant a ete tuee
#La carte en parametre est la carte a avancer et pas la carte a tuer    
def Avancer(ChampDeBataille,carte): 
    return 0
   

    