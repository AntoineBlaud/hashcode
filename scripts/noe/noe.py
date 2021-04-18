# ========================

# Imports

# ========================

import random # utile pour melanger le jeu (liste de cartes)
import affichage
import time



# ========================

# Définition des fonctions

# ========================



# Fonction permettant de creer les cartes (pour chaque poids, on cree autant de males que de femelles)

# Chaque carte est une liste de 2 elements [poids, sexe] ou le poids va de 0 à 10 et le sexe vaut "m" ou "f"

def creerCartes(): 

    cartes = [] # liste des cartes (vide)

    nbExemplaires = [3,2,3,3,3,3,2,2,1,1,1,1] # nombre de cartes identiques pour chaque poids (par sexe) -> ici 3 cartes de oids 0, 2 cartes de poids 1 etc.

    sexes = ["m", "f"]

    for s in sexes: # pour chaque sexe

        poids = 0

        while poids < len(nbExemplaires): # et pour chaque poids (= indice dans la liste nbExemplaires)

            cartes += nbExemplaires[poids] * [[poids,s]] # on cree le bon nombre d'exemplaires pour un poids et un sexe donne

            poids += 1 # on passe au poids suivant

    return(cartes) # renvoie une liste de cartes (soit une liste de listes)



# Fonction permettant de piocher des cartes

def piocher(nbCartes): # Prend en entree le nombre de cartes a piocher

    global pioche # le fait de piocher va modifier la pioche (variable globale)

    cartesPiochees = pioche[:nbCartes] # on pioche les cartes

    pioche = pioche[nbCartes:] # on les enleve donc de la pioche

    return(cartesPiochees) # renvoie une liste de cartes (soit une liste de listes)



# Procedure permettant de poser une carte de sa main sur l'une des embarcations du jeu

def jouer(joueur, numCarte, embarc): # On choisit celui qui joue ("moi" ou "ordi"), le numero de la carte a jouer (la premiere carte etant numero 0) ainsi que l'embarcation ("A","B"...)

    global mains, jeu # le fait de jouer va modifier le jeu ainsi que ma main ou celle de l'ordi

    carteAjouer = mains[joueur][numCarte] # la carte a jouer est la nieme de la main du joueur (mains etant un dictionnaire)

    jeu[embarc] += [carteAjouer] # on ajoute la carte jouee sur l'embarcation choisie du jeu

    mains[joueur].remove(carteAjouer) # on supprime donc la carte jouee de la main du joueur



# Fonction qui evalue la possibilite de jouer une carte sur une embarcation

# Une embarcation doit contenir soit uniquement des cartes de meme sexe, soit une alternance des sexes

def coupPossible(carte, cartesEmbarc): # en fonction de la carte a jouer et de la liste des cartes presentes sur l'embarcation

    if len(cartesEmbarc) <= 1 : # si pas encore de carte sur l'embarcation ou une seule

        print("Coup autorisé")

        return(True) # on peut jouer ce qu'on veut

    else: # s'il y a au moins 2 cartes sur l'embarcation

        sexe = carte[1] # sexe de la carte a jouer

        sexeDerniereCarte = cartesEmbarc[-1][1] # sexe de la derniere carte posee sur l'embarcation

        sexeAvantDerniereCarte = cartesEmbarc[-2][1] # sexe de l'avant derniere carte posee sur l'embarcation

        alternance = (sexeDerniereCarte != sexeAvantDerniereCarte) # il faut une alternance des sexes si les 2 dernieres cartes de l'embarcation sont de sexe different, sinon il faut toujours le meme sexe

        if alternance: # s'il y a alternance des sexes sur l'embarcation

            if sexe != sexeDerniereCarte: # il faut que le sexe de la carte a jouer soit different de celui de la derniere carte

                affichage.write_log("Coup autorisé")

            else:

                affichage.write_log("Coup interdit")

            return(sexe != sexeDerniereCarte)

        else: # s'il n'y a pas d'alternance, il faut que le sexe de la carte a jouer soit le meme que celui de la derniere carte

            if sexe == sexeDerniereCarte:

                affichage.write_log("Coup autorisé")

            else:

                affichage.write_log("Coup interdit")

            return(sexe == sexeDerniereCarte) # renvoie un booleen qui informe de la faisabilite du coup que souhaite faire le joueur



# Fonction qui choisit la carte que va jouer l'ordinateur en fonction de l'etat du jeu

# Choisit la premiere carte de la main de l'ordi et la joue sur l'embarcation qui permet le coup, sinon la seconde etc..

def choixCarteOrdi():

    main = mains["ordi"]

    i = 0

    while i < len(main): # parcourt les numeros de carte dans la main

        for embarc in jeu: # parcourt les embarcations du jeu

            if coupPossible(main[i], jeu[embarc]): # evalue si la carte i est compatible avec la liste de cartes de l'embarcation consideree

                return(i, embarc) # renvoie le numero de la carte a jouer et embarcation sur laquelle jouer

        i += 1

    return(0,0) # si l'ordi ne peut pas jouer, renvoie le doublet (0,0)

    

# Procedure qui donne le verdict lorsque la carte est jouee sur l'embarcation 

# Le joueur gagne si ça carte atteint exactement le poids de l'embarcation -> il gagne autant de points que le poids total de l'embarcation et l'embarcation est defaussee

# Le joueur perd si ça carte fait dépasser le poids maximal authorisé sur l'embarcation -> il perd autant de points que le poids total de l'embarcation et l'embarcation est defaussee

# Sinon, le jeu continue normalement

def verdict(joueur, carte, cartesEmbarc): # en fonction de la carte a jouer et de la liste des cartes presentes sur l'embarcation

    global scores, jeu # le fait de gagner ou perdre va modifier le jeu ainsi que mon score ou celui de l'ordi

    main = mains[joueur]

    poidsEmbarc = 0 # calcul du poids total de l'embarcation

    for c in cartesEmbarc: # pour chaque carte de l'embarcation

        poidsEmbarc += c[0] # on ajoute le poids de la carte au poids total

    if poidsEmbarc == poidsMax: # si l'embarcation atteint exactement son poids max

        scores[joueur] += poidsEmbarc # le joueur gagne des points

        jeu[embarc] = [] # les cartes de l'embarcation sont defaussees

        affichage.write_log("Coup gagnant")

    if poidsEmbarc > poidsMax: # si l'embarcation depasse le poids max

        scores[joueur] -= poidsEmbarc # le joueur perd des points

        jeu[embarc] = [] # les cartes de l'embarcation sont defaussees

        affichage.write_log("Coup perdant")



        



# ========================

# Programme principal

# ========================





# Constantes et variables globales

# ------------------------



poidsMax = 15 # poids maximal autorise sur chaque embarcation



jeu = {"A":[],"B":[],"C":[],"D":[],"E":[]} # chaque lettre correspond a une embarcation sur laquelle se trouve une liste de cartes



scores = {"ordi":0,"moi":0} # score de chaque joueur

mains = {"ordi":[],"moi":[]} # au départ, la main de chaque joueur est vide

joueur = "ordi" # nom du premier joueur





# Appel des fonctions

# ------------------------



# Creation du jeu de cartes

pioche = creerCartes() # creation du jeu de cartes complet ordonne (= pioche)

random.shuffle(pioche) # on melange la pioche (la methode shuffle du module random permet de melanger une liste aleatoirement)



# Constitution des mains des joueurs

mains["ordi"] = piocher(8) # l'ordi pioche les 8 premieres cartes de la pioche melangee = liste

mains["moi"] = piocher(8) # on pioche les 8 premieres cartes de la pioche melangee = liste



# affichage du jeu, des scores et des mains
affichage.init()
print("Début du jeu:\n==================")


affichage.display_jeu(jeu)
affichage.write_score(scores["moi"],scores["ordi"])

affichage.display_player_cards(mains["moi"])
affichage.display_computer_cards(mains["ordi"])





# Déroulement des tours de jeu



t = 1 # numero de tour

jeuTermine = False # le jeu se termine quand le joueur qui doit jouer n'a plus de carte



while not jeuTermine: # on joue tant que le jeu n'est pas termine

    affichage.write_log("============================")
    affichage.write_log("Joueur: {}".format(joueur))

    

    # Choix de la carte par joueur ou l'ordi

    if joueur == "ordi": # cas de l'ordi

        choix = choixCarteOrdi() # choix de la carte a jouer par l'ordi

        if choix == (0,0): # impossible de jouer pour l'ordi 

            mains[joueur] == [] # il defausse toutes ses cartes (sa main devient vide)

        else:

            numCarte = choix[0] # numero de la carte choisie par l'ordi

            carte = mains[joueur][numCarte] # carte choisie par l'ordi

            embarc = choix[1] # embarcation choisie par l'ordi

    else: # cas du joueur (moi)

        numCarte = int(affichage.get_input("Quelle carte voulez-vous jouer? (entrez un nombre entier; tapez 0 si aucun coup n'est possible) ")) # la premiere carte aura le numero 1 (et non 0)

        if numCarte == 0: # impossible de jouer

            mains[joueur] == [] # il defausse toutes ses cartes (sa main devient vide)

        else:

            numCarte -= 1 # on recupere l'indice de la carte choisie (en commencant pas 0)

            carte = mains[joueur][numCarte] # carte choisie par le joueur dans sa main

            embarc = affichage.get_input("Sur quelle embarcation? (A, B, C, D ou E) ") # choix de l'embarcation sur laquelle jouer

            possible = coupPossible(carte,jeu[embarc]) # on verifie que le coup choisi par le joueur est possible

            while not possible: # si le joueur veut jouer sur une embarcation non autorisee -> on lui redemande son choix

                numCarte = int(affichage.get_input(("Quelle carte voulez-vous jouer? (entrez un nombre entier; tapez 0 si aucun coup n'est possible) ")))

                if numCarte == 0: # impossible de jouer

                    mains[joueur] == []

                else:

                    numCarte -= 1 

                    carte = mains[joueur][numCarte]

                    embarc = affichage.get_input("Sur quelle embarcation? (A, B, C, D ou E) ") 

                    possible = coupPossible(carte,jeu[embarc]) 



    # action de jouer et verdict

    jouer(joueur,numCarte,embarc)

    verdict(joueur, carte, jeu[embarc])

    

    # affichage du jeu, des scores et des mains

    print("Jeu: ", jeu)
    affichage.clear()
    affichage.write_score(scores["moi"],scores["ordi"])
    affichage.update_player_cards(mains["moi"])
    affichage.update_computer_cards(mains["ordi"])
    affichage.display_jeu(jeu)



    # changement de joueur

    if joueur == "ordi":

        joueur = "moi"

    else:

        joueur = "ordi"

    t += 1 # tour suivant



    jeuTermine = (mains[joueur]==[]) # on verifie si le joueur a encore des cartes a jouer



# proclamation du gagnant

if scores["moi"] > scores["ordi"]:

    affichage.write_log("-> FELICITATIONS, VOUS AVEZ GAGNE !")

else:

    affichage.write_log("-> DOMMAGE, VOUS AVEZ PERDU...")


time.sleep(15)

    

    



# on ne verifie pas que ce que tape l'utilisateur est correct (vous pouvez améliorer ceci)













