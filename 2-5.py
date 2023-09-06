# Man kan beräkna avståndet mellan två punkter(x1. y1) och (x2, y2) i ett tvådimensionellt koordinatsystem med formeln:
# s = roten ur (x1 -x2 upphöjt till två) +(y1 -y2 upphöjt till två)

import math

x1 = float(input('punkt x1: '))
x2 = float(input('punkt x2: '))
y1 = float(input('punkt y1: '))
y2 = float(input('punkt y2: '))

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f's: {distance: .4f}')