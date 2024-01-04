from constants import *
from  def_grid import *
from fish import Fish
import time
import os

grid = generation_grid(LINES, COLUMNS)

print()
fish_1 = Fish()
# fish_2 = Fish(2,2)

grid[fish_1.x][fish_1.y] = fish_1.type
# grid[fish_2.x][fish_2.y] = fish_2.type
affichage_grid(grid)

while True:
    
    affichage_grid(grid)

    time.sleep(1)
    os.system("cls")
    
    fish_1.move_randomly(grid)
    
 


