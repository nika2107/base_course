# module: physical_constants.py

class PhysicalConstants:
    g = 9.81 
import numpy as np  
alpha = np.radians(30)   
g = PhysicalConstants.g   
t_values = np.linspace(0, 5, num=100)  
results = []

for t in t_values:
    x = v0 * np.cos(alpha) * t
    y = v0 * np.sin(alpha) * t - 0.5 * g * t**2
    results.append([t, x, y])

results_array = np.array(results)

print("t (с), x (м), y (м)")
print(results_array)
