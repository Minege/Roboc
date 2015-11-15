# coding:Utf-8

"""Ce module contient la classe Carte."""
import pickle
import os
import Labyrinthe


class Carte:
    nb_de_objet = 0
    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.chaine = chaine
        self.labyrinthe = Labyrinthe.Labyrinthe(chaine)
        Carte.nb_de_objet += 1
    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def demander_carte(self):
        carte = input("Choisisez une carte parmi celles-ci : ")

        try:
            carte = int(carte)
            carte -= 1
        except TypeError:
            print("Tu dois entrer un nombre !")
            return self.demander_carte()
        except ValueError:
            print("Tu dois entrer un nombre !")
            return self.demander_carte()
        return carte

    def enregistrer_partie(self):
        with open("partie_Roboc.minege", "wb") as partie:
            mon_pickler = pickle.Pickler(partie)
            mon_pickler.dump(self.labyrinthe)

    def ouvrire_partie(self):

        if os.path.isfile("partie_Roboc.minege"):
            with open("partie_Roboc.minege", "rb") as partie:
                mon_unpickler = pickle.Unpickler(partie)
                choix = ""
                while choix != "N" or choix != "O":
                    choix = input("Vous aviez dèja une partie en cours, voulez-vous la continuer ? O : Oui/N : Non")
                    choix = choix.upper()
                    if choix == "O":
                        print("La partie va recommencer depuis là ou vous étiez")
                        self.labyrinthe = mon_unpickler.load()
                        return True

                    if choix == "N":
                        print("Une nouvelle partie va commencer")
                        partie.close()
                        os.remove("partie_Roboc.minege")
                        return False
        else:
            pass
    def reset_map(self):
        self.labyrinthe = None
        self.labyrinthe = Labyrinthe.Labyrinthe(self.chaine)