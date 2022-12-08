from ttkthemes import ThemedTk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from idlelib.tooltip import Hovertip
import graficos as gf

def abrirGraficos(df):
    global opcion, opcionesX, opcionesY, boton
    try:
        app = ThemedTk(theme="adapta")
        app.geometry('650x420')
        app.resizable(False, False)
        app.title("Graphing Data")

        graficos = ttk.Label(app, text="GRAPHING DATA", font=('Helvetica', 15, 'bold'))
        graficos.grid(pady=5, row=0, column=0, columnspan=4)

        # Etiqueta selección de graficas 
        label1 = ttk.Label(app, text="Choose the type of chart: ",
                           font=('Helvetica', 12, 'bold'))
        label1.grid(pady=5, row=1, column=0)

        opcion = tk.IntVar()
        # Elección Barras Verticales 
        imgbV = Image.open('./img/barrasVerticales.png')
        imgbV = imgbV.resize((100, 100))
        app.imgbV = ImageTk.PhotoImage(imgbV, master=app)
        buttonbV = tk.Radiobutton(app, image=app.imgbV, text="Vertical Bar Graph",
                                  activebackground="#5ECEF4", border=0, 
                                  variable=opcion, value=0, compound="top", 
                                  command=desactivarY)
        buttonbV.grid(padx=10, pady=5, row=2, column=0)
        Hovertip(buttonbV, hover_delay=500,
                 text="Vertical Bar Graph")

        # Elección Barras Horizontales
        imgbH = Image.open('./img/barrasHorizontales.png')
        imgbH = imgbH.resize((100, 100))
        app.imgbH = ImageTk.PhotoImage(imgbH, master=app)
        buttonbH = tk.Radiobutton(app, image=app.imgbH, text="Horizontal Bar Graph",
                                  activebackground="#5ECEF4", compound="top",
                                  border=0, variable=opcion, value=1, 
                                  command=desactivarY)
        buttonbH.grid(padx=10, pady=5, row=2, column=1)
        Hovertip(buttonbH, hover_delay=500,
                 text="Horizontal Bar Graph")

        # Elección Dispersión
        imgDisp = Image.open('./img/dispersion.png')
        imgDisp = imgDisp.resize((100, 100))
        app.imgDisp = ImageTk.PhotoImage(imgDisp, master=app)
        buttonDisp = tk.Radiobutton(app, image=app.imgDisp, text="Dispersion",
                                    activebackground="#5ECEF4", compound="top",
                                    border=0, variable=opcion, value=2, 
                                    command=desactivarY)
        buttonDisp.grid(padx=10, pady=5, row=2, column=2)
        Hovertip(buttonDisp, hover_delay=500,
                 text="Dispersion")

        # Elección Lineal
        imgLin = Image.open('./img/linear.png')
        imgLin = imgLin.resize((100, 100))
        app.imgLin = ImageTk.PhotoImage(imgLin, master=app)
        buttonLin = tk.Radiobutton(app, image=app.imgLin, text="Linear",
                                   activebackground="#5ECEF4", compound="top",
                                   border=0, variable=opcion, value=3,
                                   command=desactivarY)
        buttonLin.grid(padx=10, pady=5, row=2, column=3)
        Hovertip(buttonLin, hover_delay=500,
                 text="Linear")

        # Elección Area 
        imgArea = Image.open('./img/area.png')
        imgArea = imgArea.resize((100, 100))
        app.imgArea = ImageTk.PhotoImage(imgArea, master=app)
        buttonArea = tk.Radiobutton(app, image=app.imgArea, text="Area",
                                    activebackground="#5ECEF4", compound="top",
                                    border=0, variable=opcion, value=4,
                                    command=desactivarY)
        buttonArea.grid(padx=10, pady=5, row=3, column=0)
        Hovertip(buttonArea, hover_delay=500,
                 text="Area")

        # Elección Histograma 
        imgHist = Image.open('./img/histograma.png')
        imgHist = imgHist.resize((100, 100))
        app.imgHist = ImageTk.PhotoImage(imgHist, master=app)
        buttonHist = tk.Radiobutton(app, image=app.imgHist, text="Histogram",
                                    activebackground="#5ECEF4", compound="top",
                                    border=0, variable=opcion, value=5,
                                    command=desactivarY)
        buttonHist.grid(padx=10, pady=5, row=3, column=1)
        Hovertip(buttonHist, hover_delay=500,
                 text="Histogram")

        # Elección Pastel
        imgPie = Image.open('./img/pie.png')
        imgPie = imgPie.resize((100, 100))
        app.imgPie = ImageTk.PhotoImage(imgPie, master=app)
        buttonPie = tk.Radiobutton(app, image=app.imgPie, text="Pie Chart",
                                   activebackground="#5ECEF4", compound="top",
                                   border=0, variable=opcion, value=6,
                                   command=desactivarY)
        buttonPie.grid(padx=10, pady=5, row=3, column=2)
        Hovertip(buttonPie, hover_delay=500,
                 text="Pie Chart")

        # Etiquetas para los valores X y Y
        label2 = ttk.Label(app, text="Value of X: ",
                           font=('Helvetica', 12, 'bold'))
        label2.grid(pady=5, column=0, row=4)
        label3 = ttk.Label(app, text="Value of Y: ",
                           font=('Helvetica', 12, 'bold'))
        label3.grid(pady=5, column=2, row=4)

        # Lista con el nombre de las columnas para las opciones
        listaColumnas = df.columns.tolist()

        ## Declaramos las opciones
        opcionesX = ttk.Combobox(app, state="readonly", values=listaColumnas, postcommand=desactivarBoton)
        opcionesX.grid(pady=5, column=1, row=4)

        opcionesY = ttk.Combobox(app, state="readonly", values=listaColumnas, postcommand=desactivarBoton)
        opcionesY.grid(pady=5, column=3, row=4)

        # Boton para lanzar el grafico seleccionado
        boton = tk.Button(app, text="Graph the data", background="#5ECEF4",
                          command=lambda: opcionesGraficar(df))
        boton.grid(pady=5, row=5, column=0, columnspan=4, sticky="ew")

        opcionesX.bind("<<ComboboxSelected>>", desactivarBoton)
        opcionesY.bind("<<ComboboxSelected>>", desactivarBoton)
        
        desactivarY()
        desactivarBoton()

    except Exception as e:
        tk.messagebox.showerror(
            "Error", e
        )
        return None
    
def graficar(tipoGrafica, ValoresX, ValoresY, etiquetaX, etiquetaY):
    if(tipoGrafica == 0):
        gf.diagramaBarrasVerticales(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == 1):
        gf.diagramaBarrasHorizontales(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == 2):
        gf.diagramaDispersion(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == 3):
        gf.diagramaLineas(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == 4):
        gf.diagramaAreas(ValoresX, ValoresY, etiquetaX, etiquetaY)

def graficar2(tipoGrafica, ValoresX, etiquetaX):
    if (tipoGrafica == 5):
        gf.histograma(ValoresX, etiquetaX)
    elif (tipoGrafica == 6):
        gf.diagramaSectores(ValoresX, etiquetaX)

def desactivarY():
    if (opcion.get() >= 5):
        opcionesX.configure(state="readonly")
        opcionesY.set("")
        opcionesY.configure(state="disable")
    else:
        opcionesX.configure(state="readonly")
        opcionesY.configure(state="readonly")

def desactivarBoton(Event=None):
    if (opcion.get() >= 5 and opcionesX.get() == ""):
        boton.configure(state="disable")
    elif (opcion.get() < 5 and (opcionesX.get() == "" or opcionesY.get() == "")):
        boton.configure(state="disable")
    else:
        boton.configure(state="normal")

def opcionesGraficar(df):
    if (opcion.get() >= 5):
        graficar2(
            opcion.get(), 
            df[opcionesX.get()], opcionesX.get())
        opcionesX.set("")
    else:
        graficar(
            opcion.get(), 
            df[opcionesX.get()], df[opcionesY.get()], 
            opcionesX.get(), opcionesY.get())
        opcionesX.set("")
        opcionesY.set("")
    desactivarBoton()