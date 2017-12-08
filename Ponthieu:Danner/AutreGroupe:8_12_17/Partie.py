
# Partie

#Cree une partie contenant les 2 joueurs en parametre
#Joueur x Joueur -> Partie
def creer_Partie(Joueur1,Joueur2):
	partie = {"j1" : Joueur1, "j2" : Joueur2, "finpartie" : "", "vainqueur" :""}
    return 0
 
#Le joueur passe en parametre devient le joueur courant
#Partie x Joueur -> void
def set_joueur_courant(Partie,Joueur): 
    return partie["j1"] = Joueur

#Récupère le joueur courant
#Partie -> Joueur
def getJoueurCourant(Partie): 
    return partie["j1"]

#Le joueur passe en parametre devient le joueur adverse
#Partie x Joueur -> void
def set_joueur_adverse(Partie,Joueur): 
    return partie["j2"] = Joueur

#Recupere le joueur adverse 
#Partie -> Joueur
def getJoueurAdverse(Partie): 
    return partie["j2"]

#Si la fonction renvoie false, la partie continue, sinon la partie demande la fin de la partie
#Partie -> bool
def fin_de_partie(Partie): 
    return Partie["finpartie"]

#permet de definir si c'est la fin de la partie
#si le bool en parametre est vraie, alors la partie est terminée
#Partie x bool -> void
def set_fin_de_partie(Partie,bool): 
    return Partie["finpartie"] = bool

#Definit le vainqueur
#Partie x Joueur -> void
def setVainqueur(Partie,Joueur): 
    return Partie["vainqueur"] = Joueur
  
