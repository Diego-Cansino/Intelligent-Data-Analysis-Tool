from tkinter import LEFT, RIGHT, filedialog, ttk
from idlelib.tooltip import Hovertip
from pathlib import Path
import tkinter as tk
import pandas as pd
import ventanaSeleccion as v
import ventanaGraphs as gh
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from tkinter import messagebox as MessageBox
from webbrowser import open

def abrirMenuPrincipal():
    # inicializamos la GUI
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

    img1_1 = Image.open('./img/documento.png')
    img1_1 = img1_1.resize((100,100))
    p1.img1_1 = ImageTk.PhotoImage(img1_1, master=p1)
    button1_1 = tk.Button(p1, text="Business Understanding", image=p1.img1_1,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: descargarComprension())
    button1_1.grid(padx=10, pady=5, row=1, column=0)
    Hovertip(button1_1, hover_delay=500,
             text="Search txt, xlsx or csv files")

    img1_2 = Image.open('./img/searchFile.png')
    img1_2 = img1_2.resize((100,100))
    p1.img1_2 = ImageTk.PhotoImage(img1_2, master=p1)
    button1_2 = tk.Button(p1, text="Search file", image=p1.img1_2, 
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: buscarArchivo())
    button1_2.grid(padx=10, pady=5, row=1, column=1)
    Hovertip(button1_2, hover_delay=500,
             text="Search txt, xlsx or csv files")

    img1_3 = Image.open('./img/plotting.png')
    img1_3 = img1_3.resize((100, 100))
    p1.img1_3 = ImageTk.PhotoImage(img1_3, master=p1)
    button1_3 = tk.Button(p1, text="Graphing data", image=p1.img1_3,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: gh.abrirGraficos(df))
    button1_3.grid(padx=10, pady=5, row=1, column=2)
    Hovertip(button1_3, hover_delay=500,
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
    e_limpieza = ttk.Label(p2_2, text="DATA CLEANING", font=('Helvetica', 12, 'bold'))
    e_limpieza.grid(pady=5, row=3, column=0)

    img2_2 = Image.open('./img/FFILL.png')
    img2_2 = img2_2.resize((60,60))
    p2_2.img2_2 = ImageTk.PhotoImage(img2_2, master=p2_2)
    button2_2 = tk.Button(p2_2, text="FFILL", image=p2_2.img2_2,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.selectCamposDC(df, 'FFILL'))
    button2_2.grid(padx=10, pady=5, row=4, column=0)
    Hovertip(button2_2, hover_delay=500,
             text="Cleaning data using functionality FFILL: Any missing value is filled based on the corresponding value in the previous row.")

    img2_3 = Image.open('./img/BFILL.png')
    img2_3 = img2_3.resize((60,60))
    p2_2.img2_3 = ImageTk.PhotoImage(img2_3, master=p2_2)
    button2_3 = tk.Button(p2_2, text="BFILL", image=p2_2.img2_3,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.selectCamposDC(df, 'BFILL'))
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
                          border=0, command=lambda: v.selectCamposDC(df, 'norma'))
    button2_6.grid(padx=10, pady=5, row=4, column=4)
    Hovertip(button2_6, hover_delay=500,
             text="standardize atypical data")

    img2_7 = Image.open('./img/promedio.png')
    img2_7 = img2_7.resize((60, 60))
    p2_2.img2_7 = ImageTk.PhotoImage(img2_7, master=p2_2)
    button2_7 = tk.Button(p2_2, text="MEAN", image=p2_2.img2_7,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.selectCamposDC(df, 'media'))
    button2_7.grid(padx=10, pady=5, row=5, column=0)
    Hovertip(button2_7, hover_delay=500,
             text="Cleaning data using statistical method Mean")

    img2_8 = Image.open('./img/media.png')
    img2_8 = img2_8.resize((60, 60))
    p2_2.img2_8 = ImageTk.PhotoImage(img2_8, master=p2_2)
    button2_8 = tk.Button(p2_2, text="MEDIAN", image=p2_2.img2_8,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.selectCamposDC(df, 'mediana'))
    button2_8.grid(padx=10, pady=5, row=5, column=1)
    Hovertip(button2_8, hover_delay=500,
             text="Cleaning data using statistical method Median")

    img2_9 = Image.open('./img/moda.png')
    img2_9 = img2_9.resize((60, 60))
    p2_2.img2_9 = ImageTk.PhotoImage(img2_9, master=p2_2)
    button2_9 = tk.Button(p2_2, text="MODE", image=p2_2.img2_9,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.selectCamposDC(df, 'moda'))
    button2_9.grid(padx=10, pady=5, row=5, column=2)
    Hovertip(button2_9, hover_delay=500,
             text="Cleaning data using statistical method Mode")

    img2_10 = Image.open('./img/rango.png')
    img2_10 = img2_10.resize((60, 60))
    p2_2.img2_10 = ImageTk.PhotoImage(img2_10, master=p2_2)
    button2_10 = tk.Button(p2_2, text="RANGE", image=p2_2.img2_10,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.selectCamposDC(df, 'rango'))
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
    canvas_3 = tk.Canvas(p3, border=0)
    canvas_3.pack(side=LEFT, fill="both", expand="yes")

    yscroll = tk.Scrollbar(p3, orient="vertical",
                           command=canvas_3.yview, border=0)
    yscroll.pack(side=RIGHT, fill="y")

    canvas_3.configure(yscrollcommand=yscroll.set)

    canvas_3.bind('<Configure>', lambda e: canvas_3.configure(
        scrollregion=canvas_3.bbox('all')))

    p3_2 = tk.Frame(canvas_3, border=0)
    p3_2.bind('<MouseWheel>', lambda e: canvas_3.yview_scroll(
        int(-1*(e.delta/120)), "units"))
    canvas_3.create_window((0, 0), window=p3_2, anchor="nw", width=(
        canvas_3.winfo_width()-yscroll.winfo_width()))

    e_modelado = ttk.Label(p3_2, text="MODELING", font=('Helvetica', 15, 'bold'))
    e_modelado.grid(pady=5, row=0, column=0, columnspan=4)
    
    ### MODELADO CLASIFICACION
    e_clasificacion = ttk.Label(p3_2, text="CLASSIFICATION MODELS", font=('Helvetica', 12, 'bold'))
    e_clasificacion.grid(pady=5, row=1, column=0, columnspan=4)

    img3_1 = Image.open('./img/redNeuronal.png')
    img3_1 = img3_1.resize((60, 60))
    p3_2.img3_1 = ImageTk.PhotoImage(img3_1, master=p3_2)
    button3_1 = tk.Button(p3_2, text="Artificial Neural Network", image=p3_2.img3_1,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "ann"))
    button3_1.grid(padx=10, pady=5, row=2, column=0)
    Hovertip(button3_1, hover_delay=500,
             text="Model: Classifier Artificial Neural Network.")

    img3_2 = Image.open('./img/regresion.png')
    img3_2 = img3_2.resize((60, 60))
    p3_2.img3_2 = ImageTk.PhotoImage(img3_2, master=p3_2)
    button3_2 = tk.Button(p3_2, text="Logistic Regression", image=p3_2.img3_2,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "lr"))
    button3_2.grid(padx=10, pady=5, row=2, column=1)
    Hovertip(button3_2, hover_delay=500,
             text="Model: Logistic regression classifier")

    img3_3 = Image.open('./img/arbol.png')
    img3_3 = img3_3.resize((60, 60))
    p3_2.img3_3 = ImageTk.PhotoImage(img3_3, master=p3_2)
    button3_3 = tk.Button(p3_2, text="Decision tree", image=p3_2.img3_3,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "dt"))
    button3_3.grid(padx=10, pady=5, row=2, column=2)
    Hovertip(button3_3, hover_delay=500,
             text="Model: Decision tree classifier.")

    img3_4 = Image.open('./img/vecinos.png')
    img3_4 = img3_4.resize((60, 60))
    p3_2.img3_4 = ImageTk.PhotoImage(img3_4, master=p3_2)
    button3_4 = tk.Button(p3_2, text="KNN", image=p3_2.img3_4,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "knn"))
    button3_4.grid(padx=10, pady=5, row=2, column=3)
    Hovertip(button3_4, hover_delay=500,
             text="Model: Classifier implementing the k-nearest neighbors vote.")

    img3_5 = Image.open('./img/GaussClas.png')
    img3_5 = img3_5.resize((60, 60))
    p3_2.img3_5 = ImageTk.PhotoImage(img3_5, master=p3_2)
    button3_5 = tk.Button(p3_2, text="Gaussian Naive Bayes", image=p3_2.img3_5,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "nb"))
    button3_5.grid(padx=10, pady=5, row=3, column=0)
    Hovertip(button3_5, hover_delay=500,
             text="Model: Gaussian Naive Bayes")

    img3_6 = Image.open('./img/SVM1.png')
    img3_6 = img3_6.resize((60, 60))
    p3_2.img3_6 = ImageTk.PhotoImage(img3_6, master=p3_2)
    button3_6 = tk.Button(p3_2, text="SVM CLASSIFIER", image=p3_2.img3_6,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "svm_c"))
    button3_6.grid(padx=10, pady=5, row=3, column=1)
    Hovertip(button3_6, hover_delay=500, text="Model: SVM CLASSIFIER")

    ### MODELADO REGRESION
    e_clasificacion = ttk.Label(
        p3_2, text="REGRESSION MODELS", font=('Helvetica', 12, 'bold'))
    e_clasificacion.grid(pady=5, row=4, column=0, columnspan=4)

    img3_7 = Image.open('./img/redNeuronalReg.png')
    img3_7 = img3_7.resize((60, 60))
    p3_2.img3_7 = ImageTk.PhotoImage(img3_7, master=p3_2)
    button3_7 = tk.Button(p3_2, text="Artificial Neural Network", image=p3_2.img3_7,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "ann_regression"))
    button3_7.grid(padx=10, pady=5, row=5, column=0)
    Hovertip(button3_7, hover_delay=500,
             text="Model: Regressor Artificial Neural Network.")

    img3_8 = Image.open('./img/regresionReg.png')
    img3_8 = img3_8.resize((60, 60))
    p3_2.img3_8 = ImageTk.PhotoImage(img3_8, master=p3_2)
    button3_8 = tk.Button(p3_2, text="Logistic Regression", image=p3_2.img3_8,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "lr_regression"))
    button3_8.grid(padx=10, pady=5, row=5, column=1)
    Hovertip(button3_8, hover_delay=500,
             text="Model: Linear regression")

    img3_9 = Image.open('./img/arbolReg.png')
    img3_9 = img3_9.resize((60, 60))
    p3_2.img3_9 = ImageTk.PhotoImage(img3_9, master=p3_2)
    button3_9 = tk.Button(p3_2, text="Decision tree", image=p3_2.img3_9,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "dt_regression"))
    button3_9.grid(padx=10, pady=5, row=5, column=2)
    Hovertip(button3_9, hover_delay=500,
             text="Model: Decision tree Regressor.")

    img3_10 = Image.open('./img/vecinosReg.png')
    img3_10 = img3_10.resize((60, 60))
    p3_2.img3_10 = ImageTk.PhotoImage(img3_10, master=p3_2)
    button3_10 = tk.Button(p3_2, text="KNN", image=p3_2.img3_10,
                          activebackground="#5ECEF4", compound="top",
                          border=0, command=lambda: v.abrirModelos(df, "knn_regression"))
    button3_10.grid(padx=10, pady=5, row=5, column=3)
    Hovertip(button3_10, hover_delay=500,
             text="Model: Regressor implementing the k-nearest neighbors vote.")

    img3_11 = Image.open('./img/BayesReg.png')
    img3_11 = img3_11.resize((60, 60))
    p3_2.img3_11 = ImageTk.PhotoImage(img3_11, master=p3_2)
    button3_11 = tk.Button(p3_2, text="Bayesian Ridge", image=p3_2.img3_11,
                          activebackground="#5ECEF4", compound="top",
                           border=0, command=lambda: v.abrirModelos(df, "br"))
    button3_11.grid(padx=10, pady=5, row=6, column=0)
    Hovertip(button3_11, hover_delay=500,
             text="Model: Bayesian Ridge")

    img3_12 = Image.open('./img/SVM2.png')
    img3_12 = img3_12.resize((60, 60))
    p3_2.img3_12 = ImageTk.PhotoImage(img3_12, master=p3_2)
    button3_12 = tk.Button(p3_2, text="SVM REGRESSION", image=p3_2.img3_12,
                          activebackground="#5ECEF4", compound="top",
                           border=0, command=lambda: v.abrirModelos(df, "svm_r"))
    button3_12.grid(padx=10, pady=5, row=6, column=1)
    Hovertip(button3_12, hover_delay=500,
             text="Model: SVM REGRESSION")
    
    # Agregamos las pestañas creadas
    notebook.add(p1, text='Data Understanding')
    notebook.add(p2, text='Data Preparation')
    notebook.add(p3, text='Data Modeling')

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
        
    except FileNotFoundError:
        tk.messagebox.showerror(
            "Information", f"File was not found in the path {rutaArchivo}")
        df = []


def descargarComprension():
    """Esta función descarga un archivo .word con el formato
       para la fase de comprensión del negocio"""
    link = 'https://docs.google.com/document/d/1cZz-OM-xpXeIiBX3RLh0m8zHprMz4DXbEbuhe74X5C0/edit?usp=sharing'
    open(link, new=1)

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

def dataCleaning(df):
    limpiarDatos()
    insertarDatosTreeView()
    verificarDatosNulos()

def insertarDatosTreeView():
    # Llenamos el widget con nuestros datos
    col_df = list( df.columns)
    col_df.insert(0, 'Index')
    tv1["column"] = col_df
    tv1["show"] = "headings"
    tv1.heading("Index", text="Index")
    
    for column in tv1["columns"]:
        # titulo de la columna = nombre de la columna
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()  # Convertimos el dataframe en una lista de listas
    i = 1
    
    for row in df_rows:
        # insertamos cada una de las listas dentro del treeview.
        row.insert(0,i)
        tv1.insert("", "end", values=row)
        i+=1

def cargarDatosExcel():
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    # Funcion Extraer Datos del Archivo
    extraerDatos()
    # Funcion para eliminar todo del TreeView
    limpiarDatos()

    insertarDatosTreeView()
    
def limpiarDatos():
    tv1.delete(*tv1.get_children())

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