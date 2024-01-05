from constants import *
from  def_grid import *
from fish import Fish
import time
import os

grid = generation_grid(LINES, COLUMNS)

print()



fishes = []

fish_1 = Fish(1,1,1)
fish_2 = Fish(1,2,2)
fish_3 = Fish(2,1,3)

fishes.append(fish_1)
fishes.append(fish_2)
fishes.append(fish_3)

# grid[fish_1.x][fish_1.y] = fish_1.type
# grid[fish_2.x][fish_2.y] = fish_2.type
# grid[fish_3.x][fish_3.y] = fish_3.type

for fish in fishes:
    grid[fish.x][fish.y] = fish.type

affichage_grid(grid)
print("#######")

while True:
    for fish in fishes:
        time.sleep(1)
        before_moving = (fish.x, fish.y)
        fish.move_randomly(grid)
        after_moving = (fish.x, fish.y)
        if before_moving != after_moving and fish.turn_alive == 0:
            fishes.append(Fish(before_moving[0], before_moving[1]))
            print("Un poisson se crée")
    affichage_grid(grid)



# while True:
#     print()
#     affichage_grid(grid)
    
#     time.sleep(1)
#     # os.system("cls")

#     before_moving = (fish_1.x, fish_1.y)
#     fish_1.move_randomly(grid)
#     after_moving = (fish_1.x, fish_1.y)

#     if before_moving != after_moving and fish_1.turn_alive == 1:
#         fish_child = Fish(before_moving[0], before_moving[1])
#         print(f"coordonnées de x --> {fish_child.x}, coordonnées de y --> {fish_child.y}")

#     print(Fish.all_fish_instances)
#     fish_2.move_randomly(grid)
#     fish_3.move_randomly(grid)
#     print(Fish.instance_count)


 



