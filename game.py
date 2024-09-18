import time
import numpy as np
from grid import Grid
from player import Player

class Game:
    def __init__(self):
        self.grid = Grid()
        self.players = [Player('X'), Player('O')]
        self.current_player = 0

    def play(self):
        while True:
            self.grid.display()
            player = self.players[self.current_player]
            print(f"Tour du joueur {player.symbol}")
            
            while True:
                try:
                    row, col = self.recuperer_coordonnees()
                    if self.grid.place_mark(row, col, player.symbol):
                        break
                    else:
                        print("Cette case est déjà occupée. Réessayez.")
                except ValueError:
                    print("Coordonnées invalides. Réessayez.")

            if self.grid.check_victory(player.symbol):
                self.grid.display()
                print(f"Le joueur {player.symbol} a gagné !")
                self.end_game(5) # Ajout délai à la fin d'une partie avant le fermeture de la window
                break

            if self.grid.is_full():
                self.grid.display()
                print("Match nul !")
                self.end_game(5) # Ajout délai à la fin d'une partie avant le fermeture de la window
                break

            self.current_player = (self.current_player + 1) % 2

    def recuperer_coordonnees(self):
        while True:
            try:
                row = int(input("Entrez le numéro de ligne (0-2) : "))
                col = int(input("Entrez le numéro de colonne (0-2) : "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Les coordonnées doivent être entre 0 et 2.")
            except ValueError:
                print("Veuillez entrez des nombres entiers.")
    
    def end_game(self, delay):
        print(f"La partie se terminera dans {delay} secondes...")
        time.sleep(delay)
        self.grid.close()