from tkinter import *
from PIL import ImageTk,Image

window = Tk()

window.title("Projet WA-Tor")
window.geometry("1024x512")
window.minsize(800, 288)
window.iconbitmap("logo.ico")
window.configure(background="#33d7ff")



bg_image = ImageTk.PhotoImage(file="background.png")

canvas = Canvas(window,width=800, height=288)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, image=bg_image, anchor="nw")

label = Label(window, image=bg_image)
label.place(x=0, y=0, relwidth=1, relheight=1)

B1 = Button(window, text="Play")
B2 = Button(window, text="Reset")
  
B1 = canvas.create_window(0,10, anchor="nw", window=B1)
B2 = canvas.create_window(30,10, anchor="nw", window=B2)




def resizer(e):
    global bg_image
 
    #ANTIALIAS erases any distortions around image as it is resized however doesn't work so is used BICUBIC
    resized_bg = Image.open("background.png").resize((e.width, e.height), Image.BICUBIC)
    bg_image = ImageTk.PhotoImage(resized_bg)
    label.configure(image=bg_image)
    label.image = resized_bg
 

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=10)
file_menu.add_command(label="Quit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)


window.bind('<Configure>', resizer)

window.mainloop()
