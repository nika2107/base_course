from lec_3_module import earth_mass as em 
from lec_3_module import sigma_steff_bolc as sigm 
from lec_3_module import gravity_constant as gs 

g = 500 * gs / 10**2
print (g) 

x = em * gs * sigm
print (x)


