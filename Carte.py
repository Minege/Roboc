# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
import pickle

import Labyrinthe


class Carte:
    nb_de_objet = 0
    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = Labyrinthe.Labyrinthe("X", chaine)
        Carte.nb_de_objet += 1
    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def demander_carte(self):
        carte = input("Choisisez une carte parmi celles-ci : ")

        try:
            carte = int(carte)
        except TypeError:
            print("Tu dois entrer un nombre !")
            return self.demander_carte()
        except ValueError:
            print("Tu dois entrer un nombre !")
            return self.demander_carte()
        return carte

    def enregistrer_partie(self):
        mon_pickler = pickle.Pickler("partie_Roboc")
        mon_pickler.dump(self.labyrinthe)

    def ouvrire_partie(self):
        # Verifier si il n'y a pas dèja une partie, et puis après, ouvrire le fichier
        mon_unpickler = pickle.Unpickler("partie_Roboc")
        if mon_unpickler.load() is "":
            return False
        else:
            choix = ""
            while choix != "N" or choix != "O":
                choix = input("Vous aviez dèja une partie en cours, voulez-vous la continuer ? O/N")
                if choix == "O".lower():
                    print("La partie va recommencer depuis là ou vous étiez")
                    self.labyrinthe = mon_unpickler.load()
                    return True
                elif choix == "N".lower():
                    print("Une nouvelle partie va commencer")
                    return False
        return "Partie pas ouverte"
