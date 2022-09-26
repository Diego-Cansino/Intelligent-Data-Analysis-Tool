from tkinter import LEFT, RIGHT, filedialog, ttk
from idlelib.tooltip import Hovertip
from pathlib import Path
import tkinter as tk
import pandas as pd
import graficos as gf
import redNeuronal as pr
import arbolDeDecision as ar
import kVecinos as knn
import regresionLogistica as rl
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from tkinter import messagebox as MessageBox

def abrirMenuPrincipal():
    # inicializamos la GUI
    # gui = ThemedTk(theme="adapta")
    gui = ThemedTk(theme="adapta")
    # Configuramos la gui
    gui.geometry("750x750")
    gui.title("Intelligent Data Analysis Tool")

    # Frame para el TreeView
    ventana = tk.LabelFrame(gui, text="txt, xlsx and csv files")
    ventana.pack(fill="both", expand=True)

    # Frame para el dialogo del archivo abierto
    archivo = tk.LabelFrame(gui)
    archivo.pack(side="bottom", fill="both", expand=False)

    # Ruta del archivo
    global nombreArchivo
    nombreArchivo = ttk.Label(archivo, text="No selected file")
    nombreArchivo.pack()

    # Panel para las pestañas
    notebook = ttk.Notebook(archivo)
    notebook.pack(fill='both', expand='yes')
    # Creacion de las pestañas
    p1 = ttk.Frame(notebook)
    p2 = ttk.Frame(notebook)
    p3 = ttk.Frame(notebook)
    
    # Elementos Pestaña 1
    ## COMPRENSION DE LOS DATOS
    e_comprension = ttk.Label(p1, text="DATA UNDERSTANDING", font=('Helvetica', 15, 'bold'))
    e_comprension.grid(pady=5, row=0, column=0, columnspan=2)

    img1_1 = Image.open('./img/searchFile.png')
    img1_1 = img1_1.resize((100,100))
    p1.img1_1 = ImageTk.PhotoImage(img1_1, master=p1)
    button1_1 = tk.Button(p1, text="Search file", image=p1.img1_1, 
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: buscarArchivo())
    button1_1.grid(padx=10, pady=5, row=1, column=0)
    Hovertip(button1_1, hover_delay=500,
             text="Search txt, xlsx or csv files")

    img1_2 = Image.open('./img/plotting.png')
    img1_2 = img1_2.resize((100, 100))
    p1.img1_2 = ImageTk.PhotoImage(img1_2, master=p1)
    button1_2 = tk.Button(p1, text="Graphing data", image=p1.img1_2,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: abrirGraficos())
    button1_2.grid(padx=10, pady=5, row=1, column=1)
    Hovertip(button1_2, hover_delay=500,
             text="Open a window with options for plotting")

    # Elementos Pestaña 2
    canvas = tk.Canvas(p2, border=0)
    canvas.pack(side=LEFT, fill="both", expand="yes")

    yscroll = tk.Scrollbar(p2, orient="vertical", command=canvas.yview, border=0)
    yscroll.pack(side=RIGHT, fill="y")

    canvas.configure(yscrollcommand=yscroll.set)

    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))


    p2_2 = tk.Frame(canvas, border=0)
    p2_2.bind('<MouseWheel>', lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    canvas.create_window((0, 0), window=p2_2, anchor="nw", width=(canvas.winfo_width()-yscroll.winfo_width()))
    ## PREPARACIÓN DE LOS DATOS
    e_preparacion = ttk.Label(p2_2, text="DATA PREPARATION", font=('Helvetica', 15, 'bold'))
    e_preparacion.grid(pady=5, row=0, column=0, columnspan=4)
    ### SELECCION DE DATOS
    e_seleccion = ttk.Label(p2_2, text="DATA SELECTION", font=('Helvetica', 12, 'bold'))
    e_seleccion.grid(pady=5, row=1, column=0)

    img2_1 = Image.open('./img/seleccionDatos.png')
    img2_1 = img2_1.resize((60, 60))
    p2_2.img2_1 = ImageTk.PhotoImage(img2_1, master=p2_2)
    button2_1 = tk.Button(p2_2, text="Data Selection", image=p2_2.img2_1,
                          activebackground="#5ECEF4", compound="top",
                          border=0) #, command=lambda: )
    button2_1.grid(padx=10, pady=5, row=2, column=0)
    Hovertip(button2_1, hover_delay=500,
             text="Data Selection")
    ### LIMPIEZA DE DATOS
    e_limpieza = ttk.Label(p2_2, text="CLEANING DATA", font=('Helvetica', 12, 'bold'))
    e_limpieza.grid(pady=5, row=3, column=0)

    img2_2 = Image.open('./img/FFILL.png')
    img2_2 = img2_2.resize((60,60))
    p2_2.img2_2 = ImageTk.PhotoImage(img2_2, master=p2_2)
    button2_2 = tk.Button(p2_2, text="FFILL", image=p2_2.img2_2,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: limpiarDatosForwardFill())
    button2_2.grid(padx=10, pady=5, row=4, column=0)
    Hovertip(button2_2, hover_delay=500,
             text="Cleaning data using functionality FFILL: Any missing value is filled based on the corresponding value in the previous row.")

    img2_3 = Image.open('./img/BFILL.png')
    img2_3 = img2_3.resize((60,60))
    p2_2.img2_3 = ImageTk.PhotoImage(img2_3, master=p2_2)
    button2_3 = tk.Button(p2_2, text="BFILL", image=p2_2.img2_3,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: limpiarDatosBackwardFill())
    button2_3.grid(padx=10, pady=5, row=4, column=1)
    Hovertip(button2_3, hover_delay=500,
             text="Cleaning data using functionality BFILL: Is used to backward fill the missing values in the dataset.")

    img2_4 = Image.open('./img/NONE.png')
    img2_4 = img2_4.resize((60, 60))
    p2_2.img2_4 = ImageTk.PhotoImage(img2_4, master=p2_2)
    button2_4 = tk.Button(p2_2, text="None", image=p2_2.img2_4,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: limpiarDatosColumnaVacia())
    button2_4.grid(padx=10, pady=5, row=4, column=2)
    Hovertip(button2_4, hover_delay=500,
             text="Cleaning data using functionality None: Filters the values of a dataset to leave only those that are non-null.")

    img2_5 = Image.open('./img/all.png')
    img2_5 = img2_5.resize((60, 60))
    p2_2.img2_5 = ImageTk.PhotoImage(img2_5, master=p2_2)
    button2_5 = tk.Button(p2_2, text="ALL", image=p2_2.img2_5,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: limpiarDatosAllMethods())
    button2_5.grid(padx=10, pady=5, row=4, column=3)
    Hovertip(button2_5, hover_delay=500,
             text="Cleaning data using functionality ALL: Makes a combination of FFILL, BFILL and None functionalities")

    img2_6 = Image.open('./img/normalizacion.png')
    img2_6 = img2_6.resize((60, 60))
    p2_2.img2_6 = ImageTk.PhotoImage(img2_6, master=p2_2)
    button2_6 = tk.Button(p2_2, text="standardize data", image=p2_2.img2_6,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: normalizarDatos())
    button2_6.grid(padx=10, pady=5, row=4, column=4)
    Hovertip(button2_6, hover_delay=500,
             text="standardize atypical data")

    img2_7 = Image.open('./img/promedio.png')
    img2_7 = img2_7.resize((60, 60))
    p2_2.img2_7 = ImageTk.PhotoImage(img2_7, master=p2_2)
    button2_7 = tk.Button(p2_2, text="MEAN", image=p2_2.img2_7,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: rellenarDatosMedia())
    button2_7.grid(padx=10, pady=5, row=5, column=0)
    Hovertip(button2_7, hover_delay=500,
             text="Cleaning data using statistical method Mean")

    img2_8 = Image.open('./img/media.png')
    img2_8 = img2_8.resize((60, 60))
    p2_2.img2_8 = ImageTk.PhotoImage(img2_8, master=p2_2)
    button2_8 = tk.Button(p2_2, text="MEDIAN", image=p2_2.img2_8,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: rellenarDatosMediana())
    button2_8.grid(padx=10, pady=5, row=5, column=1)
    Hovertip(button2_8, hover_delay=500,
             text="Cleaning data using statistical method Median")

    img2_9 = Image.open('./img/moda.png')
    img2_9 = img2_9.resize((60, 60))
    p2_2.img2_9 = ImageTk.PhotoImage(img2_9, master=p2_2)
    button2_9 = tk.Button(p2_2, text="MODE", image=p2_2.img2_9,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: rellenarDatosModa())
    button2_9.grid(padx=10, pady=5, row=5, column=2)
    Hovertip(button2_9, hover_delay=500,
             text="Cleaning data using statistical method Mode")

    img2_10 = Image.open('./img/rango.png')
    img2_10 = img2_10.resize((60, 60))
    p2_2.img2_10 = ImageTk.PhotoImage(img2_10, master=p2_2)
    button2_10 = tk.Button(p2_2, text="RANGE", image=p2_2.img2_10,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: rellenarDatosRango())
    button2_10.grid(padx=10, pady=5, row=5, column=3)
    Hovertip(button2_10, hover_delay=500,
             text="Cleaning data using statistical method Range")

    img2_11 = Image.open('./img/eliminar.png')
    img2_11 = img2_11.resize((60, 60))
    p2_2.img2_11 = ImageTk.PhotoImage(img2_11, master=p2_2)
    button2_11 = tk.Button(p2_2, text="remove atypical data", image=p2_2.img2_11,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: eliminarDatosAtipicos())
    button2_11.grid(padx=10, pady=5, row=5, column=4)
    Hovertip(button2_11, hover_delay=500,
             text="remove atypical data")

    ### CONSTRUCCION DE NUEVOS DATOS 
    e_nuevosDatos = ttk.Label(p2_2, text="CONSTRUCTION OF\n NEW DATA", font=('Helvetica', 12, 'bold'))
    e_nuevosDatos.grid(pady=5, row=6, column=0)

    img2_12 = Image.open('./img/nuevosDatos.png')
    img2_12 = img2_12.resize((60, 60))
    p2_2.img2_12 = ImageTk.PhotoImage(img2_12, master=p2_2)
    button2_12 = tk.Button(p2_2, text="New data", image=p2_2.img2_12,
                           activebackground="#5ECEF4", compound="top",
                        border=0) #, command=lambda: rellenarDatosRango())
    button2_12.grid(padx=10, pady=5, row=7, column=0)
    Hovertip(button2_12, hover_delay=500,
            text="Construction of new data")

    ### INTEGRACION DE DATOS
    e_integracion = ttk.Label(p2_2, text="DATA INTEGRATION", font=('Helvetica', 12, 'bold'))
    e_integracion.grid(pady=5, row=8, column=0)

    img2_13 = Image.open('./img/integracion.png')
    img2_13 = img2_13.resize((60, 60))
    p2_2.img2_13 = ImageTk.PhotoImage(img2_13, master=p2_2)
    button2_13 = tk.Button(p2_2, text="Data integration", image=p2_2.img2_13,
                           activebackground="#5ECEF4", compound="top",
                        border=0) #, command=lambda: rellenarDatosRango())
    button2_13.grid(padx=10, pady=5, row=9, column=0)
    Hovertip(button2_13, hover_delay=500,
            text="Data integration")

    ### FORMATO DE DATOS
    e_formato = ttk.Label(p2_2, text="DATA FORMAT", font=('Helvetica', 12, 'bold'))
    e_formato.grid(pady=5, row=10, column=0)

    img2_14 = Image.open('./img/formato.png')
    img2_14 = img2_14.resize((60, 60))
    p2_2.img2_14 = ImageTk.PhotoImage(img2_14, master=p2_2)
    button2_14 = tk.Button(p2_2, text="Data format", image=p2_2.img2_14,
                           activebackground="#5ECEF4", compound="top",
                           border=0) #, command=lambda: rellenarDatosRango())
    button2_14.grid(padx=10, pady=5, row=11, column=0)
    Hovertip(button2_14, hover_delay=500,
            text="Data format")

    # Elementos Pestaña 3
    ## TECNICAS DE MODELADO
    e_modelado = ttk.Label(p3, text="MODELING", font=('Helvetica', 15, 'bold'))
    e_modelado.grid(pady=5, row=0, column=0, columnspan=4)

    img3_1 = Image.open('./img/redNeuronal.png')
    img3_1 = img3_1.resize((90,90))
    p3.img3_1 = ImageTk.PhotoImage(img3_1, master=p3)
    button3_1 = tk.Button(p3, text="Artificial Neural Network", image=p3.img3_1,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=abrirModelos)
    button3_1.grid(padx=10, pady=5, row=1, column=0)
    Hovertip(button3_1, hover_delay=500,
             text="Model: Sequential Artificial Neural Network model by Keras.")

    img3_2 = Image.open('./img/regresion.png')
    img3_2 = img3_2.resize((90, 90))
    p3.img3_2 = ImageTk.PhotoImage(img3_2, master=p3)
    button3_2 = tk.Button(p3, text="Logistic Regression", image=p3.img3_2,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=abrirModelosRL)
    button3_2.grid(padx=10, pady=5, row=1, column=1)
    Hovertip(button3_2, hover_delay=500,
             text="Model: Logistic regression classifier")

    img3_3 = Image.open('./img/arbol.png')
    img3_3 = img3_3.resize((90, 90))
    p3.img3_3 = ImageTk.PhotoImage(img3_3, master=p3)
    button3_3 = tk.Button(p3, text="Decision tree", image=p3.img3_3,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=abrirModelosArbol)
    button3_3.grid(padx=10, pady=5, row=1, column=2)
    Hovertip(button3_3, hover_delay=500,
             text="Model: Decision tree classifier.")

    img3_4 = Image.open('./img/vecinos.png')
    img3_4 = img3_4.resize((90, 90))
    p3.img3_4 = ImageTk.PhotoImage(img3_4, master=p3)
    button3_4 = tk.Button(p3, text="KNN", image=p3.img3_4,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=abrirModelosKNN)
    button3_4.grid(padx=10, pady=5, row=1, column=3)
    Hovertip(button3_4, hover_delay=500,
             text="Model: Classifier implementing the k-nearest neighbors vote.")
    
    # Agregamos las pestañas creadas
    notebook.add(p1, text='Understanding')
    notebook.add(p2, text='Preparation')
    notebook.add(p3, text='Modeling')

    # Barra de Menús
    barraMenu = tk.Menu(gui)
    ## HELP
    menuHelp = tk.Menu(barraMenu, tearoff=False)
    menuHelp.add_command(label="Help", command=lambda: abrirHelp())
    barraMenu.add_cascade(label="Help", menu=menuHelp)
    ## SAVE and SAVE AS
    menuSave = tk.Menu(barraMenu, tearoff=False)
    menuSave.add_command(
        label="Save", command=lambda: guardarDataframeExcel())
    menuSave.add_command(
        label="Save As", command=lambda: guardarComoDataframeExcel()
    )
    barraMenu.add_cascade(label="Save", menu=menuSave)
    gui.config(menu=barraMenu)

    # Treeview Widget
    global tv1
    tv1 = ttk.Treeview(ventana)
    # establecemos el ancho y el alto del Widget al 100% de su contenedor (ventana).
    tv1.place(relheight=1, relwidth=1)

    # comando para actualizar el eje y de la ventana
    treescrolly = tk.Scrollbar(ventana, orient="vertical", command=tv1.yview)
    # comando para actualizar el eje x de la ventana
    treescrollx = tk.Scrollbar(ventana, orient="horizontal", command=tv1.xview)
    # asignamos el Scrollbar al Treeview Widget
    tv1.configure(xscrollcommand=treescrollx.set,
                  yscrollcommand=treescrolly.set)
    # posicionamos el Scrollbar del eje x
    treescrollx.pack(side="bottom", fill="x")
    # posicionamos el Scrollbar del eje y
    treescrolly.pack(side="right", fill="y")

def extraerDatos():
    """ Esta funcion extrae los datos del archivo seleccionado """
    rutaArchivo = nombreArchivo["text"]
    global df
    try:
        archivoExcel = r"{}".format(rutaArchivo)
        if archivoExcel[-4:] == ".csv":
            df = pd.read_csv(archivoExcel)
        elif archivoExcel[-4:] == ".txt":
            df = pd.read_table(archivoExcel, delimiter="\t")
        else:
            df = pd.read_excel(archivoExcel)

    except ValueError:
        tk.messagebox.showerror("Information", "The file is Invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror(
            "Information", f"File was not found in the path {rutaArchivo}")
        df = []
        return None


def buscarArchivo():
    """Esta funcion abre el explorador de archivos para que se busque un archivo"""
    archivo = filedialog.askopenfilename(initialdir="/",
                                         title="Select a File",
                                         filetype=(("All Files", "*.*"), ("xlsx files", ".xlsx"), ("csv files", ".csv"), ("txt files", ".txt")))
    nombreArchivo["text"] = archivo

    # Funcion para eliminar todo del TreeView
    limpiarDatos()
    # Funcion Extraer Datos del Archivo
    extraerDatos()

    insertarDatosTreeView()

    return None


def insertarDatosTreeView():
    # Llenamos el widget con nuestros datos
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        # titulo de la columna = nombre de la columna
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()  # Convertimos el dataframe en una lista de listas
    for row in df_rows:
        # insertamos cada una de las listas dentro del treeview.
        tv1.insert("", "end", values=row)
    return None


def cargarDatosExcel():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    # Funcion Extraer Datos del Archivo
    extraerDatos()
    # Funcion para eliminar todo del TreeView
    limpiarDatos()

    insertarDatosTreeView()
    return None


def limpiarDatos():
    tv1.delete(*tv1.get_children())
    return None


def limpiarDatosForwardFill():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    limpiarDatos()
    global df  # QUIZA ESTO ESTA MAL
    df = df.fillna(method="ffill")
    insertarDatosTreeView()
    verificarDatosNulos()


def limpiarDatosBackwardFill():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    limpiarDatos()
    global df
    df = df.fillna(method="backfill")
    insertarDatosTreeView()
    verificarDatosNulos()


def limpiarDatosColumnaVacia():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    limpiarDatos()  # por si no tiene nada la columna
    global df
    df = df.dropna(axis=1)
    insertarDatosTreeView()
    verificarDatosNulos()
    
def rellenarDatosMedia():
    global df
    limpiarDatos()
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    meanValues = df.mean()
    df = df.fillna(meanValues)
    insertarDatosTreeView()
    verificarDatosNulos()

def rellenarDatosMediana():
    global df
    limpiarDatos()
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    medianValues = df.median()
    df = df.fillna(medianValues)
    insertarDatosTreeView()
    verificarDatosNulos()

def rellenarDatosModa():
    global df
    limpiarDatos()
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    values = df.mode()
    modeValues = values.head(1).squeeze()
    df = df.fillna(modeValues)
    insertarDatosTreeView()
    verificarDatosNulos()

def rellenarDatosRango():
    global df
    limpiarDatos()
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    maxValues = df.max()
    minValues = df.min()
    values = maxValues - minValues
    df = df.fillna(values)
    insertarDatosTreeView()
    verificarDatosNulos()

def limpiarDatosAllMethods():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    limpiarDatos()
    global df
    df = df.fillna(method="ffill")
    df = df.fillna(method="backfill")
    df = df.dropna(axis=1)
    insertarDatosTreeView()
    verificarDatosNulos()

def normalizarDatos():
    """Normaliza los datos de manera global en el DataFrame"""
    limpiarDatos()
    global df
    normalizeData = ( df - df.min() ) / ( df.max() - df.min() )
    df = normalizeData
    insertarDatosTreeView()
    verificarDatosNulos()

def eliminarDatosAtipicos():
    """Elimina datos atipicos(outliers) de manera global"""
    limpiarDatos()
    global df
    for col in df.columns:
        mean = df[col].mean()
        sd = df[col].std()
        df = df[(df[col] <= mean+(3*sd))]
    insertarDatosTreeView()
    verificarDatosNulos()

def verificarDatosNulos():
    global df
    registrosVacios = df.isna().sum().sum()
    if registrosVacios > 0:
        MessageBox.showerror("Error", "Data set still has empty values.")
    else:
        MessageBox.showinfo("Success!", "The task has been performed correctly.")

def guardarDataframeExcel():
    global df
    desktopPath = str(Path.home() / "Desktop")
    desktop = desktopPath + '/exportDataTool.xlsx'
    df.to_excel(desktop, index = False, header=True)

def guardarComoDataframeExcel():
    global df
    file = filedialog.asksaveasfilename(filetypes=[(
        "xlsx files", ".xlsx")], defaultextension="*.xlsx")
    df.to_excel(file, index=False, header=True)

def abrirGraficos():
    try:
        app = ThemedTk(theme="adapta")
        app.geometry('650x420')
        app.resizable(False, False)
        app.title("Graphing Data")

        graficos = ttk.Label(app, text="GRAPHING DATA", font=('Helvetica', 15, 'bold'))
        graficos.grid(pady=5, row=0, column=0, columnspan=4)

        # Declaramos los label
        label1 = ttk.Label(app, text="Choose the type of chart: ",
                           font=('Helvetica', 12, 'bold'))
        label1.grid(pady=5, row=1, column=0)

        opcion = tk.IntVar()

        imgbV = Image.open('./img/barrasVerticales.png')
        imgbV = imgbV.resize((100, 100))
        app.imgbV = ImageTk.PhotoImage(imgbV, master=app)
        buttonbV = tk.Radiobutton(app, image=app.imgbV, text="Vertical Bar Graph",
                                  activebackground="#5ECEF4", border=0, 
                                  variable=opcion, value=0, compound="top",)
        buttonbV.grid(padx=10, pady=5, row=2, column=0)
        Hovertip(buttonbV, hover_delay=500,
                 text="Vertical Bar Graph")

        imgbH = Image.open('./img/barrasHorizontales.png')
        imgbH = imgbH.resize((100, 100))
        app.imgbH = ImageTk.PhotoImage(imgbH, master=app)
        buttonbH = tk.Radiobutton(app, image=app.imgbH, text="Horizontal Bar Graph",
                                  activebackground="#5ECEF4", compound="top",
                                  border=0, variable=opcion, value=1)
        buttonbH.grid(padx=10, pady=5, row=2, column=1)
        Hovertip(buttonbH, hover_delay=500,
                 text="Horizontal Bar Graph")

        imgDisp = Image.open('./img/dispersion.png')
        imgDisp = imgDisp.resize((100, 100))
        app.imgDisp = ImageTk.PhotoImage(imgDisp, master=app)
        buttonDisp = tk.Radiobutton(app, image=app.imgDisp, text="Dispersion",
                                    activebackground="#5ECEF4", compound="top",
                                    border=0, variable=opcion, value=2)
        buttonDisp.grid(padx=10, pady=5, row=2, column=2)
        Hovertip(buttonDisp, hover_delay=500,
                 text="Dispersion")

        imgLin = Image.open('./img/linear.png')
        imgLin = imgLin.resize((100, 100))
        app.imgLin = ImageTk.PhotoImage(imgLin, master=app)
        buttonLin = tk.Radiobutton(app, image=app.imgLin, text="Linear",
                                   activebackground="#5ECEF4", compound="top",
                                   border=0, variable=opcion, value=3)
        buttonLin.grid(padx=10, pady=5, row=2, column=3)
        Hovertip(buttonLin, hover_delay=500,
                 text="Linear")

        imgArea = Image.open('./img/area.png')
        imgArea = imgArea.resize((100, 100))
        app.imgArea = ImageTk.PhotoImage(imgArea, master=app)
        buttonArea = tk.Radiobutton(app, image=app.imgArea, text="Area",
                                    activebackground="#5ECEF4", compound="top",
                                    border=0, variable=opcion, value=4)
        buttonArea.grid(padx=10, pady=5, row=3, column=0)
        Hovertip(buttonArea, hover_delay=500,
                 text="Area")

        imgHist = Image.open('./img/histograma.png')
        imgHist = imgHist.resize((100, 100))
        app.imgHist = ImageTk.PhotoImage(imgHist, master=app)
        buttonHist = tk.Radiobutton(app, image=app.imgHist, text="Histogram",
                                    activebackground="#5ECEF4", compound="top",
                                    border=0, variable=opcion, value=5)
        buttonHist.grid(padx=10, pady=5, row=3, column=1)
        Hovertip(buttonHist, hover_delay=500,
                 text="Histogram")

        imgPie = Image.open('./img/pie.png')
        imgPie = imgPie.resize((100, 100))
        app.imgPie = ImageTk.PhotoImage(imgPie, master=app)
        buttonPie = tk.Radiobutton(app, image=app.imgPie, text="Pie Chart",
                                   activebackground="#5ECEF4", compound="top",
                                   border=0, variable=opcion, value=6)
        buttonPie.grid(padx=10, pady=5, row=3, column=2)
        Hovertip(buttonPie, hover_delay=500,
                 text="Pie Chart")

        listaColumnas = df.columns.tolist()

        label2 = ttk.Label(app, text="Value of X: ",
                           font=('Helvetica', 12, 'bold'))
        label2.grid(pady=5, column=0, row=4)

        label3 = ttk.Label(app, text="Value of Y: ",
                           font=('Helvetica', 12, 'bold'))
        label3.grid(pady=5, column=2, row=4)

        # # Declaramos las opciones
        lista2 = ttk.Combobox(app, state="readonly", values=listaColumnas)
        lista2.grid(pady=5, column=1, row=4)
        lista2.current(0)

        lista3 = ttk.Combobox(app, state="readonly", values=listaColumnas)
        lista3.grid(pady=5, column=3, row=4)
        lista3.current(0)

        boton = tk.Button(app, text="Graph the data", background="#5ECEF4",
                          command=lambda: graficar(
                            int(opcion.get()), df[lista2.get()], df[lista3.get()], lista2.get(), lista3.get()))
        boton.grid(pady=5, row=5, column=0, columnspan=4, sticky="ew")

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
    elif(tipoGrafica == 5):
        gf.histograma(ValoresX, etiquetaX)
    elif(tipoGrafica == 6):
        gf.diagramaSectores(ValoresX)

def abrirModelos():
    app = ThemedTk(theme="adapta")
    app.geometry('600x370')
    app.resizable(False, False)

    label = tk.Label(app, text="Select INPUTS and TARGET", font=('Helvetica', 12, 'bold'))
    label.pack(side=tk.TOP)
 
    # Create a listbox
    listbox = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)
    listbox2 = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)

    #Creation SCROLLBARS
    scrollbar = tk.Scrollbar(app)
    scrollbar.pack(side=LEFT, fill=tk.Y, pady=(5, 70))
    scrollbar2 = tk.Scrollbar(app)
    scrollbar2.pack(side=RIGHT, fill=tk.Y, pady=(5, 70))
 
    # Extraemos los datos
    listaCampos = df.columns.tolist()

    for i in range (len(listaCampos)):
        listbox.insert(i, listaCampos[i])
        listbox2.insert(i, listaCampos[i])

    def selected_item():
        global campos
        campos = []
        selected_campos = listbox.curselection()
        campos = list(selected_campos)


    def selected_item2():
        global objetivos
        objetivos = []
        selected_objetivos = listbox2.curselection()
        objetivos = list(selected_objetivos)
    
    def select_all():
        listbox.select_set(0, tk.END)
    
    def select_all2():
        listbox2.select_set(0, tk.END)
    
    # Boton para enviar datos
    btn1 = tk.Button(app, text='Select all', command=select_all)
    btn2 = tk.Button(app, text='Select all', command=select_all2)
    btn3 = tk.Button(app, text='Send selection', command=lambda: [selected_item(), selected_item2(), pr.solicitarDatosPrueba(), app.destroy()])

    # SCROLLBAR
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox2.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=listbox2.yview)
    
    # Placing the button and listbox
    listbox.pack(side=LEFT, fill=tk.BOTH, expand=True, pady=(5, 70))
    listbox2.pack(side=RIGHT, fill=tk.BOTH, expand=True, pady=(5, 70))
    btn1.place(x=100, y=310)
    btn2.place(x=440, y=310)
    btn3.pack(side="bottom", pady=5)

    # Barra de Menús
    barraMenu = tk.Menu(app)
    ## HELP
    menuHelp = tk.Menu(barraMenu, tearoff=False)
    menuHelp.add_command(label="Help", command=lambda: abrirHelpModelos())
    barraMenu.add_cascade(label="Help", menu=menuHelp)
    app.config(menu=barraMenu)

def abrirModelosArbol():
    app = ThemedTk(theme="adapta")
    app.geometry('600x370')
    app.resizable(False, False)

    label = tk.Label(app, text="Select INPUTS and TARGET", font=('Helvetica', 12, 'bold'))
    label.pack(side=tk.TOP)
 
    # Create a listbox
    listbox = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)
    listbox2 = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)

    #Creation SCROLLBARS
    scrollbar = tk.Scrollbar(app)
    scrollbar.pack(side=LEFT, fill=tk.Y, pady=(5, 70))
    scrollbar2 = tk.Scrollbar(app)
    scrollbar2.pack(side=RIGHT, fill=tk.Y, pady=(5, 70))
 
    # Extraemos los datos
    listaCampos = df.columns.tolist()

    for i in range (len(listaCampos)):
        listbox.insert(i, listaCampos[i])
        listbox2.insert(i, listaCampos[i])

    def selected_item():
        global campos
        campos = []
        selected_campos = listbox.curselection()
        campos = list(selected_campos)


    def selected_item2():
        global objetivos
        objetivos = []
        selected_objetivos = listbox2.curselection()
        objetivos = list(selected_objetivos)
    
    def select_all():
        listbox.select_set(0, tk.END)
    
    def select_all2():
        listbox2.select_set(0, tk.END)
    
    # Boton para enviar datos
    btn1 = tk.Button(app, text='Select all', command=select_all)
    btn2 = tk.Button(app, text='Select all', command=select_all2)
    btn3 = tk.Button(app, text='Send selection', command=lambda: [selected_item(), selected_item2(), ar.solicitarDatosPrueba(), app.destroy()])

    # SCROLLBAR
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox2.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=listbox2.yview)
    
    # Placing the button and listbox
    listbox.pack(side=LEFT, fill=tk.BOTH, expand=True, pady=(5, 70))
    listbox2.pack(side=RIGHT, fill=tk.BOTH, expand=True, pady=(5, 70))
    btn1.place(x=100, y=310)
    btn2.place(x=440, y=310)
    btn3.pack(side="bottom", pady=5)

    # Barra de Menús
    barraMenu = tk.Menu(app)
    ## HELP
    menuHelp = tk.Menu(barraMenu, tearoff=False)
    menuHelp.add_command(label="Help", command=lambda: abrirHelpModelos())
    barraMenu.add_cascade(label="Help", menu=menuHelp)
    app.config(menu=barraMenu)

def abrirModelosRL():
    app = ThemedTk(theme="adapta")
    app.geometry('600x370')
    app.resizable(False, False)

    label = tk.Label(app, text="Select INPUTS and TARGET", font=('Helvetica', 12, 'bold'))
    label.pack(side=tk.TOP)
 
    # Create a listbox
    listbox = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)
    listbox2 = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)

    #Creation SCROLLBARS
    scrollbar = tk.Scrollbar(app)
    scrollbar.pack(side=LEFT, fill=tk.Y, pady=(5, 70))
    scrollbar2 = tk.Scrollbar(app)
    scrollbar2.pack(side=RIGHT, fill=tk.Y, pady=(5, 70))
 
    # Extraemos los datos
    listaCampos = df.columns.tolist()

    for i in range (len(listaCampos)):
        listbox.insert(i, listaCampos[i])
        listbox2.insert(i, listaCampos[i])

    def selected_item():
        global campos
        campos = []
        selected_campos = listbox.curselection()
        campos = list(selected_campos)


    def selected_item2():
        global objetivos
        objetivos = []
        selected_objetivos = listbox2.curselection()
        objetivos = list(selected_objetivos)
    
    def select_all():
        listbox.select_set(0, tk.END)
    
    def select_all2():
        listbox2.select_set(0, tk.END)
    
    # Boton para enviar datos
    btn1 = tk.Button(app, text='Select all', command=select_all)
    btn2 = tk.Button(app, text='Select all', command=select_all2)
    btn3 = tk.Button(app, text='Send selection', command=lambda: [selected_item(), selected_item2(), rl.solicitarDatosPrueba(), app.destroy()])

    # SCROLLBAR
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox2.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=listbox2.yview)
    
    # Placing the button and listbox
    listbox.pack(side=LEFT, fill=tk.BOTH, expand=True, pady=(5, 70))
    listbox2.pack(side=RIGHT, fill=tk.BOTH, expand=True, pady=(5, 70))
    btn1.place(x=100, y=310)
    btn2.place(x=440, y=310)
    btn3.pack(side="bottom", pady=5)

    # Barra de Menús
    barraMenu = tk.Menu(app)
    ## HELP
    menuHelp = tk.Menu(barraMenu, tearoff=False)
    menuHelp.add_command(label="Help", command=lambda: abrirHelpModelos())
    barraMenu.add_cascade(label="Help", menu=menuHelp)
    app.config(menu=barraMenu)

def abrirModelosKNN():
    app = ThemedTk(theme="adapta")
    app.geometry('600x370')
    app.resizable(False, False)

    label = tk.Label(app, text="Select INPUTS and TARGET", font=('Helvetica', 12, 'bold'))
    label.pack(side=tk.TOP)
 
    # Create a listbox
    listbox = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)
    listbox2 = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)

    #Creation SCROLLBARS
    scrollbar = tk.Scrollbar(app)
    scrollbar.pack(side=LEFT, fill=tk.Y, pady=(5, 70))
    scrollbar2 = tk.Scrollbar(app)
    scrollbar2.pack(side=RIGHT, fill=tk.Y, pady=(5, 70))
 
    # Extraemos los datos
    listaCampos = df.columns.tolist()

    for i in range (len(listaCampos)):
        listbox.insert(i, listaCampos[i])
        listbox2.insert(i, listaCampos[i])

    def selected_item():
        global campos
        campos = []
        selected_campos = listbox.curselection()
        campos = list(selected_campos)


    def selected_item2():
        global objetivos
        objetivos = []
        selected_objetivos = listbox2.curselection()
        objetivos = list(selected_objetivos)
    
    def select_all():
        listbox.select_set(0, tk.END)
    
    def select_all2():
        listbox2.select_set(0, tk.END)
    
    # Boton para enviar datos
    btn1 = tk.Button(app, text='Select all', command=select_all)
    btn2 = tk.Button(app, text='Select all', command=select_all2)
    btn3 = tk.Button(app, text='Send selection', command=lambda: [selected_item(), selected_item2(), knn.solicitarDatosPrueba(), app.destroy()])

    # SCROLLBAR
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox2.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=listbox2.yview)
    
    # Placing the button and listbox
    listbox.pack(side=LEFT, fill=tk.BOTH, expand=True, pady=(5, 70))
    listbox2.pack(side=RIGHT, fill=tk.BOTH, expand=True, pady=(5, 70))
    btn1.place(x=100, y=310)
    btn2.place(x=440, y=310)
    btn3.pack(side="bottom", pady=5)

    # Barra de Menús
    barraMenu = tk.Menu(app)
    ## HELP
    menuHelp = tk.Menu(barraMenu, tearoff=False)
    menuHelp.add_command(label="Help", command=lambda: abrirHelpModelos())
    barraMenu.add_cascade(label="Help", menu=menuHelp)
    app.config(menu=barraMenu)

def abrirHelp():
    app = ThemedTk(theme="adapta")
    app.geometry('650x650')
    app.resizable(False, False)

    scroll = tk.Scrollbar(app)
    text = tk.Text(app)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.tag_configure('formato', font=('Arial', 12))

    help_t = """
This tool is designed to visualize the data of a dataset, analyze them by means of different graphs, clean the data and implement models in the data.\n\n
Parts of the interface:\n\n
UNDERSTANDING DATA: in this tab you can load a dataset and upload it so that the tool shows the data. You can also make graphs of the data.\n\n
BUTTONS:\n\n 
\"Search File\": pressing this button will open a new window in which you can search for a dataset.\n\n
\"Load File\": pressing this button will load the data set previously selected with the button \"Search File\" and the data will be displayed at the top of the interface.\n\n
\"Graphing Data\": pressing this button will open a new window where you can select different types of graphics according to the fields of the dataset.\n\n
DATA CLEANING: in this tab you can make the selection of some data cleaning techniques, among which are \"FFILL\", \"BFILL\", \"none\", \"ALL\".\n\n
BUTTONS:\n\n 
\"FFILL\": Populate the null values with the value from the next record.\n\n
\"BFILL\": Populate the null values with the value from the previous record.\n\n
\"none\": If null values are found, the entire record is deleted.\n\n
\"ALL\": Combination of all functions.\n\n
MODELING: in this tab, you can implement various models that analyse the data, for example \"Neural network\", \"Decision tree\", \"KNN algorithm\", \"Linear regression\"\n\n
BUTTONS:\n\n
\"Neuronal network\": Implements a neuronal network model (currently only for binary outputs).\n\n
\"Decision Tree\": Implements a Decision Tree model (currently not working).\n\n
\"KNN algorithm\": Implements a model of the KNN algorithm (currently not working).\n\n
\"Linear Regression\": Implements a Linear Regression model (currently not working).\n\n
"""

    text.configure(state='normal')
    text.insert(tk.END, help_t, 'formato')
    text.configure(state='disabled')


def abrirHelpModelos():
    app = ThemedTk(theme="adapta")
    app.geometry('650x650')
    app.resizable(False, False)

    scroll = tk.Scrollbar(app)
    text = tk.Text(app)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.tag_configure('formato', font=('Arial', 12))

    help_t = """
        Hola estos son las selecciones de los campos de entrada y objetivo
    """

    text.configure(state='normal')
    text.insert(tk.END, help_t, 'formato')
    text.configure(state='disabled')