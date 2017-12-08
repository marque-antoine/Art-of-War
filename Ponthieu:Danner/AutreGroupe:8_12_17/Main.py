
# Main

#Cree la main du joueur en parametre
#Joueur -> main
def creer_Main(Joueur):
	main = []
    return 0
  
#affiche les cartes de la main passees en parametre de la manière suivante: "Soldat", "Roi", "Garde"..  
#Main -> string
def mainToString(Main):
	mainStr = ""
	for carte in Main :
		mainStr = carteToString(carte) + "  "
    return 0

#Recupere la carte de la main passee en parametre
#Main x carte -> carte
def getCarteMain(Main,carte):
    return 0

#Recupere le nombre de cartes de la main passee en parametre
#main -> int
def getNbCartesMain(main):
    return len(Main)

#true si vide, false sinon
#Main ->bool
def mainVide(Main):
    return len(Main) == 0

#Passe une carte de la main au royaume
def demobiliser(Joueur,carte):
    joueur["royaume"].append(carte)

#Pose une carte de la main vers le champ de bataille
def main_vers_cdb(Joueur,carte,position,ChampDeBataille):
    return 0

#Passe une carte de la main a la reserve
def main_vers_reserve(Joueur,carte):
    

