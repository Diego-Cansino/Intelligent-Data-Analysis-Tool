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
    ax.hist(datos, np.arange(min(datos), max(datos) + 1))
    plot.xlabel(etiqueta)
    plot.show()


def diagramaSectores(datos):
    fig, ax = plot.subplots()
    fig.suptitle("Pie Chart")
    ax.pie(datos, labels=datos, autopct='%1.1f%%')
    plot.show()
