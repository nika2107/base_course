import numpy as np
import matplotlib.pyplot as plt

def cycloid(R):
    z = np.arange(-2*np.pi, 2*np.pi, 0.1)   

    x = R * (z - np.sin(z)**3)
    y = R * (1 - np.cos(z)**3)

    plt.plot(x, y, color='black', ls='-', lw=7)
    plt.axis('equal')
    plt.savefig('fig_cycloid.png')

cycloid = 10