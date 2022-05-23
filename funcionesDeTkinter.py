import tkinter as tk
from tkinter import BooleanVar, filedialog, ttk
from idlelib.tooltip import Hovertip
import pandas as pd
import graficos as gf
import redNeuronal as pr


def abrirMenuPrincipal():
    # inicializamos la GUI
    gui = tk.Tk()

    # Configuramos la gui
    gui.geometry("750x500")

    # Frame para el TreeView
    ventana = tk.LabelFrame(gui, text="xlsx and csv files")
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
    e_comprension = ttk.Label(p1, text="DATA UNDERSTANDING")
    e_comprension.grid(pady=5, row=0, column=0, columnspan=3)

    button1_1 = tk.Button(p1, text="Search file", width=22,
                          command=lambda: buscarArchivo())
    button1_1.grid(padx=10, pady=5, row=1, column=0)
    Hovertip(button1_1, hover_delay=500,
             text="Search xlsx or csv files")

    button1_2 = tk.Button(p1, text="Show file", width=22,
                          command=lambda: CargarDatosExcel())
    button1_2.grid(padx=10, pady=5, row=1, column=1)
    Hovertip(button1_2, hover_delay=500,
             text="Displays file data in the application")

    button1_3 = tk.Button(p1, text="Graphing data", width=22,
                          command=lambda: abrirGraficos())
    button1_3.grid(padx=10, pady=5, row=1, column=2)
    Hovertip(button1_3, hover_delay=500,
             text="Open a window with options for plotting")

    # Elementos Pestaña 2
    ## PREPARACIÓN DE LOS DATOS
    e_preparacion = ttk.Label(p2, text="DATA PREPARATION")
    e_preparacion.grid(pady=5, row=0, column=0, columnspan=4)

    button2_1 = tk.Button(p2, text="FFILL", width=22,
                          command=lambda: limpiarDatosForwardFill())
    button2_1.grid(padx=10, pady=5, row=1, column=0)
    Hovertip(button2_1, hover_delay=500,
             text="Cleaning data using functionality FFILL: Any missing value is filled based on the corresponding value in the previous row.")

    button2_2 = tk.Button(p2, text="BFILL", width=22,
                          command=lambda: limpiarDatosBackwardFill())
    button2_2.grid(padx=10, pady=5, row=1, column=1)
    Hovertip(button2_2, hover_delay=500,
             text="Cleaning data using functionality BFILL: Is used to backward fill the missing values in the dataset.")

    button2_3 = tk.Button(p2, text="None", width=22,
                          command=lambda: limpiarDatosColumnaVacia())
    button2_3.grid(padx=10, pady=5, row=1, column=2)
    Hovertip(button2_3, hover_delay=500,
             text="Cleaning data using functionality None: Filters the values of a dataset to leave only those that are non-null.")

    button2_4 = tk.Button(p2, text="ALL", width=22,
                          command=lambda: limpiarDatosAllMethods())
    button2_4.grid(padx=10, pady=5, row=1, column=3)
    Hovertip(button2_4, hover_delay=500,
             text="Cleaning data using functionality ALL: Makes a combination of FFILL, BFILL and None functionalities")

    # Elementos Pestaña 3
    ## TECNICAS DE MODELADO
    e_modelado = ttk.Label(p3, text="MODELING")
    e_modelado.grid(pady=5, row=0, column=0, columnspan=4)

    button3_1 = tk.Button(p3, text="Artificial Neural Network", width=22,
                          command=abrirModelos)
    button3_1.grid(padx=10, pady=5, row=1, column=0)
    Hovertip(button3_1, hover_delay=500,
             text="Model: Artificial Neural Network")

    button3_2 = tk.Button(p3, text="Linear Regression", width=22,
                          command=abrirModelos)
    button3_2.grid(padx=10, pady=5, row=1, column=1)
    Hovertip(button3_2, hover_delay=500,
             text="Model: Linear Regression")

    button3_3 = tk.Button(p3, text="Decision tree", width=22,
                          command=abrirModelos)
    button3_3.grid(padx=10, pady=5, row=1, column=2)
    Hovertip(button3_3, hover_delay=500,
             text="Model: Decision tree")

    button3_4 = tk.Button(p3, text="KNN", width=22,
                          command=abrirModelos)
    button3_4.grid(padx=10, pady=5, row=1, column=3)
    Hovertip(button3_4, hover_delay=500,
             text="Model: KNN")

    # Agregamos las pestañas creadas
    notebook.add(p1, text='Understanding')
    notebook.add(p2, text='Preparation')
    notebook.add(p3, text='Modeling')

    # Barra de Menús
    barraMenu = tk.Menu(gui)
    menuHelp = tk.Menu(barraMenu, tearoff=False)
    menuHelp.add_command(label="Help", command=lambda: abrirHelp())
    barraMenu.add_cascade(label="Help", menu=menuHelp)
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
        else:
            df = pd.read_excel(archivoExcel)

    except ValueError:
        tk.messagebox.showerror("Information", "The file is Invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror(
            "Information", f"File was not found in the path {rutaArchivo}")
        return None


def buscarArchivo():
    """Esta funcion abre el explorador de archivos para que se busque un archivo"""
    archivo = filedialog.askopenfilename(initialdir="/",
                                         title="Select a File",
                                         filetype=(("csv files", ".csv"), ("xlsx files", ".xlsx"), ("All Files", "*.*")))
    nombreArchivo["text"] = archivo
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


def CargarDatosExcel():
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


def limpiarDatosBackwardFill():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    limpiarDatos()
    global df
    df = df.fillna(method="backfill")
    insertarDatosTreeView()


def limpiarDatosColumnaVacia():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    limpiarDatos()  # por si no tiene nada la columna
    global df
    df = df.dropna(axis=1)
    insertarDatosTreeView()


def limpiarDatosAllMethods():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    limpiarDatos()
    global df
    df = df.fillna(method="ffill")
    df = df.fillna(method="backfill")
    df = df.dropna(axis=1)
    insertarDatosTreeView()


def abrirGraficos():
    app = tk.Tk()
    app.geometry('800x120')

    # Extraemos los datos

    listaGraficos = ["Vertical bar graph", "horizontal bar graph",
                     "Dispersion", "Linear", "Area", "Histogram", "Pie Chart"]
    listaColumnas = df.columns.tolist()

    # Declaramos los label
    label1 = tk.Label(app, text="Choose the type of chart: ")
    label1.grid(column=0, row=0)

    label2 = tk.Label(app, text="Value of X: ")
    label2.grid(column=2, row=0)

    label3 = tk.Label(app, text="Value of Y: ")
    label3.grid(column=4, row=0)

    # Declaramos las opciones
    lista1 = ttk.Combobox(app, state="readonly", values=listaGraficos)
    lista1.grid(column=1, row=0)
    lista1.current(0)

    lista2 = ttk.Combobox(app, state="readonly", values=listaColumnas)
    lista2.grid(column=3, row=0)
    lista2.current(0)

    lista3 = ttk.Combobox(app, state="readonly", values=listaColumnas)
    lista3.grid(column=5, row=0)
    lista3.current(0)

    boton = tk.Button(app, text="Graph the data", command=lambda: graficar(
        lista1.get(), df[lista2.get()], df[lista3.get()], lista2.get(), lista3.get()))
    boton.place(relx=0.5, rely=0.75, anchor="center")


def graficar(tipoGrafica, ValoresX, ValoresY, etiquetaX, etiquetaY):
    if(tipoGrafica == "Vertical bar graph"):
        gf.diagramaBarrasVerticales(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == "horizontal bar graph"):
        gf.diagramaBarrasHorizontales(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == "Dispersion"):
        gf.diagramaDispersion(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == "Linear"):
        gf.diagramaLineas(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == "Area"):
        gf.diagramaAreas(ValoresX, ValoresY, etiquetaX, etiquetaY)
    elif(tipoGrafica == "Histogram"):
        gf.histograma(ValoresX, etiquetaX)
    elif(tipoGrafica == "Pie Chart"):
        gf.diagramaSectores(ValoresX)


def abrirModelos():
    app = tk.Tk()
    app.geometry('1000x1000')

    # Extraemos los datos
    listaCampos = df.columns.tolist()

    #Declaramos las listas que nos ayudarán a seleccionar los datos
    listaCampos2 = []
    listaObjetivo = []

    #Creamos los Frame que nos permiten seleccionar los datos
    frame1 = tk.Label(app)
    frame1.pack()
    frame2 = tk.LabelFrame(frame1, text='INPUT', padx=30, pady=10)
    frame3 = tk.LabelFrame(frame1, text='TARGET', padx=30, pady=10)

    i = 0
    #Ciclos para ingresar todos los campos como opciones a los frames
    for campo in listaCampos:
        listaCampos2.append(BooleanVar())
        tk.Checkbutton(frame2, text=campo,
                       variable=listaCampos2[i]).pack(anchor="w")
        i += 1
    frame2.grid(row=0, column=0, columnspan=1, padx=30)

    i = 0
    for campo in listaCampos:
        listaObjetivo.append(BooleanVar())
        tk.Checkbutton(frame3, text=campo,
                       variable=listaObjetivo[i]).pack(anchor="w")
        i += 1
    frame3.grid(row=0, column=1, columnspan=1, padx=30)

    app.update()

    alto = frame1.winfo_height()
    ancho = frame1.winfo_width()
    app.geometry(f'{ancho+70}x{alto+70}')

    ##Función para mandar los datos a los arreglos que trabajarán con los modelos

    def mostrarSeleccion():
        global campos
        global objetivos
        campos = []
        objetivos = []
        for i in range(len(listaCampos2)):
            if listaCampos2[i].get():
                campos.append(i)
            if listaObjetivo[i].get():
                objetivos.append(i)

    boton = tk.Button(app, text="Build model", command=lambda: [
                      pr.solicitarDatosPrueba(), mostrarSeleccion(), app.destroy()])
    boton.pack(side="bottom", pady=20)


def abrirHelp():
    app = tk.Tk()
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
