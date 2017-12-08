#################################
#################################
#####                       #####
#####  Programme Principal  #####
#####                       #####
#################################
#################################


import sys
#importe le module random qui permet d'obtenir des nombres aleatoires
import random
#importe les fichiers des types abstraits
from Royaume import *
from Cimetiere import *
from Carte import *
from ChampDeBataille import *
from Joueur import *
from Main import *
from Partie import *
from Pioche import *
from Reserve import *

#Creation des deux joueurs(cela cree aussi les pioches, cimetieres, mains, reserves, CDB et royaumes des 2 joueurs)
print('Creation des joueurs')
j1 = creer_Joueur()
j2 = creer_Joueur()

#Recuperation des noms pour les deux joueurs
print('Quels sont les noms des joueurs?')
setNomJoueur(j1, input('nom du joueur 1'))
setNomJoueur(j2, input('nom du joueur 2'))

#Creation des deux terrains pour les deux joueurs
print('Creation du champ de bataille')
cdbj1 = creer_ChampDeBataille(j1)
cdbj2 = creer_ChampDeBataille(j2)


#------------------------------
#Initialisation de la partie
#------------------------------

partie = creer_Partie(j1,j2)
print('Debut de la partie')

#On melange la pioche
attribuer_pioche(j1,melanger_pioche(getPioche(j1)))
attribuer_pioche(j2,melanger_pioche(getPioche(j2)))

#On attribue un roi aleatoirement a chacun des deux joueurs(ils sont places dans la main au depart)
hasard = random.randint(1, 2)
attribuer_Roi(j1,hasard)
print('Le joueur 1 aura le Roi ',str(hasard))
if hasard == 1 :
    attribuer_Roi(j2,2)
    print('Le joueur 2 aura le deuxieme Roi')
else:
    attribuer_Roi(j2,1)
    print('Le joueur 2 aura le premier Roi'    )

#Les deux joueurs piochent 3 cartes

print('Mise en place de la partie')
for i in range(3):
    piocher(j1)
    piocher(j2)

nomJ1 = recuperer_nom(j1)
nomJ2 = recuperer_nom(j2)

#On demobilise une carte choisie du joueur
#On recupere la liste des cartes de la main et on demande au joueur d'en choisir une

print( nomJ1,' quelle carte voulez-vous demobiliser')
print(mainToString(getMain(j1)))
carte1 = input('Carte = ')
demobiliser(j1,carte1)

print( nomJ2,' quelle carte voulez-vous demobiliser')
print(mainToString(getMain(j2)))
carte2 = input('Carte = ')
demobiliser(j2,carte2)

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il possede dans sa main, on lui demande aussi une position. Finalement on deploie cette carte sur la position(Position au front).

print( nomJ1,' quelle carte voulez-vous placer sur le champ de bataille ? et ou voulez-vous la placer ?')
print(mainToString(getMain(j1)))
carte1 = input('Carte = ')
#exemple position: A1(arriere gauche)
position1 = input('Position = ')
main_vers_cdb(j1,carte1,position1,cdbj1)

print( nomJ2,' quelle carte voulez-vous placer sur le champ de bataille ? et ou voulez-vous la placer ?')
print(mainToString(getMain(j2)))
carte2 = input('Carte = ')
position2 = input('Position = ')
main_vers_cdb(j2,carte1,position1,cdbj2)

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il possede dans sa main. On met ensuite cette carte dans sa reserve

print(nomJ1,' quelle carte voulez vous mettre en reserve?')
print(mainToString(getMain(j1)))
carte1_1 = input('Carte =')
main_vers_reserve(j1,carte1_1)

print(nomJ2,' quelle carte voulez vous mettre en reserve?')
print(getMain(j2))
carte2_2 = input('Carte =')
main_vers_reserve(j2,carte2_2)



#------------------------------
#Debut de partie
#------------------------------
print('Debut de la partie')
#on assigne le joueur courant de la partie et son adversaire, un roulement sera fait a chaque fin de tour
set_joueur_courant(partie,j1)
set_joueur_adverse(partie,j2)

#tant que les conditions de fin de la partie ne sont pas remplies, on continue le jeu.
while (fin_de_partie(partie)==False):
    joueurCourant = getJoueurCourant(partie)
    joueurAdverse = getJoueurAdverse(partie)
    nomJoueurCourant = recuperer_nom(joueurCourant)
    cdb = getCDB(joueurCourant)
    reserve = getReserve(joueurCourant)
    royaume = getRoyaume(joueurCourant)
    main = getMain(joueurCourant)
    print('C est a ',nomJoueurCourant,' de jouer')

    if cdbVide(getCDB(joueurCourant)) :
        # on regarde si le champ de bataille du joueur courant est vide pour savoir s'il doit recruter ou non des unites
        if getNbCartesReserve(reserve) >= 2:
        # on regarde si le joueur possede plus de deux cartes dans sa reserve, si oui, les deux cartes de la conscription proviennent de sa reserve
            carteR = getPremiereCarteReserve(reserve)

            print('Placez la carte',carteR)
            position1 = input('Position =')
            reserve_vers_cdb(joueurCourant,carteR,position1,cdb)

            carteR = getPremiereCarteReserve(reserve)
            print('Placez la carte',carteR)
            position2 = input('Position =')

            while position2 == position1 :
                # le joueur ne doit pas mettre 2 fois la meme position
                print('Une carte est deja presente sur cette position veuillez choisir une nouvelle position !')

                print('Placez la carte ',carteR)
                position2 = input('Position =')

            reserve_vers_cdb(joueurCourant,carteR,position2,cdb)

        elif getNbCartesReserve(reserve) == 1 and not royaumeVide(royaume):
        # si le joueur ne possede plus qu'une seule carte dans sa reserve et que son royaume contient au moins 1 carte
            carteR = getPremiereCarteReserve(reserve)

            print('Ou voulez-vous mettre ',carteR,'?')
            position1 = input('Position =')
            reserve_vers_cdb(joueurCourant,carteR,position1,cdb)

            print('Quelle carte voulez-vous mettre sur le champ de bataille et ou ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position2 = input('Position =')

            while position2 == position1:
            # le joueur ne doit pas mettre 2 fois la meme position sinon il n'y aura qu'une seule carte sur le champ de bataille
                print('Vous ne pouvez pas placer les 2 cartes sur la meme position !')

                print('Ou voulez-vous mettre la carte',carte,'?')
                position2 = input('Position =')

            royaume_vers_cdb(joueurCourant,carte,position2,cdb)


        elif getNbCartesRoyaume(royaume) >= 2:
        # si le joueur ne possede plus de carte dans sa reserve et que son royaume possede au moins 2 cartes
            print('Quelle carte voulez-vous mettre sur le champ de bataille et ou ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position1 = input('Position =')
            royaume_vers_cdb(joueurCourant,carte,position1,cdb)

            print('Quelle carte voulez-vous mettre sur le champ de bataille et ou ?')
            print(royaumeToString(royaume))
            carteRoyaume = input('Carte =')
            carte = getCarteRoyaume(royaume,carteRoyaume)
            position2 = input('Position =')

            while position2 == position1:
            # le joueur ne doit pas mettre 2 fois la meme position sinon il n'y aura qu'une seule carte sur le champ de bataille
                print('Ou voulez-vous mettre ',carte,'?')
                position2 = input('Position =')

            royaume_vers_cdb(joueurCourant,carte,position2,cdb)

        else :
        # le joueur n'a plus assez de cartes pour en mettre 2 sur le champ de bataille, il a donc perdu
            set_fin_de_partie(partie, True)
            setVainqueur(partie, joueurAdverse)


    print('Initialisation phase 1:')
    # on reinitialise les points de vie des unites sur le champ de bataille, et on remet les cartes en position defensive (seulement pour le joueur courant)
    reinitilisationCDB(cdb)

    if  not piocheVide(getTaillePioche(joueurCourant)):
        # si le joueur peut piocher
        piocher(joueurCourant)

        print('Initialisation phase 2')

        print('Que voulez-vous faire ? \n 1=ne rien faire \n 2=mettre en reserve \n 3=deployer une unite \n 4=attaquer')
        ordre = int(input('Reponse ='))

        if ordre == 1:
            # le joueur ne veut rien faire
            print('ok')

        elif ordre == 2:
            # le joueur veut mettre une carte en reserve
            print('Choississez une carte de votre main que vous voulez mettre en reserve')
            # on affiche la main du joueur pour qu'il puisse choisir
            print(mainToString(getMain(getJoueurCourant)))
            carteM = input('Carte =')
            carte = getCarteMain(main,carteM)
            main_vers_reserve(joueurCourant,carte)

        elif ordre == 3:
            # le joueur veut mettre une unite sur le cdb
            if not(reserveVide(reserve)) :
                # si la reserve n'est pas vide alors on deploie la premiere unite de la reserve
                carte = getPremiereCarteReserve(reserve)
                print('Placez la carte ',carte)
                position = input('Position =')
                #si la position est deje occupee, on echange et la carte remplacee va en bout de reserve
                if positionOccupee(cdb,position):
                    remplacerCarte(carte,position,cdb)
                else:
                    reserve_vers_cdb(joueurCourant,carte,position,cdb)

            if not(mainVide(main)) :
                    # sinon on lui demande de choisir une des cartes de sa main
                    print('Choississez une carte de votre main que vous voulez mettre sur le champ de bataille')
                    # on affiche la main du joueur pour qu'il puisse choisir
                    print(mainToString(main))
                    carteM = input('Carte =')
                    carte = getCarteMain(main,carteM)
                    position = input('Position =')
                    #si la position est deje occupee, on echange et la carte remplacee va en bout de reserve
                    if positionOccupee(cdb,position):
                        remplacerCarte(carte,position,cdb)
                    else:
                        main_vers_cdb(joueurCourant,carte,position,cdb)
            else:
                    print('Vous ne pouvez pas placer de carte')

        elif ordre == 4:
            # le joueur veut attaquer
            print('la phase de combat commence')
            # on recupere la liste des unites que possede le joueur sur le champ de bataille
            cartesCDB = getCartes(cdb)
            cdbA = getCDB(joueurAdverse)
            
            print('voici votre champ de bataille')
            print(afficherCDB(cdb))
            
            print('voici le champ de bataille de votre adversaire')
            print(afficherCDB(cdbA))
            for c in cartesCDB:
                # pour toutes les cartes dans la liste des attaquants, on demande au joueur s'il veut attaquer avec
                print("Voulez vous attaquer avec ",c,"? 1=oui, 0=non")
                reponse = int(input('Reponse ='))

                if reponse == 1:
                    # lorsque le joueur veut attaquer avec la carte i
                    print(getAportee(c, cdbA))
                    # on lui affiche toutes les cartes  qui sont a portee de sa carte c
                    print('Qui voulez vous attaquer?')
                    attaquant= c
                    defenseur = input('Carte a attaquer =')
                    # on modifie l'etat de la carte qui va attaquer, qui passe de l'etat defensif a l'etat offensif
                    setPosCarte(attaquant,offensive)
                    if getattaque(attaquant) == getdefense(defenseur) and getEtatCarte(defenseur) != "affaiblie" :
                        # si la valeur de l'attaque est egale a la valeur de la defense et que la carte attaquee n'a pas deja subi de degats, alors le joueur capture la carte.
                        capturer(cdbA,defenseur,royaume)
                        #Si la carte capturee est un roi, la partie se termine, le gagnant est le joueur courant
                        if carteToString(defenseur) == 'Roi':
                            set_fin_de_partie(partie, True)
                            setVainqueur(partie, joueurCourant)
                        else :
                            # sinon on retire les degats des points de vie de la carte attaquee
                            setPDV(defenseur,getPDV(defenseur) - getattaque(attaquant)) 

                            if getPDV(defenseur) <= 0 :
                                # si les points de vie de la carte attaquee sont a 0 ou moins, la carte meurt(deplacement vers le cimetiere)
                                cdb_vers_cimetiere(cdbA,defenseur)
                                #au cas oe une unitee est derriere celle qui vient d'etre tuee, on l'avance
                                Avancer(cdbA,defenseur)
                                #Si la carte tuee est un roi, la partie se termine, le gagnant est le joueur courant
                                if carteToString(defenseur) == 'Roi':
                                    set_fin_de_partie(partie, True)
                                    setVainqueur(partie, joueurCourant)

        else:
            # si le joueur n'a pas mis 1,2,3 ou 4, il passe son tour
            print('Relisez les consignes, vous passez votre tour')

        print('Initialisation phase 3')

        if getNbCartesMain(joueurCourant) >= 6 :
            # si le joueur au moins 6 cartes dans sa main, il est oblige de demobiliser.
            print('Quelle carte voulez-vous demobiliser ?')
            # on lui affiche les cartes qu'il possede dans sa main
            print(mainToString(main))
            carte = input('Carte =')
            demobiliser(joueurCourant,carte)

        else:
            print('Voulez-vous demobilisez ? 1=oui, 0=non')
            reponse = int(input('Reponse ='))

            if reponse == 1:
                # si le joueur veut demobiliser
                print('Quelle carte voulez-vous demobiliser ?')
                # on lui affiche les cartes qu'il possede dans sa main
                print(mainToString(main))
                carte = input('Carte =')
                demobiliser(joueurCourant,carte)

    else :
        # si le joueur courant ne peut plus piocher, la partie se termine, le vainqueur est celui qui a le plus de cartes dans son royaume(ou egalite pour le joueur qui a commence en second)
        set_fin_de_partie(partie, True)
        if getNbCartesRoyaume(royaume)>getNbCartesRoyaume(getRoyaume(joueurAdverse)):
            setVainqueur(partie, joueurCourant)
        elif getNbCartesRoyaume(royaume)<=getNbCartesRoyaume(getRoyaume(joueurAdverse)):
            setVainqueur(partie, joueurAdverse)

print('Fin du tour de ',nomJoueurCourant)
set_joueur_adverse(partie, joueurCourant)
set_joueur_courant(partie, joueurAdverse)
print('Partie terminee! Bravo aux 2 joueurs, le gagnant est ', getNomJoueur(getVainqueur(partie)))
