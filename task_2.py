import numpy as np

def multiply_array_elements(arr):
    return np.prod(arr)

array = np.array([1, 2, 3, 4, 5])
result = multiply_array_elements(array)
print("произведение элементов массива:", result)