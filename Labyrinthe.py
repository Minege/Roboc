#coding:Utf-8

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, obstacles):
        self.grille = []
        self.is_on_a_port = False
        self.finish = False
        # Initialisation du dictionnaire
        self.nb_de_char_grille = []
        char_grille = []
        nb_de_char = 0
        for lettre in obstacles:
            nb_de_char += 1
            if lettre == "\n":
                self.nb_de_char_grille.append(nb_de_char)
                nb_de_char = 0
            char_grille.append(lettre)
        self.nb_de_char_grille.append(nb_de_char)
        del nb_de_char

        x = 0
        for y in self.nb_de_char_grille:
            tempList = []
            for z in range(0, y):
                tempList.append(char_grille[x + z])
            self.grille.append(tempList)
            x += y

    def __str__(self):
        for ligne in self.grille:
            for colonne in ligne:
                print(colonne, end="")

    def verifier_mur_dans_la_ligne(self, p1, p2, direction):
        direction = direction.upper()
        if direction == "N":
            for obstacle in range(p1, 0):
                print(obstacle)
                if self.grille[obstacle][p2] == "O":
                    print("Tu ne peux pas passer, il y a un mur #MINEGECODING")
                    return False
        if direction == "S":
            for obstacle in range(p1, self.nb_char_grille[p1]):
                if self.grille[obstacle][p2] == "O":
                    print("Tu ne peux pas passer, il y a un mur")
                    return False
        if direction == "E":
            pass
        if direction == "O":
            pass
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
        #TODO: Mettre les jumps de plusieurs coup

        direction = input("Choisisez une direction dans laquelle aller : ")
        direction = direction.lower()

        if direction[0] == "n" or direction[0] == "s" or direction[0] == "e" or direction[0] == "o" or direction[0] == "q":

             nb_de_fois = 1
             if direction[1:2].isnumeric():
                 nb_de_fois = direction[1:2]
                 nb_de_fois = int(nb_de_fois)
             else:
                 nb_de_fois = 1

             if direction[0] == "n":
                #On execute les actions pour le nord
                #On va au nord donc -nb_de_fois sur les lignes
                p1 = position_robot[0]
                p2 = position_robot[1]
                #Check si il y a un mur
                self.verifier_mur_dans_la_ligne(p1, p2, direction[0])
                if self.grille[p1-nb_de_fois][p2] == "O":
                    print("Il y a un mur, tu ne peux pas passer")
                    return self.bouger()
                #Check si il y a une sortie
                if self.grille[p1-nb_de_fois][p2] == "U":
                    print("Tu as réussi le labyrinthe")
                    self.finish = True
                #Check si on peut passer
                if self.grille[p1-nb_de_fois][p2] == " ":
                    self.grille[p1-nb_de_fois][p2] = "X"
                    if self.is_on_a_port:
                        self.grille[p1][p2] = "."
                        self.is_on_a_port = False
                    else:
                        self.grille[p1][p2] = " "
                if self.grille[p1-nb_de_fois][p2] == ".":
                    self.grille[p1-nb_de_fois][p2] = "X"
                    self.grille[p1][p2] = " "
                    self.is_on_a_port = True

             if direction[0] == "s":
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
             if direction[0] == "e":
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

             if direction[0] == "o":
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
