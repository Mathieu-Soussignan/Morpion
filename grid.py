import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def afficher_grille(grille):
    plt.figure(figsize=(6, 6))
    plt.gca().add_patch(Rectangle((0, 0), 1, 1, edgecolor='black', facecolor='white', linewidth=2))
    
    for i in range(1, 3):
        plt.plot([i/3, i/3], [0, 1], color='black', linewidth=2)
        plt.plot([0, 1], [i/3, i/3], color='black', linewidth=2)
    
    for i in range(3):
        for j in range(3):
            if grille[i, j] == 'X':
                plt.text(j/3 + 0.5/3, 1 - i/3 - 0.5/3, 'X', fontsize=24, ha='center', va='center', color='blue')
            elif grille[i, j] == 'O':
                plt.text(j/3 + 0.5/3, 1 - i/3 - 0.5/3, 'O', fontsize=24, ha='center', va='center', color='red')
    
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().invert_yaxis()
    plt.grid(False)
    plt.show()

def verifier_victoire(grille, joueur):
    for i in range(3):
        if np.all(grille[i, :] == joueur) or np.all(grille[:, i] == joueur):
            return True
    if np.all(np.diag(grille) == joueur) or np.all(np.diag(np.fliplr(grille)) == joueur):
        return True
    return False

def verifier_match_nul(grille):
    return np.all(grille != ' ')
