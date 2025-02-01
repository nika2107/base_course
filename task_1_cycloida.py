import numpy as np
import matplotlib.pyplot as plt

def cycloid(R = 10):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)  

    x = R * (t - np.sin(t)**3)
    y = R * (1 - np.cos(t)**3)

    plt.plot(x, y, color = "aqua", ls='-', lw=4)
    plt.axis('equal')
    plt.savefig('fig_cycloid.png')

cycloid ()