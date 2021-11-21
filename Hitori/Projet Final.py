########################
#### Projet Hitori #####
########################

from upemtk import *
from random import randint
import string
from winsound import *

PlaySound("Air.wav", SND_LOOP + SND_ASYNC)

#### Les fonctions ####

### Tache 1:  Représentation et chargement des niveaux ###

def lire_grille(nom_fichier):
    """
    Fonction qui prend en argument une chaîne de caractères nom_fichier et renvoyant une liste de listes décrivant les valeurs des cellules de la grille
    nom_fichier: Nom du fichier qu'on ouvre
    f = open("Grille.txt")
    >>> lire_grille(f.readlines())
    [['2', '2', '1', '5', '3'], ['2', '3', '1', '4', '5'], ['1', '1', '1', '3', '5'], ['1', '3', '5', '4', '2'], ['5', '4', '3', '2', '1']]
    """
    liste = []
    liste2 = []
    chiffres = string.digits #On prend la chaine de caractere contenant touts les chiffres
    for loop in range(len(nom_fichier)):
        for lettre in nom_fichier[loop]: #Pour chaque caractere de la chaine
            for chiffre in chiffres: #Pour chaque chiffre de la liste
                if lettre == chiffre: #Si le caractere est un chiffre:
                    liste2 += lettre #On l'ajoute dans la liste.
        liste += [liste2]
        liste2 = []
    return liste

def afficher_grille(grille):
    """
    Fonction qui va prendre en argument la liste de liste crée par la fonction précédente et qui l'affiche sur le terminal.
    grille: Liste de listes représentant la grille
    >>> afficher_grille([['2', '2', '1', '5', '3'], ['2', '3', '1', '4', '5'], ['1', '1', '1', '3', '5'], ['1', '3', '5', '4', '2'], ['5', '4', '3', '2', '1']])

    |2|2|1|5|3|
    |2|3|1|4|5|
    |1|1|1|3|5|
    |1|3|5|4|2|nn
    |5|4|3|2|1|
    """
    phrase = "|"
    for loop in range(len(grille)): #Pour chaque liste
        for loop2 in range(len(grille[loop])): #Pour chaque valeur de la liste
            phrase += str(grille[loop][loop2]) + "|" #On convertit la valeur parcouru en str et on additionne une variable avec cette valeur
        phrase += "\n" #A chaque fois qu'on en finit avec le parcourt d'une liste, on saute une ligne et on passe à la liste suivante
        if loop != len(grille) - 1: #Pour éviter d'avoir un | de trop à la fin de la grille
            phrase += "|"
    return phrase

def ecrire_grille(grille, nom_fichier):
    """
    Fonction qui sauvegarde la grille fournie dans le fichier indiqué, en respectant le même format.
    grille: Liste de listes représentant la grille
    nom_fichier: Nom du fichier qu'on ouvre
    """
    for loop in grille: #Pour chaque liste
        for chiffre in loop: #Pour chaque valeur de la liste
            nom_fichier.write(str(chiffre)) #On convertit la valeur en str et on l'écrit
            nom_fichier.write(" ") #On laisse une espace entre les chiffres
        nom_fichier.write("\n") #On saute une ligne à chaque passage à une autre liste
    nom_fichier.close() #On ferme le fichier

### Tache 2: Réalisation du moteur de jeu ###

## Première règle ##

def sans_conflit_ligne(grille, noircie):
    """
    Fonction qui vérifie si toutes les lignes de la grille n'ont pas deux cases contenant le meme chiffre. Renvoie True si c'est le cas et False si c'est le cas contraire
    grille = Liste de listes des valeurs de la grille
    noircie = Coordonnées des cases noircies. De type set().
    """
    ligne = 0
    length = len(grille)
    for ligne_grille in range(0, length):
        colonne = 0
        ligne = 0
        while ligne < length :
            colonne= ligne + 1
            while colonne < length:
                if (ligne_grille,ligne) in noircie or (ligne_grille,colonne) in noircie :
                    colonne+=1
                    continue
                if grille[ligne_grille][ligne] == grille[ligne_grille][colonne]:
                    return False
                else:
                    colonne+=1
            ligne+=1
    return True

def sans_conflit_colonne(grille,noircie):
    """
    Fonction qui vérifie si toutes les colonnes de la grille n'ont pas deux cases contenant le meme chiffre. Renvoie True si c'est le cas et False si c'est le cas contraire
    grille = Liste de listes des valeurs de la grille
    noircie = Coordonnées des cases noircies. De type set().
    """
    ligne=0
    length=len(grille)
    for colonne_grille in range(0,length):
        colonne = 0
        ligne = 0
        while ligne < length :
            colonne = ligne+1
            while colonne < length:
                if (ligne,colonne_grille) in noircie or (colonne,colonne_grille) in noircie :
                    colonne += 1
                    continue
                if grille[ligne][colonne_grille] == grille[colonne][colonne_grille]:
                    return False
                else:
                    colonne+=1
            ligne+=1
    return True


def sans_conflit(grille,noircie):
    """
    Fonction qui réunit les deux fonctions précédentes pour élaborer la premiere règle de l'Hitori.
    grille = Liste de listes des valeurs de la grille
    noircie = Coordonnées des cases noircies. De type set().
    """

    return (sans_conflit_colonne(grille,noircie) and sans_conflit_ligne(grille,noircie))

## Deuxième règle ##

def sans_voisines(grille, noircie):
    """
    Fonction respectant la deuxieme regle de l'Hitori. Renvoie False si deux cases noircies voisines existent, True sinon.
    grille = Liste de listes des valeurs de la grille
    noircie = Coordonnées des cases noircies. De type set().
    """
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if (j, i) in noircie:
                if (j + 1, i) in noircie or (j - 1, i) in noircie or (j, i + 1) in noircie or (j, i - 1) in noircie:
                    return False
    return True

## Troisième règle ##

def connexe(grille, noircie):
    """
    Fonction respectant la troisieme regle de l'Hitori. Renvoie True si le jeu a une seule zone blanche, False sinon.
    grille = Liste de listes des valeurs de la grille
    noircie = Coordonnées des cases noircies. De type set().
    """
    liste = set()
    cases_noires= len(noircie)
    case_totale = len(grille) * len(grille[0])
    a=recherche_cases_reliées(grille,noircie,liste)
    case_blanche=len(a)
    if cases_noires + case_blanche == case_totale :
        return True
    else :
        return False


def recherche_cases_reliées(grille, noircie, liste, x=0, y=0):
    """
    Fonction qui prend en paramètre une grille et renvoie une liste des coordonnées de toutes les cases blanches reliées entre elles de la grille.
    grille = Liste de listes des valeurs de la grille
    noircie = Coordonnées des cases noircies. De type set().
    liste= Liste qui va stocker les coordonnées des cases blanches tout le long de la récursion
    x, y = Coordonnées de la case
    """
    if (x, y) not in liste:
        if (x, y) not in noircie:
            liste.add((x, y))
        if y > 0 and (x, y - 1) not in noircie:
            recherche_cases_reliées(grille, noircie, liste, x, y - 1)
        if y < len(grille[0]) - 1 and (x, y + 1) not in noircie:
            recherche_cases_reliées(grille, noircie, liste, x, y + 1)
        if x > 0 and (x - 1, y) not in noircie:
            recherche_cases_reliées(grille, noircie, liste, x - 1, y)
        if x < len(grille) - 1 and (x + 1, y) not in noircie:
            recherche_cases_reliées(grille, noircie, liste, x + 1, y)

    return liste

### Tache 3: Interface Graphique ###

## Menu de selection de niveau ##

def affiche_selection_niveau(position):
    '''
    Fonction affichant le menu permettant de choisir le niveau
    Parametre : position, une variable contenant -1, 1 ou 0 . Defini par la fonction 'position'.
    '''
    if position == 0:
        f = (0, 0, largeur_plateau * taille_case, 95)
    elif position == 1:
        f = (0, 95, largeur_plateau * taille_case, 190)
    elif position == 2:
        f = (0, 190, largeur_plateau * taille_case, 285)
    elif position == 3:
        f = (0, 285, largeur_plateau * taille_case, 380)
    elif position == 4:
        f = (0, 380, largeur_plateau * taille_case, hauteur_plateau * taille_case)
    (x1, y1, x2, y2) = f
    rectangle(x1, y1, x2, y2, couleur = 'Black', remplissage = 'grey')
    texte(150, 30, 'Niveau 1', taille = 35)
    texte(150, 120, 'Niveau 2', taille = 35)
    texte(150, 210, 'Niveau 3', taille = 35)
    texte(150, 300, 'Niveau 4', taille = 35)
    texte(150, 390, 'Niveau 5', taille = 35)
    
def curseur_selection_menu(position, touche):
    '''
    Fonction determinant la position du curseur dans le menu.
    Parametre : position une valeur (soit -1, 0 ou 1), touche (str)
    '''
    if touche == 'Up' or touche == 'z':
        position -= 1
        if position < 0:
            position = 0
    elif touche == 'Down' or touche == 's':
        position += 1
        if position > 4:
            position = 4
    f = position
    return f

## Affichage du jeu ##

def dessine_grille(grille, noircie):
    """
    Fonction qui dessine la grille et les noircissements des cases.
    grille: Liste de listes des valeurs de la grille
    noircie: Coordonnées des cases noircies. De type set().
    """
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if (j, i) in noircie:
                rectangle(i * taille_case + 45, j * taille_case + 110, (i + 1) * taille_case + 45, (j + 1) * taille_case + 110, remplissage = "Black", epaisseur = 2)
            else:
                rectangle(i * taille_case + 45, j * taille_case + 110, (i + 1) * taille_case + 45, (j + 1) * taille_case + 110, remplissage = "White", epaisseur = 2)


def affiche_chiffre(grille):
    """
    Fonction qui affiche les chiffres à la position des cases qui lui correspondent.
    grille: Liste de listes des valeurs de la grille.
    """
    for loop in range(len(grille)):
        for loop2 in range(len(grille[loop])):
            texte(loop2 * (taille_case) + 65 , loop * (taille_case) + 130 , str(grille[loop][loop2]), couleur = "black", taille = 16)

def changer_etat(x, y, grille, noircie):
    """
    Fonction qui change l'état d'une case après un clic.
    x, y = Coordonnées du clic
    grille = Coordonnees des valeurs de la grille.
    tableau_etat = Tableau d'état des cases.
    """
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if (y, x) == (i, j):
                if (y, x) not in noircie:
                    noircie.add((y, x))
                else:
                    noircie.remove((y, x))
    return noircie


def annuler(noircie, stockage):
    """
    Fonction qui permet d'annuler le dernier coup du joueur avec le bouton n.
    noircie = Coordonnées des cases noircies. De type set().
    stockage = Liste contenant l'historique du jeu.
    """
    if stockage != [set()]:
        stockage.pop()
    noircie = stockage[len(stockage) - 1]
    return noircie
    
## Menu de pause ##

def affiche_menu_pause(position):
    '''
    Fonction affichant le menu de pause.
    Parametre : position, une variable contenant -1, 1 ou 0 . Definis par la fonction 'position'.
    '''
    if position == 0:
        f = (0, 0, largeur_plateau * taille_case, (hauteur_plateau * taille_case) // 4)
    elif position == 1:
        f = (0, (hauteur_plateau * taille_case) // 4 , largeur_plateau * taille_case, (hauteur_plateau * taille_case) // 2)
    elif position == 2:
        f = (0, (hauteur_plateau * taille_case) // 2 , largeur_plateau * taille_case, hauteur_plateau * taille_case)
    (x1, y1, x2, y2) = f
    rectangle(x1, y1, x2, y2, couleur = 'Black', remplissage = 'grey')
    texte((largeur_plateau * taille_case) / 4, (hauteur_plateau * taille_case) / 10 , 'Changer   Grille', taille = 35)
    texte((largeur_plateau * taille_case) / 4, (hauteur_plateau * taille_case) / 3 , 'Recommencer', taille = 35)
    texte((largeur_plateau * taille_case) / 3, (hauteur_plateau * taille_case) / 1.5, 'Quitter', taille = 35)

def curseur_menu_pause(position, touche):
    '''
    Fonction determinant la position du curseur dans le menu.
    Parametre : position une valeur (soit -1, 0 ou 1), touche (str)
    '''
    if touche == 'Up' or touche == 'z':
        position -= 1
        if position < 0:
            position = 0
    elif touche == 'Down' or touche == 's':
        position += 1
        if position > 2:
            position = 2
    f = position
    return f


### Tache 4: Solveur automatique ###

def sans_conflit_cellule(grille, i, j):
    """
    Une version modifiée de la fonction sans_conflit, mais uniquement pour une cellule et pas toute une grille.
    grille: Liste des listes des valeurs de la grille
    i: Abscisse de la grille
    j: Ordonnée de la grille
    """
    length = len(grille)
    for ligne in range(length):
        for colonne in range(len(grille[ligne])):
            if (grille[i][j] == grille[ligne][j] and i != ligne) or (grille[i][j] == grille[i][colonne] and j != colonne):
                return False
    return True


def resoudre(grille, noircie, i = 0, j = 0):
    """
    Fonction qui trouve automatiquement la solution d'une grille.
    grille = Liste de liste des données de la grille
    noircie = Liste des coordonnées des cases noircies
    i = Ligne
    j = Colonne
    >>> resoudre([['2','2','1','5','3'],['2','3','1','4','5'],['1','1','1','3','5'],['1','3','5','4','2'],['5','4','3','2','1']], set())
    {(0, 0), (3, 3), (3, 1), (1, 4), (2, 0), (2, 2), (0, 2)}
    """
    if i >= len(grille):
        return None
    ## 1.
    if sans_voisines(grille, noircie) == False or connexe(grille, noircie) == False:
        return None
    ## 2.
    if sans_voisines(grille, noircie) == True:
        if connexe(grille, noircie) == True:
            if sans_conflit(grille, noircie) == True:
                return noircie
    ## 3.
            else:
                ## 3.a )
                if sans_conflit_cellule(grille, i, j) == True:
                    if j >= len(grille[0]) - 1:
                        solution = resoudre(grille, noircie, i + 1, 0)
                    else:
                        solution = resoudre(grille, noircie, i, j + 1)
                ## 3.b )
                else:
                    noircie.add((i, j))
                    if j >= len(grille[0]) - 1:
                        solution = resoudre(grille, noircie, i + 1, 0)
                    else:
                        solution = resoudre(grille, noircie, i, j + 1)
                    if sans_conflit(grille, noircie) == True:
                        return noircie
                    else:
                        noircie.remove((i, j))
                        if j >= len(grille[0]) - 1:
                            solution = resoudre(grille, noircie, i + 1, 0)
                        else:
                            solution = resoudre(grille, noircie, i, j + 1)
                        if sans_conflit(grille, noircie) == True:
                            return noircie
                        else:
                            return None


#### Mise en pratique du code ####

### Choix aléatoire de la grille ###

f = 0
taille_case = 50

# Taille du plateau
largeur_plateau = 10
hauteur_plateau = 10

# Taille des cases
taille_case = 50

#Fenetre
cree_fenetre(largeur_plateau * taille_case, hauteur_plateau * taille_case)

#Initialisation des valeurs
Menu = False
nbre_coups = 0
cases_noires = set()
stockage = [set()]
SortieDuMenu = False
Sortie = False

### Boucle principale du jeu ###

while True:
    ## Menu de sélection de niveau ##
    if SortieDuMenu == False:
        ordre = 0
        while True:
            efface_tout()
            image(0, 0, "Image4.png")
            affiche_selection_niveau(ordre)
            eve = attend_ev()
            ty = type_ev(eve)
            if ty == "Touche":
                if touche(eve) == "Return":
                    if ordre == 0:
                        f = open('niveau1.txt')
                    if ordre == 1:
                        f = open('niveau2.txt')
                    if ordre == 2:
                        f = open('niveau3.txt')
                    if ordre == 3:
                        f = open('niveau4.txt')
                    if ordre == 4:
                        f = open('niveau5.txt')
                        
                    mylist = f.readlines()
                    
                    SortieDuMenu = True
                    
                    ferme_fenetre()
                    
                    largeur_plateau = len(lire_grille(mylist)[0]) + 5
                    hauteur_plateau = len(lire_grille(mylist)) + 5
                    
                    cree_fenetre(taille_case * (largeur_plateau), taille_case * (hauteur_plateau))
                    print(lire_grille(mylist))
                    print(afficher_grille(lire_grille(mylist)))
                    
                    break
            if ty == 'Quitte':
                Sortie = True
                break
            else:
                position = curseur_selection_menu(ordre, touche(eve))
                ordre = position
            
    if Sortie == True:
        break

    ev = donne_ev()
    ty = type_ev(ev)
    
    if ordre == 0:
        f = open('niveau1.txt')
    if ordre == 1:
        f = open('niveau2.txt')
    if ordre == 2:
        f = open('niveau3.txt')
    if ordre == 3:
        f = open('niveau4.txt')
    if  ordre == 4:
        f = open('niveau5.txt')
    
    mylist = f.readlines()
    efface_tout()
    
    ## Le jeu ##
    
    if ty == 'Quitte':
        break
    if Menu == False and SortieDuMenu == True:
        
        ## Interface graphique ##
        
        image(0, 0, "Image4.png")
        dessine_grille(lire_grille(mylist), cases_noires)
        affiche_chiffre(lire_grille(mylist))
        texte((largeur_plateau * taille_case) // 2.5, 20, "Hitori", couleur = "white", taille = 30)
        rectangle((largeur_plateau * taille_case) - 190, 115, (largeur_plateau * taille_case) - 20, 325, epaisseur = 5)
        texte((largeur_plateau * taille_case) - 160, 125, "Règles", couleur = "white", taille = 20)
        texte((largeur_plateau * taille_case) - 180, 175, ("Conflits?:", str(sans_conflit(lire_grille(mylist), cases_noires))), couleur = "white", taille = 16)
        texte((largeur_plateau * taille_case) - 180, 225, ("Voisines?:", str(sans_voisines(lire_grille(mylist), cases_noires))), couleur = "white", taille = 16)
        texte((largeur_plateau * taille_case) - 180, 275, ("Connexe?:", str(connexe(lire_grille(mylist), cases_noires))), couleur = "white", taille = 16)
        texte((largeur_plateau * taille_case) - ((largeur_plateau * taille_case) - 20) , (hauteur_plateau * taille_case) - 125, "Instructions:", couleur = "white", taille = 16)
        texte((largeur_plateau * taille_case) - ((largeur_plateau * taille_case) - 20) , (hauteur_plateau * taille_case) - 100, "Espace = Menu de pause", couleur = "white", taille = 16)
        texte((largeur_plateau * taille_case) - ((largeur_plateau * taille_case) - 20) , (hauteur_plateau * taille_case) - 75, "Bouton G = Annulation du dernier coup", couleur = "white", taille = 16)
        texte((largeur_plateau * taille_case) - ((largeur_plateau * taille_case) - 20) , (hauteur_plateau * taille_case) - 50, "Bouton N = Résolution automatique de la grille", couleur = "white", taille = 16)
        rectangle((largeur_plateau * taille_case) - ((largeur_plateau * taille_case) - 15) , (hauteur_plateau * taille_case) - 130, (largeur_plateau * taille_case) - 20, (hauteur_plateau * taille_case) - 20, epaisseur = 5)
        
        ## Noircissement des cases ##
        if ty == 'ClicGauche':
            x_joueur, y_joueur = ((abscisse(ev) - 45) // taille_case, (ordonnee(ev) - 110) // taille_case)
            if 0 <= x_joueur < len(lire_grille(mylist)) and 0 <= y_joueur < len(lire_grille(mylist)[0]):
                nbre_coups += 1
                print("Nombre de coups:", nbre_coups)
                cases_noires = changer_etat(x_joueur, y_joueur, lire_grille(mylist), cases_noires)
                stockage += [cases_noires.copy()]
                print("Cases noires:", cases_noires)

        if ty == 'Touche':
            
            # Annuler le dernier coup #
            if touche(ev) == 'g' or touche(ev) == 'G':
                cases_noires = annuler(cases_noires, stockage).copy()
                print("Cases noires:", cases_noires)
                
            # Solveur automatique #
            if touche(ev) == "n" or touche(ev) == "N":
                if resoudre(lire_grille(mylist), cases_noires) != None:
                    cases_noires = resoudre(lire_grille(mylist), cases_noires)
                    stockage += [cases_noires.copy()]
                    print("Cases noires:", cases_noires)
                else:
                    print("Pas de solution !")
                
        ## Message de victoire ##
        if sans_conflit(lire_grille(mylist), cases_noires) == True and sans_voisines(lire_grille(mylist), cases_noires) == True and connexe(lire_grille(mylist), cases_noires) == True:
            texte((largeur_plateau * taille_case) // 6, 60, "Victoire en " + str(nbre_coups) + " coups!", couleur = "blue", taille = 30)
            
    ## Menu de pause ##

    elif Menu == True:
        ordre2 = 0
        while True:
            efface_tout()
            image(0, 0, "Image4.png")
            affiche_menu_pause(ordre2)
            eve = attend_ev()
            if touche(eve) == 'space': # Espace = Bouton de pause
                efface_tout()
                Menu = False
                break
            if touche(eve) == 'Return' and ordre2 == 0: # Si on sélectionne "Changer de grille":
                SortieDuMenu = False
                Menu = False
                cases_noires = set()
                stockage = [set()]
                ferme_fenetre()
                largeur_plateau = 10
                hauteur_plateau = 10
                cree_fenetre(largeur_plateau * taille_case, hauteur_plateau * taille_case)
                nbre_coups = 0
                break
            if touche(eve) == 'Return' and ordre2 == 1: # Si on sélectionne "Recommencer":
                efface_tout()
                Menu = False
                cases_noires = set()
                stockage = [set()]
                nbre_coups = 0
                break
            if touche(eve) == 'Return' and ordre2 == 2:  # Si on sélectionne "Quitter":
                efface_tout()
                Menu = None
                break
            else:
                position = curseur_menu_pause(ordre2, touche(eve))
                ordre2 = position
            mise_a_jour()
    if ty == 'Touche':
        if touche(ev) == 'space': # Espace = Bouton de pause
            Menu = True
    if Menu == None:
        break
    mise_a_jour()

PlaySound(None, SND_LOOP + SND_ASYNC)
ferme_fenetre()