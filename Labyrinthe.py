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

        # On a la longueur de chaque ligne, et les caractères
        print(len(nb_de_char_grille))
        print(nb_de_char_grille)
        print(char_grille)
        print(len(char_grille))
        i = 1
        while i < len(nb_de_char_grille):
            for numero_ligne in range(len(nb_de_char_grille)):
                ligne = [char_grille[i]] * nb_de_char_grille[i]
                self.grille.append(ligne)
                i += 1
        print(self.grille)

        for ligne in self.grille:
            for case in ligne:
                print(case, end="")
            print()  # Après une ligne on fait un retour à la ligne
