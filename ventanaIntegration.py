import pandas as pd
from ttkthemes import ThemedTk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import tkinter as tk

def abrirDataIntegration(df):
    global df2
    app = ThemedTk(theme="adapta")
    app.geometry('400x300')
    app.resizable(False, False)
    app.title("Data Integration")
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.rowconfigure(2, weight=1)

    seleccion = ttk.Label(app, text="DATA INTEGRATION", font=('Helvetica', 15, 'bold'))
    seleccion.grid(pady=5, row=0, columnspan=2)

    # Etiqueta selección de tipo
    label1 = ttk.Label(app, text="Choose a type of data integration: ",
                       font=('Helvetica', 12, 'bold'))
    label1.grid(pady=5, row=1, column=0, columnspan=2, sticky="w")

    # Botones 
    ## Integración por campos 
    imgCamp = Image.open('./img/integrarCols.png')
    imgCamp = imgCamp.resize((100, 100))
    app.imgCamp = ImageTk.PhotoImage(imgCamp, master=app)
    btnCampos = tk.Button(image=app.imgCamp, text="Fields", compound="top",
                          activebackground="#5ECEF4", command=lambda: [buscarArchivo(), integrarCampos(df)])

    ## Seleccion por registros
    imgReg = Image.open('./img/integrarRegs.png')
    imgReg = imgReg.resize((100, 100))
    app.imgReg = ImageTk.PhotoImage(imgReg, master=app)
    btnReg = tk.Button(image=app.imgReg, text="Records", compound="top",
                       activebackground="#5ECEF4", command=lambda: [buscarArchivo(), integrarRegistros(df)])

    btnCampos.grid(pady=5, row=2, column=0, sticky="nsew")
    btnReg.grid(pady=5, row=2, column=1, sticky="nsew")

def integrarCampos(df):
    filas = df.shape
    filasDf2 = df2.shape
    if(filas[0] == filasDf2[0]):
        if(verificarRepetidos(df)):
            dfR = df.join(df2)
            tk.messagebox.showinfo("Success!", "Ready to save data integration")
            file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
            dfR.to_excel(file, index=False, header=True)
        else: 
            tk.messagebox.showerror("Error", "Repeated fields names")
    else:
        tk.messagebox.showerror("Error", f"The number of rows is not equal\nExpected rows: {filas[0]}")

def integrarRegistros(df):
    cols = df.shape
    cols2 = df2.shape
    if(cols[1] == cols2[1]):
        if(verificarRepetidos(df)):
            dfR = pd.concat([df, df2], sort=False)
            tk.messagebox.showinfo("Success!", "Ready to save data integration")
            file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
            dfR.to_excel(file, index=False, header=True)
        else: 
            tk.messagebox.showerror("Error", "Different field names")
    else: 
        tk.messagebox.showerror("Error", f"The number of fields is not equal\nExpected fields: {cols[0]}")

def verificarRepetidos(df):
    listaCampos = df.columns.tolist()
    listaCampos2 = df2.columns.tolist()
    repetido = True
    for campo in listaCampos:
        for campo2 in listaCampos2:
            if (campo == campo2):
                repetido = False
    return repetido

def extraerDatos(archivo):
    """ Esta funcion extrae los datos del archivo seleccionado """
    rutaArchivo = archivo
    global df2
    df2 = []
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
        df2 = []
        
    except FileNotFoundError:
        tk.messagebox.showerror(
            "Information", f"File was not found in the path {rutaArchivo}")
        df2 = []

def buscarArchivo():
    """Esta funcion abre el explorador de archivos para que se busque un archivo"""
    archivo = filedialog.askopenfilename(initialdir="/",
                                         title="Select a File",
                                         filetype=(("All Files", "*.*"), ("xlsx files", ".xlsx"), ("csv files", ".csv"), ("txt files", ".txt")))

    extraerDatos(archivo)