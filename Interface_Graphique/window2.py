from tkinter import *
from PIL import Image, ImageTk

def resize_image(event):
    global bg_image
    resized_image = original_image.resize((event.width, event.height), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(resized_image)
    label.config(image=bg_image)
    label.image = bg_image  # Keep a reference to prevent garbage collection

window = Tk()

window.title("Projet WA-Tor")
window.geometry("1024x512")
window.minsize(800, 288)
window.iconbitmap("logo.ico")
window.configure(background="#33d7ff")

original_image = Image.open("background.png")
bg_image = ImageTk.PhotoImage(original_image)

label = Label(window, image=bg_image)
label.place(x=0, y=0, relwidth=1, relheight=1)

window.bind("<Configure>", resize_image)

window.mainloop()

