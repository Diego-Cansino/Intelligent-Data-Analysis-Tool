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
        time.sleep(0.06)

    # gui.after(0,play_gif)
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


botonPrincipal = Button(text="Go to main", command= change)
botonPrincipal.pack(side=BOTTOM, pady=20)

# lambda: [abrirMenuPrincipal(), gui.destroy()]

a = play_gif()

gui.mainloop()