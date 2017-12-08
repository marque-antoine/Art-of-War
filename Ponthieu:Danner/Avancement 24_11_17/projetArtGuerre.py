# -*-coding:utf-8 -*-
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
