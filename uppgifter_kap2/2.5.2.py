# SKriv ett program som läser in punternas koordinater och beräknar avståndet mellan dem.

import math

x1 = int(input('Ange x1: '))
x2 = int(input('Angge x2: '))
y1 = int(input('Ange y1: '))
y2 = int(input('Ange y2: '))

s = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f'Anståndet mellan punkterna är {s}')
