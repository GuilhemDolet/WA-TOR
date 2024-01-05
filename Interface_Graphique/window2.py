from tkinter import *
from PIL import ImageTk, Image
from def_grid import generation_grid
from fish import Fish
import time
import os

# Assuming 'square' is your fish image, load it as a PhotoImage
square = PhotoImage(file="fish_image.png")

# Constants
LINES = 10
COLUMNS = 20

# Fish image placeholder, replace it with your actual fish image
fish_image = PhotoImage(file="fish_image.png")

grid = generation_grid(LINES, COLUMNS)

# Create fishes
fishes = [Fish(0, 0, 1), Fish(2, 2, 1), Fish(4, 4, 1)]

for fish in fishes:
    grid[fish.x][fish.y] = fish.type

def simulate_step():
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

def play_button_clicked():
    # Define the action to be performed when the "Play" button is clicked
    simulate_step()



# Tkinter GUI
window = Tk()
window.title("Projet WA-Tor")
window.geometry("1024x512")
window.minsize(800, 288)
window.iconbitmap("logo.ico")
window.configure(background="#33d7ff")

# Background image
bg_image = ImageTk.PhotoImage(file="background.png")

canvas = Canvas(window, width=800, height=288)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

label = Label(window, image=bg_image)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Fish image placeholder
fish = canvas.create_image(0, 0, image="blue")

# Buttons
B1 = Button(window, text="Play", command=play_button_clicked)
B2 = Button(window, text="Reset", command=reset_button_clicked)
B1 = canvas.create_window(0, 10, anchor="nw", window=B1)
B2 = canvas.create_window(30, 10, anchor="nw", window=B2)

# Resize handler
def resizer(e):
    global bg_image

    # BICUBIC works better for resizing images
    resized_bg = Image.open("background.png").resize((e.width, e.height), Image.BICUBIC)
    bg_image = ImageTk.PhotoImage(resized_bg)
    label.configure(image=bg_image)
    label.image = resized_bg

# Menu
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=10)
file_menu.add_command(label="Quit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

window.bind('<Configure>', resizer)

window.mainloop()


