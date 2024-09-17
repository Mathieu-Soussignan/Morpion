def player(grille):
    while True:
        try:
            ligne = int(input("Entrez la ligne (0, 1, 2) : "))
            colonne = int(input("Entrez la colonne (0, 1, 2) : "))
            if grille[ligne, colonne] == ' ' and 0 <= ligne < 3 and 0 <= colonne < 3:
                return ligne, colonne
            else:
                print("Coordonnées invalides ou case déjà occupée. Essayez de nouveau.")
        except (ValueError, IndexError):
            print("Entrée invalide. Assurez-vous de saisir des nombres entiers entre 1 et 3.")

def placer_marque(grille, ligne, colonne, joueur):
    grille[ligne, colonne] = joueur
