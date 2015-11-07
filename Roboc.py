#coding:Utf-8
"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from Carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            cartes.append(Carte(nom_carte, contenu))
# On affiche les cartes existantes

continuer_jeu = True

while continuer_jeu:
    print("")
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))

    # if Carte.Carte.ouvrire_partie():
    #    print("---Reprise de la partie en cours---")
    # else:
    choix = Carte.demander_carte(Carte)
    cartes[choix].ouvrire_partie()
    while cartes[choix].labyrinthe.finish != True:
        if cartes[choix].labyrinthe.bouger() == True:
            cartes[choix].enregistrer_partie()
            quit()
        else:
            cartes[choix].enregistrer_partie()

    if os.path.isfile("partie_Roboc.minege"):
        os.remove("partie_Roboc.minege")

    cartes[choix].reset_map()
    while continuer_jeu:
        l = input("Voulez-vous refaire une partie ? [O : Oui/N : Non] : ")
        l = l.upper()
        print(l.upper())
        if l == "N":
            continuer_jeu = False
            print("Au revoir !")
            quit()
        if l == "O":
            continuer_jeu = False
        else:
            continue
        pass
    continuer_jeu = True