import ventanaPrincipal as vp

def realizarLimpieza(df, columns, cleaningMethod):
    if(cleaningMethod == 'FFILL'):
        limpiarDatosForwardFill(df, columns)
    elif (cleaningMethod == 'BFILL'):
        limpiarDatosBackwardFill(df, columns)
    elif (cleaningMethod == 'media'):
        rellenarDatosMedia(df, columns)
    elif (cleaningMethod == 'moda'):
        rellenarDatosModa(df, columns)
    elif (cleaningMethod == 'mediana'):
        rellenarDatosMediana(df, columns)
    elif (cleaningMethod == 'rango'):
        rellenarDatosRango(df, columns)
    elif (cleaningMethod == 'norma'):
        normalizarDatos(df, columns)
    vp.dataCleaning(df)

def limpiarDatosForwardFill(df, columns):
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""  # QUIZA ESTO ESTA MAL
    df.iloc[:, columns] = df.iloc[:, columns].fillna(method="ffill")

def limpiarDatosBackwardFill(df, columns):
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    df.iloc[:, columns] = df.iloc[:, columns].fillna(method="backfill")
    
def rellenarDatosMedia(df, columns):
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    meanValues = df.iloc[:, columns].mean()
    df.iloc[:, columns] = df.iloc[:, columns].fillna(meanValues)

def rellenarDatosMediana(df, columns):
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    medianValues = df.iloc[:, columns].median()
    df.iloc[:, columns] = df.iloc[:, columns].fillna(medianValues)

def rellenarDatosModa(df, columns):
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    values = df.iloc[:, columns].mode()
    modeValues = values.head(1).squeeze()
    df.iloc[:, columns] = df.iloc[:, columns].fillna(modeValues)

def rellenarDatosRango(df, columns):
    """Si el archivo seleccionado es valido, este se mostrará en la GUI"""
    maxValues = df.iloc[:, columns].max()
    minValues = df.iloc[:, columns].min()
    values = maxValues - minValues
    df.iloc[:, columns] = df.iloc[:, columns].fillna(values)

def normalizarDatos(df, columns):
    """Normaliza los datos de manera global en el DataFrame"""
    normalizeData = ( df.iloc[:, columns] - df.iloc[:, columns].min() ) / ( df.iloc[:, columns].max() - df.iloc[:, columns].min() )
    df.iloc[:, columns] = normalizeData