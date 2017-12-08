# -*- codind:utf-8 -*-
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
	joueurAdverse = j2
	print ("Le jeu peut commencer !")
	while (continuerJeu):
		# On change de joueurAct pour le tour suivant
		print ("\nC'est au tour de " + getNomJoueur(joueurAct))

		# Phase de preparation
		print(getNomJoueur(joueurAct) + ", toutes vos cartes sont remises en mode attaque et soignées.")
		remettreCarteModeAttaque(getChampDeBatailleJoueur(joueurAct))
		
		piocheCarteJoueur(joueurAct)


		#PHASE ACTION
		faireAction = demanderBool("Voulez vous faire la phase d'action ? ") #Possibilité de passer la phase 

		if faireAction :
			recruter=demanderBool("Voulez-vous recruter ? (si non, vous attaquez)")
			if recruter :
				print ("C'est parti pour la phase de recrutement :")
				# Pour la phase de recrutement : si le joueur a une carte dans sa réserve il la place où il veut
				# Sinon il peut choisir une carte de sa main qu'il place où il veut

				if nbCarteReserve (getReserveJoueur(joueurAct)) > 0 :
					print ("Où voulez-vous placer la carte " + getNomCarteReserve(getReserveJoueur(joueurAct)) +  " ?")

					# on place une carte de la reserve vers le cdb du joueur
					carteReserveVersCDB (joueurAct)


				else :
					demanderRemPlacerCarteChampDeBataille(joueur)

			# S'il ne veut pas recruter alors il veut attaquer
			else :
				# Renvoi false si le joueur Adverde a perdu durant l'attaque
				if attaque (joueurAct, joueurAdverse) :
					print (getNomJoueur(joueurAdverse) + " a perdu, il a plus de carte à mettre dans son champ de bataille.")
					break

		# Phase de developpement
		
		if (nbCarteMain(getMainJoueur(joueurAct)) > 5) :
			print ("Vous avez trop de carte dans votre main, veuillez-en placer une dans votre royaume.")
			demanderPlacerCarteRoyaume(joueurAct)
		elif (nbCarteMain(getMainJoueur(joueurAct)) > 0) :
			# On demander au joueur s'il veut poser une carte de sa main dans son royaume
			boolPoserCarte = demanderBool("Vous-vous ajouter une carte de votre main à votre royaume ? ")
			if boolPoserCarte  :
				demanderPlacerCarteRoyaume(joueurAct)

		# Vérification de la fin du jeu

		# Arrete le jeu si les deux joueurs n'ont plus de carte dans leur pioche
		if (nbCartePioche(getPiocheJoueur(joueurAct)) == 0 and nbCartePioche(getPiocheJoueur(joueurAdverse)) == 0 ) :
			
			# affiche le resultat
			finGuerre(joueurAct, joueurAdverse)
			continuerJeu = False

		
		jInter = joueurAct
		joueurAct = joueurAdverse
		joueurAdverse = jInter


def finGuerre (joueurAct, joueurAdverse) :
	joueurActAGagne = ""

	if nbCarteRoyaume(getRoyaumeJoueur(joueurAct)) == nbCarteRoyaume(getRoyaumeJoueur(joueurAdverse)) : 
		if nbCarteCimetiere(getCimetiereJoueur(joueurAct)) == nbCarteCimetiere(getCimetiereJoueur(joueurAdverse)) :
			print ("La partie est terminée : match nul.")

		elif nbCarteCimetiere(getCimetiereJoueur(joueurAct)) > nbCarteCimetiere(getCimetiereJoueur(joueurAdverse)) :
			print ("La partie est terminée, c'est " + getNomJoueur(joueurAct) + " qui a gagné.")
		else :
			print ("La partie est terminée, c'est " + getNomJoueur(joueurAdverse) + " qui a gagné.")

	elif nbCarteRoyaume(getRoyaumeJoueur(joueurAct)) > nbCarteRoyaume(getRoyaumeJoueur(joueurAdverse)) :
		print ("La partie est terminée, c'est " + getNomJoueur(joueurAct) + " qui a gagné.")
	else :
		print ("La partie est terminée, c'est " + getNomJoueur(joueurAdverse) + " qui a gagné.")


def peutAttaquer (portee, coordonneesAttaquant, coordonneesAdverse) :
		def coordonneesUniv (coordonnees, estAttaquant) :
			# Renvoie la coordonnees comme si c'etait une matrice 4*4
			if estAttaquant :
				if (coordonnees[0] == "a") :
					return([1, int(coordonnees[1])])
				else :
					return([2, int(coordonnees[1])])

			else :
				colonne = int(coordonnees[1])
				if colonne == 1 :
					colonne = 3
				elif colonne == 3 : 
					colonne = 1 
				if (coordonnees[0] == "a") :
					return([4, colonne])
				else :
					return([3, colonne])

		def coordonneesCible (cAttUniv, portee) :
			return [cAttUniv[0] + portee[0], cAttUniv[1] + portee[1]]

		boolPeutAtt = False 
		
		# Changement de référentiel
		cAttUniv = coordonneesUniv(coordonneesAttaquant, True)
		cAdvUniv = coordonneesUniv(coordonneesAdverse, False)
		
		for portee in portee :
			cible = coordonneesCible(cAttUniv, portee)
			if cible == cAdvUniv :
				boolPeutAtt = True 

		return boolPeutAtt


def attaque (joueurAct, joueurAdverse) :
	# renvoie un boolean qui dit si le jeu est fini. Si le joueur adverse n'a pas pu conscrire
	print ("C'est parti pour la phase d'attaque :\n")
	jeuFini = False
	recommencer = True

	while recommencer :

		# Vérifie que le joueur a encore des cartes pour attaquer
		if (nbCarteModeAttaqueCDB(getChampDeBatailleJoueur(joueurAct)) <= 0) :
			print ("Aucune carte ne peut attaquer sur ce champ de bataille.")
			break

		print ("Voici le champ de bataille de votre adversaire :")
		print (toStringCDB(getChampDeBatailleJoueur(joueurAdverse)))

		print ("Choisissez une carte de votre champ de bataille pour attaquer.")
		carteAttaque, coordonneesAttaquant = demanderCarteAttaqueCDB(getChampDeBatailleJoueur(joueurAct)) #Il faut garder les coordonnées de la carteg qui attaque


		print("Choisissez une carte du champ de bataille de votre adversaire que vous voulez attaquer.")
		carteAdverse, coordonneesAdverse = demanderCarteCDB(getChampDeBatailleJoueur(joueurAdverse))

		# On vérifie que la carte est à la portée de l'autre joueur.
		if not (peutAttaquer(getPorteeCarte(carteAttaque),  coordonneesAttaquant, coordonneesAdverse)) :
			print("La carte adverse que vous avez choisie n'est pas à la portée de votre carte.")
			print("Choisissez une autre carte du champ de bataille de votre adversaire que vous voulez attaquer.")
			carteAdverse, coordonneesAdverse = demanderCarteCDB(getChampDeBatailleJoueur(joueurAdverse))

		# On regarde le resultat de l'attaque
		valAttaque = 0
		if (estSoldat(carteAttaque)) :
			valAttaque = nbCarteMain (getMainJoueur(joueurAct))
		else :
			valAttaque = getAttaqueCarte (carteAttaque)

		# On verifie que la carte ne peut pas etre capturee
		if (valAttaque == getVieCarte(carteAdverse)) :
			if dejaAttaquee (carteAdverse) or estRoi(carteAdverse) :
				print("Vous avez tué la carte adverse.")
				tueCarte (joueurAdverse, carteAdverse, coordonneesAdverse)
				perdVieCarte(carteAdverse, valAttaque)

			else :
				print("Vous avez capturé la carte adverse.")
				captureCarte (getChampDeBatailleJoueur(joueurAdverse), carteAdverse, coordonneesAdverse, getRoyaumeJoueur(joueurAct))
				perdVieCarte(carteAdverse, valAttaque)

		# si l'attaque est plus forte que le reste de pts de vie restant de la carte 
		elif (valAttaque > getVieCarte(carteAdverse)) : 
			print ("Vous avez tué la carte adverse.")
			tueCarte (joueurAdverse, carteAdverse, coordonneesAdverse)
			perdVieCarte(carteAdverse, valAttaque)

		elif (valAttaque < getVieCarte(carteAdverse)) :
			print ("Vous avez blessé la carte adverse.")
			estAttaqueeCarte (carteAdverse)
			perdVieCarte (carteAdverse, valAttaque)
			print ("Il reste " + str(getVieCarte(carteAdverse)) + " points de vie à cette carte.")


		# Vérifie qu'on a pas tue le roi
		if estRoi(carteAdverse) and getVieCarte(carteAdverse) == 0 :
			print ("Vous avez tué le roi !")
			jeuFini = True
			break

		remettreCarteFrontCDB(getChampDeBatailleJoueur(joueurAdverse))

		# On verifie que le joueur adverse à une carte sur son champ de bataille 
		if (nbCarteCDB(getChampDeBatailleJoueur(joueurAdverse)) <= 0) :
			print ("Le joueur " + getNomJoueur(joueurAdverse) + " n'a plus de carte sur son champ de bataille. Il doit conscrire.")
			
			# Si le joueur ne peut pas conscrire le jeu est fini
			if conscription(joueurAdverse) :
				print ("Vous avez gagné, le joueur en face n'a pas pû conscrire !")
				jeuFini = True
				break
		
		# On verifie que le joueurAct a encore des cartes qui peuvent attaquer

		if nbCarteModeAttaqueCDB(getChampDeBatailleJoueur(joueurAct)) == 0 :
			print("Vous n'avez plus de carte en mode attaque.")
			break

		recommencer = demanderBool("Voulez-vous continuer à attaquer ?")

	return jeuFini

		
def captureCarte (cdb, carte, coordonnees, royaume) :
	enleveCarteCDB (cdb, coordonnees)
	placerCarteRoyaume(royaume, carte)


def tueCarte (joueur, carte, coordonnees) :
	enleveCarteCDB (getChampDeBatailleJoueur(joueur), coordonnees)
	placerCarteDansCimetiere(getCimetiereJoueur(joueur), carte)


def demanderCarteCDB (cdb) :
	# Demande une carte au joueur
	# pre : il doit y avoir une carte en mode attaque dans le cdb
	# post : la carte est en mode attaque
	print(toStringCDB(cdb))

	coordonnees = demanderCoordonneesChampDeBataille()
	carte = getCarteCDB(cdb, coordonnees)

	while carte == None :
		print ("Il n'y a pas de carte à cette endroit, veuillez choisir un autre endroit.")
		coordonnees = demanderCoordonneesChampDeBataille()
		carte = getCarteCDB(cdb, coordonnees)

	return carte, coordonnees

def demanderCarteAttaqueCDB (cdb) :
	# Demande une carte au joueur
	# pre : il doit y avoir une carte en mode attaque dans le cdb
	# post : la carte est en mode attaque
	carteAttaque, coordonnees = demanderCarteCDB(cdb)
	while not estModeAttaqueCarte(carteAttaque) :
		print ("Cette carte n'est pas en mode attaque.")
		carteAttaque, coordonnees = demanderCarteCDB(cdb)
	return carteAttaque, coordonnees

def carteReserveVersCDB (joueur) :
	#Place une carte de la reserve vers le champ de bataille.
	# Pre : la reserve doit etre non vide
	print (toStringCDB(getChampDeBatailleJoueur(joueur)))
	coordonnees = demanderCoordonneesChampDeBataille ()
	
	if not  estVidePlaceCDB(getChampDeBatailleJoueur(joueur), coordonnees) :
		cartePresente = getCarteCDB(getChampDeBatailleJoueur(joueur), coordonnees)
		enleveCarteCDB(getChampDeBatailleJoueur(joueur), coordonnees)
		placerCarteReserve(getReserveJoueur(joueur), cartePresente)

	carte = getCarteReserve(getReserveJoueur(joueur))
	placerCarteCDB (getChampDeBatailleJoueur(joueur), carte, coordonnees)

# Fait piocher une carte au joueur et lui affiche
def piocheCarteJoueur (joueur):
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

	# On attribut un roi different à chacun des joueurs 
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

		nomCarte, n = demanderNomCarteMainJoueur(joueur)
		while nomCarte == "Roi" :
			print ("Un roi ne peut pas aller dans son royaume.")
			nomCarte, n = demanderNomCarteMainJoueur(joueur)
		
		carte = getCarteMain (getMainJoueur(joueur), n)
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
	placerCarteRoyaume (getRoyaumeJoueur (joueur), carte)

def demanderRemPlacerCarteChampDeBataille(joueur) :
	# On commence par lui demander de choisir une carte de sa main
	print (getNomJoueur(joueur) +" doit choisir une carte à mettre dans son champ de bataille.")
	carte = demanderCarteMainJoueur (joueur)

	print (toStringCDB(getChampDeBatailleJoueur(joueur)))

	coordonnees = demanderCoordonneesValideChampDeBataille (getChampDeBatailleJoueur(joueur))

	if not (estVidePlaceCDB(getChampDeBatailleJoueur(joueur), coordonnees)) : 
		cartePresente = getCarteCDB(getChampDeBatailleJoueur(joueur), coordonnees)
		enleveCarteCDB(getChampDeBatailleJoueur(joueur), coordonnees)
		mettreCarteMain(getMainJoueur, cartePresente)

	placerCarteCDB (getChampDeBatailleJoueur(joueur), carte, coordonnees)

	print ('Voici maintenant votre champ de bataille : ')
	print (toStringCDB(getChampDeBatailleJoueur(joueur)))
	print ("\n")

# Fait placer une carte de la main du joueur dans son champs de bataille
def demanderPlacerCarteChampDeBataille(joueur) :
	# On commence par lui demander de choisir une carte de sa main
	print (getNomJoueur(joueur) +" doit choisir une carte à mettre dans son champ de bataille.")
	carte = demanderCarteMainJoueur (joueur)

	print (toStringCDB(getChampDeBatailleJoueur(joueur)))
	
	# Puis on demande la position juqsuqu'a ce que la place choisie soit vide
	estVide = False
	while not (estVide) :
		coordonnees = demanderCoordonneesValideChampDeBataille (getChampDeBatailleJoueur(joueur))
		if not estVidePlaceCDB(getChampDeBatailleJoueur(joueur), coordonnees) :
			print ("La place n'est pas libre ! ")
		else :
			estVide = True


	placerCarteCDB (getChampDeBatailleJoueur(joueur), carte, coordonnees)

	print ('Voici maintenant votre champ de bataille : ')
	print (toStringCDB(getChampDeBatailleJoueur(joueur)))
	print ("\n")

# Commme la fonction en dessous elle ne retire pas la carte pour pouvoir faire un test avant
def demanderNomCarteMainJoueur (joueur) :
	print (getStringMain(getMainJoueur(joueur)))
	numeroCarte = 0
	while (numeroCarte < 1 or numeroCarte > nbCarteMain(getMainJoueur(joueur))):
		numeroCarte = demanderNombre ("Rentrer le nombre correspondant à la carte que vous voulez-choisir : ")

	return getNomCarteMain(getMainJoueur(joueur), numeroCarte), numeroCarte

# Fait choisir au joueur une carte de sa main
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
		nomCarte = ""
		idCarte = 0
		# Demande le type de carte voulu
		while idCarte < 1 or idCarte > 3 : 
			idCarte = demanderNombre("Veuillez-choisir la carte de votre royaume que vous voulez prendre. (1 -> soldat, 2 -> archer et 3 -> garde)")
			if (idCarte == 1 ) :
				nomCarte = "Soldat"
			elif (idCarte == 2) :
				nomCarte = "Archer"
			elif (idCarte == 3) :
				nomCarte = "Garde"
			else : 
				print ("Vous devez choisir 1, 2 ou 3.")


		possede = possedeCarteRoyaume (getRoyaumeJoueur(joueur), nomCarte)
		if not (possede) : 
			print ("Cette carte n'est pas presente dans votre royaume.")
		else : 
			carte = getCarteRoyaume (getRoyaumeJoueur(joueur), nomCarte)

	return carte

def demanderCoordonneesValideChampDeBataille(cdb):
	coordonnees = demanderCoordonneesChampDeBataille()
	while not (estPlaceValableCDB(cdb, coordonnees)) :
		print ("Cette place n'est pas valide.")
		coordonnees = demanderCoordonneesChampDeBataille()
	return coordonnees

# demande des coordonnees a l'utilisateur
def demanderCoordonneesChampDeBataille () :
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
		coordonnees = input ("Rentrer les coordonnees correspondantes à la case du champ de bataille que vous-voulez choisir. (Ex : A1) ")
		coordonnees = coordonnees.lower()

	return coordonnees

# demande au joueur de placer une carte de sa main dans la reserve
def demanderPlacerCarteReserve (joueur) :
	print (getNomJoueur(joueur) +" doit choisir une carte à mettre dans sa réserve.")
	carte = demanderCarteMainJoueur(joueur)
	placerCarteReserve(getReserveJoueur(joueur), carte)

def piocheCarteJoueur (joueur) :
	carte = piocherCarte(getPiocheJoueur(joueur))
	print ("Vous avez pioché la carte " + toStringNomCarte(carte))
	mettreCarteMain(getMainJoueur(joueur), carte)

# Si un joueur n'a plus de carte il faut lancer conscription. Return un bool qui dit si la partie doit se finir ou pas
def conscription (joueur) :
	print ("Vous n'avez plus de carte dans votre champ de bataille.")
	nbCarteRes = nbCarteReserve(getReserveJoueur(joueur))
	nbCarteRoy = nbCarteRoyaume(getRoyaumeJoueur(joueur))
	carte1 = ""
	carte2 = ""
	estFiniJeu = False

	# On fait choisir les deux cartes selon le jeu du joueur
	if (nbCarteRes >= 2 ) : 
		print ("Vous devez placer deux cartes de votre reserve dans votre champ de bataille.")
		carte1 = getCarteReserve (getReserveJoueur(joueur))
		carte2 = getCarteReserve (getReserveJoueur(joueur))
		

	elif (nbCarteRes == 1 and nbCarteRoy >= 1) :
		print ("Vous devez placer une carte de votre reserve et une carte de votre royaume dans votre champ de bataille.")
		carte1 = getCarteReserve (getReserveJoueur(joueur))
		carte2 = demanderCarteRoyaume(joueur)
		
	
	elif (nbCarteRoy >= 2) : 
		print ("Vous devez placer deux cartes de votre royaume dans votre champ de bataille.")
		carte1 = demanderCarteRoyaume(joueur)
		carte2 = demanderCarteRoyaume(joueur)
		
	else :
		estFiniJeu = True

	
	if not (estFiniJeu) :
		print ("Vous devez placer les cartes : " + toStringNomCarte(carte1)+" et " + toStringNomCarte(carte2) + " dans votre champ de bataille vide.")
		print ("Où vous voulez placer la carte " + toStringNomCarte(carte1) + " dans votre champ de bataille ?")
		coordonnees = demanderCoordonneesChampDeBataille()

		placerCarteCDB(getChampDeBatailleJoueur(joueur), carte1, coordonnees)

		print ("Où vous voulez placer la carte " + toStringNomCarte(carte2) + " dans votre champ de bataille ?")
		coordonnees = demanderCoordonneesChampDeBataille()
		placerCarteCDB(getChampDeBatailleJoueur(joueur), carte2, coordonnees)

	return estFiniJeu

def placerCarteReserveChampDeBataille(joueur) :
	
	carte = carteGaucheReserve(reserve)

	afficherCDB (getChampDeBatailleJoueur(joueur))
	
	# On demande la position juqsuqu'a ce que la place choisie soit vide
	estVide = False
	while not (estVide) :
		coordonnees = demanderCoordonneesChampDeBataille ()
		if not estVidePlaceCDB(getChampDeBatailleJoueur(autreJoueur), coordonnees) :
			print ("La place n'est pas libre ! ")
		else :
			estVide = True


	placerCarteCDB (getChampDeBatailleJoueur(autreJoueur), carte, coordonnees)


	# place une carte de la main du joueur dans son champs de bataille
# pre : la placeCarteMain doit etre plus petit que le nombre de carte dans la main
# 		Les coordonnees doivent être valides
# Liste des fonctions appelees :
#	demanderCarteJoueur, placerCarteCDB
# Joueur*int*Coordonnees->x
def placerCarteMainCDB (joueur, placeCarteMain, coordonnees) :
	carte = enleverCarte(getMainJoueur(joueur), placeCarteMain)
	placerCarteCDB(getChampDeBatailleJoueur(joueur))



# Mise des fonctiosn dans la meme file

# Carte 

# Spécification fonctionnelle du type Carte


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

# Renvoie true si la carte est un soldat
# Carte -> bool
def estSoldat (carte) :
	return carte.nom == "Soldat"

def estModeAttaqueCarte (carte) :
	return carte.estVertical

# Revoie la valeur de l'attaque de la carte
# carte -> int
def getValAttaque (carte) :
	return carte.attaque

# Renvoie la vie de la carte. On doit prendre en compte le mode de la carte(mode attaque ou mode defense) et les pts de vie restant de la carte (elle a pu deja etre attaquée)
def getVieCarte (carte) :
	return carte.getVie()

# Renvoie le boolean qui dit si une carte a deja ete attaquee.
# Carte -> bool
def dejaAttaquee (carte) :
	return carte.estAttaquee

# Met le bool qui dit si une carte est deja attaque à True
# Carte -> x
def estAttaqueeCarte(carte) :
	carte.estAttaquee = True

# Met une carte en position défensive
# Carte -> x
def metPositionDefCarte (carte) :
	carte.estVertical = False

# Fait perdre le nombre de ptsVie à la carte.
# carte*Vie -> x
def perdVieCarte (carte, nbVie) :
	carte.ptsPerdu += nbVie

# Renvoie le tableau de portée
# carte -> list (portee)
def getPorteeCarte (carte) :
	return carte.portee

# Renvoie la valeur d'attaque de la carte. 
# pre : la carte n'est pas un soldat
# Carte -> int
def getAttaqueCarte (carte) :
	return carte.attaque

# Renvoie True si la carte est en mode attaque et false si elle est en mode défense
def estModeAttaqueCarte (carte) :
	return carte.estVertical





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

# Renvoie true si la place aux coordonnees passees en argument est une place valable pour mettre une carte
# C'est une place valable s'il n'y a pas deja une carte à cet endroit.
# Si la place demandée est à l'arriere s'il y a une carte devant
# ChampDeBataille*coordonnees -> bool
def estPlaceValableCDB (cdb, coordonnees) :
	return cdb.estPlaceValable(coordonnees)

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
def toStringCDB (cdb) :
	return cdb.toString()


def getCarteCDB (cdb, coordonnees) :
	# Renvoie la carte correspondante aux coordonnees
	# S'il n'y a pas de carte à cet endroit, renvoie None
	return cdb.getCarte(coordonnees)

# Renvoie le nombre de carte dans le champ de bataille
def nbCarteCDB (cdb) :
	return cdb.nbCarte()

# Renvoie le nombre de carte en mode attaque sur le cdb
def nbCarteModeAttaqueCDB (cdb) :
	return cdb.nbCarteModeAttaque()

# Enleve la carte du champs de bataille aux coordonnees indiquees. En fait on supprime simplement la carte du cimetiere 
def enleveCarteCDB (cdb, coordonnees) :
	cdb.enleveCarte(coordonnees)

# Remet les cartes qui sont sur l'arriere sans carte devant elle sur le front.
# Si le champ de bataille est vide ou que toute les cartes sont bien placés on ne fait rien
# ChampDeBataille -> x
def remettreCarteFrontCDB(cdb) : 
	cdb.remettreCarteFront()




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

# Renvoie le nombre de carte dans le cimetiere
# Cimetiere -> int
def nbCarteCimetiere(cimetiere) :
	return cimetiere.nbCarte()


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
# post : La carte DOIT etre supprimer de la main
def getCarteMain (main, n) :
	return main.enleverCarte (n)

# Renvoie le type ("Roi", "Soldat"..) de la n-ieme carte de la main
# Main*int -> String
# pre : le numero de la carte demander est plus petit que que le nombre de carte du paquet
# post : La carte NE doit PAS etre supprimee
def getNomCarteMain (main, n) :
	return main.getNomCarte (n)

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
# pre : il y a au moins une carte dans la pioche 
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
def nbCarteReserve (reserve): 
	return reserve.nbCarte()


# Renvoie la carte la plus a gauche de la reserve et la supprime de celle-ci
# Toute les cartes de la reserve doivent se decaler vers la gauche
# Reserve -> carte
def getCarteReserve (reserve) : 
	return reserve.enleverCarte()

# Renvoie le nom de la premiere carte de la réserve
# Reserve -> String
def getNomCarteReserve (reserve) : 
	return reserve.getNomCarte()



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
# Le code : 1 -> soldat, 2 -> archer et 3 -> garde
# Royaume*int -> bool
def possedeCarteRoyaume (royaume, nom) : 
	return royaume.possedeCarte(nom)

# Renvoie la carte correspondante au nom en parametre ("Soldat", "Garde", "Archer")
# Supprime cette carte du royaume
# pre : il existe au moins une carte de ce type dans le royaume 
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

	def getNomCarte (self, n) :
		return self.main[n-1].nom

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
		carte = self.reserve[0]
		del self.reserve[0]
		return carte

	def nbCarte (self) :
		return len (self.reserve)

	def getNomCarte (self) :
		return self.reserve[0].nom

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
		self.estAttaquee = False

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
		self.estAttaquee = False

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
		self.estAttaquee = False

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
					carte.ptsPerdu = 0
					carte.estAttaquee = False

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

	def estPlaceValable(self, coordonnees) :
		estValable = self.estVidePlace(coordonnees)

		# Verif si c'est pas derriere sans carte devant
		colonne = int(coordonnees[1]) - 1
		if (coordonnees[0] == 'a') :
			if (self.champ[0][colonne] == None) :
				estValable = False
		return estValable


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
		
		return "Le champ de bataille :\n" + ligne0 + "\n" + ligne1 +"\n" + ligne2 

	def nbCarte(self) :
		nbCarte = 0
		for ligne in self.champ :
			for carte in ligne :
				if carte != None :
					nbCarte += 1
		return nbCarte

	def nbCarteModeAttaque (self) :
		nbCarte = 0
		for ligne in self.champ :
			for carte in ligne :
				if carte != None :
					if carte.estVertical:
						nbCarte += 1
		return nbCarte

	def enleveCarte (self, coordonnees) :
		colonne = int(coordonnees[1]) -1
		if (coordonnees[0] == 'f') :
			self.champ[0][colonne] = None
		else : 
			self.champ[1][colonne] = None

	def remettreCarteFront(self) :
		c = self.champ
		# On parcourt la ligne arriere
		for place in range (0, len(c[1])) :
			# Si il y a une carte sur l'arriere sans carte sur l'avant
			if c[1][place] != None and c[0][place] == None :
				# Change de place la carte 
				c[0][place] = c[1][place]
				c[1][place] = None

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
		self.portee = [[1,0]] #La portée est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0
		self.estAttaquee = False

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerd
			
programmePrincipal()
