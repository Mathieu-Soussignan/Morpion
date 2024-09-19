# tests_unitaires/test_game.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game import Game
from unittest.mock import patch


def test_initialisation_du_jeu():
    # Création d'une nouvelle instance de jeu
    game = Game()

    # Vérification que le premier joueur utilise bien le symbole "X"
    assert game.players[game.current_player].symbol == "X", "Le premier joueur doit être X"
    # Vérification que la grille a bien une taille de 3x3
    assert game.grid.grid.shape == (3, 3), "Le plateau doit être 3x3"
    # Vérification que toutes les cases de la grille sont vides
    assert (game.grid.grid == ' ').all(), "Toutes les cases doivent être vides (espaces) à l'initialisation"

def test_recuperer_coordonnees():
    game = Game()

    # Test pour des entrées valides
    with patch('builtins.input', side_effect=['1', '2']):
        row, col = game.recuperer_coordonnees()
        assert (row, col) == (1, 2), "Les coordonnées devraient être (1, 2)"

    # Test pour une entrée incorrecte puis correcte
    with patch('builtins.input', side_effect=['5', '1', '0', '2']):
        row, col = game.recuperer_coordonnees()
        assert (row, col) == (0, 2), "Les coordonnées devraient être (0, 2)"



