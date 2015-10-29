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
        for lettre in obstacles:
            if lettre == "\n":
                ligne += 1
                colonne = 0
            colonne += 1
            self.grille[ligne, colonne] = lettre
        # Affichage POUR QUE CA MARCHE IL FAUT QUE SELF.GRILLE AIS PAS DE LA MERDE DEDANS
        l = 0
        c = 0
        ligne_str = ""
        while l < ligne:
            while c < colonne:
                ligne_str += self.grille[ligne, colonne]
                c += 1
            l += 1
            c = 0
            print(ligne_str, end="")
            ligne_str = ""  # Clean de la ligne, pour afficher les autres

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
