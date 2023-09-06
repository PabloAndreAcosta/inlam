#Skriv ett program som beräknar volymen och arean av en sfär.
# Om radien är mindre än 0 ska det utges ett felmeddelande.

import math

r = float(input('Vad är sfärens radie? '))

sfär_volym = ((4 * math.pi * r**3) /3)

sfär_area = 4 * math.pi * r**2

print(f'Volume: {sfär_volym: .2f}')
print(f'Area: {sfär_area: .2f}')

if r <= 0:
    print ('Error')