
# Joueur

#Cree un joueur
#cree aussi sa main, reserve, cimetiere, royaume, cdb, pioche
def creer_Joueur(): 
	joueur  = {"nom" : "" "main" : "", "reserve ":"", "cimetiere":"", "royaume":  "", "cdb":"", "pioche":""}
	creer_Main (joueur)
	creer_Reserve(joueur)
	creer_Cimetiere(joueur)
	creer_Royaume(joueur)
	creer_pioche(joueur)
	creer_ChampDeBataille(joueur)

    return joueur
   
#Attribue un nom au joueur passé en paramètre, utilise la fonction 'recuperer_nom'   
def setNomJoueur(Joueur,string): 
    return joueur["nom"] = string

#Recupere le nom du joueur passe en parametre
#Joueur -> string
def recuperer_nom(Joueur): 
    return joueur["nom"]

#Cr�e un des deux rois selon le numero plac� en param�tre et l'attribue au joueur passé en paramètre, directement dans la main
def attribuer_Roi(Joueur,x):
    return 0

#Recupere la main du joueur passe en parametre
#Joueur -> Main
def getMain(Joueur):
    return joueur["main"]

#Recupere la pioche du joueur passe en parametre
#Joueur -> Pioche
def getPioche(Joueur): 
    return joueur["pioche"]

#Recupere le cimetiere du joueur passe en parametre
#Joueur -> Cimetiere
def getCimetiere(Joueur):
    return joueur["cimetiere"]

#Recupere la reserve du joueur passe en parametre
#Joueur -> Reserve
def getReserve(Joueur):
    return joueur["reserve"]

#Recupere le champ de bataille du joueur en parametre
#Joueur -> ChampDeBataille
def getCDB(Joueur):
    return joueur["cdb"]
