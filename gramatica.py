tokens  = (
    'REVALUAR',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'PTCOMA',
    'CADENA'
)

# Tokens
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIV       = r'/'
t_AND       = r'\&'
t_OR        = r'\|'
t_NOT       = r'\!'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
from tkinter import messagebox, filedialog
import pandas
import ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','AND','OR'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV'),
    ('right','UMENOS'),
    ('right','NOT')
    )

# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''

def p_instrucciones_evaluar(t):
    'instruccion : CORIZQ expresion CORDER'
    save_data(df)

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIV expresion
                  | expresion AND expresion
                  | expresion OR expresion'''
    if t[2] == '+'  :
        if (type(t[1]) == str and type(t[3]) == str): 
            t[0] = df[t[1]] + df[t[3]]
        elif (type(t[1]) == str and (type(t[3]) == int or type(t[3]) == float)) :
            t[0] = df[t[1]] + t[3]
        elif ((type(t[1]) == int or type(t[1]) == float) and type(t[3]) == str) :
            t[0] = t[1] + df[t[3]]
        elif (type(t[1]) == pandas.core.series.Series and type(t[3]) == str): 
            t[0] = t[1] + df[t[3]]
        elif (type(t[1]) == str and type(t[3]) == pandas.core.series.Series):
            t[0] = df[t[1]] + t[3]
        else:
            t[0] = t[1] + t[3]  

    elif t[2] == '-': 
        if (type(t[1]) == str and type(t[3]) == str): 
            t[0] = df[t[1]] - df[t[3]]
        elif (type(t[1]) == str and (type(t[3]) == int or type(t[3]) == float)) :
            t[0] = df[t[1]] - t[3]
        elif ((type(t[1]) == int or type(t[1]) == float) and type(t[3]) == str) :
            t[0] = t[1] - df[t[3]]
        elif (type(t[1]) == pandas.core.series.Series and type(t[3]) == str): 
            t[0] = t[1] - df[t[3]]
        elif (type(t[1]) == str and type(t[3]) == pandas.core.series.Series):
            t[0] = df[t[1]] - t[3]
        else:
            t[0] = t[1] - t[3]  

    elif t[2] == '*': 
        if (type(t[1]) == str and type(t[3]) == str): 
            t[0] = df[t[1]] * df[t[3]]
        elif (type(t[1]) == str and (type(t[3]) == int or type(t[3]) == float)) :
            t[0] = df[t[1]] * t[3]
        elif ((type(t[1]) == int or type(t[1]) == float) and type(t[3]) == str) :
            t[0] = t[1] * df[t[3]]
        elif (type(t[1]) == pandas.core.series.Series and type(t[3]) == str): 
            t[0] = t[1] * df[t[3]]
        elif (type(t[1]) == str and type(t[3]) == pandas.core.series.Series):
            t[0] = df[t[1]] * t[3]
        else:
            t[0] = t[1] * t[3]  

    elif t[2] == '/': 
        if (type(t[1]) == str and type(t[3]) == str): 
            t[0] = df[t[1]] / df[t[3]]
        elif (type(t[1]) == str and (type(t[3]) == int or type(t[3]) == float)) :
            t[0] = df[t[1]] / t[3]
        elif ((type(t[1]) == int or type(t[1]) == float) and type(t[3]) == str) :
            t[0] = t[1] / df[t[3]]
        elif (type(t[1]) == pandas.core.series.Series and type(t[3]) == str): 
            t[0] = t[1] / df[t[3]]
        elif (type(t[1]) == str and type(t[3]) == pandas.core.series.Series):
            t[0] = df[t[1]] / t[3]
        else:
            t[0] = t[1] / t[3]  

    elif t[2] == '&': 
        if (type(t[1]) == str and type(t[3]) == str): 
            t[0] = df[t[1]] and df[t[3]]
        elif (type(t[1]) == str and (type(t[3]) == int or type(t[3]) == float)) :
            t[0] = df[t[1]] and t[3]
        elif ((type(t[1]) == int or type(t[1]) == float) and type(t[3]) == str) :
            t[0] = t[1] and df[t[3]]
        elif (type(t[1]) == pandas.core.series.Series and type(t[3]) == str): 
            t[0] = t[1] and df[t[3]]
        elif (type(t[1]) == str and type(t[3]) == pandas.core.series.Series):
            t[0] = df[t[1]] and t[3]
        else:
            t[0] = t[1] and t[3]  

    elif t[2] == '|': 
        if (type(t[1]) == str and type(t[3]) == str): 
            t[0] = df[t[1]] or df[t[3]]
        elif (type(t[1]) == str and (type(t[3]) == int or type(t[3]) == float)) :
            t[0] = df[t[1]] or t[3]
        elif ((type(t[1]) == int or type(t[1]) == float) and type(t[3]) == str) :
            t[0] = t[1] or df[t[3]]
        elif (type(t[1]) == pandas.core.series.Series and type(t[3]) == str): 
            t[0] = t[1] or df[t[3]]
        elif (type(t[1]) == str and type(t[3]) == pandas.core.series.Series):
            t[0] = df[t[1]] or t[3]
        else:
            t[0] = t[1] or t[3]  

    # Se guarda la operación en el df
    df[n] = t[0]
        
def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                  | NOT expresion %prec NOT'''
    if t[1] == '-'  : 
        if type(t[2]) == str: t[0] = -df[t[2]]
        else:
            t[0] = -t[2]             
    elif t[1] == '!': 
        if type(t[2]) == str: t[0] = not df[t[2]]
        else:
            t[0] = not t[2] 
    # Se guarda la operación en el df
    df[n] = t[0]


def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL
                    | CADENA'''
    t[0] = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    messagebox.showerror("Error", "Error sintáctico")

def save_data(df):
    try:
        file = filedialog.asksaveasfilename(filetypes=[("xlsx files", ".xlsx")], defaultextension="*.xlsx")
        df.to_excel(file, index=False, header=True)
        messagebox.showinfo("Success!", "Saved data")
    except ValueError:
        messagebox.showerror("Error", "Unsaved data")

# MAIN
import ply.yacc as yacc

def contruirCampo(input, df_p, n_p):
    global df, n
    df = df_p
    n = n_p
    parser = yacc.yacc()
    parser.parse(input)