# -*-coding:utf-8 -*-
# Joueur


# Specification fonctionnelle du type Joueur

# en initilisant ce joueur c-à-d en lui donnant :
#   - une pioche contenant 20 cartes, 
#   - une main contenant uniquement une carte Roi du type correspond à l'id reçu en param
#   - un champ de bataille vide
#	- Un nom en fonction de l'id : "joueur + id" 
# Liste des fonctions appelees :
#   creerMain, creerPioche, creerCarte, creerChampDeBataille, creerCimetiere, creerRoyaume, creerReserve
# x->Joueur
#
def creerJoueur(id):
  return 0

# Renvoie la main du joueur
# Joueur -> Main
def getMainJoueur (joueur) :
	return 0

# Joueur -> Pioche
def getPiocheJoueur (joueur) :
	return 0

# Joueur -> ChampDeBataille
def getChampDeBatailleJoueur (joueur) :
	return 0

# Joueur -> Cimetiere
def getCimetiereJoueur (joueur) :
	return 0

# Joueur -> Royaume
def getRoyaumeJoueur (joueur) :
	return 0

# Joueur -> Reserve
def getReserveJoueur (joueur) :
	return 0

def getNomJoueur (joueur) : 
	return 0

# place une carte de la main du joueur dans son champs de bataille
# pre : la placeCarteMain doit etre plus petit que le nombre de carte dans la main
# 		Les coordonnees doivent être valides
# Liste des fonctions appelees :
#	demanderCarteJoueur, placerCarteCDB
# Joueur*int*Coordonnees->x
def placerCarteMainCDB (joueur, placeCarteMain, coordonnees) :
	carte = joueur.main.enleverCarte(placeCarteMain)
	joueur.cdb.placerCarte (carte, coordonnees)



# place une carte de la main du joueur dans son champs de bataille
# Liste des fonctions appelees :
#	demanderCarteJoueur, placerCarteCDB
# Joueur*Coordonnees->x
def placerCarteReserveCDB (joueur, coordonnees) :
	carte = joueur.reserve.enleverCarte()
	joueur.cdb.placerCarte (carte, coordonnees)


# Renvoie la carte à l'emplacement demandé dans la main
# pre : placeCarteMain est plus petit que le nombre de carte dans la main
# Joueur * int -> carte
def demanderCarteJoueur (joueur, placeCarteMain) :
	return 0
	

