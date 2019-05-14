import numpy as np
from mandelbrot import mandelbrot


def mandelbrotArray (plotCenter, numberOfCalculationPoints, maxIterationsCount):
    xValues = np.linspace(plotCenter[0]-plotCenter[2]/2, plotCenter[0]+plotCenter[2]/2, numberOfCalculationPoints)
    yValues = np.linspace(plotCenter[1]-plotCenter[2]/2, plotCenter[1]+plotCenter[2]/2, numberOfCalculationPoints)
    xLength = len(xValues)
    yLength = len(yValues)
    viewWindow = np.empty((len(xValues), len(yValues)))
    for x in range(xLength):
        for y in range(yLength):
            b = complex(xValues[x], yValues[y])
            viewWindow[x, y] = mandelbrot(b, maxIterationsCount)

    return viewWindow
