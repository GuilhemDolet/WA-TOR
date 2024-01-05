from constants import *
from def_grid import *
import random

grid = generation_grid(LINES, COLUMNS)
affichage_grid(grid)


class Fish:

    def __init__(self, x = 1, y = 1, type = 1):
        self.x = x
        self.y = y
        self.type = type
        self.turn_alive = G_FISH

    def get_coord(self, direction):
        # Scan de la case à droite
        if self.y < (COLUMNS - 1):
            coord_droite = (self.x, (self.y + 1))
        else: 
            coord_droite = (self.x, 0)
        #  Scan de la case à gauche
        if self.y > 0:
            coord_gauche = (self.x, (self.y - 1))
        else: 
            coord_gauche = (self.x, (COLUMNS - 1))
        # Scan de la case en bas
        if self.x < (LINES - 1):
            coord_bas = ((self.x + 1), self.y)
        else: 
            coord_bas = (0, self.y)
        # Scan de la case en haut
        if self.x > 0:
            coord_haut = ((self.x - 1), self.y)
        else: 
            coord_haut = ((LINES - 1), self.y)

        if direction == "R":
            return coord_droite
        elif direction == "L":
            return coord_gauche
        elif direction == "D":
            return coord_bas
        elif direction == "U":
            return coord_haut
        else:
            print("Wrong direction")

    def scan_des_cases_voisines(self):

        case_droite = self.get_coord("R")
        case_gauche = self.get_coord("L")
        case_bas = self.get_coord("D")
        case_haut = self.get_coord("U")


        # renvoie les coordonnées des cases adjacentes
        return (case_droite, case_gauche, case_bas, case_haut)

   
        
    def move_randomly(self, grid):
        self.turn_alive -= 1
        grid[self.x][self.y] = 0
        self.x, self.y = random.choice(self.scan_des_cases_voisines_avec_type(grid))
        grid[self.x][self.y] = self.type

    def scan_des_cases_voisines_avec_type(self, grid, type=0): # c'est validé
        return_variable = []

        case_droite = self.get_coord("R")
        if grid[case_droite[0]][case_droite[1]] == type:
            return_variable.append(case_droite)

        case_gauche = self.get_coord("L")
        if grid[case_gauche[0]][case_gauche[1]] == type:
            return_variable.append(case_gauche)
        
        case_bas = self.get_coord("D")
        if grid[case_bas[0]][case_bas[1]] == type:
            return_variable.append(case_bas)
        
        case_haut = self.get_coord("U")
        if grid[case_haut[0]][case_haut[1]] == type:
            return_variable.append(case_haut)
        
        # renvoie les coordonnées des cases qui contiennent des 0
        return return_variable