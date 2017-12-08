    
            #################################
            #################################
            #####                       #####
            #####  Programme Principal  #####
            #####                       #####
            #################################
            #################################

#Création des deux joueurs
print('Création des joueurs')
j1 = créer_Joueur()
j2 = créer_Joueur()

#Récupération des noms pour les deux joueurs
print('Quels sont les noms des joueurs?')
setNomJoueur(j1, input('nom du joueur 1'))
setNomJoueur(j2, input('nom du joueur 2'))

#Création des deux terrains pour les deux joueurs
print('Création du champ de bataille')
cdbj1 = créer_ChampDeBataille(j1)
cdbj2 = créer_ChampDeBataille(j2)
#Création des decks
print('Création des pioches')
p1 = créer_pioche()
attribuer_pioche(p1)
p2 = créer_pioche()
attribuer_pioche(p2)

#------------------------------
#Initialisation de la partie
#------------------------------

partie = créer_Partie(j1,j2)
print('Début de la partie')

#On mélange la pioche
mélanger_pioche(p1)
mélanger_pioche(p2)

#On attribue un roi aléatoirement à  chacun des deux joueurs(ils sont placés dans la main au départ)
hasard = random.randint(1, 2)
attribuer_Roi(j1,hasard)
print('Le joueur 1 aura le Roi ',hasard)
if hasard == 1 :
    attribuer_Roi(j2,2)
    print('Le joueur 2 aura le deuxième Roi')
else:
    attribuer_Roi(j2,1)
    print('Le joueur 2 aura le premier Roi'    )

#Les deux joueurs piochent 3 cartes

print('Mise en place de la partie')
for i in range(3):
    piocher(j1,x)
    piocher(j2,y)

#On démobilise une carte au hasard qui va dans le royaume...
#On récupère la liste des cartes de la main et on en choisit une au hasard(fonction random)
hasard = random.randint(0, 2)
cartesMain = getCartesMain(getMain(j1))
demobiliser(j1,cartesMain[hasard])

hasard = random.randint(0, 2)
cartesMain = getCartesMain(getMain(j2))
demobiliser(j2,cartesMain[hasard])

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il possède dans sa main, on lui demande aussi une position. Finalement on deploie cette carte sur la position(Position au front).
nomJ1 = recuperer_nom(j1)
nomJ2 = recuperer_nom(j2)
print( nomJ1,' quelle carte voulez-vous placer sur le champ de bataille ? et où voulez-vous la placer ?')
print(mainToString(getMain(j1)))
carte1 = input('Carte = ')
position1 = input('Position = ')
main_vers_cdb(j1,carte1,position1,cdbj1)

print( nomJ2,' quelle carte voulez-vous placer sur le champ de bataille ? et où voulez-vous la placer ?')
print(mainToString(getMain(j2)))
carte2 = input('Carte = ')
position2 = input('Position = ')
main_vers_cdb(joueur2,carte1,position1,cdbj2)

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il possède dans sa main. On met ensuite cette carte dans sa reserve

print(nomJ1,' quelle carte voulez vous mettre en réserve?')
print(mainToString(getMain(joueur1)))
carte1_1 = input('Carte =')
main_vers_reserve(joueur1,carte1_1)

print(nomJ2,' quelle carte voulez vous mettre en réserve?')
print(getMain(joueur2))
carte2_2 = input('Carte =')
main_vers_reserve(joueur2,carte2_2)



#------------------------------
#Début de partie
#------------------------------
print('Début de la partie')
#on assigne le joueur courant de la partie et son adversaire, un roulement sera fait à  chaque fin de tour
set_joueur_courant(partie,j1)
set_joueur_adverse(partie,j2)

#tant que les conditions de fin de la partie ne sont pas remplies, on continue le jeu.
while (fin_de_partie(partie)==False):
	joueurCourant = get_joueur_courant(partie)
	joueurAdverse = get_joueur_adverse(partie)
	nomJoueurCourant = recuperer_nom(joueurCourant)
	cdb = getCDB(joueurCourant)
	reserve = getReserve(joueurCourant)
	royaume = getRoyaume(joueurCourant)
	main = getMain(joueurCourant)
	print('C est à  ',nomJoueurCourant,'de jouer')
	
	if cdbVide(getCDB(joueurCourant)) :
        	# on regarde si le champ de bataille du joueur courant est vide pour savoir s'il doit recruter ou non des unités
        	if getNbCartesReserve(reserve) >= 2:
        	# on regarde si le joueur possède plus de deux cartes dans sa réserve, si oui, les deux cartes de la conscription proviennent de sa réserve
		    carteR = getPremiereCarteReserve(reserve)
            
		    print('Placez la carte',carteR)
		    position1 = input('Position =')
		    reserve_vers_cdb(joueurCourant,carteR,position1,cdb)

		    carteR = getPremiereCarteReserve(reserve)
		    print('Placez la carte',carteR)
		    position2 = input('Position =')
            
		    while position2 == position1 :
                	# le joueur ne doit pas mettre 2 fois la même position 
                	print('Une carte est déjà  présente sur cette position veuillez choisir une nouvelle position !')
                
                	print('Placez la carte ',carteR)
                	position2 = input('Position =')

		    reserve_vers_cdb(joueurCourant,carteR,position2,cdb)

        elif getNbCartesReserve(reserve) == 1 and not royaumeVide(royaume):
        # si le joueur ne possède plus qu'une seule carte dans sa réserve et que son royaume contient au moins 1 carte
            carteR = getPremiereCarteReserve(reserve)
            
            print('Ou voulez-vous mettre ',carteR,'?')
            position1 = input('Position =')
	    reserve_vers_cdb(joueurCourant,carteR,position1,cdb)
            
            print('Quelle carte voulez-vous mettre sur le champ de bataille et où ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position2 = input('Position =')

            while position2 == position1:
                # le joueur ne doit pas mettre 2 fois la même position sinon il n'y aura qu'une seule carte sur le champ de bataille
                print('Vous ne pouvez pas placer les 2 cartes sur la même position !')
                
                print('Ou voulez-vous mettre la carte',carte,'?')
                position2 = input('Position =')

            royaume_vers_cdb(joueurCourant,carte,position2,cdb)


        elif getNbCartesRoyaume(royaume) >= 2:
            # si le joueur ne possède plus de carte dans sa réserve et que son royaume possède au moins 2 cartes
            print('Quelle carte voulez-vous mettre sur le champ de bataille et où ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position1 = input('Position =')
            royaume_vers_cdb(joueurCourant,carte,position1,cdb)

            print('Quelle carte voulez-vous mettre sur le champ de bataille et où ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position2 = input('Position =')

            while position2 == position1:
                # le joueur ne doit pas mettre 2 fois la même position sinon il n'y aura qu'une seule carte sur le champ de bataille
                print('Ou voulez-vous mettre ',carte,'?')
                position2 = input('Position =')

            royaume_vers_cdb(joueurCourant,carte,position2,cdb)

        else :
            # le joueur n'a plus assez de cartes pour en mettre 2 sur le champ de bataille, il a donc perdu
            set_fin_de_partie(partie, True)
	    setVainqueur(partie, joueurAdverse)
	
	
	    print('Initialisation phase 1:')
	    # on réinitialise les points de vie des unités sur le champ de bataille, et on remet les cartes en position défensive (seulement pour le joueur courant)
	    reinitilisationCDB(cdb)
	
	    if  not piocheVide(getTaillePioche(joueurCourant)):
		# si le joueur peut piocher
		piocher(joueurCourant)
	
		print('Initialisation phase 2')
	
		print('Que voulez-vous faire ? \n 1=ne rien faire \n 2=mettre en réserve \n 3=déployer une unité \n 4=attaquer')
		ordre = int(input('Réponse ='))
	
		if ordre == 1:
		    # le joueur ne veut rien faire
		    print('ok')
	
		if ordre == 2:
		    # le joueur veut mettre une carte en réserve
		    print('Choississez une carte de votre main que vous voulez mettre en réserve')
		    # on affiche la main du joueur pour qu'il puisse choisir
		    print(mainToString(getMain(getJoueurCourant)))
		    carteM = input('Carte =')
		    carte = getCarteMain(main,carteM)
		    main_vers_reserve(joueurCourant,carte)
	
		if ordre == 3:
		    # le joueur veut mettre une unité sur le cdb
		    if not(reserveVide(reserve)) :
			# si la réserve n'est pas vide alors on déploie la première unité de la réserve
			carte = getPremiereCarteReserve(reserve)
			print('Placez la carte ',carte)
			position = input('Position =')
			#si la position est déjà occupée, on échange et la carte remplacée va en bout de réserve
			if positionOccupée(cdb,position):
			    remplacerCarte(carte,position,cdb)
			else:
			    reserve_vers_cdb(joueurCourant,carte,position,cdb)
	
		    else :
			if not(mainVide(main)) :
			    # sinon on lui demande de choisir une des cartes de sa main
			    print('Choississez une carte de votre main que vous voulez mettre sur le champ de bataille')
			    # on affiche la main du joueur pour qu'il puisse choisir
			    print(mainToString(main))
			    carteM = input('Carte =')
			    carte = getCarteMain(main,carteM)
			    position = input('Position =')
			    #si la position est déjà occupée, on échange et la carte remplacée va en bout de réserve
			    if positionOccupée(cdb,position):
				remplacerCarte(carte,position,cdb)
			    else:			   
				main_vers_cdb(joueurCourant,carte,position,cdb)
			else:
			    print('Vous ne pouvez pas placer de carte')
	
		if ordre == 4:
		    # le joueur veut attaquer
		    print('la phase de combat commence')
		    # on récupère la liste des unités que possède le joueur sur le champ de bataille
		    cartesCDB = getCartes(cdb)
		    cdbA = getCDB(joueurAdverse)
		    for c in cartesCDB:
			# pour toutes les cartes dans la liste des attaquants, on demande au joueur s'il veut attaquer avec
			print("Voulez vous attaquer avec ",c,"? 1=oui, 0=non")
			réponse = int(input('Réponse ='))
	
			if réponse == 1:
			    # lorsque le joueur veut attaquer avec la carte i
			    print(getAportée(c, cdbA))
			    # on lui affiche toutes les cartes (sous forme d'une liste) qui sont à  portée de sa carte c
			    print('Qui voulez vous attaquer?')
			    attaquant= c
			    defenseur = input('Carte à  attaquer =')
			    # on modifie l'état de la carte qui va attaquer, qui passe de l'état défensif à  l'état offensif
			    setPosCarte(attaquant,offensive)			    
			    if getattaque(attaquant) == getdefense(defenseur) and getEtatCarte(defenseur) != "affaiblie" :
				# si la valeur de l'attaque est égale à  la valeur de la défense et que la carte attaquée n'a pas déjà  subi de dégats, alors le joueur capture la carte.
				capturer(cdbA,defenseur,royaume)
				#Si la carte capturée est un roi, la partie se termine, le gagnant est le joueur courant
				if carteToString(defenseur) == 'Roi':
				    set_fin_de_partie(partie, True)
				    setVainqueur(partie, joueurCourant)				    
			    else :
				# sinon on retire les dégats des points de vie de la carte attaquée
				setPDV(defenseur) = getPDV(defenseur) - getattaque(attaquant)
	
				if getPDV(defenseur) <= 0 :
				    # si les points de vie de la carte attaquée sont à  0 ou moins, la carte meurt(déplacement vers le cimetière)
				    cdb_vers_cimetiere(cdbA,defenseur)
				    #au cas où une unitée est derrière celle qui vient d'être tuée, on l'avance
				    Avancer(cdbA,defenseur)
				    #Si la carte tuée est un roi, la partie se termine, le gagnant est le joueur courant
				    if carteToString(defenseur) == 'Roi':
					set_fin_de_partie(partie, True)
					setVainqueur(partie, joueurCourant)					    
	
		else:
		    # si le joueur n'a pas mis 1,2,3 ou 4, il passe son tour
		    print('Relisez les consignes, vous passez votre tour')
	
		print('Initialisation phase 3')
	
		if getNbCartesMain(joueurCourant) >= 6 :
		    # si le joueur au moins 6 cartes dans sa main, il est obligé de démobiliser.
		    print('Quelle carte voulez-vous démobiliser ?')
		    # on lui affiche les cartes qu'il possède dans sa main
		    print(mainToString(main))
		    carte = input('Carte =')
		    demobiliser(carte,getJoueurCourant)
	
		else:
		    print('Voulez-vous démobilisez ? 1=oui, 0=non')
		    réponse = int(input('Réponse ='))
	
		    if réponse == 1:
			# si le joueur veut démobiliser
			print('Quelle carte voulez-vous démobiliser ?')
			# on lui affiche les cartes qu'il possède dans sa main
			print(mainToString(main))
			carte = input('Carte =')
			démobiliser(carte,joueur1)	

	    else :
		# si le joueur courant ne peut plus piocher, la partie se termine, le vainqueur est celui qui a le plus de cartes dans son royaume(ou égalité pour le joueur qui a commencé en second)
		    set_fin_de_partie(partie, True)
		    if getNbCartesRoyaume(royaume)>getNbCartesRoyaume(getRoyaume(joueurAdverse)):
			setVainqueur(partie, joueurCourant)
		    elif getNbCartesRoyaume(royaume)<=getNbCartesRoyaume(getRoyaume(joueurAdverse)):
			setVainqueur(partie, joueurAdverse)
			
	    print('Fin du tour de ',nomJoueurCourant)
	    set_joueur_adverse(partie, joueurCourant)
	    set_joueur_courant(partie, joueurAdverse)
print('Partie terminée! Bravo aux 2 joueurs, le gagnant est ', getNomJoueur(getVainqueur(partie)))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
    
