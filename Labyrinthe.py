# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}
        colonne = 0
        for lettre in obstacles:
            ligne = 0
            if lettre == "\n":
                self.grille[colonne, ligne] = lettre
                ligne += 1
                colonne = 0
            self.grille[colonne, ligne] = lettre
            colonne += 1

    def __str__(self):
        print(self.grille)
