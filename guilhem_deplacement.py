from def_grid import generation_grid, affichage_grid
import random
import time
import os
import constants

grille_test = generation_grid(constants.LINES, constants.COLUMNS)

# variable pour les coordonnées d'un poisson
x = 5
y = 5 

# ajouter un poisson
grille_test[x][y] = 1

# ------------------ Déplacement horizontal vers la droite
# while True:

#     affichage_grid(grille_test)
#     time.sleep(1)
#     os.system("cls")
#     grille_test[x][y] = 0
#     if y < nbr_column - 1:
#         y += 1
#     else:
#         y = 0
#     grille_test[x][y] = 1

# ------------------ Déplacement horizontal vers la gauche
# while True : 

#     affichage_grid(grille_test)
#     time.sleep(1)
#     os.system("cls")
#     grille_test[x][y] = 0
#     if y > 0:
#         y -= 1
#     else:
#         y = nbr_column - 1
    # grille_test[x][y] = 1

# Déplacement vertical vers la haut
# while True : 

#     affichage_grid(grille_test)
#     time.sleep(1)
#     os.system("cls")
#     grille_test[x][y] = 0
#     if x > 0:
#         x -= 1
#     else:
#         x = nbr_ligne - 1
#     grille_test[x][y] = 1
    
# Déplacement vertical vers la bas
while True : 

    affichage_grid(grille_test)
    time.sleep(1)
    os.system("cls")
    grille_test[x][y] = 0
    if x < (constants.LINES - 1):
        x += 1
    else:
        x = 0
    grille_test[x][y] = 1



