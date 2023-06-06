import tkinter as tk
from tkinter import filedialog, ttk
import warnings
import pandas as pd
from idlelib.tooltip import Hovertip
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, plot_confusion_matrix, classification_report, mean_absolute_error, mean_squared_error, r2_score
from sklearn.exceptions import DataConversionWarning
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def solicitarDatosPrueba(df, campos, objetivos, model):

    gui2 = ThemedTk(theme="adapta")

    global datosEntrada, datosObjetivo
    datosEntrada = df.iloc[:, campos]
    datosObjetivo = df.iloc[:, objetivos]

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
    boton1.grid(padx=10, pady=5, row=4, column=0)
    Hovertip(boton1, hover_delay=500,
            text="Search xlsx or csv files")

    img2 = Image.open('./img/prediccion.png')
    img2 = img2.resize((100, 100))
    gui2.img2 = ImageTk.PhotoImage(img2, master=gui2)
    boton2 = tk.Button(archivo2, text="Make prediction", image=gui2.img2,
                       activebackground="#5ECEF4", compound="top",
                       border=0, command=lambda: CargarDatosPrediccion( datosEntrada, datosObjetivo, model ))
    boton2.grid(padx=10, pady=5, row=4, column=2)
    Hovertip(boton2, hover_delay=500,
            text="Makes a prediction based on the selected model and evaluation data")

    # Ruta del archivo2
    global nombreArchivo2
    nombreArchivo2 = ttk.Label(archivo2, text="No selected File")
    nombreArchivo2.grid(pady=5, row=0, column=0, columnspan=3)

    global metric_one
    metric_one = ttk.Label(archivo2, text="")
    metric_one.grid(pady=5, padx=0, row=1, column=0, sticky='w')

    global metric_two
    metric_two = ttk.Label(archivo2, text="")
    metric_two.grid(pady=5, padx=0, row=2, column=0, sticky='w')

    global metric_three
    metric_three = ttk.Label(archivo2, text="")
    metric_three.grid(pady=5, padx=0, row=3, column=0, sticky='w')

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

def insertarDatosTreeView():
    # Llenamos el widget con nuestros datos
    col_df = list( df2.columns)
    col_df.insert(0, 'Index')
    tv2["column"] = col_df
    tv2["show"] = "headings"
    tv2.heading("Index", text="Index")

    for column in tv2["columns"]:
        tv2.heading(column, text=column) # titulo de la columna = nombre de la columna

    df_rows = df2.to_numpy().tolist() # Convertimos el dataframe en una lista de listas
    i = 1

    for row in df_rows:
        # insertamos cada una de las listas dentro del treeview.
        row.insert(0,i)
        tv2.insert("", "end", values=row)
        i+=1

def insertarDatosDePrediccion():
    tv2["column"] = "Predict"
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column) # titulo de la columna = nombre de la columna

    df_rows = listaResultado # Convertimos el dataframe en una lista de listas
    for row in df_rows:
        tv2.insert("", "end", values=row) # insertamos cada una de las listas dentro del treeview.  

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
        
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"File was not found in the path {rutaArchivo}")        

############################CODIGO DE REDES NEURONALES#################################################

def CargarDatosPrediccion(input_columns_df, target_column_df, model ):

    warnings.filterwarnings(action='ignore', category=DataConversionWarning)
    warnings.filterwarnings(action='ignore', category=FutureWarning)

    try:

        # Crear copias de los DataFrames de entrada y objetivo para no modificar los originales
        input_columns_df = input_columns_df.copy()
        target_column_df = target_column_df.copy()

        # Identificar y codificar columnas alfanuméricas en el DataFrame de entrada
        encoders = {}
        for col in input_columns_df.columns:
            if input_columns_df[col].dtype == 'object':
                le = LabelEncoder()
                input_columns_df.loc[:, col] = le.fit_transform(input_columns_df[col])
                encoders[col] = le

        # Codificar la columna objetivo si es alfanumérica
        target_column_name = target_column_df.columns[0]
        if target_column_df[target_column_name].dtype == 'object':
            le = LabelEncoder()
            target_column_df.loc[:, target_column_name] = le.fit_transform(target_column_df[target_column_name])
            encoders[target_column_name] = le

        # Definir las características (X) y la variable objetivo (y)
        X = input_columns_df
        y = target_column_df

        try:
            x_train, x_val, y_train, y_val = train_test_split(X, y,
                                                        test_size = 0.10,
                                                        shuffle = True,
                                                        random_state = 1)
            
            # Scale the features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(x_train)
            X_val_scaled = scaler.transform(x_val)
            predict_df_scaled = scaler.transform(df2)

            # Model
            generated_model = model
            generated_model.fit(X_train_scaled, y_train)

        except:
            # Create a message box with a message and a title 
            tk.messagebox.showerror("Error", "Verify that the construction of the model is correct. Close the process and try again.")
            return None

        # Realizar predicciones con el conjunto de prueba
        y_pred = generated_model.predict(X_val_scaled)

        # Guardamos los valores numéricos para la matriz de confusión
        y_val2 = y_val

        # Invertir la transformación del encoder para las etiquetas predichas y verdaderas
        if target_column_name in encoders:
            y_pred = encoders[target_column_name].inverse_transform(y_pred)
            y_val = encoders[target_column_name].inverse_transform(y_val[target_column_name])
        else:
            y_val = y_val[target_column_name]

        # Hacemos la predicción
        prediction = generated_model.predict(predict_df_scaled)

        print(f'La predicción es: \n{prediction}')

        global listaResultado
        listaResultado = list(prediction) if target_column_name not in encoders else list(encoders[target_column_name].inverse_transform(prediction))
        # Funcion para eliminar todo del TreeView
        limpiarDatos()

        insertarDatosDePrediccion()

        # Create a message box with a message and a title 
        tk.messagebox.showinfo("Displays visual information", "When you close this window, you will be able to see the metrics obtained from the generated model.")

        model_type = generated_model.__class__.__name__

        if 'Classifier' in model_type or 'LogisticRegression' == model_type or 'SVC' == model_type or 'GaussianNB' == model_type:
            # Hacemos la prueba de efectividad
            if len(datosObjetivo.values.flatten().tolist()) > 2:
                average = 'macro'
            else:
                average = 'binary'
            modelAccuracy = accuracy_score(y_val, y_pred)
            modelPrecision = precision_score(y_val, y_pred, average=average)
            modelRecall = recall_score(y_val, y_pred, zero_division=1, average=average)

            # Cambiamos las metricas
            metric_one["text"] = str(f'Model Accuracy: {(modelAccuracy*100):.2f}%')
            metric_two["text"] = str(f'Model Precision: {(modelPrecision*100):.2f}%')
            metric_three["text"] = str(f'Model Recall: {(modelRecall*100):.2f}%')
            
            #PLOT CONFUSION MATRIX
            plot_confusion_matrix(generated_model, X_val_scaled, y_val2)
            plt.show()

            model_type = generated_model.__class__.__name__

            #SHOW REPORT
            classificationReport = classification_report(y_val, y_pred, output_dict=True)
            sns.heatmap(pd.DataFrame(classificationReport).T, annot=True)
        else:
            # Calculate the evaluation metrics
            mae = mean_absolute_error(y_val, y_pred)
            mse = mean_squared_error(y_val, y_pred)
            r2 = r2_score(y_val, y_pred)

            # Actualizamos el valor de las metricas
            metric_one["text"] = str(f'MAE: {(mae*100):.2f}%')
            metric_two["text"] = str(f'MSE: {(mse*100):.2f}%')
            metric_three["text"] = str(f'R^2: {(r2*100):.2f}%')

            # create a dataframe with the values
            df = pd.DataFrame({'metric': ['MAE', 'MSE', 'R^2'],
                            'value': [mae, mse, r2]})

            # plot the data
            sns.barplot(x='metric', y='value', hue='metric', data=df)

            # set the y-axis labels to percentages
            plt.yticks(np.arange(0, 1.1, 0.1))
            plt.ylabel('percent')

            # set the y-axis labels to include the % symbol
            ax = plt.gca()
            vals = ax.get_yticks()
            ax.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
            ax.set_title('Evaluation metrics for linear regression model')
        plt.show()
    except Exception as e:
        # We show the message
        tk.messagebox.showerror("Error", str(e))