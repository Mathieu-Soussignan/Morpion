# Jeu du Morpion (Tic-Tac-Toe)

## Description

Le Morpion (Tic-Tac-Toe) est une implémentation en Python du célèbre jeu où deux joueurs s'affrontent pour aligner trois symboles (X ou O) sur une grille 3x3. Ce projet utilise une architecture modulaire pour séparer la logique du jeu, la grille et les joueurs, facilitant ainsi l'extension ou la modification du code.

## Prérequis

Assurez-vous d'avoir Python 3.x installé sur votre machine. Vous pouvez le télécharger [ici](https://www.python.org/downloads/).

## Installation

Clonez ce dépôt et accédez au répertoire du projet.

```bash
git clone https://github.com/Mathieu-Soussignan/Morpion.git
cd Morpion
```
## Utilisation

Pour lancer le jeu, exécutez simplement le fichier main.py :

```bash
python main.py
```

## Structure du projet

```bash
	•	main.py : Le point d’entrée du programme. Ce fichier lance le jeu.
	•	game.py : Gère la logique du jeu, le déroulement des tours, et les vérifications pour voir si un joueur a gagné ou si le match est nul.
	•	grid.py : Responsable de la gestion de la grille (plateau de jeu), incluant la mise à jour des positions et la vérification des conditions de victoire.
	•	player.py : Contient la logique des joueurs. Chaque joueur a un symbole (X ou O) et peut effectuer un mouvement sur la grille.
```


### Fonctionnement

Le jeu se déroule en alternance entre deux joueurs (X et O), qui choisissent chacun une case sur la grille 3x3 pour y placer leur symbole. Le but est d’aligner trois symboles identiques à l’horizontale, verticale, ou diagonale. Le premier joueur à le faire gagne la partie. Si toutes les cases sont remplies sans qu’un joueur ait gagné, le jeu se termine par un match nul.

### Contribution

Si vous souhaitez contribuer à ce projet, merci de suivre les étapes suivantes :

```bash
	1.	Fork ce dépôt.
	2.	Créez une branche pour votre fonctionnalité (git checkout -b fonctionnalité/nouvelle-fonctionnalité).
	3.	Commitez vos changements (git commit -m 'Ajout de nouvelle fonctionnalité').
	4.	Poussez vers la branche (git push origin fonctionnalité/nouvelle-fonctionnalité).
	5.	Ouvrez une Pull Request.
```
## Auteurs

- Mathieu Soussignan.
- 
-


