#coding:Utf-8

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, obstacles):
        self.grille = []
        self.is_on_a_port = False
        self._finish = False
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

    def verifier_mur_dans_la_ligne(self, p1, p2, direction, nb_de_coups):
        direction = direction.upper()
        if direction == "N":
            a = p1-nb_de_coups
            while a < p1:
                if self.grille[a][p2] == "O" :
                    return False
                a += 1
            #Si il sort de la boucle sans être passé par un mur, on return True
            return True
        if direction == "S":
            a = p1+nb_de_coups
            while a > p1:
                if self.grille[a][p2] == "O" :
                    return False
                a -= 1
            #Si il sort de la boucle sans être passé par un mur, on return True
            return True
        if direction == "E":
            a = p2-nb_de_coups
            while a < p2:
                if self.grille[p1][a] == "O" :
                    return False
                a += 1
            #Si il sort de la boucle sans être passé par un mur, on return True
            return True
        if direction == "O":
            a = p2+nb_de_coups
            while a > p2:
                if self.grille[p1][a] == "O" :
                    return False
                a -= 1
            #Si il sort de la boucle sans être passé par un mur, on return True
            return True


    def bouger(self):
        """ Fonction qui demande la direction, la vérifie, bouge le robot et si
        on demande de quitter avec la lettre "q", elle renvoie True, ce que permet d'enregistrer la partie """
        try:
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
            if direction == "" or direction == None:
                return self.bouger()
            if direction[0] == "n" or direction[0] == "s" or direction[0] == "e" or direction[0] == "o" or direction[0] == "q":

                 nb_de_fois = 1
                 if direction[1:2].isnumeric():
                     nb_de_fois = direction[1:2]
                     nb_de_fois = int(nb_de_fois)
                 else:
                     nb_de_fois = 1
                 p1 = position_robot[0]
                 p2 = position_robot[1]
                 if direction[0] == "n":
                    #Check si il y a un mur
                    if self.verifier_mur_dans_la_ligne(p1, p2, direction[0], nb_de_fois):
                        if self.grille[p1-nb_de_fois][p2] == "O":
                            print("Il y a un mur, tu ne peux pas passer")
                            return self.bouger()
                        #Check si il y a une sortie
                        if self.grille[p1-nb_de_fois][p2] == "U":
                            print("Tu as réussi le labyrinthe")
                            self._finish = True
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
                    else:
                        print("Il y a un mur, tu ne peux pas passer !")
                        return self.bouger()
                 if direction[0] == "s":
                    #Action pour le sud
                    #Check si il y a un mur
                    if self.verifier_mur_dans_la_ligne(p1, p2, direction[0], nb_de_fois):
                        if self.grille[p1+nb_de_fois][p2] == "O":
                            print("Il y a un mur, tu ne peux pas passer")
                            return self.bouger()
                        #Check si il y a une sortie
                        if self.grille[p1+1][p2] == "U":
                            print("Tu as réussi le labyrinthe")
                            self._finish = True
                        #Check si on peut passer
                        if self.grille[p1+nb_de_fois][p2] == " ":
                            self.grille[p1+nb_de_fois][p2] = "X"
                            if self.is_on_a_port:
                                self.grille[p1][p2] = "."
                                self.is_on_a_port = False
                            else:
                                self.grille[p1][p2] = " "
                        if self.grille[p1+nb_de_fois][p2] == ".":
                            self.grille[p1+nb_de_fois][p2] = "X"
                            self.grille[p1][p2] = " "
                            self.is_on_a_port = True
                    else:
                        print("Il y a un mur, tu ne peux pas passer !")
                        return self.bouger()

                 if direction[0] == "e":
                       #Action pour le sud
                    #+2 lignes
                    #Check si il y a un mur
                    if self.verifier_mur_dans_la_ligne(p1, p2, direction[0], nb_de_fois):
                        if self.grille[p1][p2-nb_de_fois] == "O":
                            print("Il y a un mur, tu ne peux pas passer")
                            return self.bouger()
                        #Check si il y a une sortie
                        if self.grille[p1][p2-nb_de_fois] == "U":
                            print("Tu as réussi le labyrinthe")
                            self._finish = True
                        #Check si on peut passer
                        if self.grille[p1][p2-nb_de_fois] == " ":
                            self.grille[p1][p2-nb_de_fois] = "X"
                            if self.is_on_a_port:
                                self.grille[p1][p2] = "."
                                self.is_on_a_port = False
                            else:
                                self.grille[p1][p2] = " "
                        if self.grille[p1][p2-nb_de_fois] == ".":
                            self.grille[p1][p2-nb_de_fois] = "X"
                            self.grille[p1][p2] = " "
                            self.is_on_a_port = True
                    else:
                        print("Il y a un mur, tu ne peux pas passer !")
                        return self.bouger()
                 if direction[0] == "o":
                    #Action pour le sud
                    #+2 lignes
                    #Check si il y a un mur
                    if self.verifier_mur_dans_la_ligne(p1, p2, direction[0], nb_de_fois):
                        if self.grille[p1][p2+nb_de_fois] == "O":
                            print("Il y a un mur, tu ne peux pas passer")
                            return self.bouger()
                        #Check si il y a une sortie
                        if self.grille[p1][p2+nb_de_fois] == "U":
                            print("Tu as réussi le labyrinthe")
                            self._finish = True
                        #Check si on peut passer
                        if self.grille[p1][p2+nb_de_fois] == " ":
                            self.grille[p1][p2+nb_de_fois] = "X"
                            if self.is_on_a_port:
                                self.grille[p1][p2] = "."
                                self.is_on_a_port = False
                            else:
                                self.grille[p1][p2] = " "
                        if self.grille[p1][p2+nb_de_fois] == ".":
                            self.grille[p1][p2+nb_de_fois] = "X"
                            self.grille[p1][p2] = " "
                            self.is_on_a_port = True
                    else:
                        print("Il y a un mur, tu ne peux pas passer !")
                        return self.bouger()
                 if direction == "q":
                    #Save the game
                    return True
            else:
                print("Veuillez entrer une direction valide (N, S, E, O)")
                return self.bouger()
        except IndexError:
            print("Il y a un mur, tu ne peux pas passer !")
    def _get_finish(self): return self._finish
    def _set_finish(self, new_finish): self._finish = new_finish
    finish = property(_get_finish, _set_finish)