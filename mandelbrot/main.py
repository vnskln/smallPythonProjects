import matplotlib.pyplot as plt
from mandelbrotArray import mandelbrotArray
from tkinter import *

# plot details contains data about localization of plot on xy plane
# [x coordinate of plot center, y coordinate of plot center, size of plot box]
plotDetails = [-0.75, 0, 3.0]
noCalcPoints = 0.0
maxIterCount = 0.0
zoomFactor = 0.0

def showPlot():
    global noCalcPoints
    global maxIterCount
    global zoomFactor
    noCalcPoints = int(entry_1.get())
    maxIterCount = int(entry_2.get())
    zoomFactor = int(entry_3.get())
    window.destroy()
    resultArray = mandelbrotArray(plotDetails, noCalcPoints, maxIterCount)
    fig = plt.imshow(resultArray.T, cmap='hot', interpolation="nearest")
    fig.figure.canvas.mpl_connect('button_press_event', onclick)
    plt.show()


def onclick(event):
    global noCalcPoints
    global maxIterCount
    global zoomFactor
    plotDetails[0] = (plotDetails[0] - plotDetails[2] / 2.0) + event.xdata / noCalcPoints * plotDetails[2]
    plotDetails[1] = (plotDetails[1] - plotDetails[2] / 2.0) + event.ydata / noCalcPoints * plotDetails[2]
    if event.button == 1:
        plotDetails[2] = plotDetails[2] / zoomFactor
    if event.button == 3:
        plotDetails[2] = plotDetails[2] * zoomFactor
    resultArray = mandelbrotArray(plotDetails, noCalcPoints, maxIterCount)
    fig = plt.imshow(resultArray.T, cmap='hot', interpolation="nearest")
    fig.figure.canvas.mpl_connect('button_press_event', onclick)
    plt.show(block=False)


window = Tk()
window.title("Mandelbrot set - settings")
window.geometry("350x125")
frame = Frame(window)
frame.grid()
label_1 = Label(text="Ilość punktów obliczeniowych: ")
label_1.grid(row=0, column=0, sticky=W, padx=12, pady=5)
entry_1 = Entry()
entry_1.grid(row=0, column=1, sticky=W)
entry_1.insert(0,1000)
label_2 = Label(text="Maksymalna liczba iteracji: ")
label_2.grid(row=1, column=0, sticky=W, padx=12, pady=5)
entry_2 = Entry()
entry_2.grid(row=1, column=1, sticky=W)
entry_2.insert(0,120)
label_3 = Label(text="Współczynnik przybliżenia: ")
label_3.grid(row=2, column=0, sticky=W, padx=12, pady=5)
entry_3 = Entry()
entry_3.grid(row=2, column=1, sticky=W)
entry_3.insert(0,2)
button_1 = Button(text="Wyświetl wykres",width=20)
button_1.grid(row=3, column=0, sticky=W, padx=20)
button_1["command"] = showPlot
window.mainloop()


