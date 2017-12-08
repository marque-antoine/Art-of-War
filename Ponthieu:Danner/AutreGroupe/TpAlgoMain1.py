    
            #################################
            #################################
            #####                       #####
            #####  Programme Principal  #####
            #####                       #####
            #################################
            #################################

#Cr�ation des deux joueurs
print('Cr�ation des joueurs')
j1 = cr�er_Joueur()
j2 = cr�er_Joueur()

#R�cup�ration des noms pour les deux joueurs
print('Quels sont les noms des joueurs?')
setNomJoueur(j1, input('nom du joueur 1'))
setNomJoueur(j2, input('nom du joueur 2'))

#Cr�ation des deux terrains pour les deux joueurs
print('Cr�ation du champ de bataille')
cdbj1 = cr�er_ChampDeBataille(j1)
cdbj2 = cr�er_ChampDeBataille(j2)
#Cr�ation des decks
print('Cr�ation des pioches')
p1 = cr�er_pioche()
attribuer_pioche(p1)
p2 = cr�er_pioche()
attribuer_pioche(p2)

#------------------------------
#Initialisation de la partie
#------------------------------

partie = cr�er_Partie(j1,j2)
print('D�but de la partie')

#On m�lange la pioche
m�langer_pioche(p1)
m�langer_pioche(p2)

#On attribue un roi al�atoirement � chacun des deux joueurs(ils sont plac�s dans la main au d�part)
hasard = random.randint(1, 2)
attribuer_Roi(j1,hasard)
print('Le joueur 1 aura le Roi ',hasard)
if hasard == 1 :
    attribuer_Roi(j2,2)
    print('Le joueur 2 aura le deuxi�me Roi')
else:
    attribuer_Roi(j2,1)
    print('Le joueur 2 aura le premier Roi'    )

#Les deux joueurs piochent 3 cartes

print('Mise en place de la partie')
for i in range(3):
    piocher(j1,x)
    piocher(j2,y)

#On d�mobilise une carte au hasard qui va dans le royaume...
#On r�cup�re la liste des cartes de la main et on en choisit une au hasard(fonction random)
hasard = random.randint(0, 2)
cartesMain = getCartesMain(getMain(j1))
demobiliser(j1,cartesMain[hasard])

hasard = random.randint(0, 2)
cartesMain = getCartesMain(getMain(j2))
demobiliser(j2,cartesMain[hasard])

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il poss�de dans sa main, on lui demande aussi une position. Finalement on deploie cette carte sur la position(Position au front).
nomJ1 = recuperer_nom(j1)
nomJ2 = recuperer_nom(j2)
print( nomJ1,' quelle carte voulez-vous placer sur le champ de bataille ? et o� voulez-vous la placer ?')
print(mainToString(getMain(j1)))
carte1 = input('Carte = ')
position1 = input('Position = ')
main_vers_cdb(j1,carte1,position1,cdbj1)

print( nomJ2,' quelle carte voulez-vous placer sur le champ de bataille ? et o� voulez-vous la placer ?')
print(mainToString(getMain(j2)))
carte2 = input('Carte = ')
position2 = input('Position = ')
main_vers_cdb(joueur2,carte1,position1,cdbj2)

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il poss�de dans sa main. On met ensuite cette carte dans sa reserve

print(nomJ1,' quelle carte voulez vous mettre en r�serve?')
print(mainToString(getMain(joueur1)))
carte1_1 = input('Carte =')
main_vers_reserve(joueur1,carte1_1)

print(nomJ2,' quelle carte voulez vous mettre en r�serve?')
print(getMain(joueur2))
carte2_2 = input('Carte =')
main_vers_reserve(joueur2,carte2_2)



#------------------------------
#D�but de partie
#------------------------------
print('D�but de la partie')
#on assigne le joueur courant de la partie et son adversaire, un roulement sera fait � chaque fin de tour
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
	print('C est � ',nomJoueurCourant,'de jouer')
	
	if cdbVide(getCDB(joueurCourant)) :
        	# on regarde si le champ de bataille du joueur courant est vide pour savoir s'il doit recruter ou non des unit�s
        	if getNbCartesReserve(reserve) >= 2:
        	# on regarde si le joueur poss�de plus de deux cartes dans sa r�serve, si oui, les deux cartes de la conscription proviennent de sa r�serve
		    carteR = getPremiereCarteReserve(reserve)
            
		    print('Placez la carte',carteR)
		    position1 = input('Position =')
		    reserve_vers_cdb(joueurCourant,carteR,position1,cdb)

		    carteR = getPremiereCarteReserve(reserve)
		    print('Placez la carte',carteR)
		    position2 = input('Position =')
            
		    while position2 == position1 :
                	# le joueur ne doit pas mettre 2 fois la m�me position 
                	print('Une carte est d�j� pr�sente sur cette position veuillez choisir une nouvelle position !')
                
                	print('Placez la carte ',carteR)
                	position2 = input('Position =')

		    reserve_vers_cdb(joueurCourant,carteR,position2,cdb)

        elif getNbCartesReserve(reserve) == 1 and not royaumeVide(royaume):
        # si le joueur ne poss�de plus qu'une seule carte dans sa r�serve et que son royaume contient au moins 1 carte
            carteR = getPremiereCarteReserve(reserve)
            
            print('Ou voulez-vous mettre ',carteR,'?')
            position1 = input('Position =')
	    reserve_vers_cdb(joueurCourant,carteR,position1,cdb)
            
            print('Quelle carte voulez-vous mettre sur le champ de bataille et o� ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position2 = input('Position =')

            while position2 == position1:
                # le joueur ne doit pas mettre 2 fois la m�me position sinon il n'y aura qu'une seule carte sur le champ de bataille
                print('Vous ne pouvez pas placer les 2 cartes sur la m�me position !')
                
                print('Ou voulez-vous mettre la carte',carte,'?')
                position2 = input('Position =')

            royaume_vers_cdb(joueurCourant,carte,position2,cdb)


        elif getNbCartesRoyaume(royaume) >= 2:
            # si le joueur ne poss�de plus de carte dans sa r�serve et que son royaume poss�de au moins 2 cartes
            print('Quelle carte voulez-vous mettre sur le champ de bataille et o� ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position1 = input('Position =')
            royaume_vers_cdb(joueurCourant,carte,position1,cdb)

            print('Quelle carte voulez-vous mettre sur le champ de bataille et o� ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position2 = input('Position =')

            while position2 == position1:
                # le joueur ne doit pas mettre 2 fois la m�me position sinon il n'y aura qu'une seule carte sur le champ de bataille
                print('Ou voulez-vous mettre ',carte,'?')
                position2 = input('Position =')

            royaume_vers_cdb(joueurCourant,carte,position2,cdb)

        else :
            # le joueur n'a plus assez de cartes pour en mettre 2 sur le champ de bataille, il a donc perdu
            set_fin_de_partie(partie, True)
	    setVainqueur(partie, joueurAdverse)
	
	
	    print('Initialisation phase 1:')
	    # on r�initialise les points de vie des unit�s sur le champ de bataille, et on remet les cartes en position d�fensive (seulement pour le joueur courant)
	    reinitilisationCDB(cdb)
	
	    if  not piocheVide(getTaillePioche(joueurCourant)):
		# si le joueur peut piocher
		piocher(joueurCourant)
	
		print('Initialisation phase 2')
	
		print('Que voulez-vous faire ? \n 1=ne rien faire \n 2=mettre en r�serve \n 3=d�ployer une unit� \n 4=attaquer')
		ordre = int(input('R�ponse ='))
	
		if ordre == 1:
		    # le joueur ne veut rien faire
		    print('ok')
	
		if ordre == 2:
		    # le joueur veut mettre une carte en r�serve
		    print('Choississez une carte de votre main que vous voulez mettre en r�serve')
		    # on affiche la main du joueur pour qu'il puisse choisir
		    print(mainToString(getMain(getJoueurCourant)))
		    carteM = input('Carte =')
		    carte = getCarteMain(main,carteM)
		    main_vers_reserve(joueurCourant,carte)
	
		if ordre == 3:
		    # le joueur veut mettre une unit� sur le cdb
		    if not(reserveVide(reserve)) :
			# si la r�serve n'est pas vide alors on d�ploie la premi�re unit� de la r�serve
			carte = getPremiereCarteReserve(reserve)
			print('Placez la carte ',carte)
			position = input('Position =')
			#si la position est d�j� occup�e, on �change et la carte remplac�e va en bout de r�serve
			if positionOccup�e(cdb,position):
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
			    #si la position est d�j� occup�e, on �change et la carte remplac�e va en bout de r�serve
			    if positionOccup�e(cdb,position):
				remplacerCarte(carte,position,cdb)
			    else:			   
				main_vers_cdb(joueurCourant,carte,position,cdb)
			else:
			    print('Vous ne pouvez pas placer de carte')
	
		if ordre == 4:
		    # le joueur veut attaquer
		    print('la phase de combat commence')
		    # on r�cup�re la liste des unit�s que poss�de le joueur sur le champ de bataille
		    cartesCDB = getCartes(cdb)
		    cdbA = getCDB(joueurAdverse)
		    for c in cartesCDB:
			# pour toutes les cartes dans la liste des attaquants, on demande au joueur s'il veut attaquer avec
			print("Voulez vous attaquer avec ",c,"? 1=oui, 0=non")
			r�ponse = int(input('R�ponse ='))
	
			if r�ponse == 1:
			    # lorsque le joueur veut attaquer avec la carte i
			    print(getAport�e(c, cdbA))
			    # on lui affiche toutes les cartes (sous forme d'une liste) qui sont � port�e de sa carte c
			    print('Qui voulez vous attaquer?')
			    attaquant= c
			    defenseur = input('Carte � attaquer =')
			    # on modifie l'�tat de la carte qui va attaquer, qui passe de l'�tat d�fensif � l'�tat offensif
			    setPosCarte(attaquant,offensive)			    
			    if getattaque(attaquant) == getdefense(defenseur) and getEtatCarte(defenseur) != "affaiblie" :
				# si la valeur de l'attaque est �gale � la valeur de la d�fense et que la carte attaqu�e n'a pas d�j� subi de d�gats, alors le joueur capture la carte.
				capturer(cdbA,defenseur,royaume)
				#Si la carte captur�e est un roi, la partie se termine, le gagnant est le joueur courant
				if carteToString(defenseur) == 'Roi':
				    set_fin_de_partie(partie, True)
				    setVainqueur(partie, joueurCourant)				    
			    else :
				# sinon on retire les d�gats des points de vie de la carte attaqu�e
				setPDV(defenseur) = getPDV(defenseur) - getattaque(attaquant)
	
				if getPDV(defenseur) <= 0 :
				    # si les points de vie de la carte attaqu�e sont � 0 ou moins, la carte meurt(d�placement vers le cimeti�re)
				    cdb_vers_cimetiere(cdbA,defenseur)
				    #au cas o� une unit�e est derri�re celle qui vient d'�tre tu�e, on l'avance
				    Avancer(cdbA,defenseur)
				    #Si la carte tu�e est un roi, la partie se termine, le gagnant est le joueur courant
				    if carteToString(defenseur) == 'Roi':
					set_fin_de_partie(partie, True)
					setVainqueur(partie, joueurCourant)					    
	
		else:
		    # si le joueur n'a pas mis 1,2,3 ou 4, il passe son tour
		    print('Relisez les consignes, vous passez votre tour')
	
		print('Initialisation phase 3')
	
		if getNbCartesMain(joueurCourant) >= 6 :
		    # si le joueur au moins 6 cartes dans sa main, il est oblig� de d�mobiliser.
		    print('Quelle carte voulez-vous d�mobiliser ?')
		    # on lui affiche les cartes qu'il poss�de dans sa main
		    print(mainToString(main))
		    carte = input('Carte =')
		    demobiliser(carte,getJoueurCourant)
	
		else:
		    print('Voulez-vous d�mobilisez ? 1=oui, 0=non')
		    r�ponse = int(input('R�ponse ='))
	
		    if r�ponse == 1:
			# si le joueur veut d�mobiliser
			print('Quelle carte voulez-vous d�mobiliser ?')
			# on lui affiche les cartes qu'il poss�de dans sa main
			print(mainToString(main))
			carte = input('Carte =')
			d�mobiliser(carte,joueur1)	

	    else :
		# si le joueur courant ne peut plus piocher, la partie se termine, le vainqueur est celui qui a le plus de cartes dans son royaume(ou �galit� pour le joueur qui a commenc� en second)
		    set_fin_de_partie(partie, True)
		    if getNbCartesRoyaume(royaume)>getNbCartesRoyaume(getRoyaume(joueurAdverse)):
			setVainqueur(partie, joueurCourant)
		    elif getNbCartesRoyaume(royaume)<=getNbCartesRoyaume(getRoyaume(joueurAdverse)):
			setVainqueur(partie, joueurAdverse)
			
	    print('Fin du tour de ',nomJoueurCourant)
	    set_joueur_adverse(partie, joueurCourant)
	    set_joueur_courant(partie, joueurAdverse)
print('Partie termin�e! Bravo aux 2 joueurs, le gagnant est ', getNomJoueur(getVainqueur(partie)))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
    
