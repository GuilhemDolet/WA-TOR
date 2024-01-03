from def_grid import generation_grid, affichage_grid
import random
import time
import os

nbr_ligne = 10
nbr_column = 10

grille_test = generation_grid(nbr_ligne,nbr_column)

# variable pour les coordonnées d'un poisson
x = 5
y = 5 

# ajouter un poisson
grille_test[x][y] = 1

affichage_grid(grille_test)

# Scanner la case à droite:

if y < nbr_ligne - 1:
    case_droite = grille_test[x][(y+1)]
else: 
    case_droite = grille_test[x][0]
    
print(case_droite)


def scan_des_cases_voisines(x,y):
