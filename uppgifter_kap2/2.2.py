#Skriv ett program som beräknar volymen och arean av en sfär. 

import math

# Ange radie
r = float(input('Vad är sfärens radie? '))

# Beräkna volymen av sfären
volym = (4 * math.pi * r **3) / 3

# Beräkna arean av sfären
area = 4 * math.pi * r **2

print(f'Sfärens volym är {volym: .2f} och area är {area: .2f}')