# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = []
        self.is_on_a_port = False
        self.finish = False
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
        """ Fonction qui demande la direction, la vérifie, bouge le robot et si
        on demande de quitter avec la lettre "q", elle renvoie True, ce que permet d'enregistrer la partie """
        self.__str__()
        print("\n\n")
        position_robot = None
        #Pour trouver la position du robot
        for ligne in range(0, len(self.grille)):
            for colonne in range(0, len(self.grille[ligne])):
                if self.grille[ligne][colonne] == "X":
                    position_robot = [ligne, colonne]
        #------------------------------------------------------
        direction = input("Choisisez une direction dans laquelle aller : ")
        direction = direction.lower()
        if direction[0] == "n" or direction[0] == "s" or direction[0] == "e" or direction[0] == "o" or direction[0] == "q":
             nb_de_fois = 0
             if direction[1:2].isnumeric():
                 nb_de_fois = direction[1:2]
             if direction == "n":
                #On execute les actions pour le nord
                #On va au nord donc
                p1 = position_robot[0]
                p2 = position_robot[1]
                #Check si il y a un mur
                if self.grille[p1-1][p2] == "O":
                    print("Il y a un mur, tu ne peux pas passer")
                    return self.bouger()
                #Check si il y a une sortie
                if self.grille[p1-1][p2] == "U":
                    print("Tu as réussi le labyrinthe")
                    self.finish = True
                #Check si on peut passer
                if self.grille[p1-1][p2] == " ":
                    self.grille[p1-1][p2] = "X"
                    if self.is_on_a_port:
                        self.grille[p1][p2] = "."
                        self.is_on_a_port = False
                    else:
                        self.grille[p1][p2] = " "
                if self.grille[p1-1][p2] == ".":
                    self.grille[p1-1][p2] = "X"
                    self.grille[p1][p2] = " "
                    self.is_on_a_port = True

             if direction == "s":
                #Action pour le sud
                #+2 lignes
                p1 = position_robot[0]
                p2 = position_robot[1]
                #Check si il y a un mur
                if self.grille[p1+1][p2] == "O":
                    print("Il y a un mur, tu ne peux pas passer")
                    return self.bouger()
                #Check si il y a une sortie
                if self.grille[p1+1][p2] == "U":
                    print("Tu as réussi le labyrinthe")
                    self.finish = True
                #Check si on peut passer
                if self.grille[p1+1][p2] == " ":
                    self.grille[p1+1][p2] = "X"
                    if self.is_on_a_port:
                        self.grille[p1][p2] = "."
                        self.is_on_a_port = False
                    else:
                        self.grille[p1][p2] = " "
                if self.grille[p1+1][p2] == ".":
                    self.grille[p1+1][p2] = "X"
                    self.grille[p1][p2] = " "
                    self.is_on_a_port = True
             if direction == "e":
                   #Action pour le sud
                #+2 lignes
                p1 = position_robot[0]
                p2 = position_robot[1]
                #Check si il y a un mur
                if self.grille[p1][p2-1] == "O":
                    print("Il y a un mur, tu ne peux pas passer")
                    return self.bouger()
                #Check si il y a une sortie
                if self.grille[p1][p2-1] == "U":
                    print("Tu as réussi le labyrinthe")
                    self.finish = True
                #Check si on peut passer
                if self.grille[p1][p2-1] == " ":
                    self.grille[p1][p2-1] = "X"
                    if self.is_on_a_port:
                        self.grille[p1][p2] = "."
                        self.is_on_a_port = False
                    else:
                        self.grille[p1][p2] = " "
                if self.grille[p1][p2-1] == ".":
                    self.grille[p1][p2-1] = "X"
                    self.grille[p1][p2] = " "
                    self.is_on_a_port = True
             if direction == "o":
                                 #Action pour le sud
                #+2 lignes
                p1 = position_robot[0]
                p2 = position_robot[1]
                #Check si il y a un mur
                if self.grille[p1][p2+1] == "O":
                    print("Il y a un mur, tu ne peux pas passer")
                    return self.bouger()
                #Check si il y a une sortie
                if self.grille[p1][p2+1] == "U":
                    print("Tu as réussi le labyrinthe")
                    self.finish = True
                #Check si on peut passer
                if self.grille[p1][p2+1] == " ":
                    self.grille[p1][p2+1] = "X"
                    if self.is_on_a_port:
                        self.grille[p1][p2] = "."
                        self.is_on_a_port = False
                    else:
                        self.grille[p1][p2] = " "
                if self.grille[p1][p2+1] == ".":
                    self.grille[p1][p2+1] = "X"
                    self.grille[p1][p2] = " "
                    self.is_on_a_port = True
             if direction == "q":
                #Save the game
                return True

        else:
            print("Veuillez entrer une direction valide (N, S, E, O)")
            return self.bouger()
