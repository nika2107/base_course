from scipy.constants import g

def mechanical_energy (m, h, v):
     p_energy = m * g * h 
     k_energy = 0.5 * m * v **2
     t_energy = p_energy + k_energy
     return (t_energy)

m = 10.0  
h = 5.0   
v = 15.0  

result = mechanical_energy(m, h, v)
print("Полная механическая энергия:", result, "Дж")