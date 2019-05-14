def mandelbrot (b, maxIterationsCount):
    a = complex(0,0)
    for iteration in range (maxIterationsCount):
        a=a*a+b;
        if (abs(a)>4):
            return iteration+1
    return iteration+1