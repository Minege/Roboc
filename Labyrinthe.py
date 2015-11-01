# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = []
        # Initialisation du dictionnaire
        nb_de_char_grille = []
        char_grille = []
        nb_de_char = 0
        for lettre in obstacles:
            nb_de_char += 1
            if lettre == "\n":
                nb_de_char_grille.append(nb_de_char)
                nb_de_char = 0
            char_grille.append(lettre)

        x = 0
        for y in nb_de_char_grille:
            tempList = []
            for z in range(0, y):
                tempList.append(char_grille[x + z])

            self.grille.append(tempList)
            x += y

    def __str__(self):
        for ligne in self.grille:
            for colonne in ligne:
                print(colonne, end="")
