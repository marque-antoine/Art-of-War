# -*-coding:utf-8 -*-
# Carte 

# Spécification fonctionnelle du type Carte


# Renvoie la valeur d'attaque de la carte.
def getValeurAttaque (carte, main) :
	return 0

def getVie (carte) :
	return 0


# Crée un soldat qui comme caracteristiques :
#	2 de defense en position defensive
#	1 de defense en position offensive
#	1 case devant lui pour sa portee
#	Autant de point d'attaque que de cartes dans la main du joueur
def creerSoldat () :
	return 0

# Crée un garde qui comme caracteristiques :
#	3 de defense en position defensive
#	2 de defense en position offensive
#	1 case devant lui pour sa portee
#	1 d'attaque
def creerGarde () :
	return 0

# Crée un archer qui comme caracteristiques :
#	2 de defense en position defensive
#	1 de defense en position offensive
#	4 cases devant lui qui serait les cases d'arrivee par un mouvement de cavalier aux echecs
#	1 d'attaque
def creerArcher () :
	return 0

# Cette fonction peut creer deux rois selon le nombre reçu en parametre. Si le nombre est 1 alors elle renvoie un roi avec les caracteristiques suivantes :
#	4 de defense en position defensive
#	4 de defense en position offensive
#	4 cases de portees, 1 devant lui, 1 en diagonale à gauche, une en diagonale a droite et 1 deux cases devant lui
#	1 d'attaque
# Le deuxieme roi aura comme caracteristiques :
#	5 de defense en position defensive
#	4 de defense en position offensive
#	3 cases de portees, 1 devant lui, 1 en diagonale à gauche, une en diagonale a droite
#	1 d'attaque
# int -> Carte
def creerRoi (id) :
	return 0

# retourne le nom de la carte en chaine de caracteres
def toStringNomCarte (carte) :
	return 0

# Renvoie true si la carte est un roi est false sinon
# carte -> bool
def estRoi(carte) :
	return 0






