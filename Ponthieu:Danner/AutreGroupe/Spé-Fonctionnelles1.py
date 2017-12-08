    # Spécialités Fonctionnelles #

# SF Joueur

def creer_Joueur(): #Crée un joueur
    return Joueur
def set_nom(J:Joueur,input('Quel est le nom du joueur?')): #Attribue un nom au joueur passé en paramètre, utilise la fonction 'recuperer_nom'
    return 0
def getNomJoueur(J:Joueur): #Donne un nom
    return string
def piocher_roi(J:Joueur,pioche:list[carte]): #Sort le roi de la pioche et le met dans la main du joueur passé en paramètre
    return 0
def attribuer_Roi1(J:Joueur): #Attribue le roi 1 au joueur passé en paramètre, directement dans la main
    return J
def attribuer_Roi2(J:Joueur): #Attribue le roi 2 au joueur passé en paramètre, directement dans la main
    return J
def attribuer_pioche(J:Joueur,pioche:list[carte]): #Attribue la pioche passée en paramètre au joueur passé en paramètre
    return J
def get_royaume(J:Joueur):
    return Royaume
def get_main(J:Joueur):
    return Main
def get_cimetiere(J:Joueur):
    return Cimetiere
def get_reserve(J:Joueur):
    return Reserve

# SF Pioche

def creer_pioche(): #Crée une pioche
    return list[carte]
def piocher(J:Joueur,pioche:list[carte]): #Pioche une carte
    return pioche
def melanger_pioche(J:Joueur,pioche:list[carte]): #Mélange la pioche
    return pioche

# SF Carte

def creer_carte(): #Crée une carte (Nom, Attaque,DéfenseAttaque,DéfenseDéfense,Portée)
    return carte
def attaquer(A:carte,B:carte): #La carte A attaque la carte B
    return bool
def position_attaque(A:carte): #La carte passée en paramètre passe en position d'attaque
    return A
def diminuer_Defense(A:carte): #Diminue la défense de la carte passée en paramètre dans le cas ou celle-ci a été attaquée
    return A
def recuperer_Type(A:carte): #Récupère le type de la carte (soldat, archer, guarde, roi)
    return string
def recuperer_attaque(A:carte): #Récupère l'attaque de la carte passée en paramètre
    return int
def recuperer_defense (A:carte): #Récupère la défense de la carte
    return int
def recuperer_position(A:carte): #Récupère la position de la carte (attaque/défense)
    return bool
def change_position(A:carte): #Change la position de la carte
    return bool
def recuperer_portee (A:carte): #Récupère la portée de la carte
    return int,int
def capturer(A:carte): #Capture la carte passée en paramètre si la fonction renvoie true
    return bool
def tuer(A:carte): #Tue la carte passée en paramètre si la fonction renvoie true
    return bool

# SF Partie

def creer_Partie(J1:Joueur,J2:Joueur): #Crée une partie
    return Partie
def set_joueur_courant(P:Partie,J:Joueur): #Le joueur passé en paramètre devient le joueur courant
    return J
def set_joueur_adverse(P:Partie,J:Joueur): #Le joueur passé en paramètre devient le joueur adverse
    return J
def choix_action(): #Choisir une action durant la phase d'action
    return 0
def passer_au_developpement(): #Passe à la phase de développement
    return 0
def fin_de_partie(P:Partie): #Si la fonction renvoie false, la partie continue, sinon la partie demande la fin de la partie
    return bool
def set_fin_de_partie(P:Partie,bool):
    return 0
def terminaison_partie(P:Partie): #Termine la partie
    return 0
def setVainqueur(P:Partie, J:Joueur):
    return J

# SF Main

def creer_Main(J:Joueur): #Crée une main
    return list[carte]
def get_Main(J:Joueur):
    return Main
def set_Main(J:Joueur):
    return J
def mainToString(M:Main): #Montre la main
    return M
def demobiliser(C:carte,J:Joueur): #Passe une carte de la main au royaume
    return 0
def main_vers_reserve(J:Joueur,c:carte): #Passe une carte de la main à la réserve
    return 0

#SF Champ de bataille

def creer_ChampDeBataille(J:Joueur): #Crée un champ de bataille qui sera inclue dans le terrain
    return ChampDeBataille
def get_CDB(J:Joueur):
    return ChampDeBataille
def set_CDB(J:Joueur):
    return J
def champdebataille_vide(Ch:ChampDeBataille):
    return Ch
def conscription(Ch:ChampDeBataille): #Fonction assimilée à la conscription dans le jeu 'Art of War'
    return 0
def echanger(Ch:ChampDeBataille,R:Reserve): #Echange la position d'une carte du champ de bataille avec une carte de la réserve
    return 0
def champdebataille_vers_cimetiere(Ch:ChampDeBataille,C:Cimetiere): #Passe une carte du champ de bataille au cimetière
    return 0
def position_defensive(Ch:ChampDeBataille): #Passe toutes les cartes du champ de bataille en position défensive
    return 0

#SF Royaume

def creer_Royaume(J:Joueur): #Crée un royaume qui sera inclue dans le terrain
    return Royaume
def getRoyaume(J:Joueur):
    return Royaume
def getNbCartesRoyaume(R:Royaume):
    return int
def set_Royaume(J:Joueur):
    return J

#SF Réserve

def creer_Reserve(J:Joueur): #Crée une réserve qui sera inclue dans le terrain
    return Reserve
def get_Reserve(J:Joueur):
    return Reserve
def set_Reserve(J:Joueur):
    return J
def get_premiere_carte_reserve(R:Reserve):
    return carte
def get_nbr_carte_reserve(R:Reserve):
    return int
def reserve_vers_cdb(J:Joueur,c:carte,p:position,Ch:ChampDeBataille): #Passe une carte de la réserve au champ de bataille
    return 0

#SF Cimetière

def creer_Cimetiere(J:Joueur): #Crée un cimetière qui sera inclue dans le terrain
    return Cimetiere
def get_Cimetiere(J:Joueur):
    return Cimetiere
def set_Cimetiere(J:Joueur):
    return J
