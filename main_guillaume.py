from constants import *
from  def_grid import *
from fish import Fish
import time
import os

grid = generation_grid(LINES, COLUMNS)

print()
fish_1 = Fish()
fish_2 = Fish(1,2,2)
fish_3 = Fish(2,1,3)

grid[fish_1.x][fish_1.y] = fish_1.type
grid[fish_2.x][fish_2.y] = fish_2.type
grid[fish_3.x][fish_3.y] = fish_3.type






while True:
    print()
    affichage_grid(grid)
    
    time.sleep(1)
    # os.system("cls")

    fish_1.move_randomly(grid)
    fish_2.move_randomly(grid)
    fish_3.move_randomly(grid)
 



