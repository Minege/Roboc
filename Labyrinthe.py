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

    def bouger(self):
        direction = input("Choisisez une direction dans laquelle aller : ")
        if direction == "n".upper() or direction == "n".upper() or direction == "n".upper() or direction == "n".upper():
             if direction == "N":
                #On execute les actions pour le nord
                print(self.grille)
                self.grille = ["O", "O"]
                position_robot = self.grille.index('O')
                print(self.grille)
                print(position_robot)
             if direction == "S":
                #Action pour le sud
                pass
             if direction == "E":
                pass
             if direction == "O":
                pass

        else:
            print("Veuillez entrer une direction valide (N, S, E, O)")
            return self.bouger()
