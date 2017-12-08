# -*-coding:utf-8 -*-

# CJoueur

class CJoueur() :
	def __init__(self, id) :
		self.nom = "Joueur " + str(id)
		self.main = CMain()	
		self.pioche = CPioche()
		self.cdb = CChampDeBataille()
		self.cimetiere = CCimetiere()
		self.royaume = CRoyaume()
		self.reserve = CReserve()

class CMain () :
	# possede les cartes de la main du joueur
	def __init__ (self) :
		self.main = []

	def ajoutCarte(self, carte) :
		self.main.append (carte)

	def enleverCarte(self, n) :
		# Retire la n-ieme-1 carte de la main et la renvoie
		cpt = 0
		carte = self.main[n-1]
		del self.main[n-1]
		return carte


	def nbCarte (self) :
		return len(self.main)

	def toString (self) :
		mainStr = "Votre main :\n	"
		cpt = 0
		while cpt < len(self.main) :
			mainStr += str(cpt+1) + " -> " + self.main[cpt].nom

			if len (self.main) > cpt+1 :
				mainStr += " | "
			cpt +=1
		return mainStr

class CPioche () :
	def __init__(self): 
		self.pioche = []
		for i in range(0, 9): 
			self.pioche.append(CSoldat())
		for l in range(0, 6): 
			self.pioche.append(CGarde())
		for o in range(0, 5): 
			self.pioche.append(CArcher())
		
	def ajouterCarte (self, carte) :
		self.pioche.append(carte)

	def piocher (self) :
		nbAl = random.randint (0, len(self.pioche)-1)
		carte = self.pioche[nbAl]
		del self.pioche[nbAl]
		return carte

	def nbCarte (self) :
		return len(self.pioche)

class CReserve():

	def __init__(self):
		self.reserve = []


	def placerCarte (self, carte) :
		self.reserve.append (carte)

		
	def toString (self) :
		r = self.reserve
		resString = ""
		cpt = 1
		for carte in self.reserve :
			resString += str(cpt) + " : " + r[cpt].nom + "  "
			cpt += 1


	def enleverCarte (self) :
		# Pre : il y a une carte dans la pioche
		return self.reserve[0]

	def nbCarte (self) :
		return len (self.reserve)

class CRoi():
	"""La classe Roi représente la carte Roi"""
	def __init__(self, defDef, defAtt, attaque, portee):
		self.nom = "Roi"
		self.defDef = defDef
		self.defAtt = defAtt
		self.attaque = attaque
		self.portee = portee #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerdu

class CRoyaume () :
	# Gere les cartes du royaume d'un joueur

	def __init__ (self) :
		self.royaume = {"Garde" :0, "Soldat" :0, "Archer":0}

	def ajoutCarte (self, carte) :
		self.royaume[carte.nom] += 1

	def nbCarte (self) :
		r = self.royaume
		return r["Garde"] + r["Soldat"] + r["Archer"]

	def toString (self) :
		royStr = "Votre royaume :\n	"

		royStr += "1 : Soldat = " + str(self.royaume["Soldat"]) + " | "+ "2 : Garde = " + str(self.royaume["Garde"])+ " | " +"3 : Archer = " + str(self.royaume["Archer"])
		return royStr


	def retirerCarte (self, type) :
		self.royaume[type] -= 1
		if (type == "Soldat") :
			return CSoldat()
		if (type == "Archer") :
			return CArcher()
		if (type == "Garde") :
			return CGarde()

	def possedeCarte(self, type) :
		return self.royaume[type] > 0

class CSoldat():
	"""La classe Soldat représente la carte soldat"""
	def __init__(self):
		self.nom = "Soldat"
		self.defDef = 2
		self.defAtt = 1
		self.portee = [[1,0]] #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	# L'attaque dépend de la main du joueur
	def getAttaque (self, main) :
		return main.getNbCarte()

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerdu
		
class CArcher():
	"""La classe Archer représente la carte Archer"""
	def __init__(self):
		self.nom = "Archer"
		self.defDef = 2
		self.defAtt = 1
		self.attaque = 1
		self.portee = [[1,1], [1, -1], [2, 1], [2, -1]] #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerdu
	
class CChampDeBataille():
	def __init__(self):
		self.champ = [[None, None, None], [None, None, None]]

	def setCarteModeAttaque(self) :
		for ligne in self.champ :
			for carte in ligne :
				if carte != None :
					carte.estVertical = True
					carte.vie = carte.defDef
					carte.ptsPerdu = 0

	def placerCarte (self, carte, coordonnees) :
		# pre : coordonnees valide
		# Les coordonnées sont de la forme "a1", "a2"
		ligneAddr = coordonnees[0]
		ligne=[]
		
		# On commence par extraire la bonne ligne
		if (ligneAddr == 'f' or ligneAddr == 'F') :
			ligne = self.champ[0]
		else :
			ligne = self.champ[1]

		#On place la carte à la bonne colonne
		ligne[int(coordonnees[1])-1] = carte
		

	def getCarte (self, coordonnees) :
		# pre : coordonnees valide
		# Les coordonnées sont de la forme "a1", "a2"
		ligneAddr = coordonnees[0]
		ligne=[]
		
		# On commence par extraire la bonne ligne
		if (ligneAddr == 'f') :
			ligne = self.champ[0]
		else :
			ligne = self.champ[1]

		# On retourne la bonne colonne
		return ligne[int(coordonnees[1])-1]

	def estVidePlace (self, coordonnees) :
		# pre : coordonnees valide
		# Les coordonnées sont de la forme "a1", "a2"
		ligneAddr = coordonnees[0]
		ligne=[]
		
		# On commence par extraire la bonne ligne
		if (ligneAddr == 'f') :
			ligne = self.champ[0]
		else :
			ligne = self.champ[1]

		# On retourne la bonne colonne
		return ligne[int(coordonnees[1])-1] == None


	def toString (self) :
		ligne0="	1	2	3"
		ligneCpt = 1
		ligne1 = "f	"
		ligne2 = "a	"
		for ligne in self.champ :
			for carte in ligne :
				if carte != None :
					if ligneCpt == 1 :
						ligne1 += carte.nom + "	"
					elif ligneCpt == 2 :
						ligne2 += carte.nom + "	"
				else :
					if ligneCpt == 1 :
						ligne1 += "None 	"
					elif ligneCpt == 2 :
						ligne2 += "None 	"

			ligneCpt += 1
		
		return "Votre champ de bataille :\n 	" + ligne0 + "\n" + ligne1 +"\n" + ligne2 

class CCimetiere () :
	
	def __init__ (self) :
		self.cimetiere = []

	def ajouterCarte (self, carte) :
		self.cimetiere.append(carte)

	def nbCarte (self) :
		return len(self.cimetiere)

class CGarde():
	"""La classe Garde représente la carte Garde"""
	def __init__(self):
		self.nom = "Garde"
		self.defDef = 3
		self.defAtt = 2
		self.attaque = 1
		self.portee = [[1,0]] #La porté est une liste de coordonnées.
		self.estVertical = True
		self.ptsPerdu = 0

	def getVie (self) :
		if (self.estVertical) :
			return self.defDef - self.ptsPerdu
		else :
			return self.defAtt - self.ptsPerd


jt1 = creerJoueur(1)
jt2 = creerJoueur(2)

mettreCarteMain(getMainJoueur(jt1), creerSoldat())
mettreCarteMain(getMainJoueur(jt1), creerGarde())
mettreCarteMain(getMainJoueur(jt1), creerArcher())

mettreCarteMain(getMainJoueur(jt2), creerSoldat())
mettreCarteMain(getMainJoueur(jt2), creerGarde())
mettreCarteMain(getMainJoueur(jt2), creerArcher())


placerCarteCDB (getChampDeBatailleJoueur(jt1), creerArcher(), "A2")

