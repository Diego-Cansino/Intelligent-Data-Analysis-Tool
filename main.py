import tkinter as tk
from tkvideo import tkvideo
from funcionesDeTkinter import abrirMenuPrincipal

# inicializamos la GUI
gui = tk.Tk()

# Configuramos la gui
gui.title("Intelligent Data Analysis Tool")
gui.geometry("650x650")
gui.resizable(False, False)
titulo = tk.Label(text='Intelligent Data Analysis Tool')
titulo.pack()
titulo.config(font=('Helvatical bold',20), pady=10)

# Ingresamos el titulo de la GUI
video_label = tk.Label(gui)
video_label.pack()
player = tkvideo(path="./Bd.mp4", label=video_label, loop = 2, size = (376, 500))
player.play()


#configuramos el boton
botonPrincipal = tk.Button(text="Go to main", command=lambda: [abrirMenuPrincipal(), gui.destroy()])
botonPrincipal.pack(side=tk.BOTTOM, pady=20)

gui.mainloop()