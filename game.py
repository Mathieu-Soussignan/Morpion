import numpy as np
import matplotlib.pyplot as plt
from grid import afficher_grille
from player import player, placer_marque
from grid import verifier_victoire, verifier_match_nul

class Game:
    def __init__(self):
        self.grille = np.full((3, 3), ' ')
        self.joueurs = ['X', 'O']
        self.tour = 0

    def jouer(self):
        while True:
            afficher_grille(self.grille)
            joueur_courant = self.joueurs[self.tour % 2]
            print(f"Tour du joueur {joueur_courant}")

            ligne, colonne = recuperer_coordonnees(self.grille)
            placer_marque(self.grille, ligne, colonne, joueur_courant)

            if verifier_victoire(self.grille, joueur_courant):
                afficher_grille(self.grille)
                print(f"Le joueur {joueur_courant} a gagné !")
                break
            elif verifier_match_nul(self.grille):
                afficher_grille(self.grille)
                print("Match nul !")
                break

            self.tour += 1
