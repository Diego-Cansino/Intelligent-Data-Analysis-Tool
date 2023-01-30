import tkinter as tk
import pandas as pd
from tkinter import filedialog
from ttkthemes import ThemedTk

def newData(df):
    global data1_listbox, data2_listbox, result_name_entry
    root = ThemedTk(theme="adapta")
    root.geometry('600x370')
    root.resizable(False, False)
    root.title("Data Calculator")

    # Extraemos los datos
    listaCampos = df.columns.tolist()

    data1_listbox = tk.Listbox(root, width=40, height=10, exportselection=False)#, selectmode="single")
    data1_listbox.pack(side="left", fill=tk.BOTH, expand=True, pady=(5, 70))
    data2_listbox = tk.Listbox(root, width=40, height=10, exportselection=False)
    data2_listbox.pack(side="right", fill=tk.BOTH, expand=True, pady=(5, 70))

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="left", fill=tk.Y, pady=(5, 70))
    scrollbar2 = tk.Scrollbar(root)
    scrollbar2.pack(side="right", fill=tk.Y, pady=(5, 70))

    for i in range (len(listaCampos)):
            data1_listbox.insert(i, listaCampos[i])
            data2_listbox.insert(i, listaCampos[i])

    add_button = tk.Button(root, text="Add", command=lambda:add_data(df))
    add_button.pack(side="bottom")
    subtract_button = tk.Button(root, text="Subtract", command=lambda:subtract_data(df))
    subtract_button.pack(side="bottom")
    multiply_button = tk.Button(root, text="Multiply", command=lambda:multiply_data(df))
    multiply_button.pack(side="bottom")
    divide_button = tk.Button(root, text="Divide", command=lambda:divide_data(df))
    divide_button.pack(side="bottom")
    and_button = tk.Button(root, text="AND", command=lambda:and_data(df))
    and_button.pack(side="bottom")
    or_button = tk.Button(root, text="OR", command=lambda:or_data(df))
    or_button.pack(side="bottom")
    not_button = tk.Button(root, text="NOT", command=lambda:not_data(df))
    not_button.pack(side="bottom")
    result_name_label = tk.Label(root, text="Enter the name for the resulting field:")
    result_name_label.pack(side="bottom")
    result_name_entry = tk.Entry(root)
    result_name_entry.pack(side="bottom")

    # SCROLLBAR
    data1_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=data1_listbox.yview)
    data2_listbox.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=data2_listbox.yview)

def add_data(df):
    data1 = data1_listbox.get(data1_listbox.curselection())
    data2 = data2_listbox.get(data2_listbox.curselection())
    result = df[data1] + df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result
    save_data(df)

def subtract_data(df):
    data1 = data1_listbox.get(data1_listbox.curselection())
    data2 = data2_listbox.get(data2_listbox.curselection())
    result = df[data1] - df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result
    save_data(df)

def multiply_data(df):
    data1 = data1_listbox.get(data1_listbox.curselection())
    data2 = data2_listbox.get(data2_listbox.curselection())
    result = df[data1] * df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result
    save_data(df)

def divide_data(df):
    data1 = data1_listbox.get(data1_listbox.curselection())
    data2 = data2_listbox.get(data2_listbox.curselection())
    result = df[data1] / df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result
    save_data(df)
    
def and_data(df):
    data1 = data1_listbox.get(data1_listbox.curselection())
    data2 = data2_listbox.get(data2_listbox.curselection())
    result = df[data1] & df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result
    save_data(df)

def or_data(df):
    data1 = data1_listbox.get(data1_listbox.curselection())
    data2 = data2_listbox.get(data2_listbox.curselection())
    result = df[data1] | df[data2]
    result_name = result_name_entry.get()
    df[result_name] = result
    save_data(df)

def not_data(df):
    data1 = data1_listbox.get(data1_listbox.curselection())
    result = ~df[data1]
    result_name = result_name_entry.get()
    df[result_name] = result
    save_data(df)

def save_data(df):
    try:
        file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
        df.to_excel(file, index=False, header=True)
    except ValueError:
        tk.messagebox.showerror("Error", "Unsaved df")

# df = pd.read_csv(r'C:\Users\Diego\Downloads\Intelligent-Data-Analysis-Tool\archivos p\Caso_analisis_crediticio.csv')