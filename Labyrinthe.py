# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}
        # Initialisation du dictionnaire
        ligne = 0
        colonne = 0
        for lettre in obstacles:
            if lettre == "\n":
                ligne += 1
                colonne = 0
            self.grille[ligne, colonne] = lettre
            colonne += 1

        # Affichage
        l = 0
        c = 0
        ligne_str = ""
        while l < ligne:
            print("")
            while c < colonne:
                ligne_str += self.grille[ligne, colonne - 1]
                c += 1
            print(ligne_str)
            l += 1
