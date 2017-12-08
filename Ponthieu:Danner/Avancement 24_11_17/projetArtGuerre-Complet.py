# -*- codind:Latin-1 -*-
import random

def programmePrincipal () :
	# La creation des joueurs entraine la creation de toute es carte et les zones de jeux
	print("Début du jeu : Art of War.")
	
	# Création des deux joueurs
	j1 = creerJoueur(1)
	j2 = creerJoueur(2)

	initialisationPioche(j1, j2)

	# On demande de choisir qui commence. j1 se 
	demanderOrdreJoueur(j1, j2)

	# Les joueurs doivent mettre une carte de leur main dans le champ de bataille
	demanderPlacerCarteChampDeBataille(j1)
	demanderPlacerCarteChampDeBataille(j2)

	
	demanderPlacerCarteReserve(j1)
	demanderPlacerCarteReserve(j2)


	continuerJeu = True
	joueurAct = j1
	while (continuerJeu) :
		print ("Le jeu peut commencer !")

		# Phase de preparation
		print(getNomJoueur(joueur) + ", toutes vos cartes sont remises en mode attaque et soignées.")
		remettreCarteModeAttaque(getChampDeBatailleJoueur(joueurAct))
		
		piocherCarte(joueurAct)


		#PHASE ACTION
		passer=demanderBool("Voulez vous passez la phase d'action ? ") #Possibilité de passer la phase 

		if not(passer):
			reorganiserOuAttaquer=input("Voulez vous Reorganiser votre champ de bataille ou Attaquer ? Reorganiser/Attaquer")
			if reorganiserOuAttaquer==("Reorganiser"):
#Reorganiser
				estVidePlaceCDB(joueurAct)	#Renvoi les places libres sur le champ de bataille du joueur Courant
				if reserveVide(joueurAct)==[]:	#Cas ou la reserve du joueur est  vide
					demanderPlacerCarteChampDeBataille(joueurAct)	 #Place la carte et si la case choisie n'est pas vide: place la carte du Champ de Bataille dans la reserve
				
				else:
				
					placerCarteReserveChampDeBataille(joueurAct)  #Place la carte la plus à gauche de la reserve et l'echange avec celle du Champ de Bataille si la case n'est pas vide
#Attaquer
			elif reorganiserOuAttaquer==("Attaquer") : 
				attaquer=False
				while carteTournees(joueurAct) and not(attaquer):	#Tant que toutes les cartes du champ de bataile du joeur ne sont pas tournées
					attaquer=demanderBool("Voulez vous attaquer ? ")
					if attaquer:				#Tant que toutes les cartes ne sont pas tournées

						carteChoisie=demanderCarteCDB(joueurAct) #Le joueur choisit une carte de son CdB
						changerCarteSens(carteChoisie) #On change de sens la carte pour la mettre en mode "attaque"
						valAttaque=getValeurAttaque(carteChoisie, getMainJoueur(joueurAct)) #On recupere la valeur de la l'attaque en fonction du nombre ou du nombre de cartes en main pour le soldat
						carteEnnemi=choisirEnnemi(autreJoueur) #On choisie la carte que l'on veut attaquer en vérifiant que la portée correspond
						valVie=getVie(carteEnnemi) #Nous donne le nombre de points de vie de la carte choisie

						premAttaque=carteDejaAttaquee(carteEnnemi) #Renvoie un booleen pour savoir si la carte a ete attaquee

						if valAttaque>valVie:	
							placerCarteDansCimetiere(carteEnnemi) #Déplace la carte dans le champ de bataille
							enleverCarteDuChampDeBataille(carteEnnemi)
						elif (valAttaque==valVie and premiereAttaque):
							captureCarte(carteEnnemi)	 #Capture la carte
							enleverCarteDuChampDeBataille(carteEnnemi)
						else:
							valVie=valVie-valAttaque	#Reduit le nombre de points de vie de la cible
							effetAttaque(carteChoisie,carteEnnemi) #Réduit le nombre de points de vie apres attaque
			
		#FIN DE LA PHASE DACTION


		# Phase de developpement
		
		if (nbCarteMain(getMainJoueur(joueur)) > 5) :
			print ("Vous avez trop de carte dans votre main, veuillez-en placer une dans votre royaume.")
			demanderPlacerCarteRoyaume(joueur)
		else :
			
			# On demander au joueur s'il veut poser une carte de sa main dans son royaume
			boolPoserCarte = demanderBool("Vous-vous ajouter une unite de  votre main pour la mettre dans votre royaume ? ")
			if boolPoserCarte  :
				demanderPlacerCarteRoyaume(joueur)
			



#Début du jeu, initialisation de la pioche

# Fait piocher une carte au joueur et lui affiche
def piocheCarteJoueur (joueur)
	c = piocherCarte(getPiocheJoueur(joueur))
	mettreCarteMain (getMainJoueur(joueur), c)
	print(getNomJoueur(joueur) + " a pioché un " + toStringNomCarte(c))

def demanderOrdreJoueur (j1,j2):
	#Inverse l'ordre des joueurs si j2 veut commencer
	if not (demanderBool("Le joueur 1 commence ?")) :
		jInter = j1
		j1 = j2
		j2 = jInter


def initialisationPioche(j1, j2) :

	# On attribut un roi different a chacun des joueurs 
	mettreCarteMain (getMainJoueur(j1), creerRoi(1))
	mettreCarteMain (getMainJoueur(j2), creerRoi(2))

	# Debut de la partie : les joueurs choisissent leur carte
	for joueur in [j1, j2] :

		print ("Le " + getNomJoueur(joueur) + " pioche trois cartes.")
		
		# On fait piocher le joueur. Si accepte pas les trois cartes proposer, on lui met trois autres cartes tirees au hasard dans sa main
		if (not(proposerTroisCartes (joueur))) :
			for i in range (0,3) :
				piocheCarteJoueur(joueur)

		# Phase de preparation, le joueur pose la premiere carte de la pioche dans son Royaume
		print ("Vous devez maintenant placer une carte dans votre royaume.")
		carte = demanderCarteMainJoueur(joueur)
		placerCarteRoyaume (getRoyaumeJoueur(joueur), carte)
		print ("\n")


# proposerTroisCartes : Joueur -> bool
# propose trois cartes au joueur de sa main. Renvoie true s'il accepte et false sinon.
# Liste des fonctions appelees :
#   tirerCarte, afficherCarte, mettreCarteMain, mettreCartePioche
def proposerTroisCartes (joueur) :
	c1 = piocherCarte(getPiocheJoueur (joueur))
	c2 = piocherCarte(getPiocheJoueur(joueur))
	c3 = piocherCarte(getPiocheJoueur (joueur))
	
	print ("Vous avez piocher ces cartes : ")
	afficherCarte(c1)
	afficherCarte(c2)
	afficherCarte(c3)

	accepte = demanderBool ("Voulez-vous garder cette pioche ?")

	# si le joueur accepte les cartes il faut les mettre dans sa main sinon les remettre dans sa pioche
	if (accepte) :
		mettreCarteMain (getMainJoueur(joueur), c1)
		mettreCarteMain (getMainJoueur(joueur), c2)
		mettreCarteMain (getMainJoueur(joueur), c3)
	else :
		mettreCartePioche(getPiocheJoueur(joueur), c1)
		mettreCartePioche(getPiocheJoueur(joueur), c2)
		mettreCartePioche(getPiocheJoueur(joueur), c3)

	return accepte

# Permet d'afficher le type d'une carte
def afficherCarte (carte) :
		print ("Type de la carte : " + toStringNomCarte(carte) + ".")

# affiche la main d'un joueurs
def afficherMain (main) :
	return main.toString()

# Permet de demander a l'utilisateur de boolean quelque soit la question 
def demanderBool (question) :
	while True:
		try:
		# on convertie la reponse de l'utilisateur grace a un dictionnaire
			return {"oui":True,"non":False}[input(question + " Oui/Non ").lower()]
		except KeyError:
			print ("Ce n'est pas une réponse valide. Vous devez répondre oui ou non !")

# Demande a l'utilisateur de saisir un nombre
def demanderNombre (question) :
	estNombre = False
	
	while not (estNombre) :
		chaine = input(question)
		estNombre = est_nombre (chaine)
		if not(estNombre) :
			print("Ce n'est pas un nombre !")
	return int(chaine)

# verifie si un caractere est un nombre
def est_nombre (chaine) :
		# verifie si une chaine passe en argument est un nombre ou pas
		try:
			int(chaine)
			return True
		except ValueError:
			return False

# Fait placer une carte de la main au royaume du joueur 
def demanderPlacerCarteRoyaume (joueur) :
	print ("Choisissez-une carte pour la placer dans votre royaume.")
	carte = demanderCarteMainJoueur(joueur)
	while (estRoi(carte)) :
		print ("Attention la carte choisie est votre roi, veuillez choisir une autre carte.")
		carte = demanderCarteMainJoueur(joueur)
	mettreCarteRoyaume (getRoyaumeJoueur (joueur), carte)


# Fait placer une carte de la main du joueur dans son champs de bataille
def demanderPlacerCarteChampDeBataille(joueur) :
	# On commence par lui demander de choisir une carte de sa main
	print (getNomJoueur(joueur) +" doit choisir une carte à mettre dans son champ de bataille.")
	carte = demanderCarteMainJoueur (joueur)

	print (toStringCdb(getChampDeBatailleJoueur(joueur)))
	
	# Puis on demande la position juqsuqu'a ce que la place choisie soit vide
	estVide = False
	while not (estVide) :
		coordonnees = demanderCoordonneesChampDeBataille (joueur)
		if not estVidePlaceCDB(getChampDeBatailleJoueur(joueur), coordonnees) :
			print ("La place n'est pas libre ! ")
		else :
			estVide = True


	placerCarteCDB (getChampDeBatailleJoueur(joueur), carte, coordonnees)

	print ('Voici maintenant votre champ de bataille : ')
	print (toStringCdb(getChampDeBatailleJoueur(joueur)))
	print ("\n")

# Fait choisir au joueur une cartep de sa main
# Joueur->Carte
def demanderCarteMainJoueur (joueur) :
	print (getStringMain(getMainJoueur(joueur)))

	# Quand on afficher les cartes on afficher aussi un numero pour les identifier
	# Le joueur peut alors saisir ce numero pour choisir la carte voulu
	numeroCarte = 0
	while (numeroCarte < 1 or numeroCarte > nbCarteMain(getMainJoueur(joueur))):
		numeroCarte = demanderNombre ("Rentrer le nombre correspondant à la carte que vous voulez-choisir : ")


	return getCarteMain(getMainJoueur(joueur), numeroCarte)

# demande a l'utilisateur de choisir un carte de son roayume et la retire de celui ci
def demanderCarteRoyaume (joueur) : 
	print (toStringRoyaume(getRoyaumeJoueur(joueur)))

	possede = False
	while not (possede) :
		nbCarte = demanderNombre("Veuillez-choisir la carte de votre royaume que vous voulez prendre. (1 -> soldat, 2 -> archer et 3 -> garde)")
		possede = possedeCarteRoyaume (getRoyaumeJoueur(joueur), nbCarte)
		if not (possede) : 
			print ("Cette carte n'est pas presente dans votre royaume.")
		else : 
			carte = getNbCarteRoyaume (getRoyaumeJoueur(joueur), nbCarte)

	return carte

# demande des coordonnees a l'utilisateur
def demanderCoordonneesChampDeBataille (joueur) :
	coordonnees = ""

	

	def estCoordonneesValide (chaine) : 
		# lettre correspond a la ligne et nombre a la colonne
		if (len(chaine) != 2) :
			return False

		lettre = chaine[0]
		nombre = chaine[1]

		if (len(chaine) != 2) :
			return False

		if est_nombre(nombre) :
			nombre = int(nombre)
		else :
			return False

			# On verifie que le lettre soit un A ou un F 					On verifie que le nombre soit entre 1 et 3
		if ((lettre.lower() == 'a') or (lettre.lower() == 'f')) and (nombre >= 1 and nombre <= 3) : 
			return True
		else :
			return False

	while not (estCoordonneesValide(coordonnees)) :
		coordonnees = input ("Rentrer les coordonnees correspondantes a la case du champs de bataille que vous-voulez choisir. (Ex : A1) ")

	return coordonnees

# demande au joueur de placer une carte de sa main dans la reserve
def demanderPlacerCarteReserve (joueur) :
	print (getNomJoueur(j1) +" doit choisir une carte à mettre dans sa réserve.")
	carte = demanderCarteMainJoueur(joueur)
	placerCarteReserve(getReserveJoueur(joueur), carte)

def piocheCarteJoueur (joueur) :
	carte = piocherCarte(getPiocheJoueur(joueur))
	print ("Vous avez pioché cette carte : " + toStringNomCarte(carte))
	mettreCarteMain(getMainJoueur(joueur), carte)


# Si un joueur n'a plus de carte il faut lancer conscription. Return un bool qui dit si la partie doit se finir ou pas
def conscription (joueur) :
	print ("Vous n'avez plus de carte dans votre champ de bataille.")
	nbCarteReserve = getNbCarteReserve(getReserveJoueur(joueur))
	nbCarteRoyaume = getNbCarteRoyaume(getNbCarteRoyaume(joueur))
	carte1 = 0
	carte2 = 0
	estFiniJeu = False

	# On fait choisir les deux cartes selon le jeu du joueur
	if (nbCarteReserve >= 2 ) : 
		carte1 = getCarteReserve (getReserveJoueur(joueur))
		carte2 = getCarteReserve (getReserveJoueur(joueur))
		print ("Vous devez placer deux cartes de votre reserve dans votre champ de bataille")

	elif (nbCarteReserve == 1 and nbCarteRoyaume >= 1) :
		carte1 = getCarteReserve (getReserveJoueur(joueur))
		carte2 = demanderCarteRoyaume(joueur)
		print ("Vous devez placer une carte de votre reserve et une carte de votre royaume dans votre champ de bataille")
	elif (nbCarteRoyaume > 2) : 
		carte1 = demanderCarteRoyaume(joueur)
		carte2 = demanderCarteRoyaume(joueur)
		print ("Vous devez placer deux cartes de votre royaume dans votre champ de bataille")

	else :
		estFiniJeu = True

	if not (estFiniJeu) :
		print (toStringNomCarte(carte1))
		print ("Ou vous voulez placer cette carte dans votre champ de bataille ?")
		coordonnes = demanderCoordonneesChampDeBataille()

		placerCarteCDB(getChampDeBatailleJoueur(joueur), carte1, coordonnees)

		print (toStringNomCarte(carte2))
		print ("Et celle-ci ?")
		coordonnees = demanderCoordonneesChampDeBataille()
		placerCarteCDB(getChampDeBatailleJoueur(joueur), carte2, coordonnees)

	return estFiniJeu

	
def placerCarteReserveChampDeBataille(joueur) :
	
	carte = carteGaucheReserve(reserve)

	afficherCDB (getChampDeBatailleJoueur(joueur))
	
	# On demande la position juqsuqu'a ce que la place choisie soit vide
	estVide = False
	while not (estVide) :
		coordonnees = demanderCoordonneesChampDeBataille (autreJoueur)
		if not estVidePlaceCDB(getChampDeBatailleJoueur(autreJoueur), coordonnees) :
			print ("La place n'est pas libre ! ")
		else :
			estVide = True


	placerCarteCDB (getChampDeBatailleJoueur(autreJoueur), carte, coordonnees)



# Mise des fonctiosn dans la meme file

# Carte 

# Spécification fonctionnelle du type Carte


# Renvoie la valeur d'attaque de la carte.
def getValeurAttaque (carte, main) :
	if isinstance(carte, CSoldat) :
		return main.getNbCarte()
	else : 
		return carte.attaque

def getVie (carte) :
	return carte.vie


# Crée un soldat qui comme caracteristiques :
#	2 de defense en position defensive
#	1 de defense en position offensive
#	1 case devant lui pour sa portee
#	Autant de point d'attaque que de cartes dans la main du joueur
def creerSoldat () :
	return CSoldat()

# Crée un garde qui comme caracteristiques :
#	3 de defense en position defensive
#	2 de defense en position offensive
#	1 case devant lui pour sa portee
#	1 d'attaque
def creerGarde () :
	return CGarde()

# Crée un archer qui comme caracteristiques :
#	2 de defense en position defensive
#	1 de defense en position offensive
#	4 cases devant lui qui serait les cases d'arrivee par un mouvement de cavalier aux echecs
#	1 d'attaque
def creerArcher () :
	return CArcher()

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
	if id == 1 :
		return CRoi(4, 4, 1, [[1,0], [2, 0], [1, -1], [1, 1]])
	elif id == 2 :
		return CRoi(5, 4, 1, [[1,0], [1,1], [1, -1]])

# retourne le nom de la carte en chaine de caracteres
def toStringNomCarte (carte) :
	return carte.nom

# Renvoie true si la carte est un roi est false sinon
# carte -> bool
def estRoi(carte) :
	return isinstance(carte, CRoi)


# Champ de bataille


# Specification fonctionnelle du type ChampDeBataille


# Creer un champ de bataille vide avec 6 places pouvant accueillir des cartes disposees en 2 lignes. 
def creerChampDeBataille (joueur) :
	return creerChampDeBataille()

# Met toute les cartes du champ de bataille en position attaque et réinitialise leur point de vie
# ChampDeBataille ->x
def remettreCarteModeAttaque (cdb) :
	cdb.setCarteModeAttaque()


# place une carte au choix dans le champ de bataille
# Si la carte est placee sur une autre carte alors la carte est remplacee
# ChampDeBataille*Carte -> Carte
# Les coordonnes sont de la sous la forme d'une chaine de caractere. La lettre en premier puis le numero
# ex : "a1", le joueur choisi de la placer la carte dans ligne arriere colonne gauche de son cdb
# Si la positition choisie est arriere et qu'il ni a pas de carte sur l'avant alors la carte est mise sur l'avant
# 	pre : La carte est mise sur un position vide
# ChampDeBataille*Carte*Coordonnees->x
def placerCarteCDB (cdb, carte, coordonnees) :
	cdb.placerCarte(carte, coordonnees)

# Envoie True si la place demandee est vide
# cbd*Coordonnee -> bool
def estVidePlaceCDB(cbd, coordonnees) : 
	return cbd.estVidePlace(coordonnees)

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
	return cdb.toString()

# Renvoie la carte correspondante au coordonnees
def getCarteCDB (cdb, coordonnees) :
	return cdb.getCarte(coordonnees)



# Cimetiere

# Specification fonctionnelle du type Cimetiere


# Cree un cimetiere qui peut contenir des cartes
# x -> Cimetiere
def creerCimetiere ():
	return CCimetiere()

# Permet de placer une carte dans le cimetière
# Carte*Cimetiere -> x
def placerCarteDansCimetiere(cimetiere, carte):
	cimetiere.ajouterCarte (carte)


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
  return CJoueur(id)

# Renvoie la main du joueur
# Joueur -> Main
def getMainJoueur (joueur) :
	return joueur.main

# Joueur -> Pioche
def getPiocheJoueur (joueur) :
	return joueur.pioche

# Joueur -> ChampDeBataille
def getChampDeBatailleJoueur (joueur) :
	return joueur.cdb

# Joueur -> Cimetiere
def getCimetiereJoueur (joueur) :
	return joueur.cimetiere

# Joueur -> Royaume
def getRoyaumeJoueur (joueur) :
	return joueur.royaume

# Joueur -> Reserve
def getReserveJoueur (joueur) :
	return joueur.reserve

def getNomJoueur (joueur) : 
	return joueur.nom

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
	return joueur.main.enleverCarte(placeCarteMain)
	


#MAIN


# Specification fonctionnelle du type Main

# Retourne une main vide pouvant accueillir de 0 à 6 cartes.
# x -> Main
def creerMain () : 
	return CMain()

# Met une carte dans le main du joueur
# Main*Carte -> x
def mettreCarteMain (main, carte) :
	main.ajoutCarte(carte)

# Renvoie n-ieme carte de la main et la supprime de celle-ci
# Main*int -> Carte
# pre : le numero de la carte demander est plus petit que que le nombre de carte du paquet
def getCarteMain (main, n) :
	return main.enleverCarte (n)

# Renvoie le nombre de carte de la main
def nbCarteMain (main) :
	return main.nbCarte()

# Renvoie une chaine de cractere pour afficher la main 
#
# Doit être afficher sous cette forme
# 1 -> Garde | 2 -> Archer | 3 -> Archer 

#Ici le joueur à un garde et deux archers dans la main

def getStringMain (main) :
	return main.toString()




#Pioche

# Specification fonctionnelle du type Pioc


# Retourne une pioche remplie de 20 cartes : 9 soldats, 6 gardes et 5 archers
# Liste des fonctions appelees :
#		creerSoldat, creerGarde, creerArcher
# x -> Pioche
def creerPioche () : 
	return CPioche()

# Renvoie une carte au hasard de la pioche. Retire la carte de la pioche.
# Il faut qu'il reste au moins une carte dans la pioche
# Pioche -> Carte
def piocherCarte (pioche):
	return pioche.piocher()

# Renvoie le nombre de carte restante dans la pioche
# Pioche -> int
def nbCartePioche (pioche): 
	return pioche.nbCarte()

def mettreCartePioche(pioche, carte) :
	pioche.ajouterCarte(carte)


# REserve
# Specification fonctionnelle du type Reserve


# Cree une reserve vide qui peut contenir des cartes. Elle doit etre ordonnee en file d'attente. 
# La premier unite a rentrer dans la reserve sera la premiere a pouvoir en sortir
# x -> Reserve
def creerReserve ():
	return CReserve()

# Place une carte dans la reserve
# pre : il faut faire attention que la reserve ne soit pas pleine 
# Reserve*Carte -> x
def placerCarteReserve (reserve, carte) :
	reserve.placerCarte(carte)


# Renvoie le combre de carte dans la reserve
# Reserve -> int
def getNbCarteReserve (reserve): 
	return self.nbCarte()


# Renvoie la acrte la plus a gauche de la reserve et la supprime de celle-ci
# Toute les cartes de la reserve doivent se decaler vers la gauche
# Reserve -> carte
def getCarteReserve (reserve) : 
	return reserve.enleverCarte()



#Royaume
# Specification fonctionnelle du type Royaume


# Cree un royaume vide qui peut contenir des cartes. On doit pouvoir savoir a tout moment combien d'unite de chaque type sont dans ce royaume
# x -> Royaume
def creerRoyaume () :
	return CRoyaume()

# Renvoi le nombre de cartes presentent dans le royaume
# Royaume -> int
def nbCarteRoyaume (royaume) : 
	return royaume.nbCarte()

# Renvoie le royaume sous forme de chaine de caracteres de cette forme

# Voici le votre royaume :
# 1 : Soldat = nbCarte | 2 : Archer = nbCarte| 3 : Garde = nbCarte 

# Avec nbCarte qui doit etre remplacer par le nombre de carte presente dans royaume qui correspond a ce type là
# Royaume -> String 
def toStringRoyaume (royaume) :
	return royaume.toString()

# Renvoie true si la carte est presente dans le royaume ("Soldat", "Garde", "Archer")
# Royaume*String -> bool
def possedeCarteRoyaume (royaume, nom) : 
	return royaume.possedeType(nom)

# Renvoie la carte correspondante au nom en parametre ("Soldat", "Garde", "Archer")
# Supprime cette carte du royaume
#royaume*String -> carte 
def getCarteRoyaume (royaume, nom) : 
	return royaume.retirerCarte (nom)

# permet de placer une carte dans le royaume
# pre : La carte existe dans la main
# Fonction utilisee:
#	mettreCarteRoyaume
# Royaume*Carte->x
def placerCarteRoyaume (royaume, carte) :
	royaume.ajoutCarte(carte)


# CJoueur

class CJoueur() :
	def __init__(self, id) :
		self.nom = "Joueur " + str(id)
		self.main = CMain()	
		self.pioche = CPioche()
		self.cdb = CChampDeBataille()
		self.cimetiere = CCimetiere()
		self.royaume = CRoyaume()
		self.reserve = CReserve()

class CMain () :
	# possede les cartes de la main du joueur
	def __init__ (self) :
		self.main = []

	def ajoutCarte(self, carte) :
		self.main.append (carte)

	def enleverCarte(self, n) :
		# Retire la n-ieme-1 carte de la main et la renvoie
		cpt = 0
		carte = self.main[n-1]
		del self.main[n-1]
		return carte


	def nbCarte (self) :
		return len(self.main)

	def toString (self) :
		mainStr = "Votre main :\n	"
		cpt = 0
		while cpt < len(self.main) :
			mainStr += str(cpt+1) + " -> " + self.main[cpt].nom

			if len (self.main) > cpt+1 :
				mainStr += " | "
			cpt +=1
		return mainStr

class CPioche () :
	def __init__(self): 
		self.pioche = []
		for i in range(0, 9): 
			self.pioche.append(CSoldat())
		for l in range(0, 6): 
			self.pioche.append(CGarde())
		for o in range(0, 5): 
			self.pioche.append(CArcher())
		
	def ajouterCarte (self, carte) :
		self.pioche.append(carte)

	def piocher (self) :
		nbAl = random.randint (0, len(self.pioche)-1)
		carte = self.pioche[nbAl]
		del self.pioche[nbAl]
		return carte

	def nbCarte (self) :
		return len(self.pioche)

class CReserve():

	def __init__(self):
		self.reserve = []


	def placerCarte (self, carte) :
		self.reserve.append (carte)

		
	def toString (self) :
		r = self.reserve
		resString = ""
		cpt = 1
		for carte in self.reserve :
			resString += str(cpt) + " : " + r[cpt].nom + "  "
			cpt += 1


	def enleverCarte (self) :
		# Pre : il y a une carte dans la pioche
		return self.reserve[0]

	def nbCarte (self) :
		return len (self.reserve)

class CRoi():
	"""La classe Roi représente la carte Roi"""
	def __init__(self, defDef, defAtt, attaque, portee):
		self.nom = "Roi"
		self.defDef = defDef
		self.defAtt = defAtt
		self.attaque = attaque
		self.portee = portee #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerdu

class CRoyaume () :
	# Gere les cartes du royaume d'un joueur

	def __init__ (self) :
		self.royaume = {"Garde" :0, "Soldat" :0, "Archer":0}

	def ajoutCarte (self, carte) :
		self.royaume[carte.nom] += 1

	def nbCarte (self) :
		r = self.royaume
		return r["Garde"] + r["Soldat"] + r["Archer"]

	def toString (self) :
		royStr = "Votre royaume :\n	"

		royStr += "1 : Soldat = " + str(self.royaume["Soldat"]) + " | "+ "2 : Garde = " + str(self.royaume["Garde"])+ " | " +"3 : Archer = " + str(self.royaume["Archer"])
		return royStr


	def retirerCarte (self, type) :
		self.royaume[type] -= 1
		if (type == "Soldat") :
			return CSoldat()
		if (type == "Archer") :
			return CArcher()
		if (type == "Garde") :
			return CGarde()

	def possedeCarte(self, type) :
		return self.royaume[type] > 0

class CSoldat():
	"""La classe Soldat représente la carte soldat"""
	def __init__(self):
		self.nom = "Soldat"
		self.defDef = 2
		self.defAtt = 1
		self.portee = [[1,0]] #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	# L'attaque dépend de la main du joueur
	def getAttaque (self, main) :
		return main.getNbCarte()

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerdu
		
class CArcher():
	"""La classe Archer représente la carte Archer"""
	def __init__(self):
		self.nom = "Archer"
		self.defDef = 2
		self.defAtt = 1
		self.attaque = 1
		self.portee = [[1,1], [1, -1], [2, 1], [2, -1]] #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerdu
	
class CChampDeBataille():
	def __init__(self):
		self.champ = [[None, None, None], [None, None, None]]

	def setCarteModeAttaque(self) :
		for ligne in self.champ :
			for carte in ligne :
				if carte != None :
					carte.estVertical = True
					carte.vie = carte.defDef
					carte.ptsPerdu = 0

	def placerCarte (self, carte, coordonnees) :
		# pre : coordonnees valide
		# Les coordonnées sont de la forme "a1", "a2"
		ligneAddr = coordonnees[0]
		ligne=[]
		
		# On commence par extraire la bonne ligne
		if (ligneAddr == 'f' or ligneAddr == 'F') :
			ligne = self.champ[0]
		else :
			ligne = self.champ[1]

		#On place la carte à la bonne colonne
		ligne[int(coordonnees[1])-1] = carte
		

	def getCarte (self, coordonnees) :
		# pre : coordonnees valide
		# Les coordonnées sont de la forme "a1", "a2"
		ligneAddr = coordonnees[0]
		ligne=[]
		
		# On commence par extraire la bonne ligne
		if (ligneAddr == 'f') :
			ligne = self.champ[0]
		else :
			ligne = self.champ[1]

		# On retourne la bonne colonne
		return ligne[int(coordonnees[1])-1]

	def estVidePlace (self, coordonnees) :
		# pre : coordonnees valide
		# Les coordonnées sont de la forme "a1", "a2"
		ligneAddr = coordonnees[0]
		ligne=[]
		
		# On commence par extraire la bonne ligne
		if (ligneAddr == 'f') :
			ligne = self.champ[0]
		else :
			ligne = self.champ[1]

		# On retourne la bonne colonne
		return ligne[int(coordonnees[1])-1] == None


	def toString (self) :
		ligne0="	1	2	3"
		ligneCpt = 1
		ligne1 = "f	"
		ligne2 = "a	"
		for ligne in self.champ :
			for carte in ligne :
				if carte != None :
					if ligneCpt == 1 :
						ligne1 += carte.nom + "	"
					elif ligneCpt == 2 :
						ligne2 += carte.nom + "	"
				else :
					if ligneCpt == 1 :
						ligne1 += "None 	"
					elif ligneCpt == 2 :
						ligne2 += "None 	"

			ligneCpt += 1
		
		return "Votre champ de bataille :\n 	" + ligne0 + "\n" + ligne1 +"\n" + ligne2 

class CCimetiere () :
	
	def __init__ (self) :
		self.cimetiere = []

	def ajouterCarte (self, carte) :
		self.cimetiere.append(carte)

	def nbCarte (self) :
		return len(self.cimetiere)

class CGarde():
	"""La classe Garde représente la carte Garde"""
	def __init__(self):
		self.nom = "Garde"
		self.defDef = 3
		self.defAtt = 2
		self.attaque = 1
		self.portee = [[1,0]] #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerd


jt1 = creerJoueur(1)
jt2 = creerJoueur(2)

mettreCarteMain(getMainJoueur(jt1), creerSoldat())
mettreCarteMain(getMainJoueur(jt1), creerGarde())
mettreCarteMain(getMainJoueur(jt1), creerArcher())

mettreCarteMain(getMainJoueur(jt2), creerSoldat())
mettreCarteMain(getMainJoueur(jt2), creerGarde())
mettreCarteMain(getMainJoueur(jt2), creerArcher())


placerCarteCDB (getChampDeBatailleJoueur(jt1), creerArcher(), "A2")

