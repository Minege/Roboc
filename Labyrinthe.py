# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}
        # Initialisation du dictionnaire
        ligne = 0
        colonne = -1
        colonne_liste = []
        for lettre in obstacles:
            if lettre == "\n":
                colonne_liste.append([ligne, colonne])
                ligne += 1
                colonne = -1
            colonne += 1
            self.grille[ligne, colonne] = lettre
        # Affichage POUR QUE CA MARCHE IL FAUT QUE SELF.GRILLE AIS PAS DE LA MERDE DEDANS
        l = 0
        c = 0
        ligne_str = ""
        i = 0
        # while i < len(colonne_liste):
        #    while l < colonne_liste[i][0]:
        #        while c < colonne_liste[i][1]:
        #            ligne_str += self.grille[l, c]
        #            c += 1
        #        l += 1
        #        c = 0
        #        print(ligne_str, end="")
        #        ligne_str = ""  # Clean de la ligne, pour afficher les autres
        #    i += 1
        print(colonne_liste)
        l = 0
        c = 0
        nb = 0
        while nb < len(colonne_liste):
            while l < colonne_liste[nb][0]:
                while c < colonne_liste[nb][1]:
                    print(self.grille[l, c], end="")
                    c += 1
                l += 1
                nb += 1
            # print("AFFICHAGE DE LA GRILLE avec le string directe:")
            # la = 0
            # ca = 0
            # ligne_str = ""
            # for lettre in obstacles:
            #    if lettre == "\n":
            #        la += 1
            #        ca = 0
            #        print(ligne_str, end="")
            #        ligne_str = ""
            #    ligne_str += lettre
            #    ca += 1
