# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            cartes.append(Carte.Carte(nom_carte, contenu))
# On affiche les cartes existantes
print("")
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# if Carte.Carte.ouvrire_partie():
#    print("---Reprise de la partie en cours---")
# else:
choix = Carte.Carte.demander_carte(Carte.Carte)

while input("entre 1 pour continuer") is not "1":
    cartes[choix]._labyrinthe.bouger()

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
