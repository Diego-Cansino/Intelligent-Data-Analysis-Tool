from ttkthemes import ThemedTk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import filedialog

def newData(df):
    global opcion, result_name_entry, lOption, opciones1, opciones2, boton
    try:
        app = ThemedTk(theme="adapta")
        app.geometry('650x520')
        app.resizable(False, False)
        app.title("Data Calculator")
        app.columnconfigure(0, weight=1)
        app.columnconfigure(1, weight=1)
        app.columnconfigure(2, weight=1)
        app.columnconfigure(3, weight=1)

        nuevosDatos = ttk.Label(app, text="NEW DATA", font=('Helveltica', 15, 'bold'))
        nuevosDatos.grid(pady=5, row=0, column=0, columnspan=4)

        #Etiqueta opereciones aritmeticas 
        label = ttk.Label(app, text="Arithmetic operations:", font=('Helvetica', 12, 'bold'))
        label.grid(pady=5, row=1, column=0, columnspan=4, sticky="w")

        opcion = tk.IntVar()
        ## suma
        imgSum = Image.open('./img/suma.png')
        imgSum = imgSum.resize((70,70))
        app.imgSum = ImageTk.PhotoImage(imgSum, master=app)
        buttonSum = tk.Radiobutton(app, image=app.imgSum, text='Sum', 
                                   activebackground="#5ECEF4", border=0,
                                   variable=opcion, value=0, compound="top",
                                   command=desactivarOp1)
        buttonSum.grid(padx=10, pady=5, row=2, column=0)
        Hovertip(buttonSum, hover_delay=500, text="Sum")
        
        ## Resta
        imgRes = Image.open('./img/resta.png')
        imgRes = imgRes.resize((70, 70))
        app.imgRes = ImageTk.PhotoImage(imgRes, master=app)
        buttonRes = tk.Radiobutton(app, image=app.imgRes, text='Subtract', 
                                   activebackground="#5ECEF4", border=0,
                                   variable=opcion, value=1, compound="top",
                                   command=desactivarOp1)
        buttonRes.grid(padx=10, pady=5, row=2, column=1)
        Hovertip(buttonRes, hover_delay=500, text="Subtract")

        ## Multiplicación
        imgMult = Image.open('./img/multi.png')
        imgMult = imgMult.resize((70, 70))
        app.imgMult = ImageTk.PhotoImage(imgMult, master=app)
        buttonMult = tk.Radiobutton(app, image=app.imgMult, text='Multiplication',
                                    activebackground="#5ECEF4", border=0,
                                    variable=opcion, value=2, compound="top",
                                    command=desactivarOp1)
        buttonMult.grid(padx=10, pady=5, row=2, column=2)
        Hovertip(buttonMult, hover_delay=500, text="Multiplication")

        ## División
        imgDiv = Image.open('./img/division.png')
        imgDiv = imgDiv.resize((70, 70))
        app.imgDiv = ImageTk.PhotoImage(imgDiv, master=app)
        buttonDiv = tk.Radiobutton(app, image=app.imgDiv, text='Division', 
                                   activebackground="#5ECEF4", border=0,
                                   variable=opcion, value=3, compound="top",
                                   command=desactivarOp1)
        buttonDiv.grid(padx=10, pady=5, row=2, column=3)
        Hovertip(buttonDiv, hover_delay=500, text="Division")

        #Etiqueta opereciones logicas
        label2 = ttk.Label(app, text="Logical operations:",
                           font=('Helvetica', 12, 'bold'))
        label2.grid(pady=5, row=3, column=0, columnspan=4, sticky="w")

        ## and
        imgAnd = Image.open('./img/and.png')
        imgAnd = imgAnd.resize((70, 70))
        app.imgAnd = ImageTk.PhotoImage(imgAnd, master=app)
        buttonAnd = tk.Radiobutton(app, image=app.imgAnd, text='And', 
                                   activebackground="#5ECEF4", border=0,
                                   variable=opcion, value=4, compound="top",
                                   command=desactivarOp1)
        buttonAnd.grid(padx=10, pady=5, row=4, column=0)
        Hovertip(buttonAnd, hover_delay=500, text="And")

        ## or
        imgOr = Image.open('./img/or.png')
        imgOr = imgOr.resize((70, 70))
        app.imgOr = ImageTk.PhotoImage(imgOr, master=app)
        buttonOr = tk.Radiobutton(app, image=app.imgOr, text='Or', 
                                  activebackground="#5ECEF4", border=0,
                                  variable=opcion, value=5, compound="top",
                                  command=desactivarOp1)
        buttonOr.grid(padx=10, pady=5, row=4, column=1)
        Hovertip(buttonOr, hover_delay=500, text="Or")

        ## not
        imgNot = Image.open('./img/not.png')
        imgNot = imgNot.resize((70, 70))
        app.imgNot = ImageTk.PhotoImage(imgNot, master=app)
        buttonNot = tk.Radiobutton(app, image=app.imgNot, text='Not', 
                                   activebackground="#5ECEF4", border=0,
                                   variable=opcion, value=6, compound="top",
                                   command=desactivarOp1)
        buttonNot.grid(padx=10, pady=5, row=4, column=2)
        Hovertip(buttonNot, hover_delay=500, text="Not")
        
        # Extraemos los datos
        listaCampos = df.columns.tolist()
        ## Declaramos las opciones
        opciones1 = ttk.Combobox(app, state="readonly",
                                values=listaCampos, postcommand=desactivarBoton)
        opciones1.grid(pady=5, column=0, row=5)

        lOption = ttk.Label(app,
                            font=('Helvetica', 12, 'bold'))
        lOption.grid(pady=5, row=5, column=1)

        opciones2 = ttk.Combobox(app, state="readonly",
                                values=listaCampos, postcommand=desactivarBoton)
        opciones2.grid(pady=5, column=2, row=5)

        # Etiqueta nombre nuevo campo
        lname = ttk.Label(app, text="New field name: ",
                          font=('Helvetica', 12, 'bold'))
        lname.grid(pady=5, row=6, column=0)
        result_name_entry = tk.Entry(app)
        result_name_entry.grid(pady=5, row=6, column=1)

        # Boton para guardar
        imgGuardar = Image.open('./img/guardar.png')
        imgGuardar = imgGuardar.resize((30, 30))
        app.imgGuardar = ImageTk.PhotoImage(imgGuardar, master=app)
        boton = tk.Button(image=app.imgGuardar, text="Save",
                           compound="top", state="disable", command=lambda: save_data(df),
                           activebackground="#5ECEF4")
        boton.grid(pady=5, row=7, column=0, columnspan=4)

        opciones1.bind("<<ComboboxSelected>>", desactivarBoton)
        opciones2.bind("<<ComboboxSelected>>", desactivarBoton)

        desactivarOp1()
        desactivarBoton()

    except Exception as e:
        tk.messagebox.showerror(
            "Error", e
        )
        return None

def desactivarBoton(Event=None):
    if (opcion.get() == 6 and opciones2.get() == ""):
        boton.configure(state="disable")
    elif (opcion.get() != 6 and (opciones1.get() == "" or opciones2.get() == "")):
        boton.configure(state="disable")
    else:
        boton.configure(state="normal")

def desactivarOp1():
    labelOperacion()
    opciones1.set("")
    opciones2.set("")
    if (opcion.get() == 6):
        opciones2.configure(state="readonly")
        opciones1.configure(state="disable")
    else:
        opciones1.configure(state="readonly")
        opciones2.configure(state="readonly")

def labelOperacion():
    desactivarBoton()
    if(opcion.get() == 0):
        lOption.config(text='+')
    if(opcion.get() == 1):
        lOption.config(text='-')
    if(opcion.get() == 2):
        lOption.config(text='*')
    if(opcion.get() == 3):
        lOption.config(text='/')
    if(opcion.get() == 4):
        lOption.config(text='AND')
    if(opcion.get() == 5):
        lOption.config(text='OR')
    if(opcion.get() == 6):
        lOption.config(text='NOT')

def operation(df):
    if (opcion.get() == 0):
        add_data(df)
    if(opcion.get() == 1):
        subtract_data(df)
    if(opcion.get() == 2):
        multiply_data(df)
    if(opcion.get() == 3):
        divide_data(df)
    if(opcion.get() == 4):
        and_data(df)
    if(opcion.get() == 5):
        or_data(df)
    if(opcion.get() == 6):
        not_data(df)

def add_data(df):
    data1 = opciones1.get()
    data2 = opciones2.get()
    result = df[data1] + df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result

def subtract_data(df):
    data1 = opciones1.get()
    data2 = opciones2.get()
    result = df[data1] - df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result

def multiply_data(df):
    data1 = opciones1.get()
    data2 = opciones2.get()
    result = df[data1] * df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result

def divide_data(df):
    data1 = opciones1.get()
    data2 = opciones2.get()
    result = df[data1] / df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result
    
def and_data(df):
    data1 = opciones1.get()
    data2 = opciones2.get()
    result = df[data1] & df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result

def or_data(df):
    data1 = opciones1.get()
    data2 = opciones2.get()
    result = df[data1] | df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result

def not_data(df):
    data1 = opciones1.get()
    result = ~df[data1]
    result_name = result_name_entry.get()
    df[result_name] = result

def save_data(df):
    try:
        operation(df)
        file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
        df.to_excel(file, index=False, header=True)
    except ValueError:
        tk.messagebox.showerror("Error", "Unsaved data")
