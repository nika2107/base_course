import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 12 * np.pi, 500)

def butterfly_t(t):
    x = np.sin(t) * ((np.e**np.cos(t)) - (2 * np.cos(4*t)) + (np.sin(t/12)**5))
    y = np.cos(t) * ((np.e**np.cos(t)) - (2 * np.cos(4*t)) + (np.sin(t/12)**5))
    return x, y

x, y = butterfly_t(t)

def butterfly_t1(x, y, t1):
    X = x * np.cos(t1) - y * np.sin(t1)
    Y = y * np.cos(t1) + x * np.sin(t1)
    return X, Y

fig, ax = plt.subplots()
butterfly, = plt.plot([], [], color ="deeppink", label = 'butterfly' )
butterfly_line, = plt.plot([], [], color = 'deeppink', label = "butterfly")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
plt.axis('equal')

def animate(i):
    t = np.linspace(0, 2*np.pi, 200) 
    x, y = butterfly_t(t)
    t1 = 0.5 * i 
    X, Y = butterfly_t1(x, y, t1)
    butterfly.set_data(X, Y)

ani = FuncAnimation(fig, animate, frames=np.arange(0, 4*np.pi, 0.1), interval=50)
ani.save('butterfly.gif')