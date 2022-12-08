import tkinter as tk
from ttkthemes import ThemedTk
import ventanaPrincipal as vp

def abrirSeleccion(df):
    
    global label3, lista, df2, lista2

    df2 = df

    app = ThemedTk(theme="adapta")
    app.geometry('600x370')
    app.resizable(False, False)

    label = tk.Label(app, text="FORMAT DATA", font=('Helvetica', 20, 'bold'))
    label.grid( pady=5, row=0, column=0)

    # Declaramos los label
    label1 = tk.Label(app, text="The column, ",
                        font=('Helvetica', 12, 'bold'))
    label1.grid( pady=5, row=1, column=0)

    listaCampos = df.columns.tolist()

    # # Declaramos las opciones
    lista = tk.ttk.Combobox(app, state="readonly", values=listaCampos)
    lista.grid( pady=5, row=1, column=1)

    lista.bind('<<ComboboxSelected>>', changeInfo)

    # Declaramos los label
    label2 = tk.Label(app, text="is type of: ",
                        font=('Helvetica', 12, 'bold'))
    label2.grid( pady=5, row=1, column=2)

    # Declaramos los label
    label3 = tk.Label(app, text="",
                        font=('Helvetica', 12, 'bold'))
    label3.grid( pady=5, row=1, column=3)

    # Declaramos los label
    label4 = tk.Label(app, text="Change column ",
                        font=('Helvetica', 12, 'bold'))
    label4.grid( pady=5, row=3, column=0)

    # Declaramos los label
    lista2 = tk.ttk.Combobox(app, state="readonly", values=listaCampos)
    lista2.grid( pady=5, row=3, column=1)

    # Declaramos los label
    label6 = tk.Label(app, text=" type to ",
                        font=('Helvetica', 12, 'bold'))
    label6.grid( pady=5, row=3, column=2)

    listaDatos = ['object', 'int64', 'float64', 'bool', 'datetime64' ,'timedelta[ns]', 'category']

    # # Declaramos las opciones
    lista3 = tk.ttk.Combobox(app, state="readonly", values=listaDatos)
    lista3.grid( pady=5, row=3, column=3)

    def changeDato( df, columna, change ):
        df = df.astype({f'{columna}': change})
        vp.dataCleaning(df)

    boton2 = tk.Button(app, text="Change type of data", background="#5ECEF4", command=lambda: changeDato(df, lista2.get(), lista3.get()))
    boton2.grid(pady=5, row=4, column=0, columnspan=4, sticky="ew")

def changeInfo(event=None):
    label3["text"] = str(df2[lista.get()].dtype)
    lista2.current(lista.current())


