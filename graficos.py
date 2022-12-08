import matplotlib.pyplot as plot
import numpy as np


def diagramaBarrasVerticales(valoresX, valoresY, etiquetaX, etiquetaY):
    fig, ax = plot.subplots()
    fig.suptitle("Vertical bar graph " + etiquetaX + " vs " + etiquetaY)
    ax.bar(valoresX, valoresY)
    plot.xlabel(etiquetaX)
    plot.ylabel(etiquetaY)
    plot.show()


def diagramaBarrasHorizontales(valoresX, valoresY, etiquetaX, etiquetaY):
    fig, ax = plot.subplots()
    fig.suptitle("Horizontal bar graph " + etiquetaX + " vs " + etiquetaY)
    ax.barh(valoresX, valoresY)
    plot.xlabel(etiquetaX)
    plot.ylabel(etiquetaY)
    plot.show()


def diagramaDispersion(valoresX, valoresY, etiquetaX, etiquetaY):
    fig, ax = plot.subplots()
    fig.suptitle("Dispersion " + etiquetaX + " vs " + etiquetaY)
    ax.scatter(valoresX, valoresY)
    plot.xlabel(etiquetaX)
    plot.ylabel(etiquetaY)
    plot.show()


def diagramaLineas(valoresX, valoresY, etiquetaX, etiquetaY):
    fig, ax = plot.subplots()
    fig.suptitle("Linear " + etiquetaX + " vs " + etiquetaY)
    ax.plot(valoresX, valoresY)
    plot.xlabel(etiquetaX)
    plot.ylabel(etiquetaY)
    plot.show()


def diagramaAreas(valoresX, valoresY, etiquetaX, etiquetaY):
    fig, ax = plot.subplots()
    fig.suptitle("Area " + etiquetaX + " vs " + etiquetaY)
    ax.fill_between(valoresX, valoresY)
    plot.xlabel(etiquetaX)
    plot.ylabel(etiquetaY)
    plot.show()


def histograma(datos, etiqueta):
    fig, ax = plot.subplots()
    fig.suptitle("Histogram " + etiqueta)
    # , np.arange(min(datos), max(datos) + 1)
    ax.hist(datos)
    plot.xlabel(etiqueta)
    plot.show()


def diagramaSectores(datos, etiqueta):
    datos = datos.tolist()
    toDict = dict(zip(datos, map(lambda x: datos.count(x), datos)))
    etiquetas = toDict.keys()
    valores = toDict.values()

    fig, ax = plot.subplots()
    fig.suptitle("Pie Chart " + etiqueta)
    ax.pie(valores, labels=etiquetas, autopct='%1.1f%%')
    plot.show()