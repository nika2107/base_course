import numpy as np
import matplotlib.pyplot as plt

def astroid(R = 5):
    z = np.arange(-5*np.pi, 5*np.pi, 0.1)  

    x = R * (np.cos(z)**3)
    y = R * (np.sin(z)**3)

    plt.plot(x, y, color='gold', ls='-', lw=4)
    plt.savefig('fig_astroid.png')

astroid ()