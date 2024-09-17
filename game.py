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
                    row, col = self.get_coordinates()
                    if self.grid.place_mark(row, col, player.symbol):
                        break
                    else:
                        print("Cette case est déjà occupée. Réessayez.")
                except ValueError:
                    print("Coordonnées invalides. Réessayez.")

            if self.grid.check_victory(player.symbol):
                self.grid.display()
                print(f"Le joueur {player.symbol} a gagné !")
                break

            if self.grid.is_full():
                self.grid.display()
                print("Match nul !")
                break

            self.current_player = (self.current_player + 1)