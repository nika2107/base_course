from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def square_move (vx0, vy0,time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange (0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='violet')
 
 
def animate(i):
    ball.set_data(circle_move(vx0=0.01, vy0=0.01, time=i))
    return ball
 
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('square.gif', writer="pillow")

