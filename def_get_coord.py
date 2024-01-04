from def_grid import generation_grid, affichage_grid
import random
import time
import os

nbr_ligne = 20
nbr_column = 20

grille_test = generation_grid(nbr_ligne,nbr_column)
affichage_grid(grille_test)

def get_coord(x,y,direction):
    # Scan de la case à droite
    if direction == "droite":
        if y < nbr_column - 1:
            coord_droite = (x, (y+1))
        else: 
            coord_droite = (x,0)
        return coord_droite
    #  Scan de la case à gauche
    elif direction == "gauche":       
        if y > 0:
            coord_gauche = (x,(y-1))
        else: 
            coord_gauche = (x,-1)
        return coord_gauche
    # Scan de la case en bas
    elif direction == "bas":        
        if x < nbr_ligne - 1:
            coord_bas = ((x+1),y)
        else: 
            coord_bas = (0,y)
        return coord_bas
    # Scan de la case en haut
    elif direction == "haut": 
        if x > 0:
            coord_haut = ((x-1),y)
        else: 
            coord_haut = (-1,y)
        return coord_haut
    else:
        print("mauvaise direction")
