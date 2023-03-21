import pandas as pd
from ttkthemes import ThemedTk
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk

def abrirSelCamp(df):
    app = ThemedTk(theme="adapta")
    app.geometry('400x420')
    app.resizable(False, False)
    app.title("Data Selection")

    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.rowconfigure(0, weight=1)
    app.rowconfigure(1, weight=5)
    app.rowconfigure(2, weight=5)
    app.rowconfigure(4, weight=1)
    
    label = tk.Label(app, text="Select fields", font=('Helvetica', 12, 'bold'))
    label.grid(pady=5, column=0, row=0, columnspan=2)

    # Create a listbox
    listbox = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE, exportselection=False)

    #Creation SCROLLBARS
    scrollbar = tk.Scrollbar(listbox)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    # Extraemos los datos
    listaCampos = df.columns.tolist()

    for i in range (len(listaCampos)):
        listbox.insert(i, listaCampos[i])

    def selected_item():
        global campos
        campos = []
        selected_campos = listbox.curselection()
        campos = list(selected_campos)

    def select_all():
        listbox.select_set(0, tk.END)

    def deselect():
        listbox.select_clear(0, tk.END)

    # Botones
    # Boton para enviar datos
    btn1 = tk.Button(app, text='Select all', command=select_all)
    btn2 = tk.Button(app, text='Deselect all', command=deselect)
    # Boton aceptar 
    imgGuardar = Image.open('./img/guardar.png')
    imgGuardar = imgGuardar.resize((30, 30))
    app.imgGuardar = ImageTk.PhotoImage(imgGuardar, master=app)
    btnAceptar = tk.Button(app, image=app.imgGuardar, text="Save selection",
                           compound="top", activebackground="#5ECEF4",
                           command=lambda: [selected_item(), guardarDatos(df), app.destroy()])

    # SCROLLBAR
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    listbox.grid(pady=5, column=0, row=1, columnspan=2, sticky="nsew", rowspan=2)
    btn1.grid(pady=5, column=0, row=3)
    btn2.grid(pady=5, column=1, row=3)
    btnAceptar.grid(pady=5, column=0, row=4, columnspan=2)

def guardarDatos(df):
    df = df.iloc[:, campos]
    try:
        file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
        df.to_excel(file, index=False, header=True)
        tk.messagebox.showinfo("Success!", "Saved data")
    except ValueError:
        tk.messagebox.showerror("Error", "Unsaved data")
