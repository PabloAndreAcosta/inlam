# Skriv ett program som läser in godtyckligt antal positiva tal.
# När användaren skriver in ett negativt tal ska programmet skriva ut det lägsta och högsta av de positiva talen.

import math

största = 1
minsta = 1000   #ett stort tal
while True:
    tal = float(input('Ange tal '))
    if tal < 0:
        break
    if tal > största:
        största = tal
    if tal < minsta:
        minsta = tal
print(f'Största talet: {största}')            
print(f'Minsta talet: {minsta}')  