def function_values(a, b, N):
    x = [a + (b - a) * i / (N - 1) for i in range(N)]
    y = [x**2 for x in x]
    
    return y 
 
a = 0   
b = 10   
N = 5   

result = function_values(a, b, N)
print("Значения функции y = x^2 на промежутке [{}, {}]:".format(a, b), result)