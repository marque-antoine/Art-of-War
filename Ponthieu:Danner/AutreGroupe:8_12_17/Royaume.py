
#Royaume

#Cree un royaume au joueur
#Joueur -> royaume
def creer_Royaume(Joueur):
    return []
    
#Recupere le royaume du joueur passe en parametre  
#Joueur -> royaume
def getRoyaume(Joueur): 
    return 0
    
#retourne vrai si le royaume est vide, faux le cas échéant 
#Royaume -> bool
def royaumeVide(Royaume): 
    return len (Royaume) == 0

#Recupere le nombre de cartes dans le royaume passe en parametre
#Royaume -> int
def getNbCartesRoyaume(Royaume): 
    return len (Royaume)
    
 #Montre le Royaume passe en parametre ( "Soldat,Archer,...")  
def royaumeToString(Royaume): 
	strRoy = ""
	for carte in Royaume :
		strRoy += carteToString (carte) + " "
    return 0
    
#Recupere une carte specifiee du royaume passe en parametre 
#Royaume x carte -> carte
def getCarteRoyaume(Royaume,carte): 
    return 0
    
#Passe une carte du royaume au champ de bataille    
def royaume_vers_cdb(Joueur,carte,position,ChampDeBataille): 
    return 0
    
