from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move (R, vx0, vy0,time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange (0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y