from ttkthemes import ThemedTk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import filedialog
import gramatica as nd


def newData(df):
    global input, name, campo
    app = ThemedTk(theme="adapta")
    app.geometry('450x450')
    app.resizable(False, False)
    app.title("Data Calculator")
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.columnconfigure(2, weight=1)
    app.columnconfigure(3, weight=1)
    app.columnconfigure(4, weight=1)
    app.columnconfigure(5, weight=1)
    app.rowconfigure(0, weight=1)
    app.rowconfigure(1, weight=1)
    app.rowconfigure(2, weight=1)
    app.rowconfigure(3, weight=1)
    app.rowconfigure(4, weight=1)
    app.rowconfigure(5, weight=1)

    nuevosDatos = ttk.Label(app, text="NEW DATA",
                            font=('Helveltica', 15, 'bold'))
    nuevosDatos.grid(pady=5, row=0, column=0, columnspan=6)

    input = tk.Text(app, state="disabled", height=3)
    input.grid(pady=5, row=1, column=0, columnspan=6, sticky="nsew")

    imgUno = Image.open('./img/uno.png')
    imgUno = imgUno.resize((50, 50))
    app.imgUno = ImageTk.PhotoImage(imgUno, master=app)
    buttonUno = tk.Button(image=app.imgUno, command=lambda: verElemento("1"),
                          activebackground="#5ECEF4")
    buttonUno.grid(pady=5, row=2, column=0)

    imgDos = Image.open('./img/dos.png')
    imgDos = imgDos.resize((50, 50))
    app.imgDos = ImageTk.PhotoImage(imgDos, master=app)
    buttonDos = tk.Button(image=app.imgDos, command=lambda: verElemento("2"),
                          activebackground="#5ECEF4")
    buttonDos.grid(pady=5, row=2, column=1)

    imgTres = Image.open('./img/tres.png')
    imgTres = imgTres.resize((50, 50))
    app.imgTres = ImageTk.PhotoImage(imgTres, master=app)
    buttonTres = tk.Button(image=app.imgTres, command=lambda: verElemento("3"),
                           activebackground="#5ECEF4")
    buttonTres.grid(pady=5, row=2, column=2)

    imgParIzq = Image.open('./img/parizq.png')
    imgParIzq = imgParIzq.resize((50, 50))
    app.imgParIzq = ImageTk.PhotoImage(imgParIzq, master=app)
    buttonParIzq = tk.Button(image=app.imgParIzq, command=lambda: verElemento("("),
                           activebackground="#5ECEF4")
    buttonParIzq.grid(pady=5, row=2, column=3)

    imgParDer = Image.open('./img/parder.png')
    imgParDer = imgParDer.resize((50, 50))
    app.imgParDer = ImageTk.PhotoImage(imgParDer, master=app)
    buttonParDer = tk.Button(image=app.imgParDer, command=lambda: verElemento(")"),
                           activebackground="#5ECEF4")
    buttonParDer.grid(pady=5, row=2, column=4)

    imgSum = Image.open('./img/suma.png')
    imgSum = imgSum.resize((50, 50))
    app.imgSum = ImageTk.PhotoImage(imgSum, master=app)
    buttonSum = tk.Button(image=app.imgSum, command=lambda: verElemento("+"),
                          activebackground="#5ECEF4")
    buttonSum.grid(pady=5, row=2, column=5)

    imgCuatro = Image.open('./img/cuatro.png')
    imgCuatro = imgCuatro.resize((50, 50))
    app.imgCuatro = ImageTk.PhotoImage(imgCuatro, master=app)
    buttonCuatro = tk.Button(image=app.imgCuatro, command=lambda: verElemento("4"),
                             activebackground="#5ECEF4")
    buttonCuatro.grid(pady=5, row=3, column=0)

    imgCinco = Image.open('./img/cinco.png')
    imgCinco = imgCinco.resize((50, 50))
    app.imgCinco = ImageTk.PhotoImage(imgCinco, master=app)
    buttonCinco = tk.Button(image=app.imgCinco, command=lambda: verElemento("5"),
                            activebackground="#5ECEF4")
    buttonCinco.grid(pady=5, row=3, column=1)

    imgSeis = Image.open('./img/seis.png')
    imgSeis = imgSeis.resize((50, 50))
    app.imgSeis = ImageTk.PhotoImage(imgSeis, master=app)
    buttonSeis = tk.Button(image=app.imgSeis, command=lambda: verElemento("6"),
                           activebackground="#5ECEF4")
    buttonSeis.grid(pady=5, row=3, column=2)

    imgAnd = Image.open('./img/and.png')
    imgAnd = imgAnd.resize((50, 50))
    app.imgAnd = ImageTk.PhotoImage(imgAnd, master=app)
    buttonAnd = tk.Button(image=app.imgAnd, command=lambda: verElemento("&"),
                          activebackground="#5ECEF4")
    buttonAnd.grid(pady=5, row=3, column=3)
    Hovertip(buttonAnd, hover_delay=500, text="Logistic operation AND")

    imgOr = Image.open('./img/or.png')
    imgOr = imgOr.resize((50, 50))
    app.imgOr = ImageTk.PhotoImage(imgOr, master=app)
    buttonOr = tk.Button(image=app.imgOr, command=lambda: verElemento("|"),
                         activebackground="#5ECEF4")
    buttonOr.grid(pady=5, row=3, column=4)
    Hovertip(buttonOr, hover_delay=500, text="Logistic operation OR")

    imgRes = Image.open('./img/resta.png')
    imgRes = imgRes.resize((50, 50))
    app.imgRes = ImageTk.PhotoImage(imgRes, master=app)
    buttonRes = tk.Button(image=app.imgRes, command=lambda: verElemento("-"),
                          activebackground="#5ECEF4")
    buttonRes.grid(pady=5, row=3, column=5)

    imgSiete = Image.open('./img/siete.png')
    imgSiete = imgSiete.resize((50, 50))
    app.imgSiete = ImageTk.PhotoImage(imgSiete, master=app)
    buttonSiete = tk.Button(image=app.imgSiete, command=lambda: verElemento("7"),
                            activebackground="#5ECEF4")
    buttonSiete.grid(pady=5, row=4, column=0)

    imgOcho = Image.open('./img/ocho.png')
    imgOcho = imgOcho.resize((50, 50))
    app.imgOcho = ImageTk.PhotoImage(imgOcho, master=app)
    buttonOcho = tk.Button(image=app.imgOcho, command=lambda: verElemento("8"),
                           activebackground="#5ECEF4")
    buttonOcho.grid(pady=5, row=4, column=1)

    imgNueve = Image.open('./img/nueve.png')
    imgNueve = imgNueve.resize((50, 50))
    app.imgNueve = ImageTk.PhotoImage(imgNueve, master=app)
    buttonNueve = tk.Button(image=app.imgNueve, command=lambda: verElemento("9"),
                            activebackground="#5ECEF4")
    buttonNueve.grid(pady=5, row=4, column=2)

    imgNot = Image.open('./img/not.png')
    imgNot = imgNot.resize((50, 50))
    app.imgNot = ImageTk.PhotoImage(imgNot, master=app)
    buttonNot = tk.Button(image=app.imgNot, command=lambda: verElemento("!"),
                          activebackground="#5ECEF4")
    buttonNot.grid(pady=5, row=4, column=3)
    Hovertip(buttonNot, hover_delay=500, text="Logistic operation NOT")

    imgDiv = Image.open('./img/division.png')
    imgDiv = imgDiv.resize((50, 50))
    app.imgDiv = ImageTk.PhotoImage(imgDiv, master=app)
    buttonDiv = tk.Button(image=app.imgDiv, command=lambda: verElemento("/"),
                          activebackground="#5ECEF4")
    buttonDiv.grid(pady=5, row=4, column=4)

    imgPor = Image.open('./img/multi.png')
    imgPor = imgPor.resize((50, 50))
    app.imgPor = ImageTk.PhotoImage(imgPor, master=app)
    buttonPor = tk.Button(image=app.imgPor, command=lambda: verElemento("*"),
                          activebackground="#5ECEF4")
    buttonPor.grid(pady=5, row=4, column=5)

    imgPunto = Image.open('./img/punto.png')
    imgPunto = imgPunto.resize((50, 50))
    app.imgPunto = ImageTk.PhotoImage(imgPunto, master=app)
    buttonPunto = tk.Button(image=app.imgPunto, command=lambda: verElemento("."),
                            activebackground="#5ECEF4")
    buttonPunto.grid(pady=5, row=5, column=0)

    imgCero = Image.open('./img/cero.png')
    imgCero = imgCero.resize((50, 50))
    app.imgCero = ImageTk.PhotoImage(imgCero, master=app)
    buttonCero = tk.Button(image=app.imgCero, command=lambda: verElemento("0"),
                           activebackground="#5ECEF4")
    buttonCero.grid(pady=5, row=5, column=1)

    imgDel = Image.open('./img/c.png')
    imgDel = imgDel.resize((50, 50))
    app.imgDel = ImageTk.PhotoImage(imgDel, master=app)
    buttonDel = tk.Button(image=app.imgDel, command=lambda: limpiarCampo(),
                          activebackground="#5ECEF4")
    buttonDel.grid(pady=5, row=5, column=2)
    Hovertip(buttonDel, hover_delay=500, text="Delete operation")
    
    # Extraemos los datos
    listaCampos = df.columns.tolist()
    campo = ttk.Combobox(app, state="readonly", values=listaCampos)
    campo.grid(pady=5, row=5, column=3, columnspan=3, sticky="we")
    Hovertip(campo, hover_delay=500, text="Select a field from the dataset")
    campo.bind("<<ComboboxSelected>>", verCampo)

    labelName = ttk.Label(app, text="Name of new field:", font=('Helvetica', 12, 'bold'))
    labelName.grid(pady=5, row=6, column=0, columnspan=3)

    name = tk.Entry(app)
    name.grid(pady=5, row=6, column=3, columnspan=2, sticky="nswe")
    Hovertip(name, hover_delay=500, text="Name of new field")

    imgIgual = Image.open('./img/igual.png')
    imgIgual = imgIgual.resize((50, 50))
    app.imgIgual = ImageTk.PhotoImage(imgIgual, master=app)
    buttonIgual =  tk.Button(image=app.imgIgual, command=lambda:nuevoCampo(df),
                             activebackground="#5ECEF4")
    buttonIgual.grid(pady=5, row=6, column=5)
    Hovertip(name, hover_delay=500, text="Calculate new field")

    verCampo()

def verElemento(elemento):
    input.configure(state="normal")
    input.insert(tk.END, elemento)
    input.configure(state="disabled")

def verCampo(Event=None):
    selection = campo.get()
    if selection != "" : verElemento('"'+selection+'"')

def limpiarCampo():
    input.configure(state="normal")
    input.delete("1.0","end")
    input.configure(state="disabled")
    name.delete(0,"end")

def nuevoCampo(df):
    n = name.get()
    inp = input.get("1.0","end")
    inp = '[' + inp[0:-1] + ']'
    limpiarCampo()
    if (n == ""):
        n = "New_Field"

    if (inp == "[]"):
        tk.messagebox.showerror("Error", "Enter Operations")
    else:
        nd.contruirCampo(inp, df, n)
