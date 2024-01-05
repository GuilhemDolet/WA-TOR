import time
from fish import *

LINES = 10
COLUMNS = 10

# génére une grille (support ou arriere plan)

grid = [['0' for _ in range(10)] for _ in range(10)]
print(type(grid))

# # j'imprime mon monde de départ sans poissons

# # ajouter un poisson (1)

# grid[0][0] = "1"

# # affiche la grille de départ

# for i in grid:
#     print(i)

# # je veux déplacer mon poisson d'un cran vers la droite

# time.sleep(1)

# os.system("cls")

# grid[0][1] = "1"
# grid[0][0] = "0"

# for i in grid:
#     print(i)

# # je veux déplacer mon poisson d'un cran vers le haut

# time.sleep(1)

# os.system("cls")

# grid[0][1] = "0"
# grid[9][1] = "1"

# for i in grid:
#     print(i)

# # je veux déplacer mon poisson d'un cran vers le bas

# time.sleep(1)

# os.system("cls")
    
# grid[9][1] = "0"
# grid[0][1] = "1"

# for i in grid:
#     print(i)

# # je veux déplacer mon poisson d'un cran vers la gauche
    
# time.sleep(1)

# os.system("cls")
    
# grid[0][1] = "0"
# grid[0][0] = "1"

# for i in grid:
#     print(i)