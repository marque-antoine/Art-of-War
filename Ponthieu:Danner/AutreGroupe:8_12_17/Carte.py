
# Carte

#Cree une carte (Nom, Attaque,DefenseAttaque,DefenseDefense,Portee)
def creer_carte():
    carte = {"nom" : "", "attaque": "", "defenseAttaque" : "", "defenseDefense": "", "Portee" : "", "estVerticale" : True, "etat" = "intacte", "pdv": 0 }
    return 0
  
#Recupere l'attaque de la carte passee en parametre
def getattaque(carte):
    return carte["attaque"]
    

#Recupere la defense de la carte
def getdefense(carte):
    return carte["defenseDefense"]
    


#Recupere le nombre de point de vie de la carte (PDV)
#carte -> int
def getPDV(carte):
    return carte["pdv"]

#Attribue un nombre de point de vie à la carte en parametre
def setPDV(carte,x):
    return carte["pdv"] = x
    
#Capture la carte passÃ©e en parametre
#La fonction envoie donc la carte du champ de bataille adverse dans le royaume du joueur courant
def capturer(ChampDeBataille,carte,Royaume):
    return 0
    
#Passe la carte en parametre en position d'attaque
def setPosCarte(carte,offensive):
    return carte["estVerticale"] = True
    
#renvoie l'état de la carte : "affaiblie" ou "intacte"  
#carte -> string
def getEtatCarte(carte):
    return carte["etat"]
    
#Affiche le nom de la carte en parametre("Soldat")
#carte -> string
def carteToString(carte):
    return carte["nom"]
    
#passe la carte en parametre de la pioche au royaume du Joueur    
def demobiliser(Joueur,carte):
    return 0

