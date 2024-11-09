import numpy as np
N = 5   
M = 4  
trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        value = np.sin(N * i + M * j + 1)
        trigonometry_array[i, j] = max(value, 0)   
 
print("Конечный массив:")
print(trigonometry_array)