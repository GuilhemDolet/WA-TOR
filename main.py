from constants import *
from  def_grid import *
from fish import Fish
import time
import os

grid = generation_grid(LINES, COLUMNS)

print()



fishes = []

fish_1 = Fish(0,0,1)
fish_2 = Fish(2,2,1)
fish_3 = Fish(4,4,1)

fishes.append(fish_1)
fishes.append(fish_2)
fishes.append(fish_3)


for fish in fishes:
    grid[fish.x][fish.y] = fish.type



print("#######")



while len(fishes) < (LINES*COLUMNS):
    os.system("cls")
    
    fishes_to_create = []

    for fish in fishes:
        
        
        before_moving = (fish.x, fish.y)
        fish.move_randomly(grid)
        after_moving = (fish.x, fish.y)

        if before_moving != after_moving and fish.turn_alive == 0:
            fishes_to_create.append((before_moving[0], before_moving[1]))
            grid[before_moving[0]][before_moving[1]] = fish.type
        

    for coord in fishes_to_create:
        fishes.append(Fish(coord[0], coord[1]))
    affichage_grid(grid)          
    time.sleep(1)
