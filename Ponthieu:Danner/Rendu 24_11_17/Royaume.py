# -*-coding:utf-8 -*-
#Royaume
# Specification fonctionnelle du type Royaume


# Cree un royaume vide qui peut contenir des cartes. On doit pouvoir savoir a tout moment combien d'unite de chaque type sont dans ce royaume
# x -> Royaume
def creerRoyaume () :
	return 0

# Renvoi le nombre de cartes presentent dans le royaume
# Royaume -> int
def nbCarteRoyaume (royaume) : 
	return 0

# Renvoie le royaume sous forme de chaine de caracteres de cette forme

# Voici le votre royaume :
# 1 : Soldat = nbCarte | 2 : Archer = nbCarte| 3 : Garde = nbCarte 

# Avec nbCarte qui doit etre remplacer par le nombre de carte presente dans royaume qui correspond a ce type là
# Royaume -> String 
def toStringRoyaume (royaume) :
	return 0

# Renvoie true si la carte est presente dans le royaume ("Soldat", "Garde", "Archer")
# Royaume*String -> bool
def possedeCarteRoyaume (royaume, nom) : 
	return 0

# Renvoie la carte correspondante au nom en parametre ("Soldat", "Garde", "Archer")
# Supprime cette carte du royaume
#royaume*String -> carte 
def getCarteRoyaume (royaume, nom) : 
	return 0
# permet de placer une carte dans le royaume
# pre : La carte existe dans la main
# Fonction utilisee:
#	mettreCarteRoyaume
# Royaume*Carte->x
def placerCarteRoyaume (royaume, carte) :
	return 0

