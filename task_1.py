def average(a):
    if len(a) == 0:
       return 0
    return sum(a) / len(a)

a = [1, 2, 3, 4, 5]
result = average(a)
print(" Srednee arifmeticheskoe:", result)