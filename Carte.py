# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
import Labyrinthe
class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        l = Labyrinthe.Labyrinthe("X", chaine)
        return l

    def demander_carte(self):
        carte = input("Choisisez une care parmi celles-ci : ")

        try:
            carte = int(carte)
        except TypeError:
            print("Tu dois entrer un nombre !")
            return self.demander_carte()
        except ValueError:
            print("Tu dois entrer un nombre !")
            return self.demander_carte()
        return carte
