import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import LEFT, RIGHT
import ventanaEvalModel as em
import models
import datacleaning as dt

def abrirModelos(df, model):
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

    sModel = selectModel(model)

    # Boton para enviar datos
    btn1 = tk.Button(app, text='Select all', command=select_all)
    btn2 = tk.Button(app, text='Select all', command=select_all2)
    btn3 = tk.Button(app, text='Send selection', command=lambda: [selected_item(), selected_item2(), em.solicitarDatosPrueba(df, campos, objetivos, sModel), app.destroy()])

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

def selectCamposDC(df, cleaningMethod):
    app = ThemedTk(theme="adapta")
    app.geometry('180x200')
    app.title("Data cleaning selection")

    label = tk.Label(app, text="Select columns for data cleaning")
    label.pack(side=tk.TOP, fill=tk.X)

    scrollbar = tk.Scrollbar(app)
    scrollbar.pack(side=RIGHT, fill=tk.Y)
 
    # Create a listbox
    listbox = tk.Listbox(app, width=40, height=10, selectmode=tk.MULTIPLE)
 
    # Inserting the listbox items
    listaColumnas = tuple(df.columns.tolist())
    listbox.insert(tk.END, *listaColumnas)
    
    def selected_item():
        camposDataCleaning = []
        selected_campos = listbox.curselection()
        camposDataCleaning = list(selected_campos)
        return camposDataCleaning
    
    def select_all():
        listbox.select_set(0, tk.END)
    
    # Boton para enviar datos
    btn = tk.Button(app, text='Send selection', command= lambda: [dt.realizarLimpieza(df, selected_item(), cleaningMethod), app.destroy()])
    btn2 = tk.Button(app, text='select all', command=select_all)

    # SCROLLBAR
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    
    # Placing the button and listbox
    btn.pack(side='bottom', fill=tk.X)
    btn2.pack(side='bottom', fill=tk.X)
    listbox.pack()

def selectModel(model):
    if model == "ann":
        SelectModel = models.getANN()
    elif model == "dt":
        SelectModel = models.getDecisionTree()
    elif model == "knn":
        SelectModel = models.getKNN()
    elif model == "nb":
        SelectModel = models.getNaiveBayes()
    elif model == "svm_c":
        SelectModel = models.getSVMClassifier()
    elif model == "lr":
        SelectModel = models.getLogisticRegression()
    elif model == "ann_regression":
        SelectModel = models.getANNRegression()
    elif model == "dt_regression":
        SelectModel = models.getDecisionTreeRegression()
    elif model == "knn_regression":
        SelectModel = models.getKNNRegression()
    elif model == "lr_regression":
        SelectModel = models.getLinearRegression()
    elif model == "svm_r":
        SelectModel = models.getSVMRegression()
    elif model == "br":
        SelectModel = models.getBayesianRidge()
    return SelectModel