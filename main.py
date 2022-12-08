from tkinter import*
from PIL import Image, ImageTk, ImageSequence
import time
from ventanaPrincipal import abrirMenuPrincipal
from ttkthemes import ThemedTk

def play_gif():
    img = Image.open("./Bd01.gif")
    lbl = Label(gui)
    lbl.place(x=150, y=50)

    for img in ImageSequence.Iterator(img):
        img = img.resize((376,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image = img)
        gui.update()
        time.sleep(0.10)

    return img

def change():

    abrirMenuPrincipal()
    gui.destroy()   


gui = ThemedTk(theme="adapta")
# Configuramos la gui
gui.title("Intelligent Data Analysis Tool")
gui.geometry("650x650")
gui.resizable(False, False)
# Ingresamos el titulo de la GUI
titulo = Label(text='Intelligent Data Analysis Tool')
titulo.pack()
titulo.config(font=('Helvatical bold',20), pady=10)

img = Image.open('./img/home.png')
img = img.resize((20, 20))
gui.img = ImageTk.PhotoImage(img, master=gui)
botonPrincipal = Button(image=gui.img, text="Go to main", compound="top",
                        activebackground="#5ECEF4", command=change, state="disable")
botonPrincipal.pack(side=BOTTOM, pady=20)

a = play_gif()
botonPrincipal.configure(state="normal")
gui.mainloop()