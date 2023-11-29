# Skriv ett program som läser in en cirkels radie.
# Programmet ska beräkna cirkelns omkrets och area. 
# Resultatet ska skrivas ut separat med två decimaler. 

# importera matematikmodul
import math

# Ange radie
r = float(input('Ange cirkelns radie: '))

# Beräkna omkrets
omkrets = 2 * math.pi * r

# Beräkna Area
area = math.pi * r **2

# Utskrifter
print(f'Omkretsen är {omkrets: .2f}')
print(f'Arean är {area: .2f}')