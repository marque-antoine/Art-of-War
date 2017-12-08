# -*-coding:utf-8 -*-
# Champ de bataille


# Specification fonctionnelle du type ChampDeBataille


# Creer un champ de bataille vide avec 6 places pouvant accueillir des cartes disposees en 2 lignes. 
def creerChampDeBataille (joueur) :
	return 0

# Met toute les cartes du champ de bataille en position attaque et réinitialise leur point de vie
# ChampDeBataille ->x
def remettreCarteModeAttaque (cdb) :
	return 0


# place une carte au choix dans le champ de bataille
# Si la carte est placee sur une autre carte alors la carte est remplacee
# ChampDeBataille*Carte -> Carte
# Les coordonnes sont de la sous la forme d'une chaine de caractere. La lettre en premier puis le numero
# ex : "a1", le joueur choisi de la placer la carte dans ligne arriere colonne gauche de son cdb
# Si la positition choisie est arriere et qu'il ni a pas de carte sur l'avant alors la carte est mise sur l'avant
# 	pre : La carte est mise sur un position vide
# ChampDeBataille*Carte*Coordonnees->x
def placerCarteCDB (cdb, carte, coordonnees) :
	return 0

# Envoie True si la place demandee est vide
# cbd*Coordonnee -> bool
def estVidePlaceCDB(cbd, coordonnees) : 
	return 0
# Affiche le champ de bataille d'un joueur de la maniere suivant : 

#	Votre champ de bataille :
#		1		2		3
# 	f	carte | carte | carte
#	a	carte | carte | carte

# Les mots cartes doivent etre remplaces par le nom de la carte presente dans la case sinon pas de carte mettre : VIDE
# Liste des fonctions utilisees
# 	toStringNomCarte
#ChampDeBataille -> String
def toStringCdb (cdb) :
	return 0

# Renvoie la carte correspondante au coordonnees
def getCarteCDB (cdb, coordonnees) :
	return 0


