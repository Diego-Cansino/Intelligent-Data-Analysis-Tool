from ttkthemes import ThemedTk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import tkinter as tk
import ventanaCampSelection as vcs

def abrirDataSelection(df):
    global rbAlea, rbRango, de, valDe, hasta, valHasta, label3, porcentaje, btnAceptar, opcion
    app = ThemedTk(theme="adapta")
    app.geometry('400x420')
    app.resizable(False, False)
    app.title("Data Selection")
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.columnconfigure(2, weight=1)
    app.columnconfigure(3, weight=1)

    seleccion = ttk.Label(app, text="DATA SELECTION", font=('Helvetica', 15, 'bold'))
    seleccion.grid(pady=5, row=0, columnspan=4)

    # Etiqueta selección de tipo
    label1 = ttk.Label(app, text="Choose a type of data selection: ",
                       font=('Helvetica', 12, 'bold'))
    label1.grid(pady=5, row=1, column=0, columnspan=4, sticky="w")

    # Botones 
    ## Seleccion de campos
    imgCamp = Image.open('./img/selCampos.png')
    imgCamp = imgCamp.resize((100, 100))
    app.imgCamp = ImageTk.PhotoImage(imgCamp, master=app)
    btnCampos = tk.Button(image=app.imgCamp, text="Fields", compound="top",
                          activebackground="#5ECEF4", command=lambda:[desactivarTodo(), vcs.abrirSelCamp(df)])

    ## Seleccion de registros
    imgReg = Image.open('./img/selRegistros.png')
    imgReg = imgReg.resize((100, 100))
    app.imgReg = ImageTk.PhotoImage(imgReg, master=app)
    btnReg = tk.Button(image=app.imgReg, text="Records", compound="top",
                       activebackground="#5ECEF4", command=lambda:activarRadios())

    btnCampos.grid(pady=5, row=2, column=0, columnspan=2, sticky="nsew")
    btnReg.grid(pady=5, row=2, column=2, columnspan=2, sticky="nsew")

    # SELECCIÓN REGISTROS
    opcion = tk.IntVar()
    ## Radio Rango
    rbRango = tk.Radiobutton(app, text="By range",
                              activebackground="#5ECEF4", border=0, 
                              variable=opcion, value=0, compound="top", 
                              font=('Helvetica', 15, 'bold'),
                              state="disable", command=lambda: activarRango())
    rbRango.grid(padx=10, pady=15, row=3, column=0, columnspan=2, sticky="nsew")
    ## Radio Aleatorio
    rbAlea = tk.Radiobutton(app, text="Random",
                              activebackground="#5ECEF4", border=0, 
                              variable=opcion, value=1, compound="top", 
                              font=('Helvetica', 15, 'bold'),
                              state="disable", command=lambda: activarAleatorio())
    rbAlea.grid(padx=10, pady=15, row=3, column=2, columnspan=2, sticky="nsew")

    ### Selección rango
    de = ttk.Label(app, text="Range of:", font=('Helvetica', 12, 'bold'),
                       state="disable")
    de.grid(pady=5, row=4, column=0)
    valDe = ttk.Entry(app, state="disable", width=5)
    valDe.grid(pady=5, row=4, column=1, sticky="nsew")

    hasta = ttk.Label(app, text=" to: ", font=('Helvetica', 12, 'bold'),
                       state="disable")
    hasta.grid(pady=5, row=4, column=2)
    valHasta = ttk.Entry(app, state="disable", width=5)
    valHasta.grid(pady=5, row=4, column=3, sticky="nsew")

    ### Selección aleatoria
    label3 = ttk.Label(app, text="Percentage: ", font=('Helvetica', 12, 'bold'),
                       state="disable")
    label3.grid(pady=5, row=5, column=0, columnspan=2)

    porcentaje = ttk.Spinbox(app, from_=1, to=100, increment=1, format="%.0f", 
                             state="disable")
    porcentaje.grid(pady=5, row=5, column=2, columnspan=2, sticky="nsew")

    # Boton aceptar 
    imgGuardar = Image.open('./img/guardar.png')
    imgGuardar = imgGuardar.resize((30, 30))
    app.imgGuardar = ImageTk.PhotoImage(imgGuardar, master=app)
    btnAceptar = tk.Button(image=app.imgGuardar, text="Save selection",
                           compound="top", state="disable", command=lambda :elegirFuncion(df),
                           activebackground="#5ECEF4")
    btnAceptar.grid(pady=15, row=6, column=0, columnspan=4)

def activarRadios():
    # Activar los RadioButton
    rbRango.configure(state="normal")
    rbAlea.configure(state="normal")
    # Activar opciones 
    if (opcion.get() == 0):
        activarRango()
    else: 
        activarAleatorio()
    # Activar boton
    btnAceptar.configure(state="normal")

def activarRango():
    # Activar los campos del rango
    de.configure(state="normal")
    valDe.configure(state="normal")
    hasta.configure(state="normal")
    valHasta.configure(state="normal")
    # Desactivar los campos de aleatorio
    label3.configure(state="disable")
    porcentaje.set("")
    porcentaje.configure(state="disable")

def activarAleatorio():
    # Activar los campos aleatorio
    label3.configure(state="normal")
    porcentaje.configure(state="readonly")
    # Desactivar los campos de rango
    de.configure(state="disable")
    valDe.delete(0, len(valDe.get()))
    valDe.configure(state="disable")
    hasta.configure(state="disable")
    valHasta.delete(0, len(valHasta.get()))
    valHasta.configure(state="disable")

def desactivarTodo():
    rbRango.configure(state="disable")
    rbAlea.configure(state="disable")
    # Desasctivar los campos aleatorio
    label3.configure(state="disable")
    porcentaje.set("")
    porcentaje.configure(state="disable")
    # Desactivar los campos de rango
    de.configure(state="disable")
    valDe.delete(0, len(valDe.get()))
    valDe.configure(state="disable")
    hasta.configure(state="disable")
    valHasta.delete(0, len(valDe.get()))
    valHasta.configure(state="disable")
    btnAceptar.configure(state="disable")

def guardarAleatorio(df):
    if(porcentaje.get() != ""):
        n = float(porcentaje.get())/100
        df = df.sample(frac=n)
        file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
        df.to_excel(file, index=False, header=True)
    else:
        messagebox.showerror("Error", "Select a percentage")

def guardarRango(df):
    filas = df.shape
    if(valDe.get() == "" or valHasta.get() == ""):
        messagebox.showerror("Error", "Select a range")

    elif ((valDe.get().isdigit() and valHasta.get().isdigit()) 
          and (int(valDe.get()) <= int(valHasta.get()))
          and (int(valDe.get()) > 0)
          and (int(valHasta.get()) <= filas[0])):
        a = int(valDe.get())-1
        b = int(valHasta.get())
        df = df.iloc[range(a, b),:]
        file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
        df.to_excel(file, index=False, header=True)

    else: 
        messagebox.showerror("Error", f"Invalid range\nval min: 1, val max: {filas[0]}")

def elegirFuncion(df):
    if(opcion.get() == 0):
        guardarRango(df)
    elif(opcion.get() == 1):
        guardarAleatorio(df)
    else: 
        messagebox.showerror("Error", "Error")
    desactivarTodo()