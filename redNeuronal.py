from tabnanny import verbose
import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import funcionesDeTkinter as mn
from idlelib.tooltip import Hovertip
import matplotlib.pyplot as plot
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from tkinter import messagebox as MessageBox
import tensorflow as tf

def solicitarDatosPrueba():
    # inicializamos la GUI
    # gui2 = tk.Tk()
    gui2 = ThemedTk(theme="adapta")

    # Configuramos la gui2
    gui2.geometry("650x650")
    gui2.title("Model evaluation data")

    # Frame para el TreeView
    ventana2 = tk.LabelFrame(gui2, text="xlsx and csv files")
    ventana2.pack(fill="both", expand=True)

    # Frame para el dialogo del archivo2 abierto
    archivo2 = tk.LabelFrame(gui2, text="Use model evaluation data")
    archivo2.pack(side="bottom", fill="both", expand=False)

    img1 = Image.open('./img/searchFile.png')
    img1 = img1.resize((100, 100))
    gui2.img1 = ImageTk.PhotoImage(img1, master=gui2)
    boton1 = tk.Button(archivo2, text="Search file", image=gui2.img1,
                       activebackground="#5ECEF4", compound="top",
                       border=0, command=lambda: buscarArchivo())
    boton1.grid(padx=10, pady=5, row=2, column=0)
    Hovertip(boton1, hover_delay=500,
            text="Search xlsx or csv files")

    img2 = Image.open('./img/prediccion.png')
    img2 = img2.resize((100, 100))
    gui2.img2 = ImageTk.PhotoImage(img2, master=gui2)
    boton2 = tk.Button(archivo2, text="Make prediction", image=gui2.img2,
                       activebackground="#5ECEF4", compound="top",
                       border=0, command=lambda: CargarDatosPrediccion())
    boton2.grid(padx=10, pady=5, row=2, column=2)
    Hovertip(boton2, hover_delay=500,
            text="Makes a prediction based on the selected model and evaluation data")

    # Ruta del archivo2
    global nombreArchivo2
    nombreArchivo2 = ttk.Label(archivo2, text="No selected File")
    nombreArchivo2.grid(pady=5, row=0, column=0, columnspan=3)
    global porcentajePrecision
    porcentajePrecision = ttk.Label(archivo2, text="")
    porcentajePrecision.grid(pady=5, row=1, column=0, columnspan=3)

    # Treeview Widget
    global tv2
    tv2 = ttk.Treeview(ventana2)
    tv2.place(relheight=1, relwidth=1) # establecemos el ancho y el alto del Widget al 100% de su contenedor (ventana2).
    treescrolly = tk.Scrollbar(ventana2, orient="vertical", command=tv2.yview) # comando para actualizar el eje y de la ventana2
    treescrollx = tk.Scrollbar(ventana2, orient="horizontal", command=tv2.xview) # comando para actualizar el eje x de la ventana2
    tv2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # asignamos el Scrollbar al Treeview Widget
    treescrollx.pack(side="bottom", fill="x") # posicionamos el Scrollbar del eje x
    treescrolly.pack(side="right", fill="y") # posicionamos el Scrollbar del eje y

def buscarArchivo():
    """Esta funcion abre el explorador de archivos para que se busque un archivo2"""
    archivo2 = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetype=(("All Files", "*.*"), ("xlsx files", ".xlsx"), ("csv files", ".csv")))
    nombreArchivo2["text"] = archivo2
    # Funcion para eliminar todo del TreeView
    limpiarDatos()
    # Funcion Extraer Datos del Archivo
    extraerDatos()

    insertarDatosTreeView()

def limpiarDatos():
    tv2.delete(*tv2.get_children())
    return None

def insertarDatosTreeView():
    # Llenamos el widget con nuestros datos
    tv2["column"] = list(df2.columns)
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column) # titulo de la columna = nombre de la columna

    df_rows = df2.to_numpy().tolist() # Convertimos el dataframe en una lista de listas
    for row in df_rows:
        tv2.insert("", "end", values=row) # insertamos cada una de las listas dentro del treeview.
    return None

def insertarDatosDePrediccion():
    tv2["column"] = "Predict"
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column) # titulo de la columna = nombre de la columna

    df_rows = listaResultado # Convertimos el dataframe en una lista de listas
    for row in df_rows:
        tv2.insert("", "end", values=row) # insertamos cada una de las listas dentro del treeview.
    return None

def extraerDatos():
    """ Esta funcion extrae los datos del archivo2 seleccionado """
    rutaArchivo = nombreArchivo2["text"]
    global df2
    try:
        archivoExcel = r"{}".format(rutaArchivo)
        if archivoExcel[-4:] == ".csv":
            df2 = pd.read_csv(archivoExcel)
        elif archivoExcel[-4:] == ".txt":
            df2 = pd.read_table(archivoExcel, delimiter="\t")
        else:
            df2 = pd.read_excel(archivoExcel)

    except ValueError:
        tk.messagebox.showerror("Information", "The file is Invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"File was not found in the path {rutaArchivo}")
        return None

############################CODIGO DE REDES NEURONALES#################################################

def CargarDatosPrediccion():
    MessageBox.showinfo("Wait!", "Generating prediction! Click OK to continue.")
    early_stopping = tf.keras.callbacks.EarlyStopping(
    min_delta=0.001, # minimium amount of change to count as an improvement
    patience=15, # how many epochs to wait before stopping
    restore_best_weights=True)

    # Initialising the NN
    model = tf.keras.models.Sequential()

    # layers
    model.add(tf.keras.layers.Dense(units = 16, kernel_initializer = 'uniform', activation = 'relu', input_dim = len(mn.campos)))
    model.add(tf.keras.layers.Dense(units = 8, kernel_initializer = 'uniform', activation = 'relu'))
    model.add(tf.keras.layers.Dense(units=4, kernel_initializer='uniform', activation='relu'))
    model.add(tf.keras.layers.Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
    # Compiling the ANN
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    # Train the ANN
    datosEntrada = mn.df.iloc[:, mn.campos]
    datosObjetivo = mn.df.iloc[:, mn.objetivos]

    global historial
    historial = model.fit(datosEntrada, datosObjetivo, batch_size = 32, epochs = 500, callbacks=[early_stopping], validation_split=0.2, verbose=0)

    y_pred = model.predict(df2)
    y_pred = (y_pred > 0.4).astype('int32')

    global listaResultado
    listaResultado = []
    for res in y_pred:
        for r in res:
            listaResultado.append(r)

    # Funcion para eliminar todo del TreeView
    limpiarDatos()

    insertarDatosDePrediccion()
    MessageBox.showinfo("Success!", "The task has been performed correctly.")
    mostrarPrecision()

def mostrarPrecision():
    fig, ax = plot.subplots()
    fig.suptitle("Model Accuracy Result")
    plot.xlabel("Epoch number")
    plot.ylabel("Precision")
    ax.plot(historial.history["accuracy"])
    porcentajePrecision["text"] = str(f'The accuracy of the model is: {(historial.history["accuracy"][-1])*100:.2f}%')
    plot.show()