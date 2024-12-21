import matplotlib.pyplot as plt
import numpy as np


def ellipse(a, b, minimum,maximum, N):

    x = np.linspace(minimum, maximum, N)
    y = np.linspace(minimum, maximum, N)

    X, Y = np.meshgrid(x, y)

    fxy = (X**2)/(a**2) + (Y**2)/(b**2) - 1
    
    plt.contour(X, Y, fxy, levels=[0])
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("elipse")
    plt.grid()
    plt.savefig('fig_task3.png')

ellipse(6, 4, -10,10,100)